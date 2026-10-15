# Guia para adicionar um OAD ao catálogo

## Passos para incluir um objeto no catálogo

1. Abra o arquivo `data/catalogo.js` e localize o array principal de objetos.
2. Crie ou edite um objeto com os campos exigidos: identificação, título, descrição curta, lição, tema, status, URL de acesso e URL do repositório.
3. Confirme se a estrutura do objeto está alinhada ao esquema do projeto e aos campos da validação automática.
4. Inclua a imagem da miniatura no diretório `assets/img/oad/` e ajuste o caminho relativo apropriado.
5. Salve o arquivo e rode a verificação do catálogo e os scripts de validação disponíveis no repositório.
6. Verifique a página do portal para confirmar que o card aparece corretamente, respeitando o layout, o status e os links.
7. Se houver qualquer conflito com o escopo do projeto, revise a decisão de arquitetura antes de publicar.

## Boas práticas

- Mantenha objetos em ordem lógica por lição ou tema.
- Não invente textos, URLs ou informações que não existam no repositório do OAD.
- Preserve caminhos relativos e o padrão de escrita em português do Brasil.
- Revise também a acessibilidade do card e a coerência do texto com o restante do portal.
