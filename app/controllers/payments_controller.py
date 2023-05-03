from flask import Blueprint,request,jsonify
from app.models.transaction import Transaction,TransactionState
from app import db

import json

payments_bp = Blueprint('payments',__name__)

@payments_bp.route('/payments')
def get_payments():
    payments = Transaction.query.all()
    payments_dict = [ payment.as_dict() for payment in payments]
    print(payments_dict)
    return json.dumps(payments_dict)

@payments_bp.route('/payments/create', methods=['POST'])
def create_payments():
    data = request.json
    # Validando datos
    if not data:
        return jsonify({'message':'No se recibieron datos para crear el pago'}),400
    
    # Obtener los datos del JSON
    user_id = data.get('user_id')
    card_id = data.get('card_id')
    date_hour = data.get('date_hour')
    mount =  data.get('mount')
    state = data.get('state')

    # Validando datos 
    if not user_id or not card_id or not date_hour or not mount or not state:
        return jsonify({'message':'Los datos del pago estan incompletos'}),400

    # Creando nueva transaccion
    payment = Transaction(user_id=user_id,card_id=card_id,date_hour=date_hour,mount=mount,state=state)
    db.session.add(payment)
    db.session.commit()

    # Retornar el pago creado como respuesta
    return jsonify(payment.as_dict()),201

@payments_bp.route('/payments/<int:id>',methods=['GET'])
def get_payment(id):
    transaction = Transaction.query.get(id)
    if transaction is None:
        return jsonify({'error':'Transaccion no encontrada'}),404
    return jsonify(transaction.as_dict())

@payments_bp.route('/payments/<int:id>/refund',methods=['PUT'])
def refund_payment(id):
    transaction = Transaction.query.get(id)
    if not transaction:
        return jsonify({'message':'Transaccion no encontrada'}),404
    if transaction.state == TransactionState.REFUNDED:
        return jsonify({'message':'Transaccion ya reembolzada'}),400

    transaction.state = TransactionState.REFUNDED
    db.session.commit()

    return jsonify(transaction.as_dict())   