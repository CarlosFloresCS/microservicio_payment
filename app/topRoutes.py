from flask import Blueprint

bp = Blueprint('topROutes', __name__)

@bp.route('/')
def index():
    return "hola mundo"
