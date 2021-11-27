from context.db_context import DbContext


class GenericService():

    def __init__(self, context: DbContext, table=None):
        self.context = context
        self.table = table

    def ger_all(self):
        data = self.context.get_all_data(self.table)
        return data

    def get_by_id(self, id: int):
        data = self.context.get_data_by_id(self.table, {'id': id})
        return data

    def create(self, model):
        new_model = {'data': model.Data, 'id': model.Id}
        entity = self.get_by_id(model.Id)
        if not entity:
            data = self.context.add_data(self.table, new_model)
            return data
        else:
            return None

    def update(self, model):
        new_model = {'data': model.Data, 'id': model.Id}
        entity = self.get_by_id(model.Id)
        if entity:
            data = self.context.update_data(self.table, new_model)
            return data
        else:
            return None

    def delete(self, id: int):
        entity = self.get_by_id(id)
        if entity:
            deleted_entity = self.context.delete_data(self.table, {'id': id})
            return deleted_entity
        else:
            return None
