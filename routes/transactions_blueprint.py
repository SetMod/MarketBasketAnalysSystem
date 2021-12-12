from flask import Blueprint, jsonify, send_file, request
import json
from controllers import transactions_controller
transactions_bp = Blueprint('transactions', __name__)


@transactions_bp.get('/')
def get_transactions_list():
    transactions = transactions_controller.get_transactions_list()
    return jsonify(transactions)


# @transactions_bp.get('/pagination?pageSize=<int:pageSize>&pageNumber=<int:pageNumber>')
@transactions_bp.get('/pagination')
def get_paginated_transactions():
    pageSize = request.args.get('pageSize')
    pageNumber = request.args.get('pageNumber')
    transactions = transactions_controller.get_paginated_transactions(
        pageSize, pageNumber)
    return jsonify(transactions)


@transactions_bp.get('/<int:id>')
def get_transaction_by_id(id: int):
    transaction = transactions_controller.get_transaction_by_id(id)
    return jsonify(transaction)


# @transactions_bp.get('/images?name=<image_name>&create=<create>')
# def create_transactions_by_month_image(image_name: str, create):
#     transaction = transactions_controller.create_transactions_by_month_image(
#         image_name, create)
#     return send_file(transaction)


@transactions_bp.get('/images/<image_name>')
def get_transactions_by_month_image(image_name: str):
    transaction = transactions_controller.get_transactions_by_month_image(
        image_name)
    return send_file(transaction, mimetype='image/png'), 200
