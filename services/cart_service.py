from .generic_service import GenericService
from context.db_context import DbContext


class CartService(GenericService):

    def __init__(self, context: DbContext, table='Carts'):
        super().__init__(context, table)

    def get_by_name_value(self, name: str, value):
        data = self.context.get_all_data(self.table)
        try:
            model = list(
                filter(lambda entity: str(entity['data'][name]) == value, data))
            return model
        except KeyError as err:
            print(f'ERROR: {err}')
            return None
