from models.transaction import Transaction


def get_transactions():
    transactions = Transaction.get_transactions()
    try:
        if not transactions.empty:
            return transactions.to_dict()
        else:
            return 'No transactions'
    except AttributeError as err:
        print(err)
        return 'Error reading file'


def get_transaction_by_id(id: int):
    transactions = Transaction.get_transaction_by_id(id)
    try:
        if not transactions.empty:
            return transactions.to_dict()
        else:
            return f'No transaction with id={id}'
    except AttributeError as err:
        print(err)
        return 'Error reading file'
