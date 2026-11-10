# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Construa uma API REST com FastAPI para praticar rotas HTTP, validação de dados com modelos Pydantic e operações CRUD. Ao final, você poderá testar os endpoints pela documentação interativa gerada pelo framework.

## 📝 Tarefas

### 🛠️ Criar e executar a API

#### Descrição
Configure uma aplicação FastAPI e execute-a localmente para disponibilizar os primeiros endpoints.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI em `main.py`.
- Implementar uma rota `GET /` que retorne uma mensagem em JSON.
- Implementar uma rota `GET /health` que indique que a API está funcionando.
- Iniciar a aplicação com Uvicorn e permitir o acesso à documentação interativa em `/docs`.


### 🛠️ Criar endpoints para consultar e cadastrar livros

#### Descrição
Modele um recurso de livros e implemente endpoints para listar os livros cadastrados, consultar um livro por identificador e cadastrar novos livros. Para esta atividade, os dados podem ficar em uma lista em memória.

#### Requisitos
O programa concluído deve:

- Definir modelos Pydantic para validar os dados de entrada e representar um livro.
- Implementar `GET /livros` para retornar a lista de livros.
- Implementar `GET /livros/{livro_id}` para retornar um livro específico ou o status HTTP `404` quando ele não existir.
- Implementar `POST /livros` para cadastrar um livro e retornar o registro criado com status HTTP `201`.


### 🛠️ Atualizar e remover livros

#### Descrição
Complete as operações CRUD da API adicionando endpoints para atualizar e remover livros. Garanta que as respostas indiquem claramente quando o identificador solicitado não corresponde a um livro cadastrado.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /livros/{livro_id}` para atualizar os dados de um livro existente.
- Implementar `DELETE /livros/{livro_id}` para remover um livro existente.
- Retornar status HTTP `404` ao tentar atualizar ou remover um livro inexistente.
- Testar os endpoints de criação, consulta, atualização e remoção pela documentação em `/docs`.