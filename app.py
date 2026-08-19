from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

app.secret_key = 'dengosa_pcd'

usuario_login = ""
usuario_senha = ""

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])

def login():
    if 'usuario' in session:
        return redirect(url_for('perfil'))

    if request.method == 'POST':
        usuario_inserido = request.form.get('username')
        senha_inserida = request.form.get('password')

        if usuario_inserido == usuario_login and senha_inserida == usuario_senha:
            session['usuario'] = usuario_inserido
            return redirect(url_for('perfil'))
        else:
            flash('Usuário ou senha incorretos!', 'error')

    return render_template('login.html')

@app.route('/perfil')

def perfil():
    if 'usuario' not in session:
        flash("Por favor faça login para ")
