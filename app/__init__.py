from flask import Flask

def create_app():
    print("🔥 CREATE_APP CHAMADO 🔥")

    app = Flask(__name__)
    app.config.from_object('config.Config')

    from app.routes import main
    app.register_blueprint(main)

    return app