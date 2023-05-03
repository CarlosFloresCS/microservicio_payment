from flask import Flask
from config import Config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from app.topRoutes import bp

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)

    from app.models.card import Card
    from app.models.user import User
    from app.models.transaction import Transaction

    with app.app_context():
        db.create_all()
    
    from app import topRoutes
    app.register_blueprint(topRoutes.bp)
    return app
