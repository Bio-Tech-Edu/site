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

> **Como usar este documento.** As seções 1 a 8 definem *o quê* e *como* (decisões, design, arquitetura, dados). A seção 9 organiza o trabalho em **7 sprints**, cada um com seus **prompts prontos**, **arquivos de saída** e **critérios de aceite**. As seções 10 a 13 fecham qualidade, deploy, riscos e anexos. Todos os dados do catálogo foram **conferidos nos repositórios e nas páginas publicadas em 13/10/2026**.

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

Criar o **portal oficial da marca Bio+Tech EduDesign**: uma página estática, moderna e acolhedora que (a) apresenta a marca, sua missão e seus princípios e (b) reúne, num **catálogo de cards**, todos os Objetos de Aprendizagem Digitais (OAD) e Recursos Educacionais Abertos (REA) hoje espalhados em 10 repositórios, cada um com uma **breve descrição abaixo do card**.

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
4. A autoria dos textos institucionais é da Prof.ª Pâmella; o conteúdo da seção "A marca" usa o texto público do README do perfil da organização e deve ser **revisado por ela** antes da publicação.

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
| A2 | A Lição 20 aparece em dois repositórios (`pre-enem-quimica` publicado, `chemical-royale-v2` planejado) | Confusão de numeração | Catálogo mostra `pre-enem-quimica` como Lição 20 publicada |
| A3 | READMEs com endereços antigos: `chemical-royale-edu`, `pre-enem-quimica-equilibrio`, caminho com acento em `eletroquimica`; `cinetica` linka "Estudo das Soluções" para `pre-enem-quimica` | Visitantes caem em páginas erradas | Portal usa só as URLs verificadas; corrigir READMEs (Sprint 6) |
| A4 | `org` tem nome genérico e README com licença indefinida, imagens de `via.placeholder.com` e uma frase residual de assistente de IA no final | Primeira impressão fraca no repositório | Limpar README antes do lançamento; **não renomear** (quebraria a URL `/org/`) |
| A5 | Seis repositórios sem descrição, tópicos e site no "About" (`termoquimica`, `solucoes`, `cinetica`, `equilibrio`, `eletroquimica`, `chemical-royale-v2`) | Pior descoberta e SEO | Preencher em lote (Sprint 6); textos prontos na seção 8 |
| A6 | O perfil da organização lista só 4 OAD | Vitrine desatualizada | Atualizar com os 10 e o link do portal |
| A7 | `eletroquimica` usa badges, hero e um avatar em SVG provisórios (README informa) | Miniatura de baixa qualidade | Usar miniatura própria do portal (Sprint 3) |
| A8 | O Chemical Royale pede nome, e-mail institucional, cidade e escola ao estudante | Dado pessoal de estudantes | `privacidade.html` explica; portal em si **não coleta nada** |
| A9 | Os OAD exibem a marca do Governo de MT/SEDUC como apoio institucional | Uso de marca pública | Confirmar autorização antes de usar o logotipo no portal; começar com texto "Apoio institucional" |
| A10 | O repositório `site` foi criado hoje e está vazio | Nada a migrar | Começar do zero na Sprint 0 |
| A11 | Três repositórios não têm arquivo de licença (`pre-enem-quimica`, `org`, `chemical-royale-v2`); os outros sete usam MIT | Reuso do REA sem regra clara; o selo "licença aberta" não vale para os 10 | Catálogo registra `"a definir"` nesses três; a autora escolhe a licença e o arquivo `LICENSE` é adicionado (Sprint 6) |

---

## 3. Decisões de arquitetura

Registro curto no formato ADR (decisão, motivo, consequência). Todas podem ser revistas na Sprint 0.

| ID | Decisão | Motivo | Consequência |
|:--:|:---|:---|:---|
| **ADR-01** | Repositório alvo `Bio-Tech-Edu/site`, publicado em `/site/` | Já existe, com a descrição "Portal dedicado a apresentar os OAD"; não depende de renomear nada | Para usar a raiz `bio-tech-edu.github.io`, basta criar o repo `bio-tech-edu.github.io` e copiar os arquivos, sem alterar código |
| **ADR-02** | JavaScript clássico (sem ES modules), dados como variável global | Mesmo padrão dos OAD existentes: abre por duplo clique em `file://` sem erro de CORS | Sem `import`/`export`; um objeto global `BTE` organiza o código |
| **ADR-03** | Catálogo orientado a dados em `data/catalogo.js` | Adicionar um OAD = adicionar 1 objeto, sem tocar em HTML | Validação automática do esquema no CI |
| **ADR-04** | Caminhos 100% relativos | Funciona em `/site/`, na raiz da organização ou em domínio próprio | Proibido `href="/..."` |
| **ADR-05** | Zero CDN e zero terceiros; fontes e ícones **auto-hospedados** | LGPD (sem vazar IP de estudantes), funciona offline, desempenho previsível | Fontes `.woff2` e ícones SVG ficam no repositório |
| **ADR-06** | Deploy por branch `main` na raiz (+ `.nojekyll`); Actions só para QA | Igual ao fluxo dos outros repositórios; menos peças para quebrar | O CI não publica, apenas valida |
| **ADR-07** | Miniaturas **copiadas e otimizadas** (WebP) para `assets/img/oad/` | Link direto para imagem de outro repositório quebra se ele mudar | Script de otimização documentado na Sprint 3 |
| **ADR-08** | Tema claro e escuro por tokens CSS; segue o sistema e tem alternador | Acessibilidade e conforto em sala escura ou projetor | Dois conjuntos de tokens validados para contraste |
| **ADR-09** | Licenças: MIT (código) e CC BY 4.0 (textos e imagens autorais) | 7 dos 10 OAD já usam MIT (os outros 3 estão sem licença, achado A11); REA pede licença aberta explícita para conteúdo | Arquivo `LICENSE` e seção "Licença" no rodapé; **confirmar com a autora** |

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

> **Verificação automática:** `scripts/checar-contraste.mjs` (Sprint 1) recalcula estes pares e todos os papéis semânticos (`--text`, `--text-muted`, `--heading`, `--link`, `--accent`, `--accent-warm`) sobre `--bg`, `--surface` e `--surface-alt`, nos dois temas. Na primeira conferência, `--teal-700` original (`#0C7C79`) deu 4,38 sobre `--mist-100` e foi escurecido para `#0A716E`.

> **Regras decorrentes:** `--orange-500` sobre branco dá 2,71 (**reprova**), então no tema claro o laranja é só decorativo ou texto em `--orange-700`. `--teal-600` sobre branco dá 3,10 e serve apenas a ícones e bordas.

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

- **Logotipo:** `favicon.png` (circular, 600×600) convertido em WebP (512×512) e PNG, com fundo transparente preservado. O cabeçalho combina o logotipo circular com o nome "Bio+Tech EduDesign" em texto (Sora 700), sem imagem horizontal; um SVG só entra se a autora fornecer o arquivo vetorial original.
- **Banner:** `hero.png` (1667×584) vira imagem de compartilhamento (Open Graph 1200×630, JPEG ≤ 200 KB): remove-se a borda arredondada de 4 px e faz-se um recorte central na proporção 1200:630 (≈ 1097×576 px; mantém o DNA, os livros, o notebook e o nome), redimensionado para 1200×630. Testado: ~90 KB. Opcionalmente serve de fundo discreto do hero.
- **Miniaturas dos OAD:** 640×400, WebP, ≤ 60 KB; fallback gerado (gradiente com a inicial) se faltar imagem.
- **Ícones:** SVG inline do próprio projeto (traço de 1,75 px, cantos arredondados). Sem biblioteca externa. Emojis só em texto decorativo, nunca como único portador de significado.

### 4.9 Tom de voz

Acolhedor, direto, científico sem jargão desnecessário. Segunda pessoa ("você"), verbos de ação ("Abra a aula"), linguagem inclusiva com formas duplas apenas quando preciso ("pessoa educadora"). Sem promessas de nota ou aprovação.

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

`A marca` · `Catálogo` · `Trilha` · `Metodologia` · `Comunidade` · `Contato` · [alternador de tema]. No celular: botão "Menu" abre painel de tela cheia com foco preso e `Esc` para fechar. Primeiro elemento da página: **link "Pular para o conteúdo"**.

### 5.3 Wireframe textual das seções

| Seção | Conteúdo | Componentes |
|:---|:---|:---|
| **Hero** | Logotipo, título "Ciência aberta, gamificada e bonita de aprender", subtítulo (1 frase), 2 CTAs ("Explorar o catálogo", "Conhecer a marca"), faixa de números | Hélice→circuito animada, botões, métricas |
| **A marca** | Texto de origem, missão e visão (2 colunas), 6 princípios, "Quem está por trás" | Cards de princípio, bloco de bio |
| **Catálogo** | Busca por texto, chips de **tema** e **formato**, ordenação (por lição, por nome), contador "Mostrando N de 10", grade de cards, estado vazio | Campo de busca, chips, grade 1/2/3 colunas |
| **Trilha** | Linha do tempo horizontal (rolável no celular) com nós de 17 a 28, cada nó leva ao card | Nós, conectores, legenda de status |
| **Metodologia** | ABP, Gamificação, Storytelling, Simuladores, Fato ou Fake, Cornell Notes, feedback duplo | Cards pequenos com ícone e 1 frase |
| **Comunidade** | O que é REA, licença, tabela "Como contribuir", link para issues e discussões, badges de reconhecimento | Tabela, botões |
| **Contato** | E-mail da marca, perfil no GitHub, nota sobre apoio institucional | Links, rodapé |

### 5.4 Faixa de números do hero

Calculados a partir do `catalogo.js` (nunca digitados à mão): **OAD no catálogo** (10), **lições publicadas** (11 das 12 planejadas, de 17 a 28; a Lição 21 ainda está em construção), **OAD com simuladores ou laboratórios virtuais** (5, pela contagem do campo `recursos`) e **licença MIT** (7 de 10; os três restantes aparecem como "licença a definir" até a autora decidir, achado A11). Se um valor mudar no catálogo, o número muda sozinho.

---

## 6. Arquitetura técnica

### 6.1 Camadas

| Camada | Tecnologia | Regra |
|:---|:---|:---|
| **Estrutura** | HTML5 semântico (`header`, `nav`, `main`, `section`, `article`, `footer`) | Um `h1`; `h2` por seção; `h3` por card; `lang="pt-BR"` |
| **Apresentação** | CSS3: custom properties, Grid, Flexbox, `clamp()`, `@layer`, `:focus-visible`, `prefers-*` | Sem pré-processador; ordem de camadas `reset, tokens, base, layout, components, sections, utilities` |
| **Comportamento** | JavaScript puro, scripts clássicos com `defer`, um espaço de nomes global `BTE` | Sem `import`/`export` (compatível com `file://`); cada arquivo é uma função autoexecutável |
| **Dados** | `data/catalogo.js` define `window.BTE_CATALOGO` e `window.BTE_META` | Única fonte de verdade do catálogo, da trilha e dos números do hero |

### 6.2 Ordem de carregamento (`index.html`)

```html
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Bio+Tech EduDesign | Ciência aberta, gamificada e bonita de aprender</title>
  <meta name="description" content="Portal da marca Bio+Tech EduDesign: catálogo de objetos de aprendizagem digitais de Química para o ENEM, abertos e gratuitos.">
  <meta http-equiv="Content-Security-Policy"
        content="default-src 'self'; img-src 'self' data:; font-src 'self'; style-src 'self'; script-src 'self'; base-uri 'none'; form-action 'none'">
  <link rel="canonical" href="https://bio-tech-edu.github.io/site/">
  <link rel="icon" href="assets/logo/favicon.ico" sizes="any">
  <link rel="icon" href="assets/logo/icon-192.png" type="image/png" sizes="192x192">
  <link rel="apple-touch-icon" href="assets/logo/apple-touch-icon.png">
  <link rel="manifest" href="manifest.webmanifest">
  <link rel="preload" href="assets/fonts/sora-700.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="assets/fonts/figtree-400.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="css/tokens.css">
  <link rel="stylesheet" href="css/base.css">
  <link rel="stylesheet" href="css/layout.css">
  <link rel="stylesheet" href="css/components.css">
  <link rel="stylesheet" href="css/sections.css">
  <script src="js/theme-init.js"></script>        <!-- bloqueante, ~300 bytes: evita "flash" de tema -->
  <script src="data/catalogo.js" defer></script>
  <script src="js/util.js" defer></script>
  <script src="js/nav.js" defer></script>
  <script src="js/theme.js" defer></script>
  <script src="js/catalogo-ui.js" defer></script>
  <script src="js/trilha.js" defer></script>
  <script src="js/stats.js" defer></script>
  <script src="js/reveal.js" defer></script>
  <script src="js/main.js" defer></script>         <!-- por último: inicializa tudo -->
</head>
```

> A política de segurança (CSP) via `<meta>` é a única possível no GitHub Pages (não permite cabeçalhos HTTP próprios). Ela proíbe `style=""` e `<script>` em linha; por isso o projeto usa só classes CSS e arquivos externos. Estilos aplicados por JavaScript via `element.style.propriedade` continuam permitidos. O bloco de dados JSON-LD (`<script type="application/ld+json">`) não é executado e, por isso, não é afetado pela diretiva `script-src`. Única diferença de CSP entre as páginas: o `404.html`, que precisa de `<base>`, usa `base-uri 'self'` no lugar de `base-uri 'none'`.

### 6.3 Módulos JavaScript (espaço de nomes `BTE`)

| Arquivo | Responsabilidade | API pública |
|:---|:---|:---|
| `theme-init.js` | Lê `localStorage` (com `try/catch`) ou `prefers-color-scheme` e define `data-theme` antes da pintura | n/a |
| `util.js` | Utilitários | `BTE.$`, `BTE.$$`, `BTE.norm(texto)` (minúsculas, sem acentos e sem pontuação; espaços colapsados), `BTE.debounce(fn, ms)`, `BTE.el(tag, attrs, ...filhos)` |
| `nav.js` | Menu móvel com foco preso e `Esc`; destaque do item ativo (`IntersectionObserver`); barra de progresso de rolagem | `BTE.nav.init()` |
| `theme.js` | Alternador claro/escuro, rótulo acessível dinâmico, persistência | `BTE.theme.init()` |
| `catalogo-ui.js` | Renderiza cards, aplica busca, filtros e ordenação, atualiza contador (`aria-live`), guarda estado na URL (`replaceState` em `try/catch`) | `BTE.catalogo.init()`, `BTE.catalogo.filtrar(estado)` |
| `trilha.js` | Gera os nós 17 a 28 a partir do catálogo e liga cada nó ao card | `BTE.trilha.init()` |
| `stats.js` | Calcula os números do hero (contagens a partir dos dados) | `BTE.stats.init()` |
| `reveal.js` | Animação de entrada por `IntersectionObserver`, respeitando `prefers-reduced-motion` | `BTE.reveal.init()` |
| `main.js` | Orquestra: espera `DOMContentLoaded`, chama os `init()` na ordem, captura erros sem quebrar a página | n/a |

**Regra de renderização:** todo conteúdo vindo dos dados entra no DOM por `createElement` + `textContent` (nunca `innerHTML`). Mesmo sendo dados próprios, isso elimina uma classe inteira de falhas.

**Lógica de filtro (referência):**

```js
function filtrar(estado) {
  var termos = BTE.norm(estado.busca || '').split(' ').filter(Boolean);
  var lista = window.BTE_CATALOGO.filter(function (o) {
    if (estado.categoria && o.categoria !== estado.categoria) return false;
    if (estado.formato && o.formato !== estado.formato) return false;
    if (!termos.length) return true;
    var palheiro = ' ' + BTE.norm([o.titulo, o.descricao, o.licaoRotulo, o.tags.join(' ')].join(' ')) + ' ';
    return termos.every(function (t) { return palheiro.indexOf(' ' + t) !== -1; });
  });
  return lista.sort(estado.ordem === 'nome'
    ? function (a, b) { return a.titulo.localeCompare(b.titulo, 'pt-BR'); }
    : function (a, b) { return a.ordem - b.ordem; });
}
```

**Regra da busca:** cada palavra digitada precisa coincidir com o **início de uma palavra** do título, da descrição, do rótulo da lição ou das tags (todas as palavras, em qualquer ordem). Assim, "orgânica" encontra *Química Orgânica* e *ENEM Quest*, mas não casa com "inorgânicas" no meio da palavra (o que uma busca por trecho faria, devolvendo um resultado indevido).

**Regra da trilha:** para cada lição `n` de 17 a 28, o nó aponta para o OAD cujo campo `licao` contém `n`, preferindo o de `status: "publicado"`; se só houver um "em-construcao", o nó é tracejado e sem link.

### 6.4 Marcação do card (referência para `catalogo-ui.js`)

```html
<article class="card" data-id="termoquimica" data-categoria="fisico-quimica">
  <div class="card__media">
    <img src="assets/img/oad/termoquimica.webp" width="640" height="400"
         loading="lazy" decoding="async" alt="Tela inicial da aula Termoquímica">
    <span class="chip chip--lesson">Lição 23</span>
    <span class="chip chip--status chip--ok">Publicado</span>
  </div>
  <div class="card__body">
    <h3 class="card__title">Termoquímica</h3>
    <p class="card__desc">Endo e exotermia, entalpia, Lei de Hess e combustíveis, com Calorímetro Virtual e questões oficiais do ENEM.</p>
    <ul class="tags" aria-label="Temas"><li>Físico-química</li><li>Simulador</li><li>ENEM</li></ul>
    <div class="card__actions">
      <a class="btn btn--primary card__link" href="https://bio-tech-edu.github.io/termoquimica/"
         target="_blank" rel="noopener">Abrir aula <span class="sr-only">Termoquímica (abre em nova aba)</span></a>
      <a class="btn btn--ghost" href="https://github.com/Bio-Tech-Edu/termoquimica"
         target="_blank" rel="noopener">Código <span class="sr-only">de Termoquímica no GitHub (abre em nova aba)</span></a>
    </div>
  </div>
</article>
```

### 6.5 Acessibilidade (requisitos técnicos)

- Link "Pular para o conteúdo" como primeiro foco; marcos (`landmarks`) e hierarquia de títulos sem saltos.
- `:focus-visible` com anel de 3 px (`--focus`), nunca `outline: none` sem substituto.
- Alvos de toque ≥ 44×44 px; espaçamento entre alvos ≥ 8 px.
- Chips de filtro são `<button aria-pressed>` dentro de `role="group"` com `aria-labelledby`.
- Contador de resultados em `aria-live="polite"`; estado vazio com instrução e botão "Limpar filtros".
- Estado nunca só por cor: "Em construção" leva ícone e texto; nó tracejado leva legenda.
- `prefers-reduced-motion`, `prefers-contrast` e `prefers-color-scheme` respeitados.
- Zoom até 400% sem rolagem horizontal; texto redimensionável até 200%.
- Imagens informativas com `alt`; decorativas com `alt=""`; SVG decorativo com `aria-hidden="true"`.
- `<noscript>` com a lista estática dos 10 OAD (gerada por `scripts/sincronizar.mjs`), para que o catálogo exista mesmo sem JavaScript.

### 6.6 Desempenho

| Item | Orçamento / técnica |
|:---|:---|
| HTML | ≤ 40 KB |
| CSS (5 arquivos) | ≤ 40 KB sem compressão |
| JS (9 arquivos + dados) | ≤ 30 KB minificado equivalente; sem bibliotecas |
| Fontes | 5 arquivos `.woff2` subconjunto latino, ≤ 90 KB no total; só 2 em `preload` |
| Miniaturas | 640×400 WebP ≤ 60 KB, `loading="lazy"`, `width`/`height` declarados (evita CLS) |
| Hero | Imagem ou SVG com `fetchpriority="high"`; animação em SVG, sem vídeo |
| Cache | GitHub Pages já serve com cache curto; nomes de arquivos de imagem versionados por conteúdo quando mudarem (`termoquimica-v2.webp`) |

### 6.7 Segurança e privacidade

- Nenhum cookie, nenhuma coleta, nenhum script ou fonte de terceiros. O portal não identifica visitantes.
- Links externos com `rel="noopener"`; sem formulários (contato por e-mail e GitHub).
- `localStorage` só para o tema (valor `light` ou `dark`), sempre em `try/catch`.
- Analytics: **desativado por padrão**. Se a marca quiser métricas, usar solução sem cookies e sem dados pessoais, declarada em `privacidade.html`.
- `privacidade.html` informa também que o **Chemical Royale** pede dados do estudante (nome, e-mail institucional, cidade, escola) em seu próprio ambiente, fora do portal.

### 6.8 Compatibilidade

Navegadores atuais (últimas 2 versões de Chrome, Edge, Firefox, Safari e WebView Android). Larguras de teste: 360, 390, 768, 1024 e 1440 px. Sem suporte a Internet Explorer. Todo recurso moderno tem *fallback* gracioso (ex.: sem `@layer`, o CSS ainda funciona na ordem de leitura).

---

## 7. Estrutura de arquivos

### 7.1 Árvore de saída (repositório `site`)

```
site/
├── index.html                  Página única do portal
├── privacidade.html            Política de privacidade (LGPD)
├── 404.html                    Página não encontrada
├── manifest.webmanifest        Metadados de instalação (PWA)
├── sw.js                       Service worker (opcional, offline)
├── robots.txt                  Regras de indexação
├── sitemap.xml                 Mapa do site
├── .nojekyll                   Desliga o Jekyll no GitHub Pages
├── .gitignore
├── .htmlvalidate.json          Regras do html-validate usadas no CI
├── LICENSE                     MIT (código)
├── LICENSE-CONTEUDO.md         CC BY 4.0 (textos e imagens autorais)
├── README.md                   Visão do projeto, como rodar, como publicar
├── CONTRIBUTING.md             Como contribuir
├── CODE_OF_CONDUCT.md          Código de conduta e uso responsável de IA
├── SPRINTS.md                  Histórico vivo de sprints e backlog
│
├── css/
│   ├── tokens.css              Variáveis de cor, tipografia, espaço e tema
│   ├── base.css                Reset, tipografia base, foco, utilitários
│   ├── layout.css              Container, grades, cabeçalho, rodapé
│   ├── components.css          Botões, chips, cards, tags, nós da trilha
│   └── sections.css            Estilos específicos de cada seção
│
├── js/
│   ├── theme-init.js           Aplica o tema antes da pintura
│   ├── util.js                 Utilitários do espaço de nomes BTE
│   ├── nav.js                  Menu, scrollspy, barra de progresso
│   ├── theme.js                Alternador de tema
│   ├── catalogo-ui.js          Renderização e filtros do catálogo
│   ├── trilha.js               Linha do tempo das lições 17 a 28
│   ├── stats.js                Números do hero calculados dos dados
│   ├── reveal.js               Animações de entrada
│   └── main.js                 Inicialização
│
├── data/
│   └── catalogo.js             Fonte única: 10 OAD + metadados
│
├── assets/
│   ├── logo/                   biotech-logo.webp (512×512), favicon.ico (16/32/48),
│   │                           apple-touch-icon.png (180×180, fundo opaco), icon-192.png, icon-512.png,
│   │                           og-image.jpg (1200×630, ≤ 200 KB)
│   │   └── origem/             favicon.png e hero.png originais (fonte oficial, não editar)
│   ├── img/
│   │   ├── hero/               helice-circuito.svg (ilustração do hero), hero-bg.webp (opcional)
│   │   └── oad/                <id>.webp × 10 (640×400) + _fallback.svg
│   ├── icons/                  sprite.svg (ícones do projeto)
│   └── fonts/                  sora-600/700.woff2, figtree-400/500/700.woff2, OFL.txt
│
├── docs/
│   ├── componentes.html        Página de testes dos componentes (botões, chips, cards, nós)
│   ├── componentes-demo.js     Script da página de testes (alternador de tema)
│   ├── projeto-executivo.md    Este documento
│   ├── fontes.md               Fontes tipográficas (versões, licenças) e registro de arte gerada
│   ├── auditoria-a11y.md       Resultado da auditoria de acessibilidade (S5)
│   ├── relatorio-qa.md         Relatório do teste completo (S6)
│   ├── prompts/                00-contexto.md e um arquivo por sprint (S0 a S6)
│   ├── decisoes.md             Registro das ADR
│   ├── guia-adicionar-oad.md   Passo a passo para incluir um novo OAD
│   ├── textos-about-repos.md   Descrições e tópicos para os repositórios
│   └── checklist-lancamento.md Lista de conferência final
│
├── scripts/                    Node 18+ sem dependências (só módulos nativos); Python 3 + Pillow para imagens
│   ├── validar-catalogo.mjs    Esquema e regras do catalogo.js
│   ├── testar-catalogo.mjs     Testes da busca e dos filtros em jsdom (npm i --no-save jsdom)
│   ├── checar-links.mjs        Testa URLs do catálogo e links internos
│   ├── checar-ancoras.mjs      Confere âncoras internas e do Markdown
│   ├── checar-contraste.mjs    Calcula contraste dos pares de tokens
│   ├── checar-orcamento.mjs    Confere pesos de HTML, CSS, JS, fontes e imagens (seção 6.6)
│   ├── sincronizar.mjs         Gera JSON-LD, <noscript>, sitemap a partir dos dados
│   ├── capturar_miniaturas.py  Captura telas das páginas publicadas (Playwright) para as miniaturas
│   └── otimizar_imagens.py     Converte e redimensiona miniaturas e logotipos
│
└── .github/
    ├── workflows/qa.yml        Validação em push, PR e semanal
    ├── ISSUE_TEMPLATE/         novo-oad.yml, bug.yml, config.yml
    └── pull_request_template.md
```

### 7.2 Descrição dos arquivos-alvo

| Arquivo | Conteúdo e finalidade | Sprint | Como validar |
|:---|:---|:---:|:---|
| `index.html` | Marcação completa das 6 seções, metadados SEO/OG, CSP, JSON-LD, `<noscript>` | S1, S2, S4, S5 | Validador HTML, Lighthouse, teclado |
| `privacidade.html` | Texto de privacidade em linguagem simples; o que o portal não coleta; aviso sobre os OAD | S4 | Revisão da autora |
| `404.html` | Mensagem amigável, links para início e catálogo, caminhos relativos ao `/site/` | S4 | Abrir URL inexistente após o deploy |
| `manifest.webmanifest` | Nome, ícones 192/512, `start_url: "./"`, cores de tema | S5 | Lighthouse (instalável) |
| `sw.js` | Cache da casca do site; dados em *stale-while-revalidate*; cache versionado | S5 | Modo avião no navegador |
| `robots.txt`, `sitemap.xml` | Indexação liberada; mapa com `index`, `privacidade` | S5 | Search Console (opcional) |
| `README.md` | Descrição, captura de tela, como rodar (`python -m http.server`), como publicar, licenças | S0, S6 | Leitura por pessoa externa |
| `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` | Fluxo de contribuição; conduta e uso responsável de IA (alinhado ao README do perfil) | S4 | Links do README funcionam |
| `SPRINTS.md` | Registro de cada sprint: entregas, decisões, pendências | todos | Atualizado ao fim de cada sprint |
| `css/tokens.css` | Seção 4.3 completa, claro e escuro | S1 | `checar-contraste.mjs` |
| `css/base.css` | Reset, `font-face`, foco, `sr-only`, `skip-link`, `prefers-reduced-motion` | S1 | Inspeção visual, teclado |
| `css/layout.css` | `.container`, grade de 12 colunas, cabeçalho fixo, rodapé | S1 | Larguras 360 a 1440 |
| `css/components.css` | Botões, chips, cards, tags, nós da trilha, alternador | S1, S3 | `docs/componentes.html` |
| `docs/componentes.html` | Página de testes (claro/escuro, estados de foco, cards com e sem miniatura) | S1 | Inspeção visual e teclado |
| `css/sections.css` | Hero, marca, catálogo, trilha, metodologia, comunidade, contato | S2 a S4 | Revisão visual |
| `js/*.js` | Seção 6.3 | S1 a S5 | `node --check`, teste em jsdom, teclado |
| `data/catalogo.js` | Seção 8.2 | S0, S3 | `validar-catalogo.mjs` |
| `assets/logo/*` | Logotipo e ícones derivados de `favicon.png`; `og-image.jpg` derivado de `hero.png` | S0, S5 | Conferência visual em claro e escuro |
| `assets/img/oad/*.webp` | Uma miniatura por OAD; `_fallback.svg` para ausência | S3 | Tamanho ≤ 60 KB, `width`/`height` |
| `assets/fonts/*` | Fontes auto-hospedadas e licença OFL | S1 | Sem requisições externas na aba Rede |
| `docs/prompts/*` | Os prompts da seção 9, um arquivo por sprint | S0 | n/a |
| `scripts/*` | Seção 10.3 | S0, S1, S3, S5, S6 | Rodar localmente e no CI |
| `.github/workflows/qa.yml`, `.htmlvalidate.json` | Seção 11.2 | S6 | Execução verde no Actions |

---

## 8. Modelo de dados e catálogo

### 8.1 Esquema de cada OAD

| Campo | Tipo | Regra |
|:---|:---|:---|
| `id` | texto | Igual ao nome do repositório; só `a-z`, `0-9`, `-`; único |
| `titulo` | texto | 3 a 60 caracteres |
| `licao` | lista de inteiros | Valores de 17 a 28; vazia para painéis |
| `licaoRotulo` | texto | Ex.: `"Lição 23"`, `"Lições 17 a 19"`, `"Painel"` |
| `categoria` | opção | `geral-inorganica` · `fisico-quimica` · `organica` · `estrategia-enem` |
| `formato` | opção | `arena` · `aula` · `painel` |
| `descricao` | texto | **Descrição curta do card: ≤ 140 caracteres**, termina com ponto |
| `tags` | lista | 1 a 3 itens, ≤ 24 caracteres cada |
| `recursos` | lista | Vocabulário: `simulador`, `laboratorio-virtual`, `fato-ou-fake`, `boss`, `badges`, `storytelling`, `painel`, `checklist`, `cornell-notes` |
| `publico` | texto | Ex.: `"Ensino Médio"` |
| `status` | opção | `publicado` · `em-construcao` |
| `urlPages` | texto ou `null` | `https://bio-tech-edu.github.io/<id>/`; `null` só se `em-construcao` |
| `urlRepo` | texto | `https://github.com/Bio-Tech-Edu/<id>` |
| `licenca` | texto | `"MIT"` ou `"a definir"` (conforme o repositório) |
| `miniatura` / `miniaturaAlt` | texto | Caminho relativo em `assets/img/oad/` e texto alternativo |
| `acento` | opção | `navy` · `teal` · `orange` (cor da faixa do card) |
| `ordem` | inteiro | Único; define a ordenação padrão |

### 8.2 Arquivo `data/catalogo.js` (conteúdo completo)

```js
/* =============================================================================
 * Bio+Tech EduDesign | Catálogo de OAD/REA
 * Fonte única de dados do portal. Para incluir um OAD, copie um bloco e ajuste.
 * Script clássico (sem import/export) para funcionar também em file://.
 * Conferido nos repositórios e páginas publicadas em 13/10/2026.
 * Regras de validação: scripts/validar-catalogo.mjs
 * ========================================================================== */
window.BTE_META = {
  versao: '1.0.0',
  atualizadoEm: '2026-10-13',
  orgUrl: 'https://github.com/Bio-Tech-Edu',
  pagesBase: 'https://bio-tech-edu.github.io/',
  rotulos: {
    categoria: {
      'geral-inorganica': 'Química geral e inorgânica',
      'fisico-quimica': 'Físico-química',
      'organica': 'Química orgânica',
      'estrategia-enem': 'Estratégia ENEM'
    },
    formato: {
      arena: 'Arena gamificada',
      aula: 'Aula gamificada',
      painel: 'Painel e checklists'
    },
    status: { publicado: 'Publicado', 'em-construcao': 'Em construção' }
  }
};

window.BTE_CATALOGO = [
  {
    id: 'chemical-royale',
    titulo: 'Chemical Royale: A Arena dos Elementos',
    licao: [17, 18, 19],
    licaoRotulo: 'Lições 17 a 19',
    categoria: 'geral-inorganica',
    formato: 'arena',
    descricao: 'Arena gamificada com cientistas históricas: átomo, tabela periódica, ligações e funções inorgânicas, com Duelo Final.',
    tags: ['Química geral', 'Gamificação', 'Storytelling'],
    recursos: ['boss', 'storytelling', 'badges'],
    publico: 'Ensino Médio',
    status: 'publicado',
    urlPages: 'https://bio-tech-edu.github.io/chemical-royale/',
    urlRepo: 'https://github.com/Bio-Tech-Edu/chemical-royale',
    licenca: 'MIT',
    miniatura: 'assets/img/oad/chemical-royale.webp',
    miniaturaAlt: 'Tela inicial do Chemical Royale: A Arena dos Elementos',
    acento: 'navy',
    ordem: 10
  },
  {
    id: 'pre-enem-quimica',
    titulo: 'ENEM Quest: Química',
    licao: [20],
    licaoRotulo: 'Lição 20 e Aulão',
    categoria: 'geral-inorganica',
    formato: 'aula',
    descricao: 'Quests com storytelling ramificado: Cálculos Químicos (Lição 20) e Aulão de Química Orgânica e Solubilidade.',
    tags: ['Estequiometria', 'Orgânica', 'ENEM'],
    recursos: ['boss', 'storytelling'],
    publico: 'Ensino Médio (2º e 3º anos)',
    status: 'publicado',
    urlPages: 'https://bio-tech-edu.github.io/pre-enem-quimica/',
    urlRepo: 'https://github.com/Bio-Tech-Edu/pre-enem-quimica',
    licenca: 'a definir',
    miniatura: 'assets/img/oad/pre-enem-quimica.webp',
    miniaturaAlt: 'Portal ENEM Quest: Química com as duas quests disponíveis',
    acento: 'teal',
    ordem: 20
  },
  {
    id: 'chemical-royale-v2',
    titulo: 'Chemical Royale v2',
    licao: [20, 21],
    licaoRotulo: 'Lições 20 e 21',
    categoria: 'geral-inorganica',
    formato: 'arena',
    descricao: 'Continuação da Arena dos Elementos, com Cálculos Químicos e Radioatividade. Em construção.',
    tags: ['Química geral', 'Gamificação'],
    recursos: ['storytelling'],
    publico: 'Ensino Médio',
    status: 'em-construcao',
    urlPages: null,
    urlRepo: 'https://github.com/Bio-Tech-Edu/chemical-royale-v2',
    licenca: 'a definir',
    miniatura: 'assets/img/oad/chemical-royale-v2.webp',
    miniaturaAlt: 'Ilustração da Arena dos Elementos, versão 2, em construção',
    acento: 'navy',
    ordem: 21
  },
  {
    id: 'solucoes',
    titulo: 'Estudo das Soluções',
    licao: [22],
    licaoRotulo: 'Lição 22',
    categoria: 'fisico-quimica',
    formato: 'aula',
    descricao: 'Soluto, solvente, solubilidade, concentrações e diluição, com laboratório virtual e questões do ENEM.',
    tags: ['Físico-química', 'Laboratório virtual', 'ENEM'],
    recursos: ['laboratorio-virtual', 'badges', 'storytelling'],
    publico: 'Ensino Médio',
    status: 'publicado',
    urlPages: 'https://bio-tech-edu.github.io/solucoes/',
    urlRepo: 'https://github.com/Bio-Tech-Edu/solucoes',
    licenca: 'MIT',
    miniatura: 'assets/img/oad/solucoes.webp',
    miniaturaAlt: 'Tela inicial da aula Estudo das Soluções',
    acento: 'teal',
    ordem: 22
  },
  {
    id: 'termoquimica',
    titulo: 'Termoquímica',
    licao: [23],
    licaoRotulo: 'Lição 23',
    categoria: 'fisico-quimica',
    formato: 'aula',
    descricao: 'Endo e exotermia, entalpia, Lei de Hess e combustíveis, com Calorímetro Virtual e questões oficiais do ENEM.',
    tags: ['Físico-química', 'Simulador', 'ENEM'],
    recursos: ['simulador', 'badges', 'storytelling'],
    publico: 'Ensino Médio',
    status: 'publicado',
    urlPages: 'https://bio-tech-edu.github.io/termoquimica/',
    urlRepo: 'https://github.com/Bio-Tech-Edu/termoquimica',
    licenca: 'MIT',
    miniatura: 'assets/img/oad/termoquimica.webp',
    miniaturaAlt: 'Tela inicial da aula Termoquímica',
    acento: 'orange',
    ordem: 23
  },
  {
    id: 'cinetica',
    titulo: 'Cinética Química',
    licao: [24],
    licaoRotulo: 'Lição 24',
    categoria: 'fisico-quimica',
    formato: 'aula',
    descricao: 'Velocidade das reações, colisões, fatores cinéticos e catálise em 5 missões com questões do ENEM.',
    tags: ['Físico-química', 'Catálise', 'ENEM'],
    recursos: ['badges', 'storytelling'],
    publico: 'Ensino Médio',
    status: 'publicado',
    urlPages: 'https://bio-tech-edu.github.io/cinetica/',
    urlRepo: 'https://github.com/Bio-Tech-Edu/cinetica',
    licenca: 'MIT',
    miniatura: 'assets/img/oad/cinetica.webp',
    miniaturaAlt: 'Tela inicial da aula Cinética Química',
    acento: 'orange',
    ordem: 24
  },
  {
    id: 'equilibrio',
    titulo: 'Equilíbrio Químico',
    licao: [25],
    licaoRotulo: 'Lição 25',
    categoria: 'fisico-quimica',
    formato: 'aula',
    descricao: 'Equilíbrio químico do Cerrado ao Pantanal: Kc, Le Chatelier, pH e tampão, com simulador e mentoras brasileiras.',
    tags: ['Físico-química', 'Simulador', 'Biomas'],
    recursos: ['simulador', 'badges', 'storytelling'],
    publico: 'Ensino Médio',
    status: 'publicado',
    urlPages: 'https://bio-tech-edu.github.io/equilibrio/',
    urlRepo: 'https://github.com/Bio-Tech-Edu/equilibrio',
    licenca: 'MIT',
    miniatura: 'assets/img/oad/equilibrio.webp',
    miniaturaAlt: 'Tela inicial da aula Equilíbrio Químico',
    acento: 'teal',
    ordem: 25
  },
  {
    id: 'eletroquimica',
    titulo: 'Eletroquímica',
    licao: [26],
    licaoRotulo: 'Lição 26',
    categoria: 'fisico-quimica',
    formato: 'aula',
    descricao: 'Pilhas, corrosão, eletrólise e Leis de Faraday, com simuladores, Fato ou Fake e desafios estilo ENEM.',
    tags: ['Físico-química', 'Simulador', 'Fato ou Fake'],
    recursos: ['simulador', 'fato-ou-fake', 'badges', 'storytelling'],
    publico: 'Ensino Médio',
    status: 'publicado',
    urlPages: 'https://bio-tech-edu.github.io/eletroquimica/',
    urlRepo: 'https://github.com/Bio-Tech-Edu/eletroquimica',
    licenca: 'MIT',
    miniatura: 'assets/img/oad/eletroquimica.webp',
    miniaturaAlt: 'Tela inicial da aula Eletroquímica',
    acento: 'navy',
    ordem: 26
  },
  {
    id: 'org',
    titulo: 'Química Orgânica',
    licao: [27, 28],
    licaoRotulo: 'Lições 27 e 28',
    categoria: 'organica',
    formato: 'aula',
    descricao: 'Química Orgânica em 8 missões: hibridação, nomenclatura IUPAC e destilação do petróleo, com Cornell Notes.',
    tags: ['Orgânica', 'Simulador', 'Cornell Notes'],
    recursos: ['simulador', 'fato-ou-fake', 'cornell-notes', 'badges', 'storytelling'],
    publico: 'Ensino Médio',
    status: 'publicado',
    urlPages: 'https://bio-tech-edu.github.io/org/',
    urlRepo: 'https://github.com/Bio-Tech-Edu/org',
    licenca: 'a definir',
    miniatura: 'assets/img/oad/org.webp',
    miniaturaAlt: 'Tela inicial da aula Química Orgânica, lições 27 e 28',
    acento: 'teal',
    ordem: 27
  },
  {
    id: 'enem',
    titulo: 'Raio-X do ENEM',
    licao: [],
    licaoRotulo: 'Painel',
    categoria: 'estrategia-enem',
    formato: 'painel',
    descricao: 'Raio-X do ENEM: painéis dos dois dias com série histórica 2014 a 2024, TRI, estudo de caso e checklists de revisão.',
    tags: ['ENEM', 'Painel', 'Checklist'],
    recursos: ['painel', 'checklist'],
    publico: 'Ensino Médio e pré-vestibular',
    status: 'publicado',
    urlPages: 'https://bio-tech-edu.github.io/enem/',
    urlRepo: 'https://github.com/Bio-Tech-Edu/enem',
    licenca: 'MIT',
    miniatura: 'assets/img/oad/enem.webp',
    miniaturaAlt: 'Portal Raio-X do ENEM com os painéis do primeiro e do segundo dia',
    acento: 'navy',
    ordem: 90
  }
];
```

### 8.3 Regras de validação (`scripts/validar-catalogo.mjs`)

1. `id` único, em formato *slug*, e igual ao último trecho de `urlRepo`.
2. `descricao` ≤ 140 caracteres e terminada em ponto; `tags` de 1 a 3 itens; `titulo` de 3 a 60.
3. `categoria`, `formato`, `status`, `acento` e cada item de `recursos` pertencem aos vocabulários definidos.
4. `status: "publicado"` exige `urlPages` começando em `https://bio-tech-edu.github.io/`; `"em-construcao"` exige `urlPages: null`.
5. `licao` só com inteiros de 17 a 28; `ordem` única.
6. `miniatura` existe em disco (ou o arquivo `_fallback.svg` é usado e o aviso é registrado) e `miniaturaAlt` não está vazio.
7. Toda lição de 17 a 28 é coberta por pelo menos um OAD (publicado ou em construção); o relatório lista as lições só "em construção".

### 8.4 Trilha derivada (não precisa ser digitada)

| Lição | OAD | Estado |
|:---:|:---|:---|
| 17, 18, 19 | Chemical Royale | Publicado |
| 20 | ENEM Quest: Química | Publicado |
| 21 | Chemical Royale v2 | **Em construção** |
| 22 | Estudo das Soluções | Publicado |
| 23 | Termoquímica | Publicado |
| 24 | Cinética Química | Publicado |
| 25 | Equilíbrio Químico | Publicado |
| 26 | Eletroquímica | Publicado |
| 27, 28 | Química Orgânica | Publicado |

### 8.5 Textos "About" prontos para os repositórios (achado A5)

Aplicar em *Settings → About* de cada repositório (descrição, site e tópicos). Todos usam o site `https://bio-tech-edu.github.io/<repositório>/`.

| Repositório | Descrição (≤ 160 caracteres) | Tópicos |
|:---|:---|:---|
| `termoquimica` | Aula interativa e gamificada de Termoquímica (Lição 23) do Pré-ENEM Digital MT: entalpia, Lei de Hess e combustíveis. | `quimica` `termoquimica` `enem` `gamificacao` `rea` |
| `solucoes` | Aula interativa e gamificada de Estudo das Soluções (Lição 22) do Pré-ENEM Digital MT, com laboratório virtual de diluição. | `quimica` `solucoes` `enem` `gamificacao` `rea` |
| `cinetica` | Aula interativa e gamificada de Cinética Química (Lição 24) do Pré-ENEM Digital MT: colisões, fatores cinéticos e catálise. | `quimica` `cinetica-quimica` `enem` `gamificacao` `rea` |
| `equilibrio` | Aula interativa e gamificada de Equilíbrio Químico (Lição 25) do Pré-ENEM Digital MT, com simulador de Le Chatelier. | `quimica` `equilibrio-quimico` `enem` `gamificacao` `rea` |
| `eletroquimica` | Aula interativa e gamificada de Eletroquímica (Lição 26) do Pré-ENEM Digital MT: pilhas, eletrólise, Faraday e Fato ou Fake. | `quimica` `eletroquimica` `enem` `gamificacao` `rea` |
| `chemical-royale-v2` | Em construção: continuação da Arena dos Elementos (Lições 20 e 21). | `quimica` `enem` `gamificacao` `rea` |

---

## 9. Plano de sprints

### 9.1 Visão geral

O trabalho está dividido em **7 sprints** (S0 a S6). Cada sprint termina com algo que **abre no navegador e pode ser conferido**, nunca com "meio caminho" invisível. As estimativas são em **dias de trabalho de uma pessoa** e servem para ordenar o esforço; o calendário real depende da disponibilidade da autora.

| Sprint | Objetivo | Esforço | Prompts | Entrega que se confere |
|:---:|:---|:---:|:---:|:---|
| **S0** | Fundação e descoberta | 1 a 2 dias | 4 | Página provisória no ar em `/site/`; catálogo validado; logotipos derivados |
| **S1** | Design system e esqueleto | 2 a 3 dias | 5 | Cabeçalho, tema claro/escuro, rodapé e página de teste de componentes |
| **S2** | Hero e marca | 2 dias | 4 | Hero animado, faixa de números e seção "A marca" completos |
| **S3** | Catálogo de OAD/REA | 3 dias | 5 | 10 cards com descrição, busca, filtros e miniaturas |
| **S4** | Trilha, metodologia e comunidade | 2 a 3 dias | 4 | Trilha 17–28, metodologia, comunidade, contato, privacidade e 404 |
| **S5** | Acessibilidade, desempenho e SEO | 2 dias | 4 | Lighthouse nas metas; PWA básico; metadados de compartilhamento |
| **S6** | QA, CI e lançamento | 2 dias | 4 | CI verde, README final, repositórios corrigidos, versão 1.0.0 |
| | **Total** | **14 a 17 dias** | **30** | |

### 9.2 Como trabalhar cada sprint

**Fluxo de cada prompt** (repita para P0.1, P0.2, e assim por diante):

1. Abra uma **conversa nova** na ferramenta de IA escolhida e cole o **prompt-mestre** (seção 9.3).
2. **Anexe** `docs/projeto-executivo.md` (este documento) e, se o prompt pedir, os arquivos de entrada.
3. Cole o prompt do passo. Leia o plano de 5 linhas que a IA devolve; se estiver fora do escopo, corrija antes de aceitar.
4. Salve os arquivos entregues **nos caminhos indicados** e rode o comando da linha `VERIFICAÇÃO`.
5. Só depois de passar: `git add`, commit e, ao fim da sprint, pull request.

**Convenções.**

| Item | Regra |
|:---|:---|
| Branch | `sprint-N/<tema>` (ex.: `sprint-3/catalogo`) |
| Commit | Prefixos `feat:`, `fix:`, `docs:`, `chore:`, em português, no imperativo ("adiciona filtro por formato") |
| Pull request | Um por sprint, mesmo trabalhando sozinha: serve de registro e roda o CI (a partir da S6) |
| Versão | Tag `v0.N.0` ao fim de cada sprint; `v1.0.0` no lançamento |
| Registro | `SPRINTS.md` atualizado ao fim de cada sprint (entregas, decisões, pendências) |

