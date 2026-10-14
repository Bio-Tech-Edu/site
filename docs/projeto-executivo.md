# Projeto Executivo: Portal Bio+Tech EduDesign

**Site estático de apresentação da marca e catálogo de OAD/REA**

| | |
|:---|:---|
| **Versão** | 1.0 (14/10/2026) |
| **Responsável** | Prof.ª Pâmella Araújo Balcaçar · Bio+Tech EduDesign |
| **Repositório alvo** | `Bio-Tech-Edu/site` (já criado, vazio em 13/10/2026) |
| **Endereço previsto** | `https://bio-tech-edu.github.io/site/` |
| **Stack** | HTML5 · CSS3 · JavaScript puro · sem build, sem framework, sem CDN |
| **Hospedagem** | GitHub Pages (branch `main`, pasta raiz) |
| **Licença sugerida** | MIT para o código · CC BY 4.0 para textos e imagens autorais (ver [ADR-09](#3-decisões-de-arquitetura)) |

> **Como usar este documento.** As seções 1 a 8 definem *o quê* e *como* (decisões, design, arquitetura, dados). A seção 9 organiza o trabalho em **7 sprints**, cada um com seus **prompts pronto[...]

## Sumário

1. [Visão executiva](#1-visão-executiva)
2. [Diagnóstico do ecossistema](#2-diagnóstico-do-ecossistema)
3. [Decisões de arquitetura](#3-decisões-de-arquitetura)
4. [Identidade visual e design](#4-identidade-visual-e-design)
5. [Arquitetura da informação](#5-arquitetura-da-informação)
6. [Arquitetura técnica](#6-arquitetura-técnica)
7. [Estrutura de arquivos](#7-estrutura-de-arquivos)
8. [Modelo de dados e catálogo](#8-modelo-de-dados-e-catálogo)
9. [Plano de sprints](#9-plano-de-sprints)
   - [Sprint 0: Fundação e descoberta](#sprint-0-fundação-e-descoberta)
   - [Sprint 1: Design system e esqueleto](#sprint-1-design-system-e-esqueleto)
   - [Sprint 2: Hero e marca](#sprint-2-hero-e-marca)
   - [Sprint 3: Catálogo de OAD/REA](#sprint-3-catálogo-de-oadrea)
   - [Sprint 4: Trilha, metodologia e comunidade](#sprint-4-trilha-metodologia-e-comunidade)
   - [Sprint 5: Acessibilidade, desempenho e SEO](#sprint-5-acessibilidade-desempenho-e-seo)
   - [Sprint 6: QA, CI e lançamento](#sprint-6-qa-ci-e-lançamento)
10. [Qualidade e critérios de aceite](#10-qualidade-e-critérios-de-aceite)
11. [Deploy e operação](#11-deploy-e-operação)
12. [Riscos e pendências](#12-riscos-e-pendências)
13. [Anexos](#13-anexos)

---

## 1. Visão executiva

### 1.1 Objetivo

Criar o **portal oficial da marca Bio+Tech EduDesign**: uma página estática, moderna e acolhedora que (a) apresenta a marca, sua missão e seus princípios e (b) reúne, num **catálogo de cards**, [...]

### 1.2 Escopo

| Dentro do escopo | Fora do escopo (nesta versão) |
|:---|:---|
| Página inicial única (*one-page*) com 6 seções | Backend, banco de dados, login |
| Catálogo data-driven com busca e filtros | Coleta de dados pessoais de visitantes |
| Trilha visual das lições 17 a 28 | Reescrever ou migrar os OAD existentes |
| Páginas `privacidade.html` e `404.html` | Blog, newsletter, comentários |
| Tema claro e escuro, responsivo, acessível | Analytics de terceiros (opcional e desativado por padrão) |
| Scripts de validação e CI no GitHub Actions | Novo recurso pedagógico (ex.: `meu_dia_em_passos` entra só como backlog) |

### 1.3 Públicos

| Público | O que procura | Como o portal atende |
|:---|:---|:---|
| **Estudantes do Ensino Médio (rede pública de MT)** | Achar a aula certa e abrir rápido, no celular | Catálogo por lição, cartões grandes, abertura em 1 toque |
| **Professores(as)** | Recursos prontos para sala, licença clara | Filtros por tema, descrição pedagógica, selo de licença em cada card |
| **Gestão e parceiros (SEDUC, UFMT, comunidade)** | Entender a marca e o impacto | Seção da marca, números do ecossistema, contato |
| **Colaboradores (devs, designers, pesquisadores)** | Como contribuir | Seção comunidade com links para `CONTRIBUTING`, issues e discussões |

### 1.4 Metas mensuráveis

| Indicador | Meta |
|:---|:---|
| Lighthouse (mobile): Desempenho / Acessibilidade / Boas práticas / SEO | ≥ 95 / 100 / 100 / 100 |
| LCP / CLS / INP (simulado 4G) | ≤ 2,5 s / ≤ 0,1 / ≤ 200 ms |
| Peso inicial (HTML + CSS + JS + fontes, sem miniaturas) | ≤ 250 KB comprimido |
| JavaScript total | ≤ 30 KB minificado |
| Contraste e navegação | WCAG 2.2 nível AA, uso completo por teclado |
| Links do catálogo quebrados no CI | 0 |
| Cards com descrição curta (≤ 140 caracteres) | 10 de 10 |

### 1.5 Premissas

1. O repositório `Bio-Tech-Edu/site` é o destino (ver [ADR-01](#3-decisões-de-arquitetura)). Se a decisão for outra, só a URL base muda, pois todos os caminhos são relativos.
2. Os 10 OAD continuam hospedados em seus próprios repositórios; o portal **só aponta** para eles.
3. As imagens da marca fornecidas (`favicon.png` 600×600 com transparência e `hero.png` 1667×584) são a fonte oficial de logotipo e banner.
4. A autoria dos textos institucionais é da Prof.ª Pâmella; o conteúdo da seção "A marca" usa o texto público do README do perfil da organização e deve ser **revisado por ela** antes da publi[...]

---

## 2. Diagnóstico do ecossistema

Verificação feita em **13/10/2026** (repositório + página publicada de cada OAD).

### 2.1 Inventário dos 10 repositórios

| # | Repositório | Lição | Conteúdo | Página publicada | Status |
|:-:|:---|:---:|:---|:---|:---|
| 1 | `chemical-royale` | 17–19 | Arena gamificada: átomo, tabela periódica e ligações, funções inorgânicas, Duelo Final | `/chemical-royale/` | Publicado |
| 2 | `chemical-royale-v2` | 20–21 (planejado) | Continuação da Arena: Cálculos Químicos e Radioatividade | `/chemical-royale-v2/` | **Repositório vazio, página retorna 404** |
| 3 | `pre-enem-quimica` | 20 + Aulão | Quests: Cálculos Químicos; Química Orgânica e Solubilidade | `/pre-enem-quimica/` | Publicado |
| 4 | `solucoes` | 22 | Estudo das Soluções, laboratório virtual de diluição | `/solucoes/` | Publicado |
| 5 | `termoquimica` | 23 | Termoquímica, Calorímetro Virtual, Lei de Hess | `/termoquimica/` | Publicado |
| 6 | `cinetica` | 24 | Cinética Química, colisões, catálise | `/cinetica/` | Publicado |
| 7 | `equilibrio` | 25 | Equilíbrio Químico, simulador de Le Chatelier | `/equilibrio/` | Publicado |
| 8 | `eletroquimica` | 26 | Pilhas, corrosão, eletrólise, Faraday, Fato ou Fake | `/eletroquimica/` | Publicado |
| 9 | `org` | 27–28 | Química Orgânica: hibridação, IUPAC, destilação, Cornell Notes | `/org/` | Publicado |
| 10 | `enem` | n/a | Raio-X do ENEM: painéis dos dois dias, checklists | `/enem/` | Publicado |

Todas as páginas ficam sob `https://bio-tech-edu.github.io/<repositório>/`.

### 2.2 Outros repositórios da organização

| Repositório | Papel | Tratamento |
|:---|:---|:---|
| `site` | Portal (este projeto) | **Repositório alvo** |
| `.github` | README do perfil da organização e imagens da marca | Atualizar no lançamento para apontar ao portal |
| `meu_dia_em_passos` | Planner (PDF e versão web) | Fora do catálogo inicial; ver backlog na seção 12 |

### 2.3 Achados que afetam o projeto

| ID | Achado | Impacto | Ação |
|:--:|:---|:---|:---|
| A1 | `chemical-royale-v2` está vazio e a página dá 404, mas o README de `solucoes` já linka para ele | Link quebrado público | Card com status **Em construção**, sem botão de abrir |
| A2 | A Lição 20 aparece em dois repositórios (`pre-enem-quimica` publicado, `chemical-royale-v2` planejado) | Confusão de numeração | Catálogo mostra `pre-enem-quimica` como Lição 20 public[...]
| A3 | READMEs com endereços antigos: `chemical-royale-edu`, `pre-enem-quimica-equilibrio`, caminho com acento em `eletroquimica`; `cinetica` linka "Estudo das Soluções" para `pre-enem-quimica` | V[...]
| A4 | `org` tem nome genérico e README com licença indefinida, imagens de `via.placeholder.com` e uma frase residual de assistente de IA no final | Primeira impressão fraca no repositório | Limpa[...]
| A5 | Seis repositórios sem descrição, tópicos e site no "About" (`termoquimica`, `solucoes`, `cinetica`, `equilibrio`, `eletroquimica`, `chemical-royale-v2`) | Pior descoberta e SEO | Preencher [...]
| A6 | O perfil da organização lista só 4 OAD | Vitrine desatualizada | Atualizar com os 10 e o link do portal |
| A7 | `eletroquimica` usa badges, hero e um avatar em SVG provisórios (README informa) | Miniatura de baixa qualidade | Usar miniatura própria do portal (Sprint 3) |
| A8 | O Chemical Royale pede nome, e-mail institucional, cidade e escola ao estudante | Dado pessoal de estudantes | `privacidade.html` explica; portal em si **não coleta nada** |
| A9 | Os OAD exibem a marca do Governo de MT/SEDUC como apoio institucional | Uso de marca pública | Confirmar autorização antes de usar o logotipo no portal; começar com texto "Apoio institucion[...]
| A10 | O repositório `site` foi criado hoje e está vazio | Nada a migrar | Começar do zero na Sprint 0 |
| A11 | Três repositórios não têm arquivo de licença (`pre-enem-quimica`, `org`, `chemical-royale-v2`); os outros sete usam MIT | Reuso do REA sem regra clara; o selo "licença aberta" não vale [...]

---

## 3. Decisões de arquitetura

Registro curto no formato ADR (decisão, motivo, consequência). Todas podem ser revistas na Sprint 0.

| ID | Decisão | Motivo | Consequência |
|:--:|:---|:---|:---|
| **ADR-01** | Repositório alvo `Bio-Tech-Edu/site`, publicado em `/site/` | Já existe, com a descrição "Portal dedicado a apresentar os OAD"; não depende de renomear nada | Para usar a raiz `bio[...]
| **ADR-02** | JavaScript clássico (sem ES modules), dados como variável global | Mesmo padrão dos OAD existentes: abre por duplo clique em `file://` sem erro de CORS | Sem `import`/`export`; um ob[...]
| **ADR-03** | Catálogo orientado a dados em `data/catalogo.js` | Adicionar um OAD = adicionar 1 objeto, sem tocar em HTML | Validação automática do esquema no CI |
| **ADR-04** | Caminhos 100% relativos | Funciona em `/site/`, na raiz da organização ou em domínio próprio | Proibido `href="/..."` |
| **ADR-05** | Zero CDN e zero terceiros; fontes e ícones **auto-hospedados** | LGPD (sem vazar IP de estudantes), funciona offline, desempenho previsível | Fontes `.woff2` e ícones SVG ficam no re[...]
| **ADR-06** | Deploy por branch `main` na raiz (+ `.nojekyll`); Actions só para QA | Igual ao fluxo dos outros repositórios; menos peças para quebrar | O CI não publica, apenas valida |
| **ADR-07** | Miniaturas **copiadas e otimizadas** (WebP) para `assets/img/oad/` | Link direto para imagem de outro repositório quebra se ele mudar | Script de otimização documentado na Sprint 3 |
| **ADR-08** | Tema claro e escuro por tokens CSS; segue o sistema e tem alternador | Acessibilidade e conforto em sala escura ou projetor | Dois conjuntos de tokens validados para contraste |
| **ADR-09** | Licenças: MIT (código) e CC BY 4.0 (textos e imagens autorais) | 7 dos 10 OAD já usam MIT (os outros 3 estão sem licença, achado A11); REA pede licença aberta explícita para cont[...]

---

## 4. Identidade visual e design

### 4.1 Conceito: "Do DNA ao circuito"

O logotipo une uma **dupla hélice de DNA** (biologia) a **trilhas de circuito** que sobem em direção a uma seta (tecnologia e progresso). O portal traduz isso em três gestos visuais:

1. **Hero** com uma hélice em SVG cujas fitas se transformam em linhas de circuito com nós laranja (animação suave, desligada se o usuário prefere menos movimento).
2. **Cards** de cantos generosos com borda em gradiente turquesa→laranja ao passar o mouse ou focar, como um "circuito que acende".
3. **Trilha das lições** desenhada como um **mapa de progresso** com nós numerados (17 a 28), eco da gamificação dos OAD (XP, missões, badges).

Estilo-guia da marca: **Soft Tech / Clean Modernism**: tecnologia humana, acessível, com brilho sutil, muito respiro e pouca decoração.

### 4.2 Paleta

Cores de marca **amostradas do logotipo** (`favicon.png`) e ampliadas em escalas com contraste verificado.

| Token | Hex | Uso |
|:---|:---:|:---|
| `--navy-950` | `#061629` | Fundo do tema escuro |
| `--navy-900` | `#0B2747` | Superfícies escuras, rodapé |
| `--navy-700` | `#123A68` | **Azul-marinho da marca**: títulos, anel do logotipo, botões primários |
| `--navy-600` | `#1B5192` | Links em fundo claro, foco |
| `--teal-500` | `#2DC3BF` | **Turquesa da marca**: destaques, ícones, fitas do DNA |
| `--teal-600` | `#1AA39F` | Bordas e ícones (nunca texto pequeno em fundo branco) |
| `--teal-700` | `#0A716E` | Texto turquesa em fundo claro |
| `--teal-300` | `#7FE0DB` | Texto e ícones turquesa em fundo escuro |
| `--orange-500` | `#F47C26` | **Laranja da marca**: nós do circuito, selos, CTA em fundo escuro |
| `--orange-700` | `#A94F05` | Texto laranja em fundo claro |
| `--mist-50` / `--mist-100` | `#F3FAFB` / `#E3F2F4` | Fundos claros alternados |
| `--ink` | `#0D1B2A` | Texto principal no claro |
| `--slate` | `#44566A` | Texto secundário no claro |
| `--text-dark` / `--muted-dark` | `#E8F1F7` / `#A9BBCB` | Texto principal e secundário no escuro |

**Contraste calculado (WCAG 2.x):**

| Par (texto sobre fundo) | Razão | Nível |
|:---|:---:|:---:|
| `--ink` sobre branco | 17,39 | AAA |
| `--slate` sobre branco | 7,54 | AAA |
| `--navy-700` sobre branco | 11,47 | AAA |
| `--teal-700` sobre branco | 5,83 | AA |
| `--teal-700` sobre `--mist-100` (pior caso do tema claro) | 5,08 | AA |
| `--orange-700` sobre branco | 5,52 | AA |
| Branco sobre `--navy-700` | 11,47 | AAA |
| Branco sobre `--teal-700` | 5,83 | AA |
| `--navy-900` sobre `--teal-500` (botão turquesa) | 6,93 | AA |
| `--navy-900` sobre `--orange-500` (botão laranja) | 5,56 | AA |
| `--teal-300` sobre `--navy-950` | 11,77 | AAA |
| `--orange-500` sobre `--navy-950` | 6,72 | AA |
| `--text-dark` sobre `--navy-950` | 15,90 | AAA |
| `--muted-dark` sobre `--navy-950` | 9,23 | AAA |

> **Verificação automática:** `scripts/checar-contraste.mjs` (Sprint 1) recalcula estes pares e todos os papéis semânticos (`--text`, `--text-muted`, `--heading`, `--link`, `--accent`, `--accent-[...]

> **Regras decorrentes:** `--orange-500` sobre branco dá 2,71 (**reprova**), então no tema claro o laranja é só decorativo ou texto em `--orange-700`. `--teal-600` sobre branco dá 3,10 e serve ap[...]

### 4.3 Tokens CSS (arquivo `css/tokens.css`)

```css
:root {
  /* Cor: marca */
  --navy-950:#061629; --navy-900:#0B2747; --navy-700:#123A68; --navy-600:#1B5192;
  --teal-300:#7FE0DB; --teal-500:#2DC3BF; --teal-600:#1AA39F; --teal-700:#0A716E;
  --orange-500:#F47C26; --orange-700:#A94F05;
  --mist-50:#F3FAFB; --mist-100:#E3F2F4; --ink:#0D1B2A; --slate:#44566A;

  /* Cor: papéis semânticos (tema claro) */
  --bg: var(--mist-50);
  --surface: #FFFFFF;
  --surface-alt: var(--mist-100);
  --text: var(--ink);
  --text-muted: var(--slate);
  --heading: var(--navy-700);
  --link: var(--navy-600);
  --accent: var(--teal-700);
  --accent-warm: var(--orange-700);
  --border: #CFE3E7;
  --focus: var(--navy-600);

  /* Tipografia */
  --font-display: "Sora", system-ui, "Segoe UI", sans-serif;
  --font-body: "Figtree", system-ui, "Segoe UI", sans-serif;
  --fs-0: clamp(1rem, 0.96rem + 0.2vw, 1.0625rem);   /* corpo */
  --fs-1: clamp(1.125rem, 1.05rem + 0.4vw, 1.3rem);
  --fs-2: clamp(1.35rem, 1.2rem + 0.8vw, 1.75rem);
  --fs-3: clamp(1.75rem, 1.4rem + 1.8vw, 2.6rem);
  --fs-4: clamp(2.2rem, 1.6rem + 3.2vw, 4rem);        /* título do hero */

  /* Espaço, forma, sombra */
  --sp-1:.25rem; --sp-2:.5rem; --sp-3:.75rem; --sp-4:1rem; --sp-5:1.5rem;
  --sp-6:2rem; --sp-7:3rem; --sp-8:4.5rem; --sp-9:7rem;
  --radius-s:10px; --radius-m:16px; --radius-l:24px; --radius-pill:999px;
  --shadow-1: 0 1px 2px rgb(11 39 71 / .08), 0 4px 12px rgb(11 39 71 / .06);
  --shadow-2: 0 2px 4px rgb(11 39 71 / .08), 0 14px 32px rgb(11 39 71 / .12);
  --container: 72rem;
  --header-h: 4.25rem;
}

/* Tema escuro: automático pelo sistema ou forçado pelo alternador */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) { --bg:var(--navy-950); --surface:var(--navy-900);
    --surface-alt:#0E3156; --text:#E8F1F7; --text-muted:#A9BBCB; --heading:#FFFFFF;
    --link:var(--teal-300); --accent:var(--teal-300); --accent-warm:var(--orange-500);
    --border:#1D4572; --focus:var(--teal-300); }
}
:root[data-theme="dark"] { --bg:var(--navy-950); --surface:var(--navy-900);
  --surface-alt:#0E3156; --text:#E8F1F7; --text-muted:#A9BBCB; --heading:#FFFFFF;
  --link:var(--teal-300); --accent:var(--teal-300); --accent-warm:var(--orange-500);
  --border:#1D4572; --focus:var(--teal-300); }
```

### 4.4 Tipografia

| Papel | Fonte | Pesos | Observação |
|:---|:---|:---:|:---|
| Títulos e *display* | **Sora** (OFL) | 600, 700 | Geométrica, próxima ao peso do logotipo |
| Texto e interface | **Figtree** (OFL) | 400, 500, 700 | Leitura confortável em tela pequena |

- **Auto-hospedadas** em `assets/fonts/` (`.woff2`, subconjunto latino com acentos do português), `font-display: swap`, pilha de reserva com `system-ui`.
- Escala fluida com `clamp()`; entrelinha 1,6 no corpo; largura de leitura máxima de 70 caracteres.
- Nunca usar texto em imagem para informação essencial.

### 4.5 Componentes

| Componente | Especificação |
|:---|:---|
| **Botão primário** | Fundo `--navy-700`, texto branco, raio pill, altura mínima 44 px, foco com anel de 3 px `--focus` e deslocamento de 2 px |
| **Botão destaque (CTA)** | Fundo `--teal-500`, texto `--navy-900`; no escuro, fundo `--orange-500` com texto `--navy-950` |
| **Botão secundário** | Contorno 2 px `--navy-700`, fundo transparente |
| **Chip de filtro** | Pill 40 px, `aria-pressed`, marcado = fundo `--navy-700` e texto branco |
| **Selo de lição** | Pill pequena com "LIÇÃO 23" (versalete), fundo `--surface-alt`, borda `--teal-600` |
| **Selo de status** | "Publicado" (turquesa), "Em construção" (laranja, com ícone, nunca só cor) |
| **Card de OAD** | Ver 4.6 |
| **Nó da trilha** | Círculo 56 px com o número da lição; ativo = anel laranja; "em construção" = tracejado |
| **Alternador de tema** | Botão com `aria-label` dinâmico ("Ativar tema escuro") e estado persistido em `localStorage` (com `try/catch`) |

### 4.6 Anatomia do card de OAD

```
┌────────────────────────────────────┐
│  [ miniatura 16:10, WebP, lazy ]   │  alt descritivo
│  (LIÇÃO 23)        (● Publicado)   │  selos sobre a imagem, canto inferior
├────────────────────────────────────┤
│  Termoquímica                      │  h3, --fs-1, --heading
│  Endo e exotermia, entalpia, Lei   │  DESCRIÇÃO CURTA (≤ 140 car.),
│  de Hess e combustíveis, com       │  --text-muted, máx. 3 linhas
│  Calorímetro Virtual e questões…   │
│  #Físico-química  #ENEM            │  tags (até 3)
│  [ Abrir aula ↗ ]  [ Código ⌥ ]    │  CTA principal + link do repositório
└────────────────────────────────────┘
```

- O **card inteiro é clicável** via link esticado (`::after`) no botão principal, sem aninhar links; o link do repositório fica acima com `position: relative; z-index: 1`.
- Em "Em construção", o botão principal vira texto "Em breve" desabilitado (`aria-disabled="true"`), sem `href`.
- Hover/foco: elevação `--shadow-2` e borda em gradiente turquesa→laranja (via `background-clip`), sem mudar o tamanho (evita CLS).

### 4.7 Movimento

| Elemento | Comportamento | Regra |
|:---|:---|:---|
| Hero (hélice → circuito) | Desenho progressivo das linhas (`stroke-dashoffset`), 6 s, uma vez | Desligado em `prefers-reduced-motion: reduce` |
| Entrada dos cards | Fade + 12 px de subida ao entrar na tela (`IntersectionObserver`) | Idem; sem observer, aparece direto |
| Barra de progresso de rolagem | Linha de 3 px no topo, turquesa→laranja (eco da barra de XP) | Decorativa, `aria-hidden` |

### 4.8 Imagens e ícones

- **Logotipo:** `favicon.png` (circular, 600×600) convertido em WebP (512×512) e PNG, com fundo transparente preservado. O cabeçalho combina o logotipo circular com o nome "Bio+Tech EduDesign" em t[...]
- **Banner:** `hero.png` (1667×584) vira imagem de compartilhamento (Open Graph 1200×630, JPEG ≤ 200 KB): remove-se a borda arredondada de 4 px e faz-se um recorte central na proporção 1200:630 [...]
- **Miniaturas dos OAD:** 640×400, WebP, ≤ 60 KB; fallback gerado (gradiente com a inicial) se faltar imagem.
- **Ícones:** SVG inline do próprio projeto (traço de 1,75 px, cantos arredondados). Sem biblioteca externa. Emojis só em texto decorativo, nunca como único portador de significado.

### 4.9 Tom de voz

Acolhedor, direto, científico sem jargão desnecessário. Segunda pessoa ("você"), verbos de ação ("Abra a aula"), linguagem inclusiva com formas duplas apenas quando preciso ("pessoa educadora").[...]

---

## 5. Arquitetura da informação

### 5.1 Mapa do site

```
index.html  (one-page)
├── #topo ........... cabeçalho fixo + hero
├── #marca .......... A marca (missão, visão, princípios, quem está por trás)
├── #catalogo ....... Catálogo de OAD/REA (busca, filtros, 10 cards)
├── #trilha ......... Trilha Pré-ENEM Química (lições 17 a 28)
├── #metodologia .... Metodologias ativas e rigor pedagógico
├── #comunidade ..... REA, licenças e como contribuir
└── #contato ........ Contato e rodapé
privacidade.html .... Política de privacidade (LGPD)
404.html ............ Página não encontrada, com atalho ao catálogo
```

### 5.2 Menu (cabeçalho fixo, altura 68 px)

`A marca` · `Catálogo` · `Trilha` · `Metodologia` · `Comunidade` · `Contato` · [alternador de tema]. No celular: botão "Menu" abre painel de tela cheia com foco preso e `Esc` para fechar. Prim[...]

### 5.3 Wireframe textual das seções

| Seção | Conteúdo | Componentes |
|:---|:---|:---|
| Seção | Conteúdo | Componentes |
