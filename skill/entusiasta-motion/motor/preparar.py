#!/usr/bin/env python3
"""Prepara um reels pra edição completa no motion-studio (Remotion).

Uso: preparar.py <id> <bruto.MP4> <cortes.json>
  cortes.json = [[inicio_s, fim_s, "texto EXATO que ele fala nesse take"], ...] na ordem do vídeo.
  Escolha os takes com motor/takes.sh (regra: o ÚLTIMO take de cada fala). Dê ~0,08s de folga antes e ~0,1s depois.
Gera:
  public/brutos/<id>.mp4    proxy H.264 1080x1920 30fps BT.709 em pé (bruto 4K HEVC do DJI ou do iPhone;
                            HLG/PQ do iPhone passa por tonemap VideoToolbox e a rotação vira giro real)
  public/edicoes/<id>.json  {segs, words}: falas no tempo da edição + tempo de cada palavra
                            (texto vem do cortes.json, tempo vem do whisper; a transcrição erra nomes)
"""
import json, os, subprocess, sys, tempfile
from pathlib import Path
ID, BRUTO, CORTES = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
MS = Path(os.environ.get("MOTION_STUDIO", Path(__file__).resolve().parents[3] / "studio")) / "public"
MODELO = os.environ.get("WHISPER_MODELO", str(Path.home() / ".cache/whisper-cpp/ggml-base.bin"))
(MS / "brutos").mkdir(exist_ok=True); (MS / "edicoes").mkdir(exist_ok=True)
c = json.loads(CORTES.read_text())
T = Path(tempfile.mkdtemp())
proxy = MS / "brutos" / f"{ID}.mp4"
def sonda(arq):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                        "stream=color_transfer:stream_side_data=rotation", "-of", "json", str(arq)], capture_output=True, text=True)
    s = (json.loads(r.stdout or "{}").get("streams") or [{}])[0]
    rot = next((int(float(d["rotation"])) for d in s.get("side_data_list", []) if "rotation" in d), 0) % 360
    return s.get("color_transfer", ""), rot
SAIDA = ["-map", "0:v:0", "-map", "0:a:0", "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
         "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709", "-g", "30", "-c:a", "aac", "-b:a", "192k",
         "-movflags", "+faststart", str(proxy)]
if not proxy.exists():
    trc, rot = sonda(BRUTO)
    feito = False
    if trc in ("arib-std-b67", "smpte2084"):
        giro = {90: ",transpose=cclock", 270: ",transpose=clock", 180: ",hflip,vflip"}.get(rot, "")
        w, h = (1920, 1080) if rot in (90, 270) else (1080, 1920)
        vf = (f"scale_vt=w={w}:h={h}:color_matrix=bt709:color_primaries=bt709:color_transfer=bt709,hwdownload,format=p010le"
              f"{giro},fps=30,format=yuv420p,setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709")
        r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-noautorotate", "-hwaccel", "videotoolbox", "-hwaccel_output_format",
                            "videotoolbox_vld", "-i", str(BRUTO), "-vf", vf] + SAIDA)
        feito = r.returncode == 0
        if not feito:
            print(f"aviso: tonemap HDR->SDR pelo VideoToolbox falhou ({trc}); proxy sem tonemap vai sair lavado", file=sys.stderr)
    if not feito:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(BRUTO), "-vf", "scale=1080:1920,fps=30"] + SAIDA, check=True)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(BRUTO), "-vn", "-ac", "1", "-ar", "16000", str(T / "a.wav")], check=True)
for i, (a, b, _) in enumerate(c):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(a), "-to", str(b), "-i", str(T / "a.wav"), str(T / f"c{i}.wav")], check=True)
(T / "l.txt").write_text("\n".join(f"file 'c{i}.wav'" for i in range(len(c))))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-i", str(T / "l.txt"), str(T / "e.wav")], check=True)
subprocess.run(["whisper-cli", "-m", MODELO, "-l", os.environ.get("WHISPER_LINGUA", "pt"), "-ml", "1", "-sow", "-oj",
                "-of", str(T / "w"), "-np", "-f", str(T / "e.wav")], check=True, capture_output=True)
ww = [s["offsets"]["from"] / 1000 for s in json.loads((T / "w.json").read_text())["transcription"] if s["text"].strip()]
segs, words, t = [], [], 0.0
for a, b, txt in c:
    segs.append({"start": round(t, 3), "end": round(t + b - a, 3), "media_start": a, "text": txt}); t += b - a
for si, s in enumerate(segs):
    ws = [x for x in ww if s["start"] - .05 <= x < s["end"] - .05]
    toks = s["text"].split(); n = len(toks)
    for i, tok in enumerate(toks):
        st = ws[round(i * (len(ws) - 1) / max(1, n - 1))] if ws else s["start"] + (s["end"] - s["start"]) * i / n
        words.append({"w": tok, "t": round(max(st, s["start"]), 2), "seg": si})
for i in range(1, len(words)):
    if words[i]["t"] <= words[i - 1]["t"]: words[i]["t"] = round(words[i - 1]["t"] + .08, 2)
(MS / "edicoes" / f"{ID}.json").write_text(json.dumps({"segs": segs, "words": words}, ensure_ascii=False, indent=1))
print(f"ok · {ID} · {round(t, 2)}s · {len(segs)} falas · {len(words)} palavras · public/brutos/{ID}.mp4 + public/edicoes/{ID}.json")