**Sugestão de ferramentas** (espelha a prática de uso combinado de IAs; qualquer uma serve se receber o prompt-mestre):

| Ferramenta | Melhor uso neste projeto |
|:---|:---|
| **Claude** | Arquitetura, código dos módulos, textos e revisão de conteúdo |
| **GitHub Copilot** | Revisão de pull request, testes, documentação e correção de READMEs |
| **Gemini / Nanobanana** | Arte: fundos, ilustrações e miniaturas, conforme os prompts opcionais |

**Anatomia de todo prompt** deste documento (para você criar outros no mesmo formato):

| Bloco | Para que serve |
|:---|:---|
| `PAPEL` | Quem a IA deve ser (define vocabulário e rigor) |
| `CONTEXTO` | Quais seções deste documento ler e quais arquivos já existem |
| `TAREFA` | Passos numerados, verificáveis |
| `RESTRIÇÕES` | O que não fazer (limites de escopo, segurança, acessibilidade) |
| `ENTREGA` | Quais arquivos devolver, completos, e em que formato |
| `VERIFICAÇÃO` | Comando ou teste que prova que ficou certo |

### 9.3 Prompt-mestre (salvar em `docs/prompts/00-contexto.md`)

Cole **no início de toda conversa**. Ele evita que a IA reabra decisões já tomadas.

```text
Atue como pessoa desenvolvedora front-end sênior e designer de interface, trabalhando em português do Brasil com a Prof.ª Pâmella (Mell), da marca Bio+Tech EduDesign.

PROJETO: portal estático em HTML5 + CSS3 + JavaScript puro (sem build, sem framework, sem CDN), hospedado no GitHub Pages, repositório Bio-Tech-Edu/site. Apresenta a marca e um catálogo de 10 objetos de aprendizagem digitais (OAD/REA), cada card com uma breve descrição abaixo.

FONTE DE VERDADE: o arquivo docs/projeto-executivo.md (anexo). Antes de qualquer tarefa, leia as seções citadas no prompt. Se o prompt contrariar o documento, aponte o conflito e pergunte antes de agir.

REGRAS INEGOCIÁVEIS:
1. Caminhos sempre relativos (nunca href="/...").
2. JavaScript clássico com defer: sem import/export; sem innerHTML com dados; DOM por createElement e textContent.
3. Sem estilo nem script em linha (a CSP da seção 6.2 proíbe); sem recurso de terceiros (fontes, ícones, analytics).
4. Cores somente por tokens CSS (seção 4.3), respeitando as regras de contraste da seção 4.2.
5. Acessibilidade WCAG 2.2 AA: uso por teclado, foco visível, alvos de toque de 44 px ou mais, prefers-reduced-motion.
6. Dados do catálogo somente em data/catalogo.js; nunca digitar contagens ou números do catálogo em HTML ou JS.
7. Interface em português do Brasil, no tom da seção 4.9. Não inventar fatos sobre os OAD: usar só os campos do catálogo.
8. Comentários curtos em português; classes CSS em BEM simples (bloco__elemento--modificador).
9. Nenhuma dependência de produção; ferramentas de teste só com "npm i --no-save".
10. HTML válido (html-validate sem erros): <!DOCTYPE html> em maiúsculas, alt em toda imagem, type em todo botão.

COMO RESPONDER:
(a) liste em até 5 linhas o que vai fazer;
(b) entregue os arquivos COMPLETOS (não trechos), com o caminho de cada um em uma linha antes do bloco de código;
(c) rode ou descreva os comandos da linha VERIFICAÇÃO e mostre o resultado;
(d) termine com "Pendências e dúvidas" (no máximo 5 itens).
Não altere nada fora do escopo do prompt.
```

---

### Sprint 0: Fundação e descoberta

**Objetivo.** Deixar o repositório pronto e **publicado com uma página provisória**, o catálogo validado e os logotipos derivados, de modo que as sprints seguintes apenas acrescentem.

**Esforço:** 1 a 2 dias · **Ferramenta sugerida:** Claude (código) e Copilot (documentos de projeto).

**Pré-requisitos (autora):** acesso de escrita a `Bio-Tech-Edu/site`; Git, Node 18+ e Python 3 com Pillow (`pip install pillow`) instalados; os arquivos `favicon.png` e `hero.png` em mãos; decisões **D1, D2 e D3** da seção 12 respondidas (repositório alvo, licenças, e-mail de contato).

#### S0 · Tarefas

| ID | Tarefa | Quem | Saída |
|:--:|:---|:---:|:---|
| S0.1 | Clonar o repositório e criar a branch `sprint-0/fundacao`; copiar `favicon.png` e `hero.png` para `assets/logo/origem/` | Autora | Branch criada, originais versionados |
| S0.2 | Estrutura de pastas, arquivos de higiene e página provisória | IA (P0.1) | Árvore da seção 7.1, `LICENSE`, `README.md`, `index.html` provisório |
| S0.3 | Catálogo e validador | IA (P0.2) | `data/catalogo.js`, `scripts/validar-catalogo.mjs` |
| S0.4 | Logotipos, ícones e imagem de compartilhamento | IA (P0.3) | `scripts/otimizar_imagens.py` e arquivos em `assets/logo/` |
| S0.5 | Documentos de projeto e arquivos de prompts | IA (P0.4) | `docs/*`, `SPRINTS.md` |
| S0.6 | Abrir pull request, fazer *merge* na `main` e **ativar o Pages**: *Settings → Pages → Build and deployment → Deploy from a branch → `main` / `(root)`* | Autora | URL `https://bio-tech-edu.github.io/site/` mostra a página provisória (leva de 1 a 3 minutos) |
| S0.7 | Marcar a tag `v0.1.0` | Autora | Tag no GitHub |

#### S0 · Prompts

**P0.1 · Estrutura e higiene do repositório** (Claude Code ou Claude)

```text
PAPEL: engenheira(o) de repositório, com cuidado em simplicidade e em licenças abertas.

CONTEXTO: leia as seções 3 (ADR-04, ADR-06 e ADR-09), 7.1 e 7.2 de docs/projeto-executivo.md. A pasta assets/logo/origem/ já contém favicon.png e hero.png (não alterar).

TAREFA:
1. Crie a árvore de pastas da seção 7.1. Use um arquivo .gitkeep apenas nas pastas que ficarão vazias nesta sprint. Não crie ainda os arquivos finais de css, js e html.
2. Crie os arquivos de higiene:
   - .gitignore (node_modules/, __pycache__/, .DS_Store, *.log);
   - .nojekyll (arquivo vazio);
   - LICENSE: texto padrão da licença MIT, ano 2026, titular "Bio+Tech EduDesign";
   - LICENSE-CONTEUDO.md: resumo em português do CC BY 4.0 para textos e imagens autorais, link https://creativecommons.org/licenses/by/4.0/deed.pt-br e aviso de que logotipos de terceiros (SEDUC e Governo de MT) e a marca Bio+Tech EduDesign não estão cobertos;
   - README.md: o que é o projeto, como abrir localmente com "python3 -m http.server 8000", como publicar no GitHub Pages, licenças e link para docs/projeto-executivo.md;
   - SPRINTS.md: tabela "Sprint | Datas | Entregas | Decisões | Pendências", já com a linha da Sprint 0 em andamento.
3. Crie um index.html PROVISÓRIO, mínimo e válido (com <!DOCTYPE html> em maiúsculas): lang="pt-BR", charset, viewport, title "Bio+Tech EduDesign", um h1 com o nome da marca, um parágrafo "Portal em construção." e um link para https://github.com/Bio-Tech-Edu. Sem CSS nem JS externos. Este arquivo será substituído na Sprint 1.

RESTRIÇÕES: caminhos relativos; nenhuma dependência; textos em português do Brasil; não escrever nada que dependa de decisão ainda aberta (D1 a D3 da seção 12), apenas marcar "a confirmar" no README.

ENTREGA: a saída de "find . -not -path './.git/*' | sort" e o conteúdo de cada arquivo novo.

VERIFICAÇÃO: rode "python3 -m http.server 8000", abra http://localhost:8000/ e confirme que a página provisória aparece; confira que a árvore bate com a seção 7.1 (liste divergências, se houver).
```

**P0.2 · Catálogo e validador** (Claude Code ou Claude)

```text
PAPEL: engenheira(o) de dados e de qualidade, com foco em validação automática.

CONTEXTO: leia as seções 8.1 a 8.4 e o Anexo D de docs/projeto-executivo.md.

TAREFA:
1. Grave data/catalogo.js com o conteúdo EXATO do bloco da seção 8.2 (mesmos campos, textos, ordem e acentuação). Não reescreva descrições.
2. Crie scripts/validar-catalogo.mjs (Node 18 ou superior, só módulos nativos) que carregue o catálogo com node:vm, aplique as 7 regras da seção 8.3 e imprima:
   - uma linha de resumo ("OAD: 10 | lições publicadas: 11/12 | só em construção: [21] | OAD com simulador/lab: 5");
   - a maior descrição em caracteres;
   - os erros, um por linha, ou "Catálogo válido: 0 erros".
   O caminho do catálogo é o argumento 1 (padrão: data/catalogo.js). Código de saída 1 se houver erro. A regra 6 (miniatura existe em disco) gera AVISO por padrão e ERRO com a opção --estrito (só para OAD "publicado"; o "em-construcao" pode usar o fallback). Nesta sprint rode sem --estrito, pois as miniaturas só existem a partir da Sprint 3. Use o Anexo D como comportamento de referência.
3. No README.md, acrescente a seção "Como adicionar um OAD" resumindo a seção 11.4.

RESTRIÇÕES: não instalar pacotes; não alterar o catálogo para "fazer passar" o validador (se uma regra falhar, reporte).

ENTREGA: data/catalogo.js, scripts/validar-catalogo.mjs e o trecho novo do README.md.

VERIFICAÇÃO:
a) node scripts/validar-catalogo.mjs deve terminar com "Catálogo válido: 0 erros" e código 0;
b) teste negativo: troque temporariamente a descrição de um OAD por um texto de 150 caracteres e confirme erro e código 1; depois reverta;
c) node --check scripts/validar-catalogo.mjs sem erros.
```

**P0.3 · Logotipos, ícones e imagem de compartilhamento** (Claude Code ou Claude)

```text
PAPEL: especialista em imagens para web.

CONTEXTO: leia as seções 4.8, 6.2 (links de ícones) e 7.1 (pasta assets/logo) de docs/projeto-executivo.md.

ENTRADAS: assets/logo/origem/favicon.png (600x600, RGBA, logotipo circular com fundo transparente) e assets/logo/origem/hero.png (1667x584, banner turquesa com o nome da marca; bordas arredondadas com 1 a 3 px de borda cinza). Nunca altere os originais.

TAREFA: escreva scripts/otimizar_imagens.py (Python 3 + Pillow, sem outras dependências) que gere em assets/logo/:
- biotech-logo.webp: 512x512, qualidade 90, com transparência;
- icon-192.png e icon-512.png: com transparência, optimize=True;
- apple-touch-icon.png: 180x180, fundo branco opaco, logotipo de 150x150 centralizado;
- favicon.ico: com os tamanhos 16, 32 e 48;
- og-image.jpg: 1200x630. Remova 4 px de cada borda do hero.png, calcule o recorte central na proporção 1200:630 (com as dimensões atuais dá cerca de 1097x576), redimensione com LANCZOS e salve em JPEG qualidade 82, progressivo, com tamanho final de no máximo 200 KB (se passar, reduza a qualidade de 2 em 2).
O script deve ser idempotente, aceitar --origem e --saida (com padrões assets/logo/origem e assets/logo), imprimir uma tabela "arquivo | dimensões | modo | KB" e falhar com mensagem clara se faltar um original.

RESTRIÇÕES: não ampliar nenhuma imagem mais de 1,1x; não usar bibliotecas além de Pillow e da biblioteca padrão; mensagens do script em português.

ENTREGA: scripts/otimizar_imagens.py e a tabela impressa pela execução.

VERIFICAÇÃO: execute o script e confirme (1) og-image.jpg com no máximo 200 KB e 1200x630; (2) biotech-logo.webp e icon-*.png em modo RGBA; (3) favicon.ico com 3 tamanhos; (4) abra og-image.jpg e confirme que o nome "Pâmella Araújo Balcaçar" e o DNA aparecem inteiros, sem corte.
```

**P0.4 · Documentos do projeto e arquivos de prompts** (Copilot ou Claude)

```text
PAPEL: redatora(o) técnica(o) de documentação de projetos abertos.

CONTEXTO: leia as seções 3, 7.1, 8.5 e 9 e os Anexos B e C de docs/projeto-executivo.md.

TAREFA:
1. docs/decisoes.md: tabela com ADR-01 a ADR-09 (seção 3) mais as colunas "Status" (use "Proposta" em todas até a autora confirmar) e "Data".
2. docs/prompts/00-contexto.md com o prompt-mestre da seção 9.3 e docs/prompts/S0.md a S6.md. Cada arquivo S_N traz os prompts da respectiva sprint COPIADOS LITERALMENTE da seção 9, com os IDs (P0.1, P0.2...) como títulos.
3. docs/textos-about-repos.md com a tabela da seção 8.5.
4. docs/checklist-lancamento.md com a lista do Anexo B (caixas de seleção "- [ ]").
5. docs/guia-adicionar-oad.md com os passos da seção 11.4.
6. SPRINTS.md: preencha a linha da Sprint 0 (entregas, decisões tomadas, pendências).
7. Salve este documento como docs/projeto-executivo.md (se ainda não estiver lá).

RESTRIÇÕES: copiar, não reescrever; não alterar numeração; português do Brasil.

ENTREGA: os arquivos listados e uma tabela "arquivo | prompts contidos" para os arquivos S0 a S6.

VERIFICAÇÃO: a contagem de prompts por arquivo deve ser S0=4, S1=5, S2=4, S3=5, S4=4, S5=4, S6=4 (total 30); todos os links relativos nos arquivos novos devem apontar para arquivos que existem.
```

#### S0 · Arquivos de saída

| Arquivo | Origem |
|:---|:---|
| Árvore de pastas (seção 7.1), `.gitignore`, `.nojekyll`, `LICENSE`, `LICENSE-CONTEUDO.md`, `README.md`, `SPRINTS.md`, `index.html` provisório | P0.1 |
| `data/catalogo.js`, `scripts/validar-catalogo.mjs` | P0.2 |
| `scripts/otimizar_imagens.py`, `assets/logo/biotech-logo.webp`, `icon-192.png`, `icon-512.png`, `apple-touch-icon.png`, `favicon.ico`, `og-image.jpg` | P0.3 |
| `docs/projeto-executivo.md`, `docs/decisoes.md`, `docs/prompts/*`, `docs/textos-about-repos.md`, `docs/checklist-lancamento.md`, `docs/guia-adicionar-oad.md` | P0.4 |

#### S0 · Critérios de aceite

- [ ] `node scripts/validar-catalogo.mjs` termina com **0 erros** e resumo "OAD: 10 | lições publicadas: 11/12".
- [ ] `https://bio-tech-edu.github.io/site/` responde com a página provisória.
- [ ] `og-image.jpg` ≤ 200 KB; ícones com fundo transparente preservado; `favicon.ico` com 3 tamanhos.
- [ ] A árvore de pastas confere com a seção 7.1; nenhum caminho absoluto no repositório.
- [ ] `SPRINTS.md` e `docs/decisoes.md` preenchidos; decisões D1 a D3 registradas.

---

### Sprint 1: Design system e esqueleto

**Objetivo.** Transformar a identidade visual (seção 4) em **código reutilizável**: fontes locais, tokens, base, layout, componentes e a **casca da página** (cabeçalho, navegação, alternador de tema, rodapé), sem ainda preencher o conteúdo.

**Esforço:** 2 a 3 dias · **Ferramenta sugerida:** Claude.

**Pré-requisitos:** Sprint 0 concluída (branch `sprint-1/design-system` criada a partir da `main`).

#### S1 · Tarefas

| ID | Tarefa | Quem | Saída |
|:--:|:---|:---:|:---|
| S1.1 | Baixar e copiar as fontes (npm, sem CDN) | IA (P1.1) | 5 arquivos `.woff2` + licença OFL |
| S1.2 | Tokens e verificador de contraste | IA (P1.2) | `css/tokens.css`, `scripts/checar-contraste.mjs` |
| S1.3 | Base e layout | IA (P1.3) | `css/base.css`, `css/layout.css` |
| S1.4 | Componentes e página de teste | IA (P1.4) | `css/components.css`, `docs/componentes.html` |
| S1.5 | Esqueleto da página e JavaScript da casca | IA (P1.5) | `index.html` (6 seções vazias), `js/theme-init.js`, `util.js`, `nav.js`, `theme.js`, `main.js` |
| S1.6 | Teste manual de teclado e de tema; PR e tag `v0.2.0` | Autora | Registro em `SPRINTS.md` |

#### S1 · Prompts

**P1.1 · Fontes auto-hospedadas** (Claude Code)

```text
PAPEL: especialista em tipografia web e desempenho.

CONTEXTO: leia as seções 3 (ADR-05), 4.4 e 6.6 de docs/projeto-executivo.md.

TAREFA:
1. Em uma pasta temporária FORA do repositório, rode: npm i --no-save @fontsource/sora @fontsource/figtree
2. Copie para assets/fonts/ exatamente estes 5 arquivos do subconjunto latino (cobre o português) e mantenha os nomes:
   sora-latin-600-normal.woff2, sora-latin-700-normal.woff2,
   figtree-latin-400-normal.woff2, figtree-latin-500-normal.woff2, figtree-latin-700-normal.woff2
3. Copie o arquivo LICENSE de cada pacote para assets/fonts/OFL.txt (junte os dois, separados por uma linha com o nome da família).
4. Gere docs/fontes.md com: família, peso, arquivo, tamanho em bytes, versão do pacote e licença (OFL-1.1).
5. Escreva, no corpo da resposta (não em arquivo), os 5 blocos @font-face (font-display: swap; unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+2000-206F, U+20AC, U+2122) para serem colados em css/base.css no prompt P1.3.

RESTRIÇÕES: nenhum arquivo de node_modules entra no repositório; nada de CDN nem de Google Fonts; não renomear arquivos.

ENTREGA: os 5 .woff2, assets/fonts/OFL.txt, docs/fontes.md e os blocos @font-face.

VERIFICAÇÃO: a soma dos 5 .woff2 deve ser menor que 90 KB (esperado: cerca de 63 KB); "file assets/fonts/*.woff2" deve indicar "Web Open Font Format (Version 2)".
```

**P1.2 · Tokens e verificador de contraste** (Claude Code)

```text
PAPEL: designer de sistemas de design com foco em acessibilidade de cor.

CONTEXTO: leia as seções 4.2 e 4.3 e o Anexo E (comportamento de referência) de docs/projeto-executivo.md.

TAREFA:
1. Grave css/tokens.css com o bloco da seção 4.3, SEM alterar valores (se achar que um valor deve mudar, diga na resposta e espere).
2. Crie scripts/checar-contraste.mjs (Node 18+, só módulos nativos) que:
   a) leia css/tokens.css (argumento 1 opcional), extraia as variáveis de ":root {" e de ':root[data-theme="dark"]', resolva var(--x) e monte os temas claro e escuro;
   b) calcule a razão de contraste WCAG 2.x;
   c) verifique, nos dois temas, os papéis --text, --text-muted, --heading, --link, --accent e --accent-warm sobre --bg, --surface e --surface-alt (mínimo 4,5), --focus sobre --bg e --surface (mínimo 3) e os pares de botões da seção 4.5;
   d) imprima uma tabela "tema | par | razão | mínimo | resultado" e termine com código 1 se qualquer par obrigatório falhar.
   Marque como "decorativo" (não conta como falha) apenas o par --orange-500 sobre branco.

RESTRIÇÕES: sem dependências; a lógica deve ser reaproveitável pelo CI (seção 11.2).

ENTREGA: css/tokens.css e scripts/checar-contraste.mjs.

VERIFICAÇÃO: node scripts/checar-contraste.mjs deve terminar com "Todos os pares obrigatórios passam" e código 0. Teste negativo: troque --teal-700 por #2DC3BF, confirme que falha (código 1) e reverta.
```

**P1.3 · Base e layout** (Claude Code)

```text
PAPEL: engenheira(o) de CSS, com foco em CSS moderno e acessível.

CONTEXTO: leia as seções 4.4, 4.7, 5.2, 6.1 e 6.5 de docs/projeto-executivo.md. Os tokens estão em css/tokens.css e as fontes em assets/fonts/ (P1.1 e P1.2 já concluídos).

TAREFA:
1. css/base.css, nesta ordem: declaração "@layer reset, tokens, base, layout, components, sections, utilities;" na PRIMEIRA linha útil; os 5 blocos @font-face (caminhos relativos "../assets/fonts/..."); reset moderno (box-sizing, margens zeradas, imagens em bloco com max-width: 100%); tipografia base (corpo em var(--fs-0)/1.6 com var(--font-body); títulos em var(--font-display); largura de leitura de 70ch para parágrafos); links; :focus-visible com anel de 3px em var(--focus) e deslocamento de 2px; classes utilitárias .sr-only e .skip-link (visível ao focar); scroll-behavior suave e scroll-padding-top igual a var(--header-h); regras de prefers-reduced-motion que removem animações e transições; prefers-contrast: more com bordas mais fortes.
2. css/layout.css: .container (largura máxima var(--container), 16 px de gutter em 360 px, 24 px acima de 768 px); grade de 12 colunas via CSS Grid com variantes de 1, 2 e 3 colunas responsivas para listas de cards (.grid--cards); cabeçalho fixo (.site-header, altura var(--header-h), fundo translúcido com backdrop-filter e fallback sólido); espaçamento vertical de seções (.section, padding por tokens --sp-8 e --sp-9); rodapé (.site-footer) em --navy-900 com texto claro.

RESTRIÇÕES: nenhum valor de cor fora dos tokens; nenhum "outline: none" sem substituto; nenhuma unidade em px para tipografia; todo o CSS dentro das camadas declaradas; sem !important.

ENTREGA: css/base.css e css/layout.css completos.

VERIFICAÇÃO: abra um HTML de teste com título, parágrafo, link, botão e lista em 360, 768 e 1440 px, nos temas claro e escuro (alterne data-theme no <html>); confirme leitura confortável, foco visível ao pressionar Tab, ausência de rolagem horizontal e que o texto continua legível com zoom de 200%.
```

**P1.4 · Componentes e página de teste** (Claude Code)

```text
PAPEL: designer de interface e engenheira(o) de CSS de componentes.

CONTEXTO: leia as seções 4.5, 4.6, 4.7 e 6.4 de docs/projeto-executivo.md. Já existem css/tokens.css, base.css e layout.css.

TAREFA:
1. css/components.css (camada "components") com estes componentes e todos os estados (hover, :focus-visible, :active, disabled/aria-disabled):
   .btn (--primary, --cta, --ghost; altura mínima 44 px; raio pill), .chip (--filter com aria-pressed="true" marcado), .tag, .badge-lesson ("LIÇÃO 23" em versalete), .badge-status (--ok "Publicado", --wip "Em construção" com ícone e texto), .card (anatomia da seção 4.6: .card__media, .card__body, .card__title, .card__desc limitada a 3 linhas com line-clamp, .tags, .card__actions; link esticado via ::after no botão principal; borda em gradiente turquesa-laranja no hover e no foco sem alterar o tamanho), .trail-node (círculo de 56 px; --active com anel laranja; --wip tracejado) e .theme-toggle.
2. docs/componentes.html: página de teste que mostra cada componente em todos os estados, em uma grade, com um botão que alterna o tema e um cartão "sem miniatura" (fallback em gradiente com a inicial do título). Deve carregar css/tokens, base, layout e components por caminho relativo ("../css/...").
3. assets/icons/sprite.svg com os ícones necessários: externo (seta diagonal), código, lua, sol, menu, fechar, check, em-construção (ampulheta), busca, github, e-mail. Traço de 1,75 px, cantos arredondados, viewBox 24x24, currentColor.

RESTRIÇÕES: nenhum style="" nem <script> em linha em docs/componentes.html (a CSP vale também para a página de teste; use um arquivo docs/componentes-demo.js ou prescinda de JS); contraste conforme tokens; alvos de toque de 44 px ou mais.

ENTREGA: css/components.css, docs/componentes.html, assets/icons/sprite.svg (e docs/componentes-demo.js, se usado).

VERIFICAÇÃO: abra docs/componentes.html nos dois temas; navegue só com Tab e Enter/Espaço; confirme foco visível em todos os controles, "Em construção" com ícone além da cor e card sem miniatura legível. Rode node scripts/checar-contraste.mjs (deve continuar com código 0).
```

**P1.5 · Esqueleto da página e JavaScript da casca** (Claude Code)

```text
PAPEL: engenheira(o) front-end, com foco em HTML semântico e JavaScript acessível.

CONTEXTO: leia as seções 5.1 a 5.3, 6.1 a 6.3 e 6.5 de docs/projeto-executivo.md. CSS e componentes já existem (P1.2 a P1.4).

TAREFA:
1. Substitua o index.html provisório por um esqueleto completo: o <head> exatamente como na seção 6.2 (mas sem o manifest e sem os metadados finais de SEO, que são da Sprint 5; mantenha a CSP); <body> com link "Pular para o conteúdo", <header> (logotipo assets/logo/biotech-logo.webp com alt, nav com os itens da seção 5.2 e o botão de tema), <main id="conteudo"> com as 6 seções vazias (#marca, #catalogo, #trilha, #metodologia, #comunidade, #contato) cada uma com um <h2> e um parágrafo "Conteúdo na próxima sprint", e <footer> com créditos, links para LICENSE e para a política de privacidade (privacidade.html, ainda inexistente: manter o link), e o ano.
2. js/theme-init.js (síncrono, menos de 400 bytes): lê localStorage "bte-tema" em try/catch ou usa prefers-color-scheme e define data-theme no <html>.
3. js/util.js: namespace BTE com $, $$, norm(texto) (minúsculas, sem acentos, pontuação vira espaço, espaços colapsados), debounce(fn, ms) e el(tag, attrs, ...filhos) (cria elementos com createElement; atributos via setAttribute; filhos de texto via createTextNode).
4. js/nav.js: menu móvel (botão com aria-expanded e aria-controls, foco preso no painel, Esc fecha e devolve o foco ao botão), item ativo por IntersectionObserver (aria-current="true"), barra de progresso de rolagem decorativa (aria-hidden).
5. js/theme.js: alternador com rótulo dinâmico ("Ativar tema escuro"/"Ativar tema claro"), persistência em try/catch.
6. js/main.js: no DOMContentLoaded chama BTE.nav.init() e BTE.theme.init() (os demais módulos entram nas sprints seguintes; chame-os somente se existirem), dentro de try/catch que registra o erro sem quebrar a página.

RESTRIÇÕES: scripts clássicos com defer (exceto theme-init.js); sem import/export; sem innerHTML; sem estilo em linha; a página não pode ter rolagem horizontal em 360 px.

ENTREGA: index.html, js/theme-init.js, util.js, nav.js, theme.js e main.js completos.

VERIFICAÇÃO: "node --check js/*.js" sem erros; no navegador, com a aba Rede aberta, confirmar ZERO requisições externas; navegar só por teclado (Tab percorre link de pular, logotipo, itens do menu, alternador); alternar o tema e recarregar (persiste); em 360 px o menu abre, prende o foco e fecha com Esc; com prefers-reduced-motion ativado, a barra de progresso não anima.
```

#### S1 · Arquivos de saída

| Arquivo | Origem |
|:---|:---|
| `assets/fonts/*.woff2` (5), `assets/fonts/OFL.txt`, `docs/fontes.md` | P1.1 |
| `css/tokens.css`, `scripts/checar-contraste.mjs` | P1.2 |
| `css/base.css`, `css/layout.css` | P1.3 |
| `css/components.css`, `docs/componentes.html`, `assets/icons/sprite.svg` | P1.4 |
| `index.html` (esqueleto), `js/theme-init.js`, `util.js`, `nav.js`, `theme.js`, `main.js` | P1.5 |

#### S1 · Critérios de aceite

- [ ] `node scripts/checar-contraste.mjs` → "Todos os pares obrigatórios passam".
- [ ] Zero requisições externas na aba Rede (fontes, ícones e scripts locais).
- [ ] Tema claro/escuro funciona, persiste e respeita `prefers-color-scheme` na primeira visita.
- [ ] Todo o cabeçalho é operável por teclado; menu móvel prende o foco e fecha com `Esc`.
- [ ] `docs/componentes.html` mostra todos os componentes e estados, nos dois temas.
- [ ] `node --check js/*.js` sem erros; nenhuma rolagem horizontal em 360 px.

---

### Sprint 2: Hero e marca

**Objetivo.** Entregar a **primeira impressão**: hero com a animação "Do DNA ao circuito", faixa de números calculados do catálogo e a seção **A marca**, com textos aprovados pela autora.

**Esforço:** 2 dias · **Ferramentas sugeridas:** Claude (código e texto); Gemini/Nanobanana apenas para o fundo opcional (P2.4).

**Pré-requisitos:** Sprint 1 concluída. **Antes de começar**, a autora lê e ajusta o **banco de textos** abaixo (os textos da marca são dela).

#### S2 · Banco de textos-base (rascunho para aprovação)

| Elemento | Texto proposto |
|:---|:---|
| Título do hero (`h1`) | Ciência aberta, gamificada e bonita de aprender |
| Subtítulo | Objetos de aprendizagem digitais abertos que unem rigor pedagógico, gamificação e design acolhedor. |
| CTA principal / secundário | Explorar o catálogo · Conhecer a marca |
| Abertura de "A marca" | Aqui, biologia, computação, ciência de dados, biotecnologia e design educacional se encontram para transformar aulas complexas em experiências pedagógicas acolhedoras, gamificadas e esteticamente inspiradoras. |
| Missão | Cocriar recursos educacionais visuais, digitais e abertos que unam rigor pedagógico, metodologias ativas e estética acessível, capacitando educadores(as) e estudantes a ensinarem com autonomia e confiança. |
| Visão | Ser uma rede latino-americana de referência em educação aberta, gamificada e interseccional, onde professores, estudantes e criadores de conteúdo se sintam empoderados para experimentar, inovar e compartilhar. |
| Princípios (6) | **Acesso aberto**: todo recurso é, ou caminha para ser, um REA. · **Colaboração horizontal**: ninguém constrói sozinho. · **Rigor pedagógico**: metodologias ativas sustentam tudo. · **Estética acolhedora**: aprender também pode ser bonito. · **Acessibilidade e inclusão**: linguagem simples, contraste, alt-text. · **IA responsável**: uso consciente de assistentes de IA. |
| Quem está por trás (rascunho) | Prof.ª Pâmella Araújo Balcaçar é licenciada em Ciências Biológicas e tecnóloga em Informática. Desenvolve objetos de aprendizagem digitais na perspectiva da educação e da ciência aberta, para estudantes da rede pública de Mato Grosso. |
| Citação de fecho | "Aprender ciência pode — e deve — ser leve, rigoroso e bonito." |

Missão, visão, princípios e citação vêm do README público do perfil da organização; o bloco "Quem está por trás" é um **rascunho** a ser revisado pela autora (decisão D5, seção 12).

#### S2 · Tarefas

| ID | Tarefa | Quem | Saída |
|:--:|:---|:---:|:---|
| S2.1 | Revisar e aprovar o banco de textos | Autora | Textos finais |
| S2.2 | Hero com SVG animado | IA (P2.1) | Marcação do hero, CSS e animação |
| S2.3 | Seção "A marca" | IA (P2.2) | Marcação e CSS da seção |
| S2.4 | Faixa de números e animações de entrada | IA (P2.3) | `js/stats.js`, `js/reveal.js` |
| S2.5 | Fundo artístico do hero (opcional) | IA de imagem (P2.4) | `assets/img/hero/hero-bg.webp` |
| S2.6 | Conferência visual, PR e tag `v0.3.0` | Autora | Registro em `SPRINTS.md` |

#### S2 · Prompts

**P2.1 · Hero com a hélice que vira circuito** (Claude Code)

```text
PAPEL: designer de interface com domínio de SVG e animação CSS acessível.

CONTEXTO: leia as seções 4.1, 4.7, 5.3 (linha "Hero"), 6.2 (CSP) e o banco de textos da Sprint 2 em docs/projeto-executivo.md. Já existem o esqueleto de index.html, os componentes e os tokens.

TAREFA:
1. No index.html, dentro de <main>, ANTES de #marca, crie a seção do hero: logotipo pequeno, h1, subtítulo, dois botões (.btn--cta para #catalogo e .btn--ghost para #marca) e um contêiner para a ilustração.
2. Desenhe um SVG INLINE ORIGINAL (viewBox 0 0 640 480, aria-hidden="true", focusable="false"): uma dupla hélice de DNA na metade esquerda, cujas duas fitas (turquesa --teal-500 e azul --navy-700 no claro / --teal-300 e branco no escuro) seguem para a direita e se transformam em trilhas de circuito ortogonais (linhas horizontais e verticais com cantos retos), terminando em 6 a 8 nós circulares laranja (--orange-500) e uma seta pequena apontando para cima e para a direita. Use pathLength="1" em cada traço animado. Não copie o banner hero.png nem desenhe o logotipo existente.
3. Animação em css/sections.css (camada "sections"): desenho progressivo por stroke-dashoffset de 1 para 0, 6 segundos, uma única vez, com atraso escalonado entre traços (animation-delay em classes .delay-1 a .delay-6, nunca em style=""); nós aparecem com fade e escala de 0.6 para 1 ao final. Com prefers-reduced-motion: reduce, o desenho aparece COMPLETO e estático.
4. Cores do SVG por classes CSS que usam os tokens (sem atributos stroke="#..." fixos), para funcionar nos dois temas.
5. O LCP deve ser o texto do h1 (o SVG não pode bloquear a pintura). Reserve o espaço do SVG com aspect-ratio para evitar CLS.
6. Layout: em 360 px o texto vem primeiro e o SVG abaixo, com altura máxima de 280 px; em 1024 px ou mais, duas colunas (texto 6/12, SVG 6/12).

RESTRIÇÕES: sem imagens bitmap, sem bibliotecas de animação, sem style="" e sem <style> em linha; usar apenas tokens de cor; o SVG deve pesar menos de 6 KB.

ENTREGA: trecho do index.html (hero), css/sections.css (estilos do hero) e o SVG isolado em assets/img/hero/helice-circuito.svg para referência.

VERIFICAÇÃO: nos dois temas e em 360, 768 e 1440 px, confirme que o desenho se completa em cerca de 6 s; ative "reduzir movimento" no sistema e confirme o desenho estático completo; rode o Lighthouse mobile (Desempenho >= 95, CLS <= 0,1); contraste dos botões conforme node scripts/checar-contraste.mjs.
```

**P2.2 · Seção "A marca"** (Claude Code)

```text
PAPEL: designer de interface e redatora(o) UX em português do Brasil.

CONTEXTO: leia as seções 4.5, 4.9, 5.3 (linha "A marca") e o banco de textos da Sprint 2 (use os textos aprovados, sem reescrever).

TAREFA: preencha a seção #marca do index.html (substitua o parágrafo provisório):
1. h2 "A marca" e o parágrafo de abertura.
2. Dois cartões lado a lado (empilhados em telas estreitas): "Missão" e "Visão", com ícones do sprite.
3. Grade de 6 cartões de princípios (ícone, título em h3, uma frase), em 1, 2 e 3 colunas conforme a largura.
4. Bloco "Quem está por trás": imagem do logotipo (assets/logo/biotech-logo.webp, alt "Logotipo Bio+Tech EduDesign: dupla hélice de DNA e circuito"), texto do rascunho de bio e, abaixo, a citação de fecho em <blockquote>.
5. CSS em css/sections.css (camada "sections"), com fundo alternado (--surface-alt) para separar do hero.

RESTRIÇÕES: usar exatamente os textos do banco; nenhum fato novo sobre a autora; ícones decorativos com aria-hidden="true"; hierarquia h2 > h3 sem saltos; sem style="".

ENTREGA: trecho do index.html (#marca) e o CSS novo.

VERIFICAÇÃO: leitura por teclado e por leitor de tela (ordem lógica); contraste dos textos sobre --surface-alt (node scripts/checar-contraste.mjs); em 360 px nenhuma coluna quebra o layout; zoom de 200% sem sobreposição.
```

**P2.3 · Faixa de números e animações de entrada** (Claude Code)

```text
PAPEL: engenheira(o) de JavaScript, com foco em acessibilidade e dados.

CONTEXTO: leia as seções 5.4, 6.3 e 8.2 de docs/projeto-executivo. O catálogo está em window.BTE_CATALOGO (data/catalogo.js) e os utilitários em js/util.js.

TAREFA:
1. No hero, crie a faixa de números com 4 itens: <span data-stat="oad">, <span data-stat="licoes">, <span data-stat="simuladores">, <span data-stat="mit"> e rótulos: "OAD no catálogo", "lições publicadas de 12", "com simulador ou laboratório virtual", "com licença MIT". Dentro de comentários HTML "<!-- stats:inicio -->" e "<!-- stats:fim -->" (a Sprint 3 gera o valor inicial a partir dos dados).
2. js/stats.js: BTE.stats.init() calcula a partir de BTE_CATALOGO:
   - oad = quantidade de itens;
   - licoes = quantidade de números distintos de 17 a 28 cobertos por pelo menos um OAD com status "publicado";
   - simuladores = itens cujo array recursos contém "simulador" ou "laboratorio-virtual";
   - mit = itens com licenca === "MIT" (mostrar "7 de 10": valor e total).
   Preenche os spans com textContent. Se movimento for permitido (matchMedia "(prefers-reduced-motion: no-preference)"), faz contagem de 0 até o valor em 800 ms com requestAnimationFrame, caso contrário mostra o valor final direto. A região tem aria-label "Números do ecossistema".
3. js/reveal.js: BTE.reveal.init() usa IntersectionObserver (threshold 0.15) para adicionar a classe .is-visible a elementos com [data-reveal] (fade e subida de 12 px definidos em css/sections.css); sem IntersectionObserver ou com redução de movimento, adiciona .is-visible a todos de imediato. Marque com data-reveal os cartões da seção "A marca".
4. Registre BTE.stats.init() e BTE.reveal.init() em js/main.js.

RESTRIÇÕES: nunca escrever os números no JS ou no HTML (só nos marcadores gerados); sem innerHTML; sem bibliotecas; sem style="" (a animação é por classe CSS).

ENTREGA: js/stats.js, js/reveal.js, js/main.js atualizado, trecho do index.html e CSS novo.

VERIFICAÇÃO: node --check; abra a página e confirme "10", "11", "5" e "7 de 10"; altere temporariamente a licença de um OAD em data/catalogo.js e confirme que o número muda sozinho; reverta. Com "reduzir movimento" ativo não deve haver contagem animada.
```

**P2.4 · Fundo artístico do hero (opcional)** (Gemini / Nanobanana)

```text
Crie uma imagem de fundo abstrata para o hero de um site educacional de ciência aberta, estilo "Soft Tech / Clean Modernism".
- Composição: formas orgânicas suaves e linhas finas de circuito que se desfazem em fitas de dupla hélice de DNA, com muito espaço vazio no lado esquerdo (reservado a texto).
- Paleta: azul-marinho profundo #0B2747 e #061629, turquesa #2DC3BF e #7FE0DB, pequenos pontos de luz laranja #F47C26 (no máximo 5% da área).
- Estilo: gradientes suaves, brilho discreto, aparência limpa e acolhedora; sem textos, sem letras, sem logotipos, sem pessoas, sem marcas d'água.
- Formato: 1920x1080, horizontal, baixa densidade de detalhes (fundo, não protagonista), adequada a texto branco sobre a área esquerda com contraste mínimo de 7:1.
Gere 3 variações. Depois de escolher, otimize com: python3 scripts/otimizar_imagens.py --origem <pasta> --saida assets/img/hero (WebP até 120 KB, 1600 px de largura) e registre em docs/fontes.md a ferramenta usada e o prompt.
```

#### S2 · Arquivos de saída

