from os import path
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np


class Transaction:

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_transactions():
        try:
            read_df = pd.read_csv('data/transaction_data.csv')
            return read_df.copy()[:100].values.tolist()
        except Exception as err:
            print(err)
            return None

    @staticmethod
    def get_transaction_by_id(id: int):
        try:
            df = Transaction.get_transactions()
            return df[df.eq(id).any(1)]
        except Exception as err:
            print(err)
            return None

    @staticmethod
    def preprocess_transactions():
        try:
            # Exploratory data analysis(EDA) and data cleaning is done as follows:
            df = Transaction.get_transactions()
            df = df[df.UserId > 0]  # usedid <=0 : 25%
            df = df[df.ItemCode > 0]
            df = df[df.NumberOfItemsPurchased > 0]
            df = df[df.CostPerItem > 0]
            df = df[df.ItemDescription.notna()]
            df = df[df.TransactionTime.str[-4:] != '2028']
            df = df[:1000]
            return df
        except Exception as err:
            print(err)
            return None

    @staticmethod
    def create_transactions_by_month_image(image_name: str):
        try:
            # Lets do some exploratory data analysis now. Lets see the no. of transactions
            # being done in each part of the year.
            df = Transaction.preprocess_transactions()
            df.TransactionTime = pd.to_datetime(df.TransactionTime)
            df['month_year'] = pd.to_datetime(
                df.TransactionTime).dt.to_period('M')
            df.sort_values(by=['month_year'], inplace=True)
            Ser = df.groupby('month_year').TransactionId.nunique()
            x = np.arange(0, len(Ser), 1)
            style.use('ggplot')
            fig = plt.figure(figsize=(10, 10))
            ax1 = fig.add_subplot(111)
            ax1.plot(x, Ser, color='k')
            ax1.fill_between(x, Ser, color='r', alpha=0.5)
            ax1.set_xticks(x)
            ax1.set_xticklabels(Ser.index)
            plt.xlabel('Time period')
            plt.ylabel('No. of transactions')
            image_path = f'images/{image_name}'
            plt.savefig(image_path)
            plt.close(fig)
            return image_path
        except Exception as err:
            print(err)
            return None

    @staticmethod
    def create_transactions_by_amount_image(image_name: str):
        try:
            df = Transaction.get_transactions()
            Ser = df.groupby('TransactionId').ItemDescription.nunique()
            bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
                    110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
            fig = plt.figure(figsize=(10, 10))
            ax1 = fig.add_subplot(111)
            ax1.hist(Ser, bins, histtype='bar', rwidth=0.5)
            ax1.set_xticks(bins)
            plt.xlabel('No. of items')
            plt.ylabel('No. of transactions')
            image_path = f'images/{image_name}'
            plt.savefig(image_path)
            plt.close(fig)
            return image_path
        except Exception as err:
            print(err)
            return None

    @staticmethod
    def create_top_coast_transactions_image(image_name: str):
        try:
            df = Transaction.get_transactions()
            df['total_cost_item'] = df.NumberOfItemsPurchased*df.CostPerItem
            Ser = df.groupby('ItemDescription').total_cost_item.sum()
            Ser.sort_values(ascending=False, inplace=True)
            Ser = Ser[:10]
            fig = plt.figure(figsize=(10, 10))
            ax = fig.add_subplot(111)
            ax.barh(Ser.index, Ser, height=0.5)
            image_path = f'images/{image_name}'
            plt.savefig(image_path)
            plt.close(fig)
            return image_path
        except Exception as err:
            print(err)
            return None

    @staticmethod
    def get_frequent_itemsets(min_support: float = 0.015):
        try:
            df = Transaction.get_transactions()
            df_set = df.groupby(['TransactionId', 'ItemDescription']).NumberOfItemsPurchased.sum(
            ).unstack().reset_index().fillna(0).set_index('TransactionId')
            df_set = df_set.applymap(lambda x: 0 if x <= 0 else 1)
            frequent_itemsets = apriori(
                df_set, min_support=min_support, use_colnames=True)
            return frequent_itemsets
        except Exception as err:
            print(err)
            return None

    @staticmethod
    def create_to_items_apriori(image_name: str, min_support: float = 0.015):
        try:
            frequent_itemsets = Transaction.get_frequent_itemsets(min_support)
            top_items = frequent_itemsets.sort_values(
                'support', ascending=False)[:20]
            for i in range(len(top_items.itemsets)):
                top_items.itemsets.iloc[i] = str(
                    list(top_items.itemsets.iloc[i]))
            fig = plt.figure(figsize=(10, 10))
            ax = fig.add_subplot(111)
            ax.bar(top_items.itemsets, top_items.support)
            for label in ax.xaxis.get_ticklabels():
                label.set_rotation(90)
            image_path = f'images/{image_name}'
            plt.savefig(image_path)
            plt.close(fig)
            return image_path
        except Exception as err:
            print(err)
            return None

    @staticmethod
    def get_association_rules(min_support: float = 0.015, min_threshold: float = 0.2):
        try:
            frequent_itemsets = Transaction.get_frequent_itemsets(min_support)
            rules = association_rules(
                frequent_itemsets, metric='confidence', min_threshold=min_threshold)
            return rules
        except Exception as err:
            print(err)
            return None
