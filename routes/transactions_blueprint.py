from flask import Blueprint, jsonify
import json
from controllers import transactions_controller
transactions_bp = Blueprint('transactions', __name__)


@transactions_bp.get('/')
def get_transactions():
    transactions = transactions_controller.get_transactions()
    return jsonify(transactions)


@transactions_bp.get('/<int:id>')
def get_transaction_by_id(id: int):
    transaction = transactions_controller.get_transaction_by_id(id)
    return jsonify(transaction)
