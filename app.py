from flask import Flask, render_template, session
from config import Config
from extensions import db

from routes.auth_routes import auth_bp
from routes.item_routes import item_bp
from routes.user_routes import user_bp

from models.usuario import Usuario
from models.item import Item

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(auth_bp)
app.register_blueprint(item_bp)
app.register_blueprint(user_bp)

@app.route('/')
def index():
    return render_template('index.html', title="Início")

@app.route('/teste')
def teste():
    return str(session)

if __name__ == '__main__':
    app.run(debug=True)
