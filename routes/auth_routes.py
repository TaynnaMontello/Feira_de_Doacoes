from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from models.usuario import Usuario

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        usuario = Usuario.query.filter_by(email=email, senha=senha).first()

        if usuario:
            session['usuario_id'] = usuario.id  
            session['usuario'] = usuario.nome      
            return redirect(url_for('user.perfil'))
        else:
            flash("Usuário ou senha incorretos.")

    return render_template('login.html')

@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        telefone = request.form['telefone']

        novo_usuario = Usuario(
            nome=nome,
            email=email,
            senha=senha,
            telefone=telefone
        )

        db.session.add(novo_usuario)
        db.session.commit()

        return redirect(url_for('auth.login'))

    return render_template('cadastro.html')


@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
