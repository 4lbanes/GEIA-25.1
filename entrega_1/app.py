from flask import Flask, render_template, request, redirect, url_for
from componentes.biblioteca import Biblioteca
from componentes.livro import Livro
from componentes.usuario import Usuario

app = Flask(__name__)
biblioteca = Biblioteca()  # Instância global da biblioteca

# Rotas para as funcionalidades principais
@app.route('/')
def index():
    """Rota para a página inicial."""
    return render_template('index.html', biblioteca=biblioteca)

@app.route('/livros')
def listar_livros():
    """Rota para listar todos os livros."""
    return render_template('livros.html', livros=biblioteca.livros)

@app.route('/usuarios')
def listar_usuarios():
    """Rota para listar todos os usuários."""
    return render_template('usuarios.html', usuarios=biblioteca.usuarios)

@app.route('/buscar_livro', methods=['GET'])
def buscar_livro():
    """Rota para buscar livros."""
    termo = request.args.get('termo', '')  # Obtém o termo da query string
    resultados = biblioteca.buscar_livro(termo)
    return render_template('livros.html', livros=resultados, termo=termo) # Passa o termo para o template

@app.route('/emprestar_livro', methods=['POST'])
def emprestar_livro():
    """Rota para emprestar um livro."""
    livro_titulo = request.form['livro_titulo']
    usuario_email = request.form['usuario_email']
    try:
        biblioteca.emprestar_livro(livro_titulo, usuario_email)
        return redirect(url_for('listar_livros'))  # Redireciona para a lista de livros
    except ValueError as e:
        return render_template('erro.html', mensagem=str(e)) # Renderiza template de erro

@app.route('/devolver_livro', methods=['POST'])
def devolver_livro():
    """Rota para devolver um livro."""
    livro_titulo = request.form['livro_titulo']
    usuario_email = request.form['usuario_email']
    try:
        biblioteca.devolver_livro(livro_titulo, usuario_email)
        return redirect(url_for('listar_livros'))
    except ValueError as e:
        return render_template('erro.html', mensagem=str(e))

# Rota para adicionar um novo livro
@app.route('/adicionar_livro', methods=['GET', 'POST'])
def adicionar_livro():
    """Rota para adicionar um novo livro."""
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        ano_publicacao = int(request.form['ano_publicacao'])
        try:
            novo_livro = Livro(titulo, autor, ano_publicacao)
            biblioteca.adicionar_livro(novo_livro)
            return redirect(url_for('listar_livros'))
        except ValueError as e:
             return render_template('erro.html', mensagem=str(e))
    return render_template('adicionar_livro.html')  # Formulário para adicionar o livro

# Rota para adicionar um novo usuario
@app.route('/adicionar_usuario', methods=['GET', 'POST'])
def adicionar_usuario():
    """Rota para adicionar um novo usuario."""
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        try:
            novo_usuario = Usuario(nome, email)
            biblioteca.adicionar_usuario(novo_usuario)
            return redirect(url_for('listar_usuarios'))
        except ValueError as e:
            return render_template('erro.html', mensagem=str(e))
    return render_template('adicionar_usuario.html')  # Formulário para adicionar usuario

@app.route('/relatorio_emprestimos')
def relatorio_emprestimos():
    """Rota para exibir o relatório de empréstimos."""
    relatorio = biblioteca.relatorio_livros_emprestados()
    return render_template('relatorio_emprestimos.html', relatorio=relatorio)

if __name__ == '__main__':
    # Adicionando livros e usuários iniciais para teste
    livro1 = Livro("Dom Quixote", "Miguel de Cervantes", 1605)
    livro2 = Livro("1984", "George Orwell", 1949)
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    usuario1 = Usuario("Alice", "alice@email.com")
    usuario2 = Usuario("Bob", "bob@email.com")
    biblioteca.adicionar_usuario(usuario1)
    biblioteca.adicionar_usuario(usuario2)
    app.run(debug=True)