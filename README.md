# Portal Bio+Tech EduDesign

Site estático de apresentação da marca **Bio+Tech EduDesign** e catálogo de
Objetos de Aprendizagem Digitais (OAD) e Recursos Educacionais Abertos (REA).

- **Stack:** HTML5, CSS3 e JavaScript puro (sem build, sem framework, sem CDN).
- **Hospedagem:** GitHub Pages (branch `main`, pasta raiz).
- **Endereço previsto:** a confirmar (decisão D1).
- **Documento-mestre:** [`docs/projeto-executivo.md`](docs/projeto-executivo.md).

> Estado atual: **Sprint 0** (fundação). A página inicial é provisória.

## Como abrir localmente

Requer Python 3. Na raiz do repositório:

```bash
python3 -m http.server 8000
```

Abra <http://localhost:8000/> no navegador.

## Como publicar no GitHub Pages

1. Garanta que a branch `main` tem `index.html` e `.nojekyll` na raiz.
2. No repositório: **Settings → Pages → Build and deployment → Deploy from a branch**.
3. Escolha a branch `main` e a pasta `/(root)`, e salve.
4. Aguarde de 1 a 3 minutos e abra o endereço publicado (a confirmar, decisão D1).
5. Marque **Enforce HTTPS**.

## Licenças

| O que | Licença | Arquivo |
|:---|:---|:---|
| Código | MIT (a confirmar, decisão D2) | [`LICENSE`](LICENSE) |
| Textos e imagens autorais | CC BY 4.0 (a confirmar, decisão D2) | [`LICENSE-CONTEUDO.md`](LICENSE-CONTEUDO.md) |

Logotipos de terceiros e a marca Bio+Tech EduDesign não estão cobertos pelas licenças acima.

## Como adicionar um OAD

O catálogo é orientado a dados: incluir um OAD é incluir **um objeto** em
[`data/catalogo.js`](data/catalogo.js), sem tocar em HTML.

1. **Publique o OAD** em repositório próprio da organização, com GitHub Pages ativo e arquivo `LICENSE`.
2. **Copie um bloco** de `data/catalogo.js` e ajuste todos os campos (seção 8.1 do projeto executivo). Escolha uma `ordem` única; a `descricao` curta tem **no máximo 140 caracteres** e termina com ponto.
3. **Gere a miniatura** (640×400, WebP): `python3 scripts/capturar_miniaturas.py --somente <id>` (disponível a partir da Sprint 3).
4. **Valide**: `node scripts/validar-catalogo.mjs` (a partir da Sprint 3, use `--estrito`, que exige as miniaturas dos OAD publicados). Depois, quando existirem (Sprint 3), rode `node scripts/sincronizar.mjs` e `node scripts/testar-catalogo.mjs`.
5. **Abra um pull request** e, após o *merge*, incremente `VERSAO` em `sw.js` (a partir da Sprint 5).
6. **Depois de publicar**: preencha o "About" do novo repositório e atualize o README do perfil da organização.

Quando um OAD passa de "em construção" para "publicado", altere `status`, preencha `urlPages` e gere a miniatura.
Detalhes: seção 11.4 de [`docs/projeto-executivo.md`](docs/projeto-executivo.md).

## Contato

A confirmar (decisão D3). Enquanto isso, use o perfil da organização:
<https://github.com/Bio-Tech-Edu>.

## Acompanhamento

O histórico de sprints e o backlog ficam em [`SPRINTS.md`](SPRINTS.md).
