from pandas.core.series import Series
from models.transaction import Transaction

# df = Transaction.get_transactions_df()
# df = Transaction.preprocess_transactions(save_csv=True, to_list=False,limit=None)
# df = Transaction.get_transactions_by_month(save_csv=True, limit=0)
# df = Transaction.get_transactions_by_amount(save_csv=True, limit=0)
# df = Transaction.get_transactions_by_cost(save_csv=True, limit=0)
# df = Transaction.get_transactions_by_cost(limit=0, top=15)
# df = Transaction.get_frequent_itemsets(
#     min_support=0.02, limit=0, save_csv=True)
df = Transaction.get_association_rules(
    min_support=0.001, min_threshold=0.01, limit=100000)


# print(df.info())
# print(df.size)
# print(df.head())
print(df)
# print(df[:10])
