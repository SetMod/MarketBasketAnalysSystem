from .generic_service import GenericService
from models.cart import CartModel


class CartService(GenericService):

    def __init__(self, model: CartModel, table='Carts'):
        super().__init__(model, table)

    def get_by_name_value(self, name: str, value):
        data = self.model.get_all_data(self.table)
        try:
            model = list(
                filter(lambda entity: str(entity['data'][name]) == value, data))
            return model
        except KeyError as err:
            print(f'ERROR: {err}')
            return None
