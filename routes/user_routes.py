from flask import Blueprint, render_template, session, redirect, url_for
from models.usuario import Usuario

user_bp = Blueprint('user', __name__)

@user_bp.route('/perfil')
def perfil():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login'))

    usuario = Usuario.query.get(session['usuario_id'])
    return render_template('perfil.html', usuario=usuario)
