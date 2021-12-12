from os import path
from models.transaction import Transaction


def get_transactions_list():
    transactions = Transaction.get_transactions_list()
    try:
        if transactions:
            return transactions
        else:
            return 'No transactions'
    except AttributeError as err:
        print(err)
        return 'Error reading file'


def get_paginated_transactions(pageSize: int, pageNumber: int):
    try:
        pageSize = int(pageSize) if pageSize else 10
        pageNumber = int(pageNumber) if pageNumber else 1
        transactions = Transaction.get_paginated_transactions(
            pageSize, pageNumber)
        if transactions:
            return transactions
        else:
            return 'No transactions'
    except AttributeError as err:
        print(err)
        return 'Error reading file'


def get_transaction_by_id(id: int):
    transactions = Transaction.get_transaction_by_id(id)
    try:
        if transactions:
            return transactions
        else:
            return f'No transaction with id={id}'
    except AttributeError as err:
        print(err)
        return 'Error reading file'


def create_transactions_by_month_image(image_name: str, create: str):
    if not image_name:
        image_name = 'transactions_by_month.png'
    if create == 'yes' or create == 'true':
        transaction = Transaction.create_transactions_by_month_image(
            image_name)
        return transaction
    return 'images/no_image.png'


def get_transactions_by_month_image(image_name: str):
    try:
        if not path.exists(f'images/{image_name}'):
            print('Hello')
            image_name = 'no_image.png'
        return f'images/{image_name}'
    except FileNotFoundError as err:
        print(err)
        return 'images/no_image.png'
