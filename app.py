from flask import Flask, request, jsonify
from models import db, Usuario, Livro
from flasgger import Swagger

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
swagger = Swagger(app)

# ✅ Criação do banco + usuário padrão para testes
with app.app_context():
    db.create_all()

    # Criar usuário padrão se não existir
    if not Usuario.query.first():
        usuario_padrao = Usuario(nome="Usuário Teste", email="teste@email.com")
        db.session.add(usuario_padrao)
        db.session.commit()

# 📌 ROTA: Cadastrar usuário
@app.route('/usuarios', methods=['POST'])
def cadastrar_usuario():
    """
    Cadastrar novo usuário
    ---
    parameters:
      - name: body
        in: body
        schema:
          properties:
            nome:
              type: string
            email:
              type: string
    responses:
      200:
        description: Usuário criado com sucesso
    """
    data = request.json
    usuario = Usuario(nome=data['nome'], email=data['email'])
    db.session.add(usuario)
    db.session.commit()
    return jsonify({"mensagem": "Usuário cadastrado com sucesso!"})

# 📌 ROTA: Listar livros (corrigida)
@app.route('/livros', methods=['GET'])
def listar_livros():
    """
    Listar livros disponíveis
    ---
    responses:
      200:
        description: Lista de livros
    """
    livros = Livro.query.all()
    resultado = []
    for livro in livros:
        resultado.append({
            "id": livro.id,
            "titulo": livro.titulo,
            "autor": livro.autor,
            "usuario": livro.usuario.nome if livro.usuario else "Desconhecido"
        })
    return jsonify(resultado)

# 📌 ROTA: Cadastrar livro
@app.route('/livros', methods=['POST'])
def cadastrar_livro():
    """
    Cadastrar novo livro
    ---
    parameters:
      - name: body
        in: body
        schema:
          properties:
            titulo:
              type: string
            autor:
              type: string
            usuario_id:
              type: integer
    responses:
      200:
        description: Livro cadastrado
    """
    data = request.json
    livro = Livro(titulo=data['titulo'], autor=data['autor'], usuario_id=data['usuario_id'])
    db.session.add(livro)
    db.session.commit()
    return jsonify({"mensagem": "Livro cadastrado com sucesso!"})

# 📌 ROTA: Deletar livro por ID
@app.route('/livro/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    """
    Deletar livro por ID
    ---
    parameters:
      - name: id
        in: path
        type: integer
    responses:
      200:
        description: Livro deletado
    """
    livro = Livro.query.get(id)
    if livro:
        db.session.delete(livro)
        db.session.commit()
        return jsonify({"mensagem": "Livro deletado!"})
    else:
        return jsonify({"mensagem": "Livro não encontrado."}), 404

if __name__ == '__main__':
    app.run(debug=True)
