# Decisões de arquitetura (ADR)

Tabela com ADR-01 a ADR-09 (copiado da seção 3 do projeto executivo).

| ID | Decisão | Motivo | Consequência | Status | Data |
|:---:|:---|:---|:---|:---|:---|
| ADR-01 | Repositório alvo `Bio-Tech-Edu/site`, publicado em `/site/` | Já existe, com a descrição "Portal dedicado a apresentar os OAD"; não depende de renomear nada | Para usar a raiz`bio[...]` | Proposta | |
| ADR-02 | JavaScript clássico (sem ES modules), dados como variável global | Mesmo padrão dos OAD existentes: abre por duplo clique em `file://` sem erro de CORS | Sem `import`/`export`; um ob[...] | Proposta | |
| ADR-03 | Catálogo orientado a dados em `data/catalogo.js` | Adicionar um OAD = adicionar 1 objeto, sem tocar em HTML | Validação automática do esquema no CI | Proposta | |
| ADR-04 | Caminhos 100% relativos | Funciona em `/site/`, na raiz da organização ou em domínio próprio | Proibido `href="/..."` | Proposta | |
| ADR-05 | Zero CDN e zero terceiros; fontes e ícones **auto-hospedados** | LGPD (sem vazar IP de estudantes), funciona offline, desempenho previsível | Fontes `.woff2` e ícones SVG ficam no re[...] | Proposta | |
| ADR-06 | Deploy por branch `main` na raiz (+ `.nojekyll`); Actions só para QA | Igual ao fluxo dos outros repositórios; menos peças para quebrar | O CI não publica, apenas valida | Proposta | |
| ADR-07 | Miniaturas **copiadas e otimizadas** (WebP) para `assets/img/oad/` | Link direto para imagem de outro repositório quebra se ele mudar | Script de otimização documentado na Sprint 3 | Proposta | |
| ADR-08 | Tema claro e escuro por tokens CSS; segue o sistema e tem alternador | Acessibilidade e conforto em sala escura ou projetor | Dois conjuntos de tokens validados para contraste | Proposta | |
| ADR-09 | Licenças: MIT (código) e CC BY 4.0 (textos e imagens autorais) | 7 dos 10 OAD já usam MIT (os outros 3 estão sem licença, achado A11); REA pede licença aberta explícita para cont[...] | Proposta | |
