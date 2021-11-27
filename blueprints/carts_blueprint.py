from flask import Blueprint, jsonify, request
from context.db_context import DbContext
from services.cart_service import CartService
from models.cart_model import CartModel


carts_bp = Blueprint('carts', __name__)
context = DbContext()
cart_service = CartService(context)


# GET /carts/
@carts_bp.get('/')
def get_carts():
    carts = cart_service.ger_all()
    if carts:
        return jsonify(carts), 200
    else:
        return 'No data', 204


# GET /carts/<id>
@carts_bp.get('/<int:id>')
def get_cart_by_id(id: int):
    cart = cart_service.get_by_id(id)
    if cart:
        return jsonify(cart), 200
    else:
        return f'Cart with id={id} Not Found :(', 404


# GET /carts/<key>=<value>
@carts_bp.get('/<string:key>=<value>')
def get_cart_by_name(key: str, value):
    cart = cart_service.get_by_name_value(key, value)
    if cart:
        return jsonify(cart), 200
    else:
        return f'Cart with key={key} with value={value} Not Found :(', 404


# POST /carts/
@carts_bp.post('/')
def add_cart():
    data = request.get_json(False)
    try:
        new_cart = CartModel(data['id'], data['data'])
        cart = cart_service.create(new_cart)
        if cart:
            return jsonify(cart), 201
        else:
            return f'Cart with data={data} Bad Request :(', 400
    except KeyError as err:
        print(f'ERROR: {err}')
        return f'Cart with data={data} Bad Request :(', 400


# PUT /carts/<id>
@carts_bp.put('/<int:id>')
def update_cart_by_id(id: int):
    data = request.get_json(False)
    try:
        updated_cart = CartModel(id, data)
        cart = cart_service.update(updated_cart)
        if cart:
            return jsonify(cart), 201
        else:
            return f'Cart with data={data} and id={id} Bad Request :(', 400
    except KeyError as err:
        print(f'ERROR: {err}')
        return f'Cart with data={data} and id={id} Bad Request :(', 400


# DELETE /carts/<id>
@carts_bp.delete('/<int:id>')
def delete_cart_by_id(id):
    cart = cart_service.delete(id)
    if cart:
        return jsonify(cart), 200
    else:
        return f'Cart with id={id} Not Found :(', 404
