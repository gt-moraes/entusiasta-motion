import {AbsoluteFill} from 'remotion';
import {BrandingProvider} from '../ds/contexto';
import {BRANDINGS, type NomeBranding} from '../ds/brandings';
import type {Branding} from '../ds/tipos';
import {AreaProvider} from '../ds/formatos';
import {SomProvider} from '../ds/som';
import {Camera} from './Camera';
import {agruparLegendas, type GrupoLegenda} from './agrupar';
import {Legendas} from './Legendas';
import type {Edicao, ModoFala} from './tipos';

// Variante do ReelsEditado em TELA CHEIA (2026-10-13, reels "ChatGPT Ads"):
// a câmera ocupa 1080x1920 o tempo todo (sem painel de topo); o motion entra POR CIMA da câmera
// (texto cinético e cards no terço de cima, longe do rosto) e, quando a cena pede, em tela cheia
// de fundo claro (TelaCheia). A linguagem de animação é a mesma da skill.
// Legenda: 'peito' em cima da câmera, 'cheio' (escura) nas telas cheias.
export type PropsReelsCheio = {
  bruto: string;
  ed: Edicao;
  cheioEm?: [number, number][]; // intervalos (s) de tela cheia clara: legenda escura em 'cheio'; fora deles, branca em 'peito'
  branding?: NomeBranding | Branding;
  som?: boolean;
  manterMaiusculas?: string[];
  sobre: React.ReactNode; // peças por cima da câmera
  telaCheia?: React.ReactNode; // cenas de tela cheia (cada uma dentro de <TelaCheia>)
  ajustaLegendas?: (g: GrupoLegenda[]) => GrupoLegenda[]; // opcional: muda a altura de grupos específicos
};

export const ReelsCheio: React.FC<PropsReelsCheio> = ({bruto, ed, cheioEm = [], branding = 'apple', som = true, manterMaiusculas, sobre, telaCheia, ajustaLegendas}) => {
  const b = typeof branding === 'string' ? BRANDINGS[branding] : branding;
  const modos: ModoFala[] = ed.segs.map(() => 'peito');
  const dentro = (t: number) => cheioEm.some(([de, ate]) => t >= de - 0.05 && t < ate);
  const base = agruparLegendas(ed, modos, 3, manterMaiusculas).map((g) => (dentro(g.de) ? {...g, modo: 'cheio' as ModoFala} : g));
  const grupos = ajustaLegendas ? ajustaLegendas(base) : base;
  const claro = b.cor.fundo.toUpperCase() > '#888888';
  return (
    <BrandingProvider branding={b}>
      <SomProvider ligado={som}>
        <AbsoluteFill style={{background: '#0E0E0F'}}>
          <Camera bruto={bruto} ed={ed} deslocY={0} />
          <AreaProvider value={{largura: 1080, altura: 1920}}>
            {sobre}
            {telaCheia}
          </AreaProvider>
          <Legendas grupos={grupos} fundoClaro={claro} />
        </AbsoluteFill>
      </SomProvider>
    </BrandingProvider>
  );
};
