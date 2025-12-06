from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from extensions import db
from models.item import Item
from models.usuario import Usuario

item_bp = Blueprint('item', __name__)

@item_bp.route('/itens')
def listar_itens():
    itens = Item.query.all()
    return render_template('itens.html', itens=itens, usuario=session.get('usuario_id'))

@item_bp.route('/novo_item', methods=['GET', 'POST'])
def novo_item():
    if "usuario_id" not in session:
        flash("Você precisa estar logado para cadastrar um item.")
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        nome = request.form['nome']
        desc = request.form['descricao']
        tipo = request.form['tipo']

        usuario = Usuario.query.get(session['usuario_id'])

        novo_item = Item(
            nome=nome,
            descricao=desc,
            tipo=tipo,
            dono=usuario     
        )

        db.session.add(novo_item)
        db.session.commit()

        return redirect(url_for('item.listar_itens'))

    return render_template('novo_item.html')

@item_bp.route('/editar_item/<int:id>', methods=['GET', 'POST'])
def editar_item(id):
    item = Item.query.get_or_404(id)

    if request.method == 'POST':
        item.nome = request.form['nome']
        item.descricao = request.form['descricao']
        item.tipo = request.form['tipo']
        db.session.commit()
        return redirect(url_for('item.listar_itens'))

    return render_template('editar_item.html', item=item)

@item_bp.route('/excluir_item/<int:id>')
def excluir_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('item.listar_itens'))

@item_bp.route('/trocar/<int:id>')
def trocar(id):
    item = Item.query.get_or_404(id)
    return render_template('trocar.html', item=item)

@item_bp.route('/doar/<int:id>')
def doar(id):
    item = Item.query.get_or_404(id)
    return render_template('doar.html', item=item)


@item_bp.route('/solicitar_doacao/<int:item_id>')
def solicitar_doacao(item_id):
    item = Item.query.get_or_404(item_id)
    dono = item.dono

    return render_template(
        'solicitar_doacao.html',
        item=item,
        dono=dono
    )

@item_bp.route('/solicitar_troca/<int:item_id>')
def solicitar_troca(item_id):
    item = Item.query.get_or_404(item_id)
    dono = item.dono

    return render_template(
        'solicitar_doacao.html',
        item=item,
        dono=dono
    )
