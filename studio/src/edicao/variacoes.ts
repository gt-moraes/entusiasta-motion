import type {Edicao} from './tipos';

// Trial reels (21/10/2026): variações do mesmo vídeo aprovado, mudando só o gancho (~3 s iniciais).
// `ordem` = índices ORIGINAIS das falas na ordem nova. Serve pra puxar uma frase forte de outro trecho
// pro começo ([15, ...resto]) ou cortar a abertura (todas.slice(1)). As palavras andam junto com a fala.
export const reordena = (base: Edicao, ordem: number[]): Edicao => {
  const segs: Edicao['segs'] = [];
  const words: Edicao['words'] = [];
  let t = 0;
  ordem.forEach((o, i) => {
    const s = base.segs[o];
    const d = s.end - s.start;
    segs.push({...s, start: t, end: t + d});
    base.words.filter((w) => w.seg === o).forEach((w) => words.push({...w, t: Math.round((w.t - s.start + t) * 1000) / 1000, seg: i}));
    t += d;
  });
  return {segs, words};
};

// Índice novo de uma fala original (pra momento()/T() continuarem falando o índice do json).
export const posicao = (ordem: number[], original: number) => {
  const i = ordem.indexOf(original);
  if (i === -1) throw new Error(`fala ${original} não está nesta variação`);
  return i;
};

export const todas = (n: number) => Array.from({length: n}, (_, i) => i);
