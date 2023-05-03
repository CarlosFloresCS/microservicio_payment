from flask import Blueprint

bp = Blueprint('topRoutes', __name__)

@bp.route('/')
def index():
    return "hola mundo"
