from models.cart import CartModel


class GenericService():

    def __init__(self, model: CartModel, table=None):
        self.model = model
        self.table = table

    def ger_all(self):
        data = self.model.get_all_data(self.table)
        return data

    def get_by_id(self, id: int):
        data = self.model.get_data_by_id(self.table, {'id': id})
        return data

    def create(self, model):
        new_model = {'data': model.Data, 'id': model.Id}
        entity = self.get_by_id(model.Id)
        if not entity:
            data = self.model.add_data(self.table, new_model)
            return data
        else:
            return None

    def update(self, model):
        new_model = {'data': model.Data, 'id': model.Id}
        entity = self.get_by_id(model.Id)
        if entity:
            data = self.model.update_data(self.table, new_model)
            return data
        else:
            return None

    def delete(self, id: int):
        entity = self.get_by_id(id)
        if entity:
            deleted_entity = self.model.delete_data(self.table, {'id': id})
            return deleted_entity
        else:
            return None