| Arquivo | Origem |
|:---|:---|
| `index.html` (hero, números, #marca), `css/sections.css` (hero, marca, revelação) | P2.1 a P2.3 |
| `assets/img/hero/helice-circuito.svg` (referência) | P2.1 |
| `js/stats.js`, `js/reveal.js`, `js/main.js` | P2.3 |
| `assets/img/hero/hero-bg.webp` (opcional) | P2.4 |

#### S2 · Critérios de aceite

- [ ] Hero com `h1` como elemento de LCP; desenho completa em ~6 s e é **estático** com `prefers-reduced-motion`.
- [ ] Faixa mostra **10**, **11**, **5** e **7 de 10**, calculados dos dados (mudar o catálogo muda o número).
- [ ] "A marca" usa os textos aprovados; hierarquia `h2 > h3` sem saltos.
- [ ] Lighthouse mobile: Desempenho ≥ 95 e CLS ≤ 0,1 (medição preliminar).
- [ ] Contraste verificado (`checar-contraste.mjs` com código 0) nos dois temas.

---

### Sprint 3: Catálogo de OAD/REA

**Objetivo.** Entregar o **coração do portal**: a seção `#catalogo` com os **10 cards**, cada um com sua **breve descrição abaixo da imagem**, busca por texto, filtros por tema e formato, ordenação, contador acessível, estado vazio, miniaturas otimizadas e a versão sem JavaScript (`<noscript>`).

**Esforço:** 3 dias · **Ferramentas sugeridas:** Claude (código); Copilot (testes); Gemini/Nanobanana (arte própria das miniaturas, se a autora preferir à captura de tela).

**Pré-requisitos:** Sprint 2 concluída; `data/catalogo.js` válido. Para as miniaturas, uma máquina **com acesso à internet** (a captura abre as páginas publicadas) e Playwright (`pip install playwright` e `python3 -m playwright install chromium`).

#### S3 · Tarefas

| ID | Tarefa | Quem | Saída |
|:--:|:---|:---:|:---|
| S3.1 | Capturar telas das páginas publicadas e gerar as 10 miniaturas | IA (P3.1) + autora | `scripts/capturar_miniaturas.py`, `assets/img/oad/*.webp`, `_fallback.svg` |
| S3.2 | Marcação e CSS da seção do catálogo | IA (P3.2) | Trecho de `index.html` e `css/sections.css` |
| S3.3 | Lógica de renderização, busca, filtros e estado na URL | IA (P3.3) | `js/catalogo-ui.js`, `scripts/testar-catalogo.mjs` |
| S3.4 | Gerar `<noscript>`, valores iniciais, JSON-LD e sitemap a partir dos dados | IA (P3.4) | `scripts/sincronizar.mjs` e blocos gerados no `index.html` |
| S3.5 | Verificador de links e validação estrita das miniaturas | IA (P3.5) | `scripts/checar-links.mjs`, `validar-catalogo.mjs --estrito` verde |
| S3.6 | Revisar miniaturas e descrições; PR e tag `v0.4.0` | Autora | Registro em `SPRINTS.md` |

#### S3 · Prompts

**P3.1 · Miniaturas dos OAD** (Claude Code; executar na máquina da autora)

```text
PAPEL: engenheira(o) de automação e de imagens para web.

CONTEXTO: leia as seções 3 (ADR-07), 4.6, 4.8 e 8.1 a 8.2 de docs/projeto-executivo.md. O catálogo está em data/catalogo.js; cada OAD tem os campos id, urlPages, status, miniatura e miniaturaAlt.

TAREFA:
1. Escreva scripts/capturar_miniaturas.py (Python 3 + Playwright + Pillow) que:
   a) obtenha o catálogo com: node -e "global.window={};require('./data/catalogo.js');console.log(JSON.stringify(window.BTE_CATALOGO))" (sem parser próprio de JavaScript);
   b) para cada OAD com status "publicado", abra urlPages em Chromium com viewport 1280x800 e esquema de cores claro, espere o evento load e mais 2 segundos, e capture a janela (não a página inteira);
   c) redimensione para 640x400 com LANCZOS e grave em assets/img/oad/<id>.webp, qualidade inicial 80, reduzindo de 5 em 5 até no máximo 60 KB;
   d) aceite --somente <id> (repetível) e --pasta-manual <pasta>: se existir <pasta>/<id>.png ou .jpg, use essa imagem (recorte central 16:10) em vez da captura;
   e) imprima uma tabela "id | origem (captura ou manual) | dimensões | KB | resultado" e termine com código 1 se alguma captura falhar.
2. Crie assets/img/oad/_fallback.svg: gradiente turquesa para azul-marinho (tokens da seção 4.2), proporção 16:10, sem texto, com um traço de circuito discreto; peso menor que 2 KB.
3. Para chemical-royale-v2 (status em construção, sem página), NÃO gere captura: o card usará o fallback, e isso deve ser registrado no resumo impresso.

RESTRIÇÕES: o script nunca preenche formulários nem clica em nada nas páginas; se a tela inicial de um OAD pedir cadastro ou identificação, o resultado deve ser sinalizado "usar imagem manual" (a autora fornece a arte); respeitar robots e não sobrecarregar os sites (uma página por vez, pausa de 1 s entre páginas); mensagens em português.

ENTREGA: scripts/capturar_miniaturas.py e assets/img/oad/_fallback.svg; depois da execução pela autora, as 9 miniaturas .webp.

VERIFICAÇÃO: cada .webp tem 640x400 e no máximo 60 KB; abra as 9 imagens e confirme que mostram a tela inicial do respectivo OAD e que nenhuma exibe dado pessoal de pessoa real; a lista final bate com os campos "miniatura" do catálogo.
```

**P3.2 · Marcação e CSS da seção do catálogo** (Claude Code)

```text
PAPEL: designer de interface e engenheira(o) de HTML e CSS acessíveis.

CONTEXTO: leia as seções 4.5, 4.6, 5.3 (linha "Catálogo"), 6.4 e 6.5 de docs/projeto-executivo.md. Os componentes .card, .chip, .tag, .badge-* e .btn já existem em css/components.css.

TAREFA: preencha a seção #catalogo do index.html (substitua o provisório):
1. h2 "Catálogo de OAD/REA" e um parágrafo curto de introdução ("Aulas e arenas gamificadas, abertas e prontas para usar em sala ou em casa.").
2. Barra de controles em um contêiner com role="search":
   - <label for="busca"> "Buscar por título, tema ou lição" + <input type="search" id="busca" autocomplete="off">;
   - grupo "Tema" (role="group" aria-labelledby): botões-chip "Todos", "Química geral e inorgânica", "Físico-química", "Química orgânica", "Estratégia ENEM", cada um <button type="button" aria-pressed>, com data-filtro="categoria" e data-valor;
   - grupo "Formato": "Todos", "Arena gamificada", "Aula gamificada", "Painel e checklists", com data-filtro="formato";
   - <label for="ordem"> "Ordenar" + <select id="ordem"> com "Por lição" (valor "licao") e "Por nome" (valor "nome").
3. <p id="contador" aria-live="polite"> "Mostrando 10 de 10" (o texto será atualizado pelo JS).
4. <ul id="lista-cards" class="grid grid--cards"> vazio (o JS cria os <li><article class="card">...</article></li>).
5. Estado vazio <div id="vazio" hidden> com título "Nenhum OAD encontrado", instrução ("Tente outras palavras ou remova um filtro.") e <button type="button" id="limpar">Limpar filtros</button>.
6. Marcadores para a Sprint 3 (P3.4): "<!-- noscript:inicio -->" e "<!-- noscript:fim -->" logo após a lista.
7. CSS em css/sections.css: barra de controles (flex com quebra, espaçamento por tokens), campo de busca com altura de 44 px e ícone de lupa do sprite, chips, grade de cards (1 coluna até 639 px, 2 de 640 a 1023, 3 de 1024), estado vazio centralizado.

RESTRIÇÕES: nenhum <form> (a CSP define form-action 'none'); nenhum style=""; nenhum texto de card no HTML (vem dos dados); ordem de tabulação lógica (busca, chips de tema, chips de formato, ordenação, cards).

ENTREGA: trecho do index.html (#catalogo) e o CSS novo.

VERIFICAÇÃO: em 360 px os chips quebram em linhas sem rolagem horizontal; navegação por teclado percorre todos os controles; leitor de tela anuncia "Tema, grupo" e "pressionado" nos chips (descreva o que foi conferido).
```

**P3.3 · Lógica do catálogo** (Claude Code)

```text
PAPEL: engenheira(o) de JavaScript, com foco em acessibilidade e testes.

CONTEXTO: leia as seções 4.6, 6.3 (inclua a "Regra da busca" e a função filtrar), 6.4, 6.5 e 8.1 a 8.2 de docs/projeto-executivo.md. Já existem util.js (BTE.norm, BTE.debounce, BTE.el), data/catalogo.js e a marcação do P3.2.

TAREFA:
1. js/catalogo-ui.js (função autoexecutável; expõe BTE.catalogo.init, .filtrar(estado) e .limparFiltros()):
   a) filtrar(estado): use EXATAMENTE a função de referência da seção 6.3 (busca por prefixo de palavra, todas as palavras exigidas, ordenação por "licao" ou "nome");
   b) criarCard(o): gere a marcação da seção 6.4 com createElement e textContent (imagem com width=640 height=400 loading=lazy decoding=async e alt=o.miniaturaAlt; selo de lição = o.licaoRotulo; selo de status; título h3; descrição o.descricao; até 3 tags; botão "Abrir aula" para urlPages e link "Código" para urlRepo, ambos com target=_blank e rel=noopener e texto auxiliar em .sr-only que inclui o título, como na seção 6.4: "Abrir aula Termoquímica (abre em nova aba)" e "Código de Termoquímica no GitHub (abre em nova aba)"). Para status "em-construcao": botão principal vira <span class="btn btn--primary" aria-disabled="true">Em breve</span>, sem href; card recebe a classe card--wip. Cada card tem id="card-<id>" e tabindex="-1" (para receber foco vindo da trilha);
   c) se a imagem falhar (evento "error", adicionado ANTES de definir src) ou o.miniatura não existir, troque para o fallback: .card__media--fallback com gradiente conforme o.acento e a inicial do título (via textContent);
   d) estado { busca, categoria, formato, ordem } lido de URLSearchParams (?q=&tema=&formato=&ordem=) ao iniciar e gravado com history.replaceState em try/catch (pode falhar em file://); busca com debounce de 150 ms; chips de cada grupo são exclusivos (clicar no marcado o desmarca = "Todos"); contador "Mostrando N de 10" (o total vem de BTE_CATALOGO.length); estado vazio visível só com 0 resultados; o botão "Limpar filtros" e BTE.catalogo.limparFiltros() restauram tudo e devolvem o foco ao campo de busca;
   e) nunca use innerHTML; não roube o foco ao filtrar.
2. scripts/testar-catalogo.mjs: use jsdom (npm i --no-save jsdom): carregue o index.html SEM executar scripts (runScripts "outside-only"), avalie nesta ordem data/catalogo.js, js/util.js e js/catalogo-ui.js na janela, chame BTE.catalogo.init() e confira, simulando entradas e cliques, a tabela de resultados esperados abaixo. Saída 1 se algum caso falhar.

RESULTADOS ESPERADOS (referência obrigatória):
- sem filtro: 10 cards;
- busca "orgânica": 2 (pre-enem-quimica, org);
- busca "inorgânicas": 1 (chemical-royale);
- tema "Físico-química": 5 (solucoes, termoquimica, cinetica, equilibrio, eletroquimica);
- busca "simulador": 4 (termoquimica, equilibrio, eletroquimica, org);
- busca "lição 23": 1 (termoquimica);
- busca "enem": 6 (pre-enem-quimica, solucoes, termoquimica, cinetica, eletroquimica, enem);
- formato "Painel e checklists": 1 (enem);
- busca "xyz": 0 e estado vazio visível; depois "Limpar filtros" volta a 10;
- ordenação "Por nome": ordem alfabética em pt-BR (compare com localeCompare);
- o card de chemical-royale-v2 não tem href no botão principal e exibe "Em breve".

RESTRIÇÕES: sem bibliotecas no navegador; sem import/export; comentários curtos em português; registre BTE.catalogo.init() em js/main.js.

ENTREGA: js/catalogo-ui.js, js/main.js atualizado e scripts/testar-catalogo.mjs.

VERIFICAÇÃO: node --check js/catalogo-ui.js; npm i --no-save jsdom && node scripts/testar-catalogo.mjs (todos os casos "ok"); no navegador, recarregar com ?q=orgânica&tema=organica restaura o estado; teclado: Tab percorre os cards e Enter abre o botão principal.
```

**P3.4 · Geração a partir dos dados (noscript, números, JSON-LD, sitemap)** (Claude Code)

```text
PAPEL: engenheira(o) de automação de conteúdo estático, com foco em SEO.

CONTEXTO: leia as seções 6.2 (CSP), 6.5 (noscript), 5.4, 7.2 e 8.2 de docs/projeto-executivo.md. O catálogo é a fonte única.

TAREFA: crie scripts/sincronizar.mjs (Node 18+, só módulos nativos; carregue o catálogo com node:vm) que substitua o conteúdo ENTRE marcadores em index.html e gere sitemap.xml:
1. "<!-- noscript:inicio -->" a "<!-- noscript:fim -->": <noscript><ul> com um <li> por OAD (título como link para urlPages, ou texto "(em construção)" se não houver; descrição; selo da lição), na ordem do campo "ordem".
2. "<!-- stats:inicio -->" a "<!-- stats:fim -->": a faixa de números do hero com os valores iniciais calculados (mesmas regras de js/stats.js: OAD, lições publicadas de 12, simulador ou laboratório, licença MIT "7 de 10").
3. "<!-- jsonld:inicio -->" a "<!-- jsonld:fim -->": um <script type="application/ld+json"> com @graph contendo Organization (name "Bio+Tech EduDesign", url do portal, logo absoluto, sameAs com https://github.com/Bio-Tech-Edu), WebSite (inLanguage "pt-BR") e ItemList de LearningResource (name, description, url, inLanguage "pt-BR", learningResourceType, educationalLevel "Ensino Médio", isAccessibleForFree true, license quando houver; para "em-construcao" use urlRepo). Escape correto de JSON e de "<" como <.
4. sitemap.xml com index.html (raiz do portal) e privacidade.html, lastmod = BTE_META.atualizadoEm, URLs ABSOLUTAS (exigência do formato).
5. Opção --verificar: não grava nada; retorna código 1 se algum bloco do index.html ou o sitemap.xml difere do que seria gerado (usado no CI).
6. Opção --base <url> (padrão https://bio-tech-edu.github.io/site/) para URLs absolutas.
7. Adicione os marcadores ausentes ao index.html (jsonld dentro do <head>, depois da CSP; stats no hero; noscript já existe após a lista).

RESTRIÇÕES: idempotente (rodar duas vezes não muda nada); preservar o resto do index.html byte a byte; mensagens em português; nenhum conteúdo digitado à mão dentro dos marcadores.

ENTREGA: scripts/sincronizar.mjs, index.html com marcadores e blocos gerados, sitemap.xml.

VERIFICAÇÃO: rode "node scripts/sincronizar.mjs" e depois "node scripts/sincronizar.mjs --verificar" (código 0); mude uma descrição no catálogo, rode --verificar (deve dar 1), rode sem opção e confira que o <noscript> mudou; desative o JavaScript no navegador e confirme que a lista dos 10 OAD aparece; valide o JSON-LD em um validador de JSON.
```

**P3.5 · Verificador de links e miniaturas** (Claude Code)

```text
PAPEL: engenheira(o) de qualidade.

CONTEXTO: leia as seções 8.3, 10.3 e 11.2 de docs/projeto-executivo.md.

TAREFA:
1. scripts/checar-links.mjs (Node 18+, fetch nativo): modos --internos (padrão, sem rede) e --externos (acrescenta rede).
   - Internos: em index.html, privacidade.html e 404.html (ignore 404.html para caminhos de base), todo href/src relativo aponta para arquivo existente; todo href="#x" tem um elemento id="x".
   - Externos: para cada urlPages (OAD publicados) e urlRepo do catálogo, faça requisição com limite de 10 s, 2 novas tentativas e pausa de 500 ms; aceite 2xx e 3xx; registre status e tempo.
   - Saída: tabela "tipo | alvo | status | resultado" e código 1 se houver falha. Um OAD "em-construcao" com urlPages null não é verificado; seu urlRepo sim.
2. Sem alterar o validador (ele já tem a opção): rode node scripts/validar-catalogo.mjs --estrito, que trata miniatura inexistente de OAD "publicado" como ERRO (o "em-construcao" pode usar o fallback). A partir desta sprint, esse é o comando padrão do projeto (README, CONTRIBUTING e CI). Atualize a seção "Como adicionar um OAD" do README.md com este comando.

RESTRIÇÕES: sem dependências; não seguir mais de 5 redirecionamentos; identificar-se com o User-Agent "BTE-checar-links/1.0 (+https://github.com/Bio-Tech-Edu/site)".

ENTREGA: scripts/checar-links.mjs e o README.md atualizado.

VERIFICAÇÃO: node scripts/validar-catalogo.mjs --estrito termina com "Catálogo válido: 0 erros" (com as 9 miniaturas em disco; renomeie uma temporariamente e confirme código 1); node scripts/checar-links.mjs --internos termina com código 0; com --externos todos os 9 OAD publicados e os 10 repositórios respondem (se algum falhar, é um achado real: registre em SPRINTS.md); quebre propositalmente um href no HTML e confirme a detecção.
```

#### S3 · Arquivos de saída

| Arquivo | Origem |
|:---|:---|
| `scripts/capturar_miniaturas.py`, `assets/img/oad/*.webp` (9), `assets/img/oad/_fallback.svg` | P3.1 |
| `index.html` (#catalogo) e `css/sections.css` (controles, grade, estado vazio) | P3.2 |
| `js/catalogo-ui.js`, `js/main.js`, `scripts/testar-catalogo.mjs` | P3.3 |
| `scripts/sincronizar.mjs`, blocos gerados em `index.html`, `sitemap.xml` | P3.4 |
| `scripts/checar-links.mjs`, `README.md` (comando `--estrito`) | P3.5 |

#### S3 · Critérios de aceite

- [ ] Os **10 cards** aparecem, cada um com **imagem, selos, título e descrição curta abaixo** (≤ 140 caracteres), tags e botões.
- [ ] `node scripts/validar-catalogo.mjs --estrito` termina com "Catálogo válido: 0 erros" (as 9 miniaturas existem).
- [ ] A tabela de resultados esperados do P3.3 passa integralmente em `node scripts/testar-catalogo.mjs`.
- [ ] O card de `chemical-royale-v2` mostra "Em breve" sem link; nenhum link do catálogo está quebrado (`checar-links.mjs --externos`).
- [ ] Sem JavaScript, a lista dos 10 OAD aparece em `<noscript>`; `sincronizar.mjs --verificar` retorna 0.
- [ ] Miniaturas de 640×400 com até 60 KB cada; `width` e `height` declarados; CLS ≤ 0,1.
- [ ] Zero uso de `innerHTML`: `grep -R "innerHTML" js/` não retorna nada.

---

### Sprint 4: Trilha, metodologia e comunidade

**Objetivo.** Completar o conteúdo do portal: a **trilha de lições 17 a 28**, a **metodologia**, a **comunidade** (REA, licenças, como contribuir, badges), o **contato**, a **política de privacidade** e a **página 404**, além dos arquivos de contribuição do repositório.

**Esforço:** 2 a 3 dias · **Ferramentas sugeridas:** Claude (código e texto); Copilot (revisão dos textos jurídicos e de contribuição).

**Pré-requisitos:** Sprint 3 concluída. Decisões **D3** (e-mail de contato), **D4** (uso de logotipos institucionais) e **D6** (licença dos três repositórios sem licença) respondidas ou registradas como pendentes.

#### S4 · Tarefas

| ID | Tarefa | Quem | Saída |
|:--:|:---|:---:|:---|
| S4.1 | Trilha das lições | IA (P4.1) | `#trilha`, `js/trilha.js` |
| S4.2 | Metodologia e comunidade | IA (P4.2) | `#metodologia`, `#comunidade` |
| S4.3 | Contato, rodapé, privacidade e 404 | IA (P4.3) | `#contato`, `privacidade.html`, `404.html` |
| S4.4 | Arquivos de contribuição e modelos do GitHub | IA (P4.4) | `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `.github/*` |
| S4.5 | Revisão jurídica e de textos pela autora; PR e tag `v0.5.0` | Autora | Registro em `SPRINTS.md` |

#### S4 · Prompts

**P4.1 · Trilha das lições 17 a 28** (Claude Code)

```text
PAPEL: engenheira(o) de interface com foco em visualização acessível de progresso.

CONTEXTO: leia as seções 4.1 (gesto 3), 4.5 (nó da trilha), 5.3 (linha "Trilha"), 6.3 (regra da trilha) e 8.4 de docs/projeto-executivo.md.

TAREFA:
1. Seção #trilha do index.html: h2 "Trilha Pré-ENEM Química", um parágrafo ("Doze lições, uma jornada: escolha uma lição para ir direto ao seu OAD."), um contêiner rolável (role="region", aria-label="Trilha de lições, role para ver todas", tabindex="0") com <ol id="trilha-lista" class="trail"> vazio, e uma legenda com os dois estados (círculo cheio "Publicado"; círculo tracejado com ícone "Em construção").
2. js/trilha.js (BTE.trilha.init): para n de 17 a 28, procure em BTE_CATALOGO o OAD cujo array licao contém n, PREFERINDO status "publicado"; crie <li class="trail__item"> com:
   - se publicado: <a class="trail-node" href="#card-<id>"> com o número e o nome acessível "Lição N: <título> (publicado)";
   - se só em construção: <span class="trail-node trail-node--wip" role="img" aria-label="Lição N: <título> (em construção)"> sem link;
   - rótulo curto abaixo do nó (título do OAD, no máximo 2 linhas).
   Ao clicar em um nó publicado: chame BTE.catalogo.limparFiltros(), role até o card, dê foco ao card (id "card-<id>", já com tabindex -1) e destaque-o por 2 s com a classe .is-target (sem animação se prefers-reduced-motion).
3. CSS (css/sections.css): linha do tempo horizontal com conector entre nós (pseudo-elemento), rolagem horizontal com scroll-snap no celular (sem versão vertical); nó ativo (hover/foco) com anel laranja; legenda.
4. Registre BTE.trilha.init() em js/main.js (depois de BTE.catalogo.init()).

RESTRIÇÕES: nenhum número de lição digitado no HTML; usar o catálogo; sem innerHTML; contraste dos nós conforme tokens; o estado "em construção" nunca depende só de cor (tracejado + ícone + aria-label).

ENTREGA: trecho do index.html, js/trilha.js, js/main.js e CSS novo.

VERIFICAÇÃO: node --check; a trilha mostra 12 nós, 11 com link e 1 tracejado (lição 21); a lição 20 aponta para #card-pre-enem-quimica (não para chemical-royale-v2); clicar na lição 23 com um filtro ativo limpa o filtro e foca o card Termoquímica; teclado: Tab percorre os 11 nós e Enter ativa.
```

**P4.2 · Metodologia e comunidade** (Claude Code)

```text
PAPEL: designer de interface e redatora(o) em português do Brasil, com cuidado para não afirmar o que os OAD não fazem.

CONTEXTO: leia as seções 4.5, 4.9, 5.3 (linhas "Metodologia" e "Comunidade") e 12 (decisão D2) de docs/projeto-executivo.md, e use o banco de textos abaixo sem acrescentar fatos.

BANCO DE TEXTOS
Metodologia (7 cartões; título | frase):
- Aprendizagem baseada em problemas (ABP) | A aula parte de uma situação-problema e o conhecimento é construído para resolvê-la.
- Gamificação | XP, vidas, missões, badges e chefões transformam a prática em jornada.
- Storytelling | Narrativas e cientistas históricas dão contexto e sentido aos conceitos.
- Simuladores e laboratórios virtuais | Calorímetro, diluição e Le Chatelier para experimentar variáveis sem risco.
- Fato ou Fake | Afirmações para julgar e justificar desenvolvem o pensamento crítico.
- Cornell Notes | Método de anotação que organiza ideias, palavras-chave e síntese.
- Feedback explicativo duplo | Cada questão traz reforço para o acerto e resolução passo a passo para o erro.
Comunidade:
- O que é REA: Recursos Educacionais Abertos são materiais de ensino, aprendizagem e pesquisa em domínio público ou com licença aberta, que permitem uso, adaptação e compartilhamento.
- Licenças: o código usa MIT; textos e imagens autorais do portal usam CC BY 4.0 (a confirmar na decisão D2); alguns OAD ainda não declaram licença e aparecem como "licença a definir".
- Como contribuir (tabela perfil | como): Educador(a): testar em sala, sugerir melhorias e propor temas por issue. Estudante: relatar dúvidas, sugerir exemplos e participar dos desafios. Dev ou designer: abrir pull requests, criar modelos, melhorar acessibilidade e documentação. Pesquisador(a): revisar conteúdo científico, sugerir referências e cocriar trilhas. Criador(a) de conteúdo: adaptar recursos para outros formatos (Canva, Notion, redes sociais, vídeo).
- Reconhecimento (5 badges simbólicos; nome | como conquistar): Semente | primeira issue ou PR aceito. DNA Contributor | 5 ou mais contribuições aceitas. Design Ally | contribuições em design, ilustração ou acessibilidade. Pedagoga(o) REA | revisão pedagógica ou criação de trilhas. Core Community | manutenção contínua e mentoria de novatos.
- Links: https://github.com/Bio-Tech-Edu/site/issues (issues do portal) e https://github.com/Bio-Tech-Edu (perfil da organização).

TAREFA:
1. #metodologia: h2 "Metodologia e rigor pedagógico", parágrafo curto e grade dos 7 cartões (ícone do sprite ou ícone novo adicionado ao sprite, título h3, frase).
2. #comunidade: h2 "Comunidade e ciência aberta"; bloco "O que é REA"; bloco "Licenças" (3 linhas: código, conteúdo, OAD sem licença declarada); tabela acessível "Como contribuir" (com <caption>, <th scope>); grade de 5 badges (texto, nunca só emoji; emoji opcional com aria-hidden); botões "Abrir uma issue" e "Conhecer a organização" (target=_blank, rel=noopener).
3. CSS em css/sections.css; marque cartões com data-reveal.

RESTRIÇÕES: não afirmar que "todos os OAD" têm uma característica (cada recurso aparece em alguns OAD, conforme o campo recursos do catálogo); não prometer nota, aprovação nem resultado; tabela responsiva sem rolagem horizontal da página (use rolagem só dentro do contêiner da tabela, com tabindex 0 e aria-label).

ENTREGA: trechos do index.html (#metodologia e #comunidade) e o CSS novo.

VERIFICAÇÃO: hierarquia h2 > h3; a tabela é lida corretamente por leitor de tela (cabeçalhos associados); contraste via node scripts/checar-contraste.mjs; nenhuma frase do banco foi alterada.
```

**P4.3 · Contato, rodapé, privacidade e 404** (Claude Code)

```text
PAPEL: engenheira(o) front-end com atenção à LGPD (Lei 13.709/2018) e à linguagem simples.

CONTEXTO: leia as seções 2.3 (achados A8 e A9), 6.7 (segurança e privacidade), 5.1 e 12 (decisões D3 e D4) de docs/projeto-executivo.md.

TAREFA:
1. #contato do index.html: h2 "Contato"; link para o perfil https://github.com/Bio-Tech-Edu; e-mail da marca conforme a decisão D3 (se D3 estiver pendente, deixe um comentário HTML "TODO D3" e mostre só o GitHub). Se houver e-mail, monte o link mailto por JavaScript a partir de data-usuario e data-dominio (js/main.js), com o endereço visível em texto; sem JavaScript, mostre o link do GitHub. Nota "Apoio institucional" em TEXTO (sem logotipos de SEDUC ou Governo de MT até a decisão D4).
2. Rodapé: nome da marca, links (privacidade, licenças, GitHub), ano e a frase "Feito com cuidado por educadoras(es), cientistas e criadoras(es) que acreditam em ciência aberta."
3. privacidade.html (mesmo cabeçalho/rodapé do portal, CSS e tema; sem JS externo), em linguagem simples, com seções: Quem somos; O que este portal NÃO coleta (cookies, formulários, análises de audiência, dados pessoais); O que fica no seu navegador (apenas a preferência de tema, em localStorage); Hospedagem (o GitHub, que hospeda o portal, pode registrar dados técnicos de acesso, como o endereço IP, conforme a política de privacidade dele); Links para outros sites e para os OAD (cada um com suas regras; o Chemical Royale pede nome, e-mail institucional, cidade e escola do estudante no próprio ambiente, fora do portal); Seus direitos (LGPD, art. 18) e como exercê-los (contato conforme D3); Última atualização (data).
4. 404.html: mensagem amigável, botões "Ir para o início" e "Ver o catálogo". EXCEÇÃO documentada à ADR-04: como o GitHub Pages serve o 404.html em qualquer caminho, inclua <base href="/site/"> com um comentário HTML explicando que, se o portal mudar de endereço (domínio próprio ou repositório raiz), esta linha deve ser ajustada (seção 11.6).
5. Garanta que index.html, privacidade.html e 404.html têm <!DOCTYPE html> em maiúsculas, lang="pt-BR" e a mesma CSP. Única diferença: no 404.html use base-uri 'self' (com base-uri 'none' o navegador ignora o <base>).

RESTRIÇÕES: não inventar o nome do encarregado de dados nem telefone; não usar logotipos institucionais; sem style="" e sem script em linha.

ENTREGA: trecho do index.html (#contato e rodapé), privacidade.html, 404.html e js/main.js atualizado.

VERIFICAÇÃO: abra uma URL inexistente em http://localhost:8000/x/y/z/ (para o 404, teste após o deploy); node scripts/checar-links.mjs --internos com código 0; leia a privacidade.html em voz alta e confirme que cada afirmação é verdadeira para o portal (zero cookies, zero formulários).
```

**P4.4 · Arquivos de contribuição e modelos do GitHub** (Copilot ou Claude)

```text
PAPEL: mantenedora(or) de projeto aberto, com cuidado em acolhimento e acessibilidade.

CONTEXTO: leia as seções 1.3, 7.1 e 11 de docs/projeto-executivo.md. ENTRADA OPCIONAL: se a organização já possui CONTRIBUTING.md, CODE_OF_CONDUCT.md ou modelos no repositório .github, a autora cola aqui o conteúdo atual; nesse caso, reaproveite o texto e apenas adapte ao portal.

TAREFA:
1. CONTRIBUTING.md: como relatar problema, como propor um novo OAD (passos da seção 11.4), como rodar o portal localmente, como validar antes do pull request (node scripts/validar-catalogo.mjs, checar-contraste.mjs, sincronizar.mjs --verificar), padrão de commits, critérios de aceite de pull request (acessibilidade, sem terceiros, sem innerHTML).
2. CODE_OF_CONDUCT.md: código de conduta acolhedor com seção "Uso responsável de IA" (declarar uso de IA em contribuições, revisar o que a IA gera, nunca enviar dados pessoais de estudantes a ferramentas de IA).
3. .github/ISSUE_TEMPLATE/novo-oad.yml (formulário YAML do GitHub com campos: título, repositório, lição, categoria, formato, descrição curta de até 140 caracteres, link Pages, licença, miniatura), .github/ISSUE_TEMPLATE/bug.yml (o que aconteceu, onde, dispositivo e navegador, captura) e .github/pull_request_template.md (resumo, tipo de mudança, lista de verificação com os scripts, acessibilidade, captura antes e depois).
4. .github/ISSUE_TEMPLATE/config.yml com blank_issues_enabled: true e link de contato para o perfil da organização.

RESTRIÇÕES: tom acolhedor, linguagem simples, português do Brasil; YAML válido; nenhuma promessa de prazo de resposta.

ENTREGA: os arquivos listados.

VERIFICAÇÃO: valide os YAML com python3 -c "import yaml,sys; [yaml.safe_load(open(f)) for f in sys.argv[1:]]; print('YAML ok')" .github/ISSUE_TEMPLATE/*.yml; todos os links relativos dos Markdown apontam para arquivos existentes.
```

#### S4 · Arquivos de saída

| Arquivo | Origem |
|:---|:---|
| `index.html` (#trilha, #metodologia, #comunidade, #contato, rodapé), `css/sections.css`, `js/trilha.js`, `js/main.js` | P4.1 a P4.3 |
| `privacidade.html`, `404.html` | P4.3 |
| `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `.github/ISSUE_TEMPLATE/{novo-oad,bug}.yml`, `config.yml`, `.github/pull_request_template.md` | P4.4 |

#### S4 · Critérios de aceite

- [ ] Trilha com **12 nós** (11 com link, 1 tracejado na lição 21) e navegação por teclado.
- [ ] A lição 20 leva ao card **ENEM Quest: Química** (publicado), nunca ao OAD em construção.
- [ ] `privacidade.html` revisada pela autora; nenhuma afirmação falsa sobre coleta de dados.
- [ ] `404.html` abre corretamente em um caminho profundo (teste após o deploy) e carrega estilos.
- [ ] Nenhum logotipo institucional usado sem a decisão D4; e-mail de contato conforme D3.
- [ ] YAML dos modelos de issue válido; `checar-links.mjs --internos` com código 0.

---

### Sprint 5: Acessibilidade, desempenho e SEO

**Objetivo.** Levar o portal às **metas da seção 1.4**: acessibilidade WCAG 2.2 AA verificada, desempenho dentro do orçamento, metadados de compartilhamento e busca e um PWA básico que funciona offline.

**Esforço:** 2 dias · **Ferramentas sugeridas:** Claude (correções), Copilot (revisão), pessoas reais para o teste manual com teclado e leitor de tela.

**Pré-requisitos:** Sprint 4 concluída; `npm i --no-save playwright @axe-core/playwright` e `npx playwright install chromium` na máquina da autora.

#### S5 · Tarefas

| ID | Tarefa | Quem | Saída |
|:--:|:---|:---:|:---|
| S5.1 | Auditoria de acessibilidade (automática e manual) e correções | IA (P5.1) + autora | `docs/auditoria-a11y.md` e correções |
| S5.2 | Orçamento e otimizações de desempenho | IA (P5.2) | `scripts/checar-orcamento.mjs` e ajustes |
| S5.3 | SEO, compartilhamento e verificador de âncoras | IA (P5.3) | Metadados no `index.html`, `robots.txt`, `scripts/checar-ancoras.mjs` |
| S5.4 | PWA básico e modo offline | IA (P5.4) | `manifest.webmanifest`, `sw.js` |
| S5.5 | Teste manual com leitor de tela (NVDA ou TalkBack) e em 4 navegadores; PR e tag `v0.6.0` | Autora | Registro em `SPRINTS.md` |

#### S5 · Prompts

**P5.1 · Auditoria de acessibilidade e correções** (Claude Code)

```text
PAPEL: especialista em acessibilidade web (WCAG 2.2 AA) e em testes automatizados.

CONTEXTO: leia as seções 4.2, 6.5, 10.2 e 10.4 de docs/projeto-executivo.md. O portal está completo em conteúdo (Sprints 0 a 4).

TAREFA:
1. Execute o axe-core com Playwright (npm i --no-save playwright @axe-core/playwright) em index.html, privacidade.html e 404.html servidos por "python3 -m http.server 8000", nos temas claro e escuro (emulando colorScheme) e nas larguras 360 e 1440 px. Liste cada violação com impacto, regra, elemento e correção.
2. Revise manualmente, no código, cada item da seção 6.5 e da seção 10.4 e marque "ok", "corrigido" ou "pendente (precisa de teste humano)".
3. Corrija TODAS as violações de impacto "serious" ou "critical" e as de "moderate" que não exijam decisão de design; documente as demais.
4. Confira: ordem de foco, foco visível em todos os controles, anúncio do contador "Mostrando N de 10", rótulos únicos nos links "Abrir aula" e "Código" (o texto auxiliar em .sr-only deve incluir o título do OAD, por exemplo "Abrir aula Termoquímica (abre em nova aba)"), idioma da página, títulos, alt de imagens, contraste, zoom 400%, prefers-reduced-motion e prefers-contrast.
5. Escreva docs/auditoria-a11y.md com: resumo, tabela de violações (antes e depois), itens para teste humano (leitor de tela, ampliação, controle por voz) e data.

RESTRIÇÕES: não suprimir regras do axe sem justificar por escrito; correções somente nos arquivos do projeto; nenhuma dependência de produção.

ENTREGA: docs/auditoria-a11y.md e os arquivos corrigidos, completos.

VERIFICAÇÃO: nova execução do axe com 0 violações "serious" ou "critical" em todas as páginas, temas e larguras; node scripts/checar-contraste.mjs com código 0; node scripts/testar-catalogo.mjs com código 0 (nada quebrou).
```

**P5.2 · Orçamento e otimizações de desempenho** (Claude Code)

```text
PAPEL: engenheira(o) de desempenho web.

CONTEXTO: leia as seções 1.4, 6.2 e 6.6 de docs/projeto-executivo.md.

TAREFA:
1. scripts/checar-orcamento.mjs (Node 18+, módulos nativos): meça e compare com os limites, imprimindo tabela "item | medido | limite | resultado":
   - HTML: index.html ≤ 40 KB;
   - CSS: soma dos 5 arquivos ≤ 40 KB sem compressão;
   - JS: soma de js/*.js e data/catalogo.js ≤ 30 KB em "equivalente minificado" (remova comentários de bloco, comentários de linha inteira, indentação e linhas em branco apenas para MEDIR; não altere os arquivos); informe também o tamanho gzip;
   - fontes: soma dos .woff2 ≤ 90 KB;
   - miniaturas: cada assets/img/oad/*.webp ≤ 60 KB;
   - og-image.jpg ≤ 200 KB;
   - peso inicial comprimido (gzip de HTML + CSS + JS + fontes preload, sem miniaturas) ≤ 250 KB.
   Código de saída 1 se algum item passar do limite.
2. Otimizações no código, sem mudar comportamento: preload só das 2 fontes da seção 6.2; width e height em todas as imagens; loading=lazy nas miniaturas abaixo da dobra; "content-visibility: auto" com contain-intrinsic-size nas seções abaixo do hero; fetchpriority="high" apenas no elemento de LCP quando for imagem; remover CSS e JS sem uso.
3. Meça com Lighthouse (npx lighthouse http://localhost:8000/ --only-categories=performance,accessibility,best-practices,seo --output=json --output-path=./lh-mobile.json --chrome-flags="--headless"), perfil mobile padrão, e registre em SPRINTS.md as 4 notas, LCP, CLS e INP/TBT.

RESTRIÇÕES: não introduzir build nem minificação obrigatória; não aumentar o número de requisições; não usar CDN.

ENTREGA: scripts/checar-orcamento.mjs, arquivos otimizados e o resumo das medições.

VERIFICAÇÃO: node scripts/checar-orcamento.mjs com código 0; Lighthouse mobile com Desempenho ≥ 95, Acessibilidade 100, Boas práticas 100, SEO 100; LCP ≤ 2,5 s; CLS ≤ 0,1.
```

**P5.3 · SEO, compartilhamento e verificador de âncoras** (Claude Code)

```text
PAPEL: especialista em SEO técnico e em compartilhamento social.

CONTEXTO: leia as seções 3 (ADR-04), 5.1, 6.2, 8.2 e o Anexo F de docs/projeto-executivo.md.

TAREFA:
1. No <head> do index.html acrescente, com URLs ABSOLUTAS (exigência dos protocolos, exceção documentada à ADR-04 apenas para estes metadados): canonical; Open Graph (og:type website, og:locale pt_BR, og:site_name, og:title, og:description, og:url, og:image com assets/logo/og-image.jpg e og:image:width 1200, og:image:height 630, og:image:alt); Twitter card summary_large_image; <meta name="theme-color"> duas vezes (um com media="(prefers-color-scheme: light)" #F3FAFB e outro com media="(prefers-color-scheme: dark)" #061629); <meta name="color-scheme" content="light dark">.
2. Título com no máximo 60 caracteres e descrição entre 120 e 160 caracteres, em português, sem exageros e sem promessa de aprovação.
3. robots.txt: "User-agent: *", "Allow: /" e "Sitemap: https://bio-tech-edu.github.io/site/sitemap.xml". Rode node scripts/sincronizar.mjs --verificar e corrija o que for preciso.
4. scripts/checar-ancoras.mjs (Node 18+, módulos nativos): (a) em cada HTML do projeto, todo href="#x" tem id="x" e não há ids duplicados; (b) nos Markdown listados por argumento (padrão: README.md, docs/projeto-executivo.md), cada link [texto](#ancora) tem título correspondente, usando o algoritmo de identificadores do GitHub (descrito no Anexo F); (c) links relativos de arquivo existem. Saída 1 se houver falha.

RESTRIÇÕES: não usar imagens de terceiros; descrição única por página; 404.html leva <meta name="robots" content="noindex"> e privacidade.html pode ser indexada.

ENTREGA: index.html atualizado, robots.txt, sitemap.xml (se mudou) e scripts/checar-ancoras.mjs.

VERIFICAÇÃO: node scripts/checar-ancoras.mjs com código 0 (inclusive em docs/projeto-executivo.md); após o deploy, testar um link do portal no depurador de compartilhamento do Facebook, no Post Inspector do LinkedIn e colando em uma conversa do WhatsApp (imagem e título corretos).
```

**P5.4 · PWA básico e modo offline** (Claude Code)

```text
PAPEL: engenheira(o) de PWA com foco em simplicidade e segurança de cache.

CONTEXTO: leia as seções 6.7, 7.2 e 11.7 de docs/projeto-executivo.md.

TAREFA:
1. manifest.webmanifest: name "Bio+Tech EduDesign", short_name "Bio+Tech", description curta, lang "pt-BR", start_url "./", scope "./", display "standalone", theme_color "#123A68", background_color "#F3FAFB", ícones icon-192.png e icon-512.png (purpose "any") por caminho relativo.
2. sw.js: constante VERSAO = "bte-v1"; no install, pré-cache da "casca" (index.html, privacidade.html, os 5 CSS, os JS, data/catalogo.js, fontes, logotipo, sprite de ícones, miniaturas); no activate, apague caches com outro nome; no fetch: apenas GET do mesmo domínio; HTML em "rede primeiro, cache como reserva"; CSS, JS, fontes e imagens em "cache primeiro"; data/catalogo.js em "stale-while-revalidate"; NUNCA cachear nem interceptar outros domínios (os OAD e o GitHub); se offline e a página não estiver em cache, devolver index.html.
3. Em js/main.js, registre o service worker somente em http/https (não em file://), em try/catch: navigator.serviceWorker.register("sw.js").
4. Acrescente <link rel="manifest" href="manifest.webmanifest"> ao head, se ainda não estiver.
5. Documente em docs/guia-adicionar-oad.md e na seção 11.7: ao mudar qualquer arquivo da casca, incrementar VERSAO.

RESTRIÇÕES: sem notificações push, sem sincronização em segundo plano, sem coleta de dados; o cache nunca guarda requisições com query string de terceiros.

ENTREGA: manifest.webmanifest, sw.js, js/main.js atualizado.

VERIFICAÇÃO: no DevTools (Application) o manifesto não tem avisos e o service worker fica "activated"; ative "Offline" e recarregue: a casca e o catálogo aparecem, os botões "Abrir aula" levam ao navegador (sem cache); mude VERSAO, recarregue duas vezes e confirme que o cache antigo foi removido.
```

#### S5 · Arquivos de saída

| Arquivo | Origem |
|:---|:---|
| `docs/auditoria-a11y.md` e correções em HTML, CSS e JS | P5.1 |
| `scripts/checar-orcamento.mjs` e otimizações | P5.2 |
| `index.html` (metadados), `robots.txt`, `sitemap.xml`, `scripts/checar-ancoras.mjs` | P5.3 |
| `manifest.webmanifest`, `sw.js`, `js/main.js` | P5.4 |

#### S5 · Critérios de aceite

- [ ] Lighthouse mobile: **≥ 95 / 100 / 100 / 100** (Desempenho / Acessibilidade / Boas práticas / SEO); LCP ≤ 2,5 s; CLS ≤ 0,1.
- [ ] axe-core: **0** violações "serious" ou "critical" nas 3 páginas, 2 temas e 2 larguras.
- [ ] `node scripts/checar-orcamento.mjs` e `node scripts/checar-ancoras.mjs` com código 0.
- [ ] Teste humano com leitor de tela (NVDA no Windows ou TalkBack no Android) registrado em `docs/auditoria-a11y.md`.
- [ ] Compartilhamento mostra imagem e título corretos em ao menos 2 plataformas.
- [ ] Modo offline mostra a casca e o catálogo; nenhum domínio de terceiros no cache.

---

### Sprint 6: QA, CI e lançamento

**Objetivo.** Fechar a qualidade com **automação contínua**, executar o teste completo, **corrigir os repositórios satélites** (achados A3 a A6 e A11), publicar a versão 1.0.0 e divulgar.

**Esforço:** 2 dias · **Ferramentas sugeridas:** Claude (CI e textos), Copilot (revisão de pull requests e READMEs dos repositórios).

**Pré-requisitos:** Sprint 5 concluída; decisões **D1 a D8** da seção 12 respondidas (as que seguirem pendentes viram itens do backlog).

#### S6 · Tarefas

| ID | Tarefa | Quem | Saída |
|:--:|:---|:---:|:---|
| S6.1 | Fluxo de integração contínua | IA (P6.1) | `.github/workflows/qa.yml` |
| S6.2 | Teste completo e relatório | IA (P6.2) + autora | `docs/relatorio-qa.md` |
| S6.3 | Correção dos repositórios satélites (um pull request por repositório) | IA (P6.3) + autora | Textos "About", READMEs e licenças |
| S6.4 | Versão, divulgação e atualização do perfil | IA (P6.4) + autora | Tag `v1.0.0`, GitHub Release, textos de divulgação |
| S6.5 | Registro final e retrospectiva | Autora | `SPRINTS.md` |

#### S6 · Prompts

**P6.1 · Fluxo de integração contínua** (Claude Code)

```text
PAPEL: engenheira(o) de DevOps de projetos estáticos.

CONTEXTO: leia as seções 3 (ADR-06), 10.3 e 11.2 de docs/projeto-executivo.md.

TAREFA:
1. Crie .github/workflows/qa.yml EXATAMENTE como a seção 11.2 (mesmos gatilhos, passos e ordem). Se encontrar erro ou versão desatualizada de uma ação, aponte antes de alterar.
2. Crie .htmlvalidate.json com "extends": ["html-validate:recommended"] e ajuste somente regras que gerem falso positivo comprovado (comente o motivo de cada exceção).
3. Corrija o que o CI apontar na primeira execução local (rode cada comando do workflow na sua máquina na mesma ordem).

RESTRIÇÕES: o CI NÃO publica nada (apenas valida; o deploy é pelo branch main); permissões mínimas ("contents: read"); sem segredos; sem dependências no repositório (ferramentas via "npx --yes" ou "npm i --no-save").

ENTREGA: .github/workflows/qa.yml e .htmlvalidate.json.

VERIFICAÇÃO: valide a sintaxe com python3 -c "import yaml; yaml.safe_load(open('.github/workflows/qa.yml')); print('YAML ok')"; rode localmente cada passo; abra um pull request de teste e confirme que o job fica verde; quebre propositalmente um link e confirme que o job fica vermelho.
```

**P6.2 · Teste completo e relatório** (Claude Code + autora)

```text
PAPEL: analista de qualidade (QA) de software educacional.

CONTEXTO: leia as seções 10.1, 10.2, 10.4, 10.5 e o Anexo B de docs/projeto-executivo.md.

TAREFA:
1. Execute, nesta ordem, e cole a saída resumida de cada um: validar-catalogo, checar-contraste, testar-catalogo (jsdom), sincronizar --verificar, checar-ancoras, checar-orcamento, checar-links --externos, html-validate nos 3 HTML, axe (3 páginas x 2 temas x 2 larguras) e Lighthouse mobile.
2. Monte docs/relatorio-qa.md com: (a) tabela "critério | meta | medido | resultado" para TODOS os critérios da seção 10.5; (b) matriz de compatibilidade (Chrome, Edge, Firefox e Safari/iOS, últimas 2 versões, e WebView Android) com larguras 360, 390, 768, 1024 e 1440 px, deixando em branco o que exige dispositivo físico para a autora preencher; (c) roteiro manual de teclado e de leitor de tela da seção 10.4 com resultados; (d) lista de defeitos encontrados com severidade (bloqueante, alta, média, baixa) e responsável.
3. Corrija defeitos bloqueantes e altos; registre os demais em SPRINTS.md como backlog.

RESTRIÇÕES: não declarar "ok" sem evidência (comando, captura ou nota); não alterar metas para passar.

ENTREGA: docs/relatorio-qa.md e correções.

VERIFICAÇÃO: nenhum defeito bloqueante ou alto aberto; todos os critérios da seção 10.5 marcados "ok" ou justificados com decisão da autora.
```

**P6.3 · Correção dos repositórios satélites** (Copilot ou Claude; repetir para cada repositório)

```text
PAPEL: mantenedora(or) de repositórios abertos, com cuidado para não alterar o conteúdo pedagógico.

CONTEXTO: leia as seções 2.1 a 2.3 (achados A3 a A7, A11), 8.5 e 12 (decisão D6) de docs/projeto-executivo.md.

ENTRADA (a autora cola, um repositório por vez): nome do repositório e o conteúdo atual do README.md, da descrição do "About" e do arquivo LICENSE (ou "não existe").

TAREFA, para o repositório informado:
1. ENDEREÇOS: procure no README e devolva uma lista "linha | trecho atual | trecho corrigido" para estes problemas: (a) o endereço antigo "chemical-royale-edu"; (b) o endereço antigo "pre-enem-quimica-equilibrio"; (c) caminhos com acento (por exemplo "eletroquímica") em vez de "eletroquimica"; (d) links de "Estudo das Soluções" que apontem para pre-enem-quimica em vez de solucoes; (e) qualquer link que não esteja entre as URLs do catálogo (data/catalogo.js) ou que dê 404.
2. LIMPEZA: imagens de via.placeholder.com ou de outros hosts temporários; frases residuais de assistentes de IA (por exemplo, ofertas do tipo "se quiser, posso..."); badges de licença que contradizem o arquivo LICENSE.
3. ABOUT: se o repositório estiver na tabela da seção 8.5, entregue a descrição, o site e os tópicos exatamente como lá; senão, proponha texto no mesmo padrão (até 160 caracteres).
4. LICENÇA: se não houver LICENSE, NÃO escolha uma: escreva "pendente da decisão D6" e, se a autora informar a licença escolhida, entregue o arquivo e o badge coerentes.
5. PORTAL: acrescente ao topo do README uma linha "Faz parte do portal Bio+Tech EduDesign: https://bio-tech-edu.github.io/site/" (sem alterar o resto do cabeçalho).
6. Entregue o README corrigido completo, a mensagem do commit ("docs: ...") e o texto do pull request.

RESTRIÇÕES: não alterar conteúdo pedagógico, questões, créditos nem nomes de pessoas; não renomear repositórios (quebraria as URLs publicadas); mostrar a diferença antes do texto final.

ENTREGA: lista de correções, README corrigido, texto "About" e texto do pull request.

VERIFICAÇÃO: todos os links do README corrigido respondem 200 (rode a lista pelo scripts/checar-links.mjs ou manualmente); o README continua renderizando no GitHub sem imagens quebradas.
```

Tabela de repetição do P6.3 (um pull request por item):

| Repositório | Foco principal |
|:---|:---|
| `.github` (perfil da organização) | Listar os **10 OAD** (hoje 4) e o link do portal; conferir se os links de `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md` e `TEMPLATES/` do README funcionam (achados A6) |
| `chemical-royale`, `pre-enem-quimica`, `solucoes`, `cinetica`, `equilibrio`, `eletroquimica`, `enem` | Endereços antigos e links trocados (A3); linha de ligação ao portal |
| `termoquimica`, `solucoes`, `cinetica`, `equilibrio`, `eletroquimica`, `chemical-royale-v2` | Preencher "About": descrição, site e tópicos (A5) |
| `org` | Limpar README: imagens de `via.placeholder.com`, frase residual de IA e licença (A4) |
| `pre-enem-quimica`, `org`, `chemical-royale-v2` | Adicionar `LICENSE` conforme a decisão D6 (A11) |
| `eletroquimica` | Substituir badges, hero e avatar provisórios por arte definitiva (A7), quando a autora tiver a arte |

**P6.4 · Lançamento e divulgação** (Claude)

```text
PAPEL: redatora(o) de comunicação científica e educacional, em português do Brasil, com tom acolhedor e preciso.

CONTEXTO: leia as seções 1.1, 4.9, 5.4, 12 e o Anexo B de docs/projeto-executivo.md. O portal está publicado em https://bio-tech-edu.github.io/site/ e o relatório de QA (docs/relatorio-qa.md) está sem defeitos bloqueantes.

TAREFA:
1. Notas de versão da v1.0.0 (para o GitHub Release): o que há de novo (portal, catálogo com 10 OAD, trilha 17 a 28, tema claro e escuro, funciona offline), números do catálogo (10 OAD, 11 de 12 lições, 5 com simulador ou laboratório virtual, 7 de 10 com licença MIT), como contribuir e licenças. Sem exagero e sem promessa de resultado.
2. Três textos de divulgação, cada um com versão curta e longa: LinkedIn (profissional, 600 a 900 caracteres), Instagram (legenda leve, 3 a 5 hashtags, sugestão de imagem: og-image) e e-mail ou WhatsApp institucional (direto, com o link). Todos devem citar que os recursos são abertos, para a rede pública, e nunca prometer nota ou aprovação no ENEM.
3. Texto de 160 caracteres para a descrição do repositório `site` e tópicos sugeridos (portal, oad, rea, educacao-aberta, quimica, enem, github-pages, acessibilidade).
4. Atualização do README do perfil da organização (.github/profile/README.md): acrescentar o botão "Portal" e substituir a lista de 4 OAD pela lista dos 10 (com o status de cada um), mantendo a estrutura e o tom do texto atual (a autora cola o arquivo).

RESTRIÇÕES: não inventar depoimentos, métricas de uso nem parcerias; não incluir logotipos institucionais sem a decisão D4; não usar o nome de estudantes.

ENTREGA: notas de versão, os 3 textos (curto e longo), a descrição do repositório e o README do perfil atualizado.

VERIFICAÇÃO: todos os números citados conferem com data/catalogo.js (rode node scripts/validar-catalogo.mjs); todos os links respondem 200.
```

#### S6 · Arquivos de saída

| Arquivo | Origem |
|:---|:---|
| `.github/workflows/qa.yml`, `.htmlvalidate.json` | P6.1 |
| `docs/relatorio-qa.md` | P6.2 |
| READMEs, "About" e licenças corrigidos nos repositórios satélites (um PR por repositório) | P6.3 |
| Notas de versão, textos de divulgação, README do perfil, tag `v1.0.0` | P6.4 |

#### S6 · Critérios de aceite

- [ ] `qa.yml` verde em pull request e no agendamento semanal; falha quando um link é quebrado de propósito.
- [ ] `docs/relatorio-qa.md` com todos os critérios da seção 10.5 "ok" (ou justificados) e **0 defeitos bloqueantes ou altos**.
- [ ] Os achados **A3 a A6 e A11** estão resolvidos ou registrados como pendentes com responsável.
- [ ] Tag `v1.0.0` e GitHub Release publicados; perfil da organização aponta para o portal.
- [ ] `SPRINTS.md` com retrospectiva (o que funcionou, o que mudar, backlog).

---

## 10. Qualidade e critérios de aceite

### 10.1 Definição de pronto

Uma tarefa só está **pronta** quando todas as respostas abaixo são "sim":

1. O arquivo está no **caminho previsto** (seção 7) e **completo** (não é trecho).
2. O comando da linha `VERIFICAÇÃO` do prompt foi executado e o **resultado foi registrado** (cole a saída no pull request).
3. Não há **erro nem aviso no console** do navegador, nem **requisição externa** na aba Rede.
4. Funciona **só com teclado**, nos temas **claro e escuro**, em **360 px** e em **1440 px**.
5. Não usa `innerHTML`, `style=""`, `<script>` em linha nem recurso de terceiros.
6. `SPRINTS.md` foi atualizado (entrega, decisão, pendência).

Uma **sprint** está pronta quando todos os seus critérios de aceite estão marcados, o pull request foi aprovado (pela autora ou por revisão do Copilot) e a tag `v0.N.0` foi criada.

### 10.2 Matriz de testes

| Área | O que se testa | Como | Meta |
|:---|:---|:---|:---|
| Dados | Esquema e regras do catálogo | `validar-catalogo.mjs --estrito` | 0 erros |
| Lógica | Busca, filtros, ordenação e estado vazio | `testar-catalogo.mjs` (jsdom) | Todos os casos do P3.3 "ok" |
| Cor | Contraste dos papéis semânticos e botões | `checar-contraste.mjs` | 0 falhas obrigatórias |
| Acessibilidade automática | Violações WCAG | axe-core com Playwright (3 páginas, 2 temas, 2 larguras) | 0 "serious" ou "critical" |
| Acessibilidade manual | Teclado, leitor de tela, zoom, movimento | Roteiro 10.4 | Todos os passos "ok" |
| Desempenho | Notas e métricas | Lighthouse mobile; `checar-orcamento.mjs` | ≥ 95 / 100 / 100 / 100; LCP ≤ 2,5 s; CLS ≤ 0,1 |
| SEO e compartilhamento | Metadados, imagem, sitemap | Inspeção; depuradores de compartilhamento | Imagem e título corretos em 2 plataformas |
| HTML | Validade e boas práticas | `html-validate` | 0 erros |
| Links | Internos, âncoras e externos | `checar-links.mjs`, `checar-ancoras.mjs` | 0 quebrados |
| Sincronia | Blocos gerados a partir dos dados | `sincronizar.mjs --verificar` | Código 0 |
| Compatibilidade | Navegadores e larguras | Matriz da seção 6.8 | Sem defeito alto ou bloqueante |
| Privacidade | Cookies, requisições, armazenamento | Aba Rede, Application → Cookies e Local Storage | 0 externas, 0 cookies, só a chave `bte-tema` |
| Resiliência | Sem JavaScript, `file://`, armazenamento bloqueado, offline | Testes manuais | Catálogo acessível em todos os casos |

### 10.3 Scripts de verificação

| Script | Sprint | Comando | O que valida | No CI |
|:---|:---:|:---|:---|:---:|
| `validar-catalogo.mjs` | S0 (`--estrito` a partir da S3) | `node scripts/validar-catalogo.mjs --estrito` | 7 regras da seção 8.3; resumo de números | Sim |
| `checar-contraste.mjs` | S1 | `node scripts/checar-contraste.mjs` | Contraste WCAG dos tokens nos dois temas | Sim |
| `testar-catalogo.mjs` | S3 | `npm i --no-save jsdom && node scripts/testar-catalogo.mjs` | Busca, filtros, ordenação, estado vazio | Sim |
| `sincronizar.mjs` | S3 | `node scripts/sincronizar.mjs` (gera) · `--verificar` (confere) | `<noscript>`, números iniciais, JSON-LD, sitemap | Sim (`--verificar`) |
| `checar-links.mjs` | S3 | `--internos` (padrão) · `--externos` | Links e âncoras do HTML; URLs do catálogo | Sim (externos só no agendamento) |
| `checar-orcamento.mjs` | S5 | `node scripts/checar-orcamento.mjs` | Pesos de HTML, CSS, JS, fontes e imagens | Sim |
| `checar-ancoras.mjs` | S5 | `node scripts/checar-ancoras.mjs README.md docs/projeto-executivo.md` | Âncoras de HTML e de Markdown | Sim |
| `otimizar_imagens.py` | S0 | `python3 scripts/otimizar_imagens.py` | Gera logotipos, ícones e imagem de compartilhamento | Não |
| `capturar_miniaturas.py` | S3 | `python3 scripts/capturar_miniaturas.py [--somente id]` | Gera miniaturas das páginas publicadas (precisa de internet) | Não |
| `html-validate` | S6 | `npx --yes html-validate@11.16.2 index.html privacidade.html 404.html` | HTML válido e acessível (exige Node 22.22 ou superior) | Sim |

Implementações de **referência**, testadas na elaboração deste documento, estão nos anexos D (validador), E (contraste) e F (âncoras).

### 10.4 Roteiro manual de teclado e leitor de tela

Faça em uma janela nova, **sem usar o mouse** nos passos 1 a 9. Registre "ok" ou o defeito em `docs/relatorio-qa.md`.

**Teclado**

1. Ao carregar a página, a primeira tecla `Tab` foca "Pular para o conteúdo"; `Enter` leva ao conteúdo principal.
2. `Tab` percorre logotipo, itens do menu e alternador de tema, sempre com **anel de foco visível**.
3. Em 360 px, o botão "Menu" abre o painel, o foco fica preso nele e `Esc` fecha e devolve o foco ao botão.
4. O alternador de tema muda com `Enter` ou `Espaço`, o rótulo muda ("Ativar tema escuro" ↔ "Ativar tema claro") e a escolha persiste ao recarregar.
5. No catálogo: digitar "orgânica" mostra "Mostrando 2 de 10"; os chips mudam com `Espaço` ou `Enter`; "Limpar filtros" restaura os 10.
6. Em cada card: `Tab` alcança "Abrir aula" e "Código"; `Enter` abre em nova aba; o card "em construção" não tem link principal.
7. Na trilha: `Tab` percorre os 11 nós com link; `Enter` leva ao card correspondente e o foco vai para ele.
8. Rodapé: todos os links são alcançáveis.
9. Em nenhum momento o foco fica preso ou desaparece.

**Leitor de tela** (NVDA com Firefox ou Chrome no Windows; TalkBack com Chrome no Android)

10. Os marcos (cabeçalho, navegação, conteúdo principal e rodapé) são listados; a lista de títulos segue `h1 > h2 > h3` sem saltos.
11. Imagens informativas têm `alt` lido; ilustrações decorativas são ignoradas.
12. Chips são anunciados com "pressionado" ou "não pressionado"; ao filtrar, o novo contador é anunciado.
13. Cada link "Abrir aula" é único ("Abrir aula Termoquímica, abre em nova aba").
14. A tabela "Como contribuir" associa cabeçalhos às células.

**Outros**

15. Zoom de **200%** (só texto) e **400%** (página): sem perda de conteúdo e sem rolagem horizontal da página.
16. Com "reduzir movimento" ativado: nenhuma animação (hero estático, sem contagem de números, sem revelação).
17. Com JavaScript desativado: a lista dos 10 OAD aparece (`<noscript>`).
18. Abrindo `index.html` por duplo clique (`file://`): o catálogo funciona.
19. Em janela anônima com armazenamento bloqueado: sem erro e o tema segue o sistema.

### 10.5 Critérios de aceite do produto (versão 1.0.0)

| ID | Critério | Meta | Como medir |
|:--:|:---|:---|:---|
| **C01** | Catálogo com 10 cards, cada um com descrição curta abaixo | 10 de 10, descrição ≤ 140 caracteres | `validar-catalogo.mjs`, `testar-catalogo.mjs` |
| **C02** | Números do hero calculados dos dados | 10 OAD · 11 de 12 lições · 5 com simulador/lab · 7 de 10 com MIT | `stats.js`; alterar o dado e conferir |
| **C03** | Trilha das lições | 12 nós, 11 com link, lição 21 tracejada | Inspeção; teste do P4.1 |
| **C04** | Busca e filtros | Todos os casos de resultados esperados do P3.3 | `testar-catalogo.mjs` |
| **C05** | OAD em construção | `chemical-royale-v2` sem link, "Em breve" | Inspeção |
| **C06** | Versão sem JavaScript | Lista dos 10 OAD visível | Desativar JS |
| **C07** | Links | 0 quebrados (9 páginas publicadas e 10 repositórios) | `checar-links.mjs --externos` |
| **C08** | Textos da marca | Aprovados pela autora (D5) | Registro em `SPRINTS.md` |
| **D01** | Tema claro e escuro | Sem "flash", persiste, segue o sistema | Roteiro 10.4 (passo 4) |
| **D02** | Responsividade | Sem rolagem horizontal de 360 a 1440 px | Inspeção nas 5 larguras |
| **D03** | Contraste | 0 falhas obrigatórias | `checar-contraste.mjs` |
| **D04** | Movimento | Respeita `prefers-reduced-motion` | Roteiro 10.4 (passo 16) |
| **A01** | Acessibilidade automática | 0 violações "serious" ou "critical" | axe-core |
| **A02** | Teclado | Roteiro 10.4, passos 1 a 9 | Teste manual |
| **A03** | Leitor de tela | Roteiro 10.4, passos 10 a 14 | NVDA ou TalkBack |
| **A04** | Ampliação | Zoom 400% sem rolagem horizontal | Teste manual |
| **P01** | Lighthouse mobile | ≥ 95 / 100 / 100 / 100 | Lighthouse |
| **P02** | Métricas | LCP ≤ 2,5 s; CLS ≤ 0,1; INP ≤ 200 ms (no laboratório, TBT ≤ 200 ms como aproximação) | Lighthouse e DevTools |
| **P03** | Orçamento | 0 falhas; peso inicial ≤ 250 KB; JS ≤ 30 KB | `checar-orcamento.mjs` |
| **S01** | Terceiros | 0 requisições externas ao carregar a página | Aba Rede |
| **S02** | Cookies e armazenamento | 0 cookies; só a chave `bte-tema` | Application |
| **S03** | CSP | 0 violações no console | Console |
| **S04** | Sem `innerHTML` | `grep -R "innerHTML" js/` vazio | Linha de comando |
| **S05** | Privacidade | `privacidade.html` revisada pela autora | Registro em `SPRINTS.md` |
| **Q01** | HTML | 0 erros no `html-validate` | CI |
| **Q02** | Âncoras e links internos | 0 falhas | `checar-ancoras.mjs`, `checar-links.mjs` |
| **Q03** | Integração contínua | Verde em pull request e agendamento | Actions |
| **Q04** | Offline | Casca e catálogo disponíveis sem rede | DevTools |
| **Q05** | Compartilhamento | Imagem e título corretos em 2 plataformas | Depuradores |
| **Q06** | Licenças | `LICENSE`, `LICENSE-CONTEUDO.md`; decisões D2 e D6 registradas | Inspeção |
| **Q07** | Documentação | `README.md`, `docs/*`, `SPRINTS.md` completos; tag `v1.0.0` | Inspeção |

---

## 11. Deploy e operação

### 11.1 Publicação no GitHub Pages

1. Garanta que a `main` tem `index.html` e `.nojekyll` na raiz.
2. No repositório: *Settings → Pages → Build and deployment → Source: Deploy from a branch*; *Branch: `main`*, pasta `/(root)`; salvar.
3. Aguarde de 1 a 3 minutos (acompanhe em *Actions → pages build and deployment*). O endereço será `https://bio-tech-edu.github.io/site/`.
4. Marque *Enforce HTTPS*.
5. Em *About* do repositório, preencha descrição, site e tópicos (P6.4).

**Limites do GitHub Pages** (documentação oficial, conferida em 14/10/2026): site publicado de até 1 GB; limite flexível de 100 GB de tráfego por mês; limite flexível de 10 *builds* por hora; implantação que passe de 10 minutos falha. O portal pesa uma fração disso (menos de 5 MB com as miniaturas).

### 11.2 Fluxo de integração contínua (`.github/workflows/qa.yml`)

O CI **só valida** (ADR-06); o deploy continua sendo o do branch `main`. Roda em *push* na `main`, em *pull request*, **toda segunda-feira às 07:00 (horário de Mato Grosso)** e sob demanda. Os links externos só são testados no agendamento e no disparo manual, para que uma indisponibilidade de terceiros não bloqueie um pull request.

```yaml
name: QA

on:
  push:
    branches: [main]
  pull_request:
  schedule:
    - cron: '0 11 * * 1'   # segundas, 11:00 UTC = 07:00 em Mato Grosso (UTC-4)
  workflow_dispatch:

permissions:
  contents: read

concurrency:
  group: qa-${{ github.ref }}
  cancel-in-progress: true

jobs:
  qualidade:
    name: Validação do portal
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@v7

      - uses: actions/setup-node@v7
        with:
          node-version: 22   # o html-validate 11 exige Node 22.22 ou superior

      - name: Catálogo (esquema e regras, miniaturas obrigatórias)
        run: node scripts/validar-catalogo.mjs --estrito

      - name: Contraste dos tokens (claro e escuro)
        run: node scripts/checar-contraste.mjs

      - name: Arquivos gerados em sincronia com os dados
        run: node scripts/sincronizar.mjs --verificar

      - name: Busca e filtros do catálogo (jsdom)
        run: |
          npm i --no-save jsdom
          node scripts/testar-catalogo.mjs

      - name: Âncoras e links internos
        run: |
          node scripts/checar-ancoras.mjs README.md docs/projeto-executivo.md
          node scripts/checar-links.mjs --internos

      - name: Orçamento de desempenho
        run: node scripts/checar-orcamento.mjs

      - name: HTML válido
        run: npx --yes html-validate@11.16.2 index.html privacidade.html 404.html

      - name: Links externos (somente no agendamento semanal ou manual)
        if: github.event_name == 'schedule' || github.event_name == 'workflow_dispatch'
        run: node scripts/checar-links.mjs --externos
```

Observações: `actions/checkout` e `actions/setup-node` estavam na versão **v7** na data de elaboração (julho de 2026); confira se há versão mais nova ao criar o arquivo. O `html-validate` 11 exige Node 22.22 ou superior (por isso o `node-version: 22`); os scripts do projeto continuam compatíveis com Node 18 ou superior para uso local.

### 11.3 Fluxo de trabalho e reversão

| Situação | Como fazer |
|:---|:---|
| Mudança normal | Branch `sprint-N/tema` → pull request → CI verde → *merge* na `main` (publica sozinho em 1 a 3 min) |
| Proteção da `main` (recomendado) | *Settings → Branches → Add rule*: exigir pull request e a verificação "Validação do portal" |
| Versão | Tag `vX.Y.Z` e GitHub Release com notas |
| **Reverter uma publicação ruim** | `git revert <commit>` (ou o botão *Revert* do pull request) e *push*; o Pages republica a versão anterior em 1 a 3 min |
| Emergência no cache do navegador | Seção 11.7 (desativar o service worker) |

### 11.4 Como adicionar um OAD ao catálogo

1. **Publique o OAD** em repositório próprio da organização, com GitHub Pages ativo e `LICENSE`.
2. **Copie um bloco** de `data/catalogo.js`, ajuste todos os campos (seção 8.1) e escolha `ordem` única. A descrição curta tem **no máximo 140 caracteres** e termina com ponto.
3. **Gere a miniatura**: `python3 scripts/capturar_miniaturas.py --somente <id>` (ou coloque uma imagem manual e use `--pasta-manual`).
4. **Valide e sincronize**: `node scripts/validar-catalogo.mjs --estrito`, `node scripts/sincronizar.mjs`, `node scripts/testar-catalogo.mjs`.
5. **Pull request** com CI verde; ao fazer *merge*, incremente `VERSAO` em `sw.js` (seção 11.7).
6. **Depois da publicação**: preencha o "About" do novo repositório (seção 8.5) e atualize o README do perfil da organização.

Quando um OAD passa de "em construção" para "publicado": altere `status`, preencha `urlPages`, gere a miniatura e confirme na trilha (o nó tracejado vira link sozinho).

### 11.5 Rotina de manutenção

| Quando | O quê | Responsável |
|:---|:---|:---|
| Toda segunda (automático) | CI semanal com verificação dos links externos; falha gera e-mail do GitHub à autora | CI |
| Mensal | Conferir se as descrições e os números ainda refletem os repositórios; revisar *issues* | Autora |
| Trimestral | Atualizar ferramentas de teste (`jsdom`, `playwright`, `html-validate`), repetir Lighthouse e axe, revisar ADRs | Autora ou colaborador(a) |
| Semestral | Revisar textos da marca, `privacidade.html`, licenças e o backlog | Autora |
| A cada nova lição ou OAD | Seção 11.4 (catálogo, trilha e números se atualizam sozinhos) | Autora |

### 11.6 Domínio próprio ou mudança de endereço

O portal usa caminhos relativos (ADR-04), então **copiar os arquivos para outro endereço funciona sem alterar código**. Há poucos pontos com URL absoluta, todos listados aqui:

| Onde | O que ajustar |
|:---|:---|
| `404.html` | A linha `<base href="/site/">` (único trecho com caminho absoluto, exceção da ADR-04) |
| `index.html` (cabeçalho) | `canonical`, `og:url`, `og:image`, `twitter:image` |
| JSON-LD e `sitemap.xml` | `node scripts/sincronizar.mjs --base <novo endereço>` |
| `robots.txt` | Linha `Sitemap:` |
| `scripts/sincronizar.mjs` | Valor padrão de `--base` |

**Raiz da organização** (`https://bio-tech-edu.github.io/`): crie o repositório `bio-tech-edu.github.io`, copie os arquivos, ajuste a tabela acima (o `<base>` do 404 passa a `/`) e deixe `Bio-Tech-Edu/site` redirecionando ou arquivado. **Domínio próprio**: *Settings → Pages → Custom domain*, crie o registro DNS indicado pelo GitHub, mantenha *Enforce HTTPS* e acrescente o arquivo `CNAME` (o GitHub o cria ao salvar o domínio).

### 11.7 Cache e service worker

| Situação | Procedimento |
|:---|:---|
| Alterou qualquer arquivo da casca (HTML, CSS, JS, fontes, ícones, `data/catalogo.js`) | Incrementar a constante `VERSAO` em `sw.js` (`bte-v1` → `bte-v2`). Quem visitar o portal recebe a nova versão na visita seguinte |
| Alterou só texto de documentação (`docs/*`, `*.md`) | Não precisa |
| **Service worker com defeito** (emergência) | Substituir `sw.js` pelo código abaixo e publicar; ele se desregistra e recarrega as páginas abertas. Depois de 1 a 2 semanas, recoloque o `sw.js` normal |

```js
// sw.js de emergência: remove o service worker e limpa os caches do portal
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', (evento) => {
  evento.waitUntil((async () => {
    for (const nome of await caches.keys()) await caches.delete(nome);
    await self.registration.unregister();
    for (const janela of await self.clients.matchAll({ type: 'window' })) janela.navigate(janela.url);
  })());
});
```

---

## 12. Riscos e pendências

### 12.1 Decisões que dependem da autora

| ID | Decisão | Opções | Recomendação | Necessária na |
|:--:|:---|:---|:---|:---:|
| **D1** | Repositório e endereço do portal | `Bio-Tech-Edu/site` em `/site/` · repositório `bio-tech-edu.github.io` na raiz · domínio próprio | `site` em `/site/` agora (já existe e está vazio); migrar depois pela seção 11.6 | S0 |
| **D2** | Licenças do portal | MIT (código) + CC BY 4.0 (textos e imagens autorais) · outra combinação | MIT + CC BY 4.0, alinhadas à prática dos OAD e à ciência aberta | S0 |
| **D3** | E-mail público de contato e de privacidade | E-mail institucional · e-mail da marca · só GitHub | E-mail próprio da marca; verificar se o e-mail institucional do servidor público pode ser divulgado | S0 / S4 |
| **D4** | Uso dos logotipos da SEDUC e do Governo de MT | Usar com autorização · apenas texto "Apoio institucional" | Só texto até haver autorização formal | S4 |
| **D5** | Aprovação dos textos da marca e da biografia | Aprovar o banco da Sprint 2 · ajustar | A autora lê e ajusta antes da publicação | S2 |
| **D6** | Licença de `pre-enem-quimica`, `org` e `chemical-royale-v2` (hoje sem arquivo `LICENSE`) | MIT (como os outros sete) · outra | MIT, para o selo "licença aberta" valer nos 10 OAD | S4 / S6 |
| **D7** | Métricas de acesso | Nenhuma · solução sem cookies e sem dados pessoais, declarada em `privacidade.html` | Nenhuma na v1.0 (coerente com LGPD e simplicidade) | S5 |
| **D8** | Idiomas | Apenas português do Brasil · acrescentar inglês e espanhol | pt-BR na v1.0; EN e ES no backlog | S6 |

### 12.2 Riscos

| ID | Risco | Prob. | Impacto | Mitigação |
|:--:|:---|:---:|:---:|:---|
| R1 | Um OAD muda de endereço ou sai do ar e o card fica com link quebrado | Média | Alta | CI semanal com `checar-links --externos`; revisão mensal |
| R2 | Descrições do catálogo ficam desatualizadas em relação aos repositórios | Média | Média | Regra de 140 caracteres validada; revisão mensal (seção 11.5) |
| R3 | Miniatura capturada mostra tela de cadastro ou dado pessoal | Baixa | Alta | Revisão humana das 9 imagens (P3.1); imagem manual quando necessário |
| R4 | Uso indevido de marca institucional (SEDUC, Governo de MT) | Baixa | Alta | Decisão D4; apenas texto até autorização |
| R5 | Textos da marca publicados sem aprovação da autora | Média | Média | Decisão D5; revisão antes da Sprint 2 terminar |
| R6 | Cache do service worker serve versão antiga | Média | Média | Constante `VERSAO`; procedimento de emergência (11.7) |
| R7 | A CSP bloqueia um recurso por causa de estilo ou script em linha | Média | Baixa | Regra no prompt-mestre; `html-validate`; console sem violações (S03) |
| R8 | Mudança de endereço quebra URLs absolutas | Baixa | Média | Tabela da seção 11.6; `sincronizar.mjs --base` |
| R9 | Código gerado por IA diverge do projeto ou introduz falhas | Média | Média | Prompt-mestre, linha `VERIFICAÇÃO` em cada prompt, CI e revisão humana de cada pull request |
| R10 | Regressão de acessibilidade em edições futuras | Média | Alta | CI, critérios A01 a A04 e lista de verificação no modelo de pull request |
| R11 | Confusão de numeração das lições (Lição 20 em dois repositórios) | Média | Média | Regra da trilha (publicado tem preferência) e achado A2 documentado |
| R12 | Três OAD sem licença declarada geram dúvida de reuso | Existe hoje | Média | Decisão D6; catálogo mostra "licença a definir" até lá |
| R13 | O GitHub altera limites ou recursos do Pages | Baixa | Média | Portal pequeno e estático; migração simples (seção 11.6) |

### 12.3 Backlog pós-lançamento (v1.1 em diante)

| Ideia | Valor |
|:---|:---|
| Página-ficha por OAD (objetivos, habilidades da BNCC, tempo, pré-requisitos, créditos) | Ajuda professores a planejar |
| Incluir o planner `meu_dia_em_passos` como recurso complementar | Amplia o ecossistema além da Química |
| Versão em inglês e em espanhol (D8) | Alcance latino-americano, coerente com a visão da comunidade |
| Busca por habilidade da BNCC e por competência do ENEM | Descoberta pedagógica |
| Progresso local na trilha ("já visitei"), sem coleta, só no navegador | Engajamento sem dados pessoais |
| Selo de acessibilidade por OAD (auditoria periódica) | Transparência e melhoria contínua |
| Painel de saúde dos OAD (links, Lighthouse por OAD) no CI | Manutenção proativa |
| Seção de novidades e *changelog* público | Memória do projeto |
| Tema de alto contraste dedicado | Inclusão |

---

## 13. Anexos

### Anexo A: Glossário

| Termo | Significado |
|:---|:---|
| **ABP** | Aprendizagem Baseada em Problemas: a aula parte de uma situação-problema |
| **ADR** | *Architecture Decision Record*: registro curto de uma decisão de arquitetura |
| **BNCC** | Base Nacional Comum Curricular |
| **CLS / LCP / INP** | Métricas de experiência: deslocamento de layout, maior pintura de conteúdo e responsividade à interação |
| **CSP** | *Content Security Policy*: política que limita de onde a página pode carregar recursos e scripts |
| **ENEM** | Exame Nacional do Ensino Médio |
| **jsdom** | Simulador de navegador em Node.js, usado apenas em testes |
| **LGPD** | Lei Geral de Proteção de Dados (Lei 13.709/2018) |
| **OAD** | Objeto de Aprendizagem Digital |
| **OFL** | *SIL Open Font License*, licença das fontes Sora e Figtree |
| **PWA** | *Progressive Web App*: site instalável e com suporte a uso offline |
| **REA** | Recurso Educacional Aberto: material em domínio público ou com licença aberta |
| **Soft Tech / Clean Modernism** | Direção estética da marca: tecnologia humana, limpa e acolhedora |
| **TDIC** | Tecnologias Digitais da Informação e Comunicação |
| **WCAG** | *Web Content Accessibility Guidelines*; este projeto segue a versão 2.2, nível AA |
| **axe-core** | Biblioteca de testes automáticos de acessibilidade |

### Anexo B: Lista de conferência de lançamento (`docs/checklist-lancamento.md`)

**Antes (de 3 a 5 dias antes)**

- [ ] Decisões D1 a D8 respondidas ou registradas como pendentes no backlog.
- [ ] Textos da marca e da biografia aprovados pela autora (D5).
- [ ] 9 miniaturas revisadas (sem dados pessoais) e arte do card em construção conferida.
- [ ] `privacidade.html` revisada; e-mail de contato definido (D3); logotipos institucionais só com autorização (D4).
- [ ] `docs/relatorio-qa.md` sem defeitos bloqueantes ou altos; todos os critérios da seção 10.5 "ok".
- [ ] CI verde na `main`; tag `v0.6.0` (fim da Sprint 5) existe como ponto de retorno.

**No dia**

- [ ] *Merge* final na `main` e tag `v1.0.0` com GitHub Release (notas do P6.4).
- [ ] `https://bio-tech-edu.github.io/site/` abre com HTTPS; teste em um celular real com dados móveis.
- [ ] 404 testado em um caminho profundo (por exemplo `/site/x/y/z/`).
- [ ] Compartilhamento testado (WhatsApp, LinkedIn).
- [ ] "About" do repositório `site` preenchido; imagem de pré-visualização social enviada (*Settings → Social preview*).
- [ ] README do perfil da organização atualizado com os 10 OAD e o link do portal.
- [ ] "About" dos 6 repositórios sem descrição preenchidos (seção 8.5).
- [ ] READMEs corrigidos (endereços antigos, `org`, licenças pendentes) por pull request.
- [ ] Divulgação publicada (textos do P6.4).

**Depois (primeira semana)**

- [ ] Primeira execução semanal do CI conferida.
- [ ] *Issues* e comentários respondidos.
- [ ] Retrospectiva registrada em `SPRINTS.md` e backlog priorizado.

### Anexo C: Fontes e verificações

**Repositórios e páginas conferidos em 13/10/2026** (dados do catálogo):

| # | OAD | Repositório | Página publicada | Lição | Status |
|:--:|:---|:---|:---|:---|:---|
| 1 | Chemical Royale: A Arena dos Elementos | [`chemical-royale`](https://github.com/Bio-Tech-Edu/chemical-royale) | <https://bio-tech-edu.github.io/chemical-royale/> | Lições 17 a 19 | Publicado |
| 2 | ENEM Quest: Química | [`pre-enem-quimica`](https://github.com/Bio-Tech-Edu/pre-enem-quimica) | <https://bio-tech-edu.github.io/pre-enem-quimica/> | Lição 20 e Aulão | Publicado |
| 3 | Chemical Royale v2 | [`chemical-royale-v2`](https://github.com/Bio-Tech-Edu/chemical-royale-v2) | n/a (em construção) | Lições 20 e 21 | Em construção |
| 4 | Estudo das Soluções | [`solucoes`](https://github.com/Bio-Tech-Edu/solucoes) | <https://bio-tech-edu.github.io/solucoes/> | Lição 22 | Publicado |
| 5 | Termoquímica | [`termoquimica`](https://github.com/Bio-Tech-Edu/termoquimica) | <https://bio-tech-edu.github.io/termoquimica/> | Lição 23 | Publicado |
| 6 | Cinética Química | [`cinetica`](https://github.com/Bio-Tech-Edu/cinetica) | <https://bio-tech-edu.github.io/cinetica/> | Lição 24 | Publicado |
| 7 | Equilíbrio Químico | [`equilibrio`](https://github.com/Bio-Tech-Edu/equilibrio) | <https://bio-tech-edu.github.io/equilibrio/> | Lição 25 | Publicado |
| 8 | Eletroquímica | [`eletroquimica`](https://github.com/Bio-Tech-Edu/eletroquimica) | <https://bio-tech-edu.github.io/eletroquimica/> | Lição 26 | Publicado |
| 9 | Química Orgânica | [`org`](https://github.com/Bio-Tech-Edu/org) | <https://bio-tech-edu.github.io/org/> | Lições 27 e 28 | Publicado |
| 10 | Raio-X do ENEM | [`enem`](https://github.com/Bio-Tech-Edu/enem) | <https://bio-tech-edu.github.io/enem/> | Painel | Publicado |

Outros repositórios da organização: [`.github`](https://github.com/Bio-Tech-Edu/.github) (README do perfil e imagens da marca), [`site`](https://github.com/Bio-Tech-Edu/site) (repositório alvo, vazio em 13/10/2026) e [`meu_dia_em_passos`](https://github.com/Bio-Tech-Edu/meu_dia_em_passos) (planner).

**Materiais fornecidos pela autora:** `README.md` do perfil da organização (missão, visão, princípios, badges), `favicon.png` (600×600) e `hero.png` (1667×584).

**Referências técnicas e normativas**

| Tema | Fonte |
|:---|:---|
| Acessibilidade | [WCAG 2.2 (W3C)](https://www.w3.org/TR/WCAG22/) |
| Privacidade | [Lei 13.709/2018, LGPD](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) |
| Hospedagem | [Documentação do GitHub Pages](https://docs.github.com/pages) e [limites do Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) |
| Licença de conteúdo | [CC BY 4.0, resumo em português](https://creativecommons.org/licenses/by/4.0/deed.pt-br) |
| Métricas de desempenho | [Web Vitals (web.dev)](https://web.dev/articles/vitals) |
| Dados estruturados | [schema.org/LearningResource](https://schema.org/LearningResource) |
| Fontes | [Fontsource](https://fontsource.org/): pacotes `@fontsource/sora` e `@fontsource/figtree` 5.3.0, licença OFL-1.1 (arquivos e tamanhos conferidos) |
| Validação de HTML | [html-validate](https://html-validate.org/) |

**Verificações feitas na elaboração** (todas reproduzíveis com os scripts dos anexos D, E e F): catálogo com 0 erros; contraste de 49 pares nos dois temas (um par reprovou e foi corrigido); resultados de busca do P3.3; 5 arquivos de fonte com 63 KB no total; imagem de compartilhamento de ~90 KB; sintaxe do `qa.yml`; âncoras deste documento.

### Anexo D: Validador do catálogo (referência para o P0.2)

Salvar como `scripts/validar-catalogo.mjs`. Teste de referência: com o catálogo da seção 8.2 e **sem** miniaturas em disco, termina com código 0 e 10 avisos; com `--estrito`, termina com código 1 (miniaturas obrigatórias dos publicados); com uma descrição de 230 caracteres, termina com código 1.

```js
// Valida data/catalogo.js conforme a seção 8.3 do projeto executivo.
// Uso: node scripts/validar-catalogo.mjs [caminho] [--estrito]
//   --estrito: miniatura inexistente vira ERRO (padrão: AVISO). OAD "em-construcao" pode usar o fallback.
import vm from 'node:vm';
import fs from 'node:fs';
import path from 'node:path';

const args = process.argv.slice(2);
const estrito = args.includes('--estrito');
const arquivo = args.find((a) => !a.startsWith('--')) ?? 'data/catalogo.js';
const raiz = path.resolve(path.dirname(arquivo), '..');

const ctx = { window: {} };
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(arquivo, 'utf8'), ctx);
const { BTE_CATALOGO: C, BTE_META: M } = ctx.window;

const erros = [];
const avisos = [];
const cats = Object.keys(M.rotulos.categoria);
const fmts = Object.keys(M.rotulos.formato);
const sts = Object.keys(M.rotulos.status);
const acentos = ['navy', 'teal', 'orange'];
const recursos = ['simulador', 'laboratorio-virtual', 'fato-ou-fake', 'boss', 'badges', 'storytelling', 'painel', 'checklist', 'cornell-notes'];
const ids = new Set();
const ordens = new Set();
const cobertas = {};

for (const o of C) {
  const e = (m) => erros.push(`${o.id}: ${m}`);
  // 1. id
  if (!/^[a-z0-9-]+$/.test(o.id)) e('id fora do padrão (a-z, 0-9, hífen)');
  if (ids.has(o.id)) e('id duplicado');
  ids.add(o.id);
  if (!o.urlRepo.endsWith('/' + o.id)) e('urlRepo não termina com o id');
  // 2. textos
  if (o.titulo.length < 3 || o.titulo.length > 60) e('título fora de 3 a 60 caracteres');
  if (o.descricao.length > 140) e(`descricao com ${o.descricao.length} caracteres (máximo 140)`);
  if (!o.descricao.endsWith('.')) e('descricao deve terminar com ponto');
  if (o.tags.length < 1 || o.tags.length > 3) e('tags: de 1 a 3 itens');
  if (o.tags.some((t) => t.length > 24)) e('tag com mais de 24 caracteres');
  // 3. vocabulários
  if (!cats.includes(o.categoria)) e('categoria inválida');
  if (!fmts.includes(o.formato)) e('formato inválido');
  if (!sts.includes(o.status)) e('status inválido');
  if (!acentos.includes(o.acento)) e('acento inválido');
  if (o.recursos.some((r) => !recursos.includes(r))) e('recurso fora do vocabulário');
  // 4. status e URL
  if (o.status === 'publicado' && !(o.urlPages || '').startsWith(M.pagesBase)) e('publicado exige urlPages sob ' + M.pagesBase);
  if (o.status === 'em-construcao' && o.urlPages !== null) e('em-construcao exige urlPages null');
  // 5. lições e ordem
  if (o.licao.some((n) => !Number.isInteger(n) || n < 17 || n > 28)) e('licao deve ter inteiros de 17 a 28');
  if (ordens.has(o.ordem)) e('ordem duplicada');
  ordens.add(o.ordem);
  // 6. miniatura
  if (!o.miniaturaAlt) e('miniaturaAlt vazio');
  if (!fs.existsSync(path.join(raiz, o.miniatura))) {
    const msg = `miniatura ausente em disco: ${o.miniatura}`;
    if (estrito && o.status === 'publicado') e(msg); else avisos.push(`${o.id}: ${msg}`);
  }
  for (const n of o.licao) (cobertas[n] ||= []).push(o);
}

// 7. cobertura das lições 17 a 28
const soEmConstrucao = [];
let publicadas = 0;
for (let n = 17; n <= 28; n++) {
  if (!cobertas[n]) erros.push(`lição ${n} não é coberta por nenhum OAD`);
  else if (cobertas[n].some((o) => o.status === 'publicado')) publicadas++;
  else soEmConstrucao.push(n);
}

const comSimulador = C.filter((o) => o.recursos.some((r) => r === 'simulador' || r === 'laboratorio-virtual')).length;
console.log(`OAD: ${C.length} | lições publicadas: ${publicadas}/12 | só em construção: [${soEmConstrucao}] | OAD com simulador/lab: ${comSimulador}`);
console.log('maior descrição:', Math.max(...C.map((o) => o.descricao.length)), 'caracteres');
if (avisos.length) console.log('AVISOS:\n' + avisos.map((a) => '  ' + a).join('\n'));
console.log(erros.length ? 'ERROS:\n' + erros.map((x) => '  ' + x).join('\n') : 'Catálogo válido: 0 erros');
process.exit(erros.length ? 1 : 0);
```

### Anexo E: Verificador de contraste (referência para o P1.2)

Salvar como `scripts/checar-contraste.mjs`. Teste de referência: com o `css/tokens.css` da seção 4.3, imprime a tabela completa e termina com "Todos os pares obrigatórios passam" (código 0); o único par abaixo do mínimo é o decorativo laranja sobre branco.

```js
// Calcula o contraste WCAG 2.x dos pares de tokens de css/tokens.css (claro e escuro).
// Uso: node scripts/checar-contraste.mjs [caminho/tokens.css]   | saída 1 se algum par obrigatório reprovar
import fs from 'node:fs';
const css = fs.readFileSync(process.argv[2] ?? 'css/tokens.css', 'utf8');

// 1) lê declarações "--nome: valor;" de um trecho de CSS
const decl = (txt) => Object.fromEntries([...txt.matchAll(/--([\w-]+)\s*:\s*([^;]+);/g)].map(m => [m[1], m[2].trim()]));
const bloco = (ini) => { const i = css.indexOf(ini); if (i < 0) throw new Error('bloco não encontrado: ' + ini);
  let d = 0, j = css.indexOf('{', i); const ini2 = j; for (; j < css.length; j++) { if (css[j] === '{') d++; if (css[j] === '}' && --d === 0) break; }
  return css.slice(ini2 + 1, j); };
const base = decl(bloco(':root {'));
const escuroSel = decl(bloco(':root[data-theme="dark"]'));
const temas = { claro: base, escuro: { ...base, ...escuroSel } };

// 2) resolve var(--x) e converte #hex em [r,g,b]
const resolver = (t, v) => { let n = 0; while (/var\(--([\w-]+)\)/.test(v) && n++ < 8) v = v.replace(/var\(--([\w-]+)\)/g, (_, k) => t[k]); return v; };
const rgb = (hex) => { const h = hex.replace('#', ''); const f = h.length === 3 ? h.split('').map(c => c + c).join('') : h; return [0, 2, 4].map(i => parseInt(f.slice(i, i + 2), 16)); };
const lum = ([r, g, b]) => { const c = [r, g, b].map(v => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }); return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]; };
const razao = (a, b) => { const [x, y] = [lum(a), lum(b)].sort((p, q) => q - p); return (x + 0.05) / (y + 0.05); };

// 3) pares: [tema, texto, fundo, mínimo, descrição]  (4,5 = texto; 3 = ícone/borda/texto grande)
const T = (t) => (k) => rgb(resolver(temas[t], temas[t][k] ?? k));
const pares = [];
const add = (tema, fg, bg, min, nota = '') => pares.push({ tema, fg, bg, min, nota });
for (const t of ['claro', 'escuro']) {
  for (const fg of ['text', 'text-muted', 'heading', 'link', 'accent', 'accent-warm']) for (const bg of ['bg', 'surface', 'surface-alt']) add(t, fg, bg, 4.5, 'papel semântico');
  add(t, 'focus', 'bg', 3, 'anel de foco (UI)'); add(t, 'focus', 'surface', 3, 'anel de foco (UI)'); add(t, 'border', 'bg', 1, 'informativo');
}
add('claro', '#FFFFFF', 'navy-700', 4.5, 'botão primário'); add('claro', 'navy-900', 'teal-500', 4.5, 'botão turquesa');
add('escuro', 'navy-950', 'orange-500', 4.5, 'botão laranja (escuro)'); add('claro', '#FFFFFF', 'teal-700', 4.5, 'texto sobre turquesa escuro');
add('claro', 'teal-600', '#FFFFFF', 3, 'só ícones e bordas'); add('claro', 'orange-500', '#FFFFFF', 3, 'DECORATIVO: não usar como texto');

let falhas = 0;
console.log('tema   | par (texto / fundo)               | razão | mín. | resultado');
for (const p of pares) {
  const f = T(p.tema); const r = razao(f(p.fg), f(p.bg));
  const ok = r >= p.min; const decorativo = p.nota.startsWith('DECORATIVO') || p.nota === 'informativo';
  if (!ok && !decorativo) falhas++;
  console.log(`${p.tema.padEnd(6)} | ${(p.fg + ' / ' + p.bg).padEnd(33)} | ${r.toFixed(2).padStart(5)} | ${String(p.min).padStart(4)} | ${ok ? 'ok' : decorativo ? 'abaixo (esperado: ' + p.nota + ')' : 'FALHA'}`);
}
console.log(falhas ? `\n${falhas} par(es) obrigatório(s) reprovado(s)` : '\nTodos os pares obrigatórios passam');
process.exit(falhas ? 1 : 0);
```

### Anexo F: Âncoras de Markdown, algoritmo do GitHub (referência para o P5.3)

O GitHub gera o identificador de cada título assim: (1) converte para minúsculas; (2) remove marcas de formatação e pontuação, mantendo letras (inclusive acentuadas), números, hífens e sublinhados; (3) troca cada espaço por hífen; (4) se o identificador já existiu no documento, acrescenta `-1`, `-2` etc. Exemplo: "Sprint 3: Catálogo de OAD/REA" vira `sprint-3-catálogo-de-oadrea`. Títulos dentro de blocos de código não contam. A parte de HTML do `checar-ancoras.mjs` (todo `href="#x"` precisa de `id="x"`, sem ids duplicados) segue o mesmo espírito e fica a cargo do prompt P5.3.

```js
// Referência da parte Markdown de scripts/checar-ancoras.mjs: confere âncoras internas e links de arquivo,
// com o algoritmo de identificadores do GitHub (a parte HTML é descrita no P5.3).
// Uso: node scripts/checar-ancoras.mjs arquivo.md [outro.md ...]   (saída 1 se houver falha)
import fs from 'node:fs';
import path from 'node:path';

// Texto do título -> identificador (regras do GitHub: minúsculas, sem pontuação, espaços viram hífens)
export function slugGithub(titulo) {
  return titulo
    .replace(/!?\[([^\]]*)\]\([^)]*\)/g, '$1') // links e imagens: fica o texto
    .replace(/<[^>]+>/g, '')                    // HTML em linha
    .replace(/[`*~]/g, '')                      // código, negrito, tachado (o "_" é mantido)
    .trim()
    .toLowerCase()
    .replace(/[^\p{L}\p{N}\p{M}\s_-]/gu, '')    // remove pontuação e emojis, mantém letras acentuadas
    .replace(/\s/g, '-');                       // cada espaço vira hífen (hífens repetidos permanecem)
}

// Lista os identificadores de um Markdown, ignorando blocos de código e numerando duplicados (-1, -2...)
export function ancorasDe(md) {
  const vistos = new Map();
  const ids = new Set();
  let dentro = false;
  for (const linha of md.split('\n')) {
    if (/^\s*(```|~~~)/.test(linha)) { dentro = !dentro; continue; }
    if (dentro) continue;
    const m = linha.match(/^#{1,6}\s+(.+?)\s*#*\s*$/);
    if (!m) continue;
    const base = slugGithub(m[1]);
    const n = vistos.get(base) ?? 0;
    vistos.set(base, n + 1);
    ids.add(n === 0 ? base : `${base}-${n}`);
  }
  return ids;
}

if (process.argv[1] && import.meta.url === new URL(process.argv[1], 'file://').href) {
  let falhas = 0;
  for (const arq of process.argv.slice(2)) {
    const md = fs.readFileSync(arq, 'utf8');
    const ids = ancorasDe(md);
    const semCodigo = md.replace(/```[\s\S]*?```/g, '');
    let internos = 0, arquivos = 0;
    for (const m of semCodigo.matchAll(/\[[^\]]*\]\(([^)\s]+)\)/g)) {
      const alvo = m[1];
      if (alvo.startsWith('#')) {
        internos++;
        const id = decodeURIComponent(alvo.slice(1));
        if (!ids.has(id)) { falhas++; console.log(`${arq}: âncora sem título correspondente: ${alvo}`); }
      } else if (!/^[a-z]+:/i.test(alvo)) {
        arquivos++;
        const f = path.resolve(path.dirname(arq), decodeURIComponent(alvo.split('#')[0]));
        if (!fs.existsSync(f)) { falhas++; console.log(`${arq}: arquivo inexistente: ${alvo}`); }
      }
    }
    console.log(`${arq}: ${ids.size} títulos | ${internos} âncoras internas | ${arquivos} links de arquivo`);
  }
  console.log(falhas ? `${falhas} falha(s)` : 'Âncoras e links de arquivo ok');
  process.exit(falhas ? 1 : 0);
}
```

### Anexo G: Histórico de versões

| Versão | Data | Mudanças |
|:---|:---:|:---|
| **1.0** | 14/10/2026 | Primeira versão do projeto executivo: diagnóstico dos 10 repositórios, identidade visual, arquitetura, catálogo de dados, 7 sprints com 30 prompts, qualidade, deploy e riscos |

Notas de elaboração: o documento foi produzido com apoio do Claude (Anthropic) e conferido por scripts (anexos D, E e F) e por leitura dos repositórios e das páginas publicadas. Na verificação automática de contraste, `--teal-700` foi escurecido de `#0C7C79` para `#0A716E` (a versão original dava 4,38 sobre `--mist-100`). A **revisão humana** dos textos da marca (D5) e as decisões D1 a D8 continuam com a autora.
