# 📘 Atividade: Testes Automatizados para APIs FastAPI

## 🎯 Objetivo

Escreva testes automatizados para uma API feita com FastAPI usando `pytest` e `TestClient`. Você vai verificar respostas de sucesso, validar dados de entrada e confirmar o tratamento de recursos inexistentes.

## 📝 Tarefas

### 🛠️ Preparar o ambiente de testes

#### Descrição
Use o código inicial fornecido como a API que será testada. Configure as dependências e crie um cliente de teste para enviar requisições sem iniciar um servidor externo.

#### Requisitos
O programa concluído deve:

- Copiar `starter-code.py` para `main.py`.
- Instalar `fastapi`, `pytest` e `httpx` no ambiente Python.
- Criar `test_main.py` e configurar nele um `TestClient` para a aplicação.
- Executar os testes com o comando `pytest`.


### 🛠️ Testar respostas de sucesso

#### Descrição
Adicione testes para confirmar que os endpoints de saúde e de livros retornam os dados e os códigos HTTP esperados.

#### Requisitos
O programa concluído deve:

- Testar `GET /health` e verificar o status `200` e o JSON `{"status": "ok"}`.
- Testar `GET /livros` e verificar que a resposta inicial contém uma lista vazia.
- Testar `POST /livros` com título, autor e ano válidos, verificando o status `201` e o livro criado com identificador.
- Após criar um livro, testar `GET /livros/{livro_id}` e verificar os dados retornados.


### 🛠️ Testar validação e casos de erro

#### Descrição
Complete a suíte testando entradas inválidas e operações sobre livros que não existem. Garanta também que cada teste começa com o estado de dados limpo.

#### Requisitos
O programa concluído deve:

- Usar uma fixture do `pytest` para limpar os livros antes de cada teste.
- Verificar que um `POST /livros` sem um campo obrigatório retorna o status `422`.
- Verificar que `GET`, `PUT` e `DELETE` para um identificador inexistente retornam o status `404`.
- Testar `PUT /livros/{livro_id}` e `DELETE /livros/{livro_id}` com um livro existente e verificar que as alterações são refletidas nas respostas.
- Executar toda a suíte com `pytest` e confirmar que os testes passam.