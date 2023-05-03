from flask import Flask
from config import Config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate = Migrate(app,db,compare_type=True)

    from app.models.card import Card
    from app.models.user import User
    from app.models.transaction import Transaction

    with app.app_context():
        db.create_all()
    
    from app import topRoutes
    from app.controllers.payments_controller import payments_bp
    app.register_blueprint(topRoutes.bp)
    app.register_blueprint(payments_bp)
    return app
