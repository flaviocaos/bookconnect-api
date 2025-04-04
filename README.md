API REST desenvolvida em Flask para gerenciamento de usuários e livros compartilhados. Parte do MVP da disciplina de Desenvolvimento Full Stack da Pós-Graduação da PUC-Rio.

## 🎯 Objetivo

Facilitar o empréstimo e compartilhamento de livros entre usuários, promovendo acesso à leitura e otimização de recursos.

---

## ⚙️ Tecnologias

- Python 3.13
- Flask
- Flask-SQLAlchemy
- Flasgger (Swagger para documentação)
- SQLite

---

## 🚀 Como rodar localmente

### 1. Clone o repositório e navegue até a pasta:

```bash
cd bookconnect-api

2. Instale as dependências
pip install -r requirements.txt

3. Rode o app:
http://localhost:5000/apidocs

Documentação Swagger
http://localhost:5000/apidocs

Rotas disponíveis
POST /usuarios → Cadastrar novo usuário

POST /livros → Cadastrar novo livro

GET /livros → Listar todos os livros

DELETE /livro/<id> → Excluir livro por ID


