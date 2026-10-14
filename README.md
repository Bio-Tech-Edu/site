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

## Contato

A confirmar (decisão D3). Enquanto isso, use o perfil da organização:
<https://github.com/Bio-Tech-Edu>.

## Acompanhamento

O histórico de sprints e o backlog ficam em [`SPRINTS.md`](SPRINTS.md).
