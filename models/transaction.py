import pandas as pd
# from mlxtend.frequent_patterns import apriori
# from mlxtend.frequent_patterns import association_rules
# import matplotlib.pyplot as plt
# from matplotlib import style
# import numpy as np


class Transaction:

    def __init__(self) -> None:
        self.df = None

    @staticmethod
    def get_transactions():
        try:
            read_df = pd.read_csv('data/transaction_data.csv')
            return read_df.copy()[:10]
        except Exception as err:
            print(err)
            return None

    @staticmethod
    def get_transaction_by_id(id: int):
        try:
            read_df = pd.read_csv('data/transaction_data.csv')
            return read_df[read_df.eq(id).any(1)]
        except Exception as err:
            print(err)
            return None
