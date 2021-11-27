class CartModel():

    def __init__(self, id: int, data: dict):
        self.id = id
        self.data = data

    @property
    def Id(self):
        return self.id

    @property
    def Data(self):
        return self.data
