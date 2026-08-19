from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
# Chave de segurança obrigatória para ativar o sistema de sessões/cookies do Flask
app.secret_key = 'uma_chave_secreta_e_segura_aqui'

# Usuário de teste fixo para simular um banco de dados
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "1234"

# Rota Inicial / Tela de Login
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Se o usuário já estiver logado, manda direto para o perfil
    if 'usuario' in session:
        return redirect(url_for('perfil'))

    if request.method == 'POST':
        usuario_inserido = request.form.get('username')
        senha_inserida = request.form.get('password')

        if usuario_inserido == USUARIO_CORRETO and senha_inserida == SENHA_CORRETA:
            session['usuario'] = usuario_inserido  # Salva o usuário na sessão
            return redirect(url_for('perfil'))
        else:
            flash('Usuário ou senha incorretos!', 'error')
            
    return render_template('login.html')

# Rota Protegida da Tela de Perfil
@app.route('/perfil')
def perfil():
    # Segurança: Verifica se o usuário tem permissão para acessar
    if 'usuario' not in session:
        flash('Por favor, faça login para acessar essa página.', 'error')
        return redirect(url_for('login'))
        
    return render_template('perfil.html', usuario=session['usuario'])

# Rota para fazer Logout e encerrar a sessão
@app.route('/logout')
def logout():
    session.pop('usuario', None)  # Remove o usuário da sessão
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
