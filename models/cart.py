import json


class CartModel():

    def __init__(self):
        try:
            with open('data/data.json') as file:
                self.tables = json.load(file)
        except FileNotFoundError as err:
            self.tables = None

    def get_table(self, table_name: str, model, func):
        if self.tables:
            for table in self.tables:
                if table.get('table') == table_name:
                    return func(table, model)
            return None
        else:
            return None

    def get_all_data(self, table_name: str) -> list[dict]:
        return self.get_table(table_name, None, lambda table, _: table.get('data'))

    def get_data_by_id(self, table_name: str, model: dict):
        def get_by_id(table, model):
            try:
                for entity in table.get('data'):
                    if entity['id'] == model['id']:
                        return entity
                return None
            except KeyError as err:
                print(f'ERROR: {err}')
                return None

        return self.get_table(table_name, model, get_by_id)

    def add_data(self, table_name: str, model: dict):
        def add(table, model):
            table.get('data').append(model)
            return model

        return self.get_table(table_name, model, add)

    def update_data(self, table_name: str, model: dict):
        def update(table, model):
            for entity in table.get('data'):
                if entity['id'] == model['id']:
                    entity['data'] = model['data']
                    return entity
            return None

        return self.get_table(table_name, model, update)

    def delete_data(self, table_name: str, model: dict):
        def delete(table, model):
            try:
                new_table = list()
                deleted_entity = None
                for entity in table.get('data'):
                    if entity['id'] != model['id']:
                        new_table.append(entity)
                    else:
                        deleted_entity = entity
                table['data'] = new_table
                return deleted_entity
            except KeyError as err:
                print(f'ERROR: {err}')
                return None

        return self.get_table(table_name, model, delete)
