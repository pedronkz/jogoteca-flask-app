from flask import Flask, render_template, request, redirect, session, flash, url_for

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario("Pedro Ferreira", "PF", "teste01")
usuario2 = Usuario("Felipe Chagas", "BADCHAGAS", "fisica")
usuario3 = Usuario("Domenico Iuliano", "GOAT", "bode")

usuarios = { usuario1.nickname : usuario1, 
             usuario2.nickname : usuario2,
             usuario3.nickname : usuario3 }

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Hack n Slash', 'PS2')
jogo3 = Jogo('Skyrim', 'RPG', 'PC')
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.secret_key = 'projetojogoteca'

@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('index')))
    return render_template('lista.html', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    novo_jogo = Jogo(nome, categoria, console)
    lista.append(novo_jogo)
    return redirect(url_for('index'))


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastrar', methods=['POST',])
def cadastrar():
    nome = request.form['nome']
    nickname = request.form['nickname']
    senha = request.form['senha']


    if nickname in usuarios:
        flash('Usuário já existente!')
        return redirect(url_for('cadastro'))
    else:

        novo_usuario = Usuario(nome, nickname, senha)
        usuarios[nickname] = novo_usuario
        flash('Usuário cadastrado com sucesso!')
        return redirect(url_for('login'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form.get('proxima')
            return redirect(proxima_pagina if proxima_pagina and proxima_pagina != 'None' else url_for('index'))
        else:
            flash('Usuário não logado.')
            return redirect(url_for('login'))
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)