## 📌 Descrição do Projeto
O Sistema de Doações e Trocas é uma aplicação web desenvolvida com Flask que permite que usuários cadastrem itens
para doação ou troca, visualizem itens disponíveis, solicitem um item, além de manter um perfil simples de usuário.

## O sistema possui:
> 🧍 Cadastro e login de usuários (com senha criptografada)
> 📦 Cadastro de itens (troca ou doação)
> 🔄 Solicitação de troca
> 🎁 Solicitação de doação
> ✏️ Edição e exclusão dos próprios itens
> 👀 Visualização dos itens de outras pessoas
> 🧩 Controle de login com sessão
> 🗄 Integração completa com SQLite + SQLAlchemy

_(O objetivo principal é facilitar a organização de uma feira onde pessoas possam doar ou trocar objetos que não usam mais.)_

## 🛠 Tecnologias utilizadas
- Python 3
-  Flask
- Flask-SQLAlchemy
- Werkzeug (hash de senha)
- HTML + Jinja2
- CSS
- SQLite

## 🚀 Como rodar o projeto
1. Clonar o repositório
  git clone https://github.com/TaynnaMontello/Feira_de_Doacoes.git
  cd Feira_de_Doacoes

2. Criar um ambiente virtual (opcional, mas recomendado)
  python -m venv ambiente
  source ambiente/bin/activate  # Linux/Mac
  ambiente\Scripts\activate     # Windows

3. Instalar as dependências
   pip freeze > requirements.txt  # caso não tenha a pasta (que é o meu caso)
   pip install -r requirements.txt 

4. Configurar o banco de dados
  **O SQLite será criado automaticamente na primeira execução.**

Se quiser criar manualmente: (python)
  >>> from app import db
  >>> db.create_all()
  >>> exit()

5. Rodar a aplicação
  python app.py

_outras opções:_
  👉 http://127.0.0.1:5000
  👉 ou http://localhost:5000

## 📚 Estrutura do Projeto
/projeto_feira_de_doações
│── app.py
│── config.py
│── extensions.py
│── /models
|     ├── _init_.py
│     ├── usuario.py
│     └── item.py
│── /routes
|     ├── _init_.py
│     ├── auth_routes.py
│     ├── item_routes.py
│     └── user_routes.py
│── /templates
│── /static
│── readme.md
|── reflexão.md

## 👤 Funcionalidades de Usuário
🔐 Cadastro e Login
Criação de conta com nome, email, senha e telefone.

(Senha armazenada com hash.)

🧺 Itens
Cadastrar item com nome, descrição e tipo (troca ou doação).
Listar itens disponíveis.
Excluir e editar apenas seus próprios itens.
Solicitar troca/doação de itens de outros usuários.

👤 Perfil
Mostra o nome do usuário logado.

⭐ Objetivo Educacional
Este projeto foi desenvolvido como atividade para a disciplina de Programação de Sistemas para Internet (PSI), visando:

1. Aprender Flask
2. Entender sessões e autenticação
3. Usar banco de dados com SQLAlchemy
4. Trabalhar rotas e templates
5. Criar um CRUD simples

