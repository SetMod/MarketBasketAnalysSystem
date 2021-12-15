import re
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from pandas.core.frame import DataFrame
from pandas.core.series import Series


class Transaction:

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_transactions_df(limit: int = 10000) -> DataFrame:
        """[summary]

        Args:
            limit (int, optional): [description]. Defaults to 10000.

        Returns:
            DataFrame: [description]
        """
        try:
            read_df = pd.read_csv('data/transaction_data.csv')
            if limit and limit < len(read_df):
                return read_df.copy()[:limit]
            else:
                return read_df.copy()
        except Exception as err:
            print(err)
            return None

    @staticmethod
    def get_transactions_list(limit: int = 10000) -> list:
        """[summary]

        Args:
            limit (int, optional): [description]. Defaults to 10000.

        Returns:
            list: [description]
        """
        try:
            df = Transaction.get_transactions_df(limit=limit)
            if limit and limit < len(df):
                return df[:limit].values.tolist()
            else:
                return df.values.tolist()
        except Exception as err:
            print(err)
            return None

    @staticmethod
    def get_paginated_transactions(pageSize: int, pageNumber: int) -> list:
        """[summary]

        Args:
            pageSize (int): [description]
            pageNumber (int): [description]

        Returns:
            list: [description]
        """
        try:
            df = Transaction.get_transactions_list(limit=None)
            if pageNumber <= 1:
                return df[0:pageSize]
            elif pageSize * pageNumber > len(df):
                return df[len(df)-pageSize:len(df)]
            else:
                start = pageSize * pageNumber - pageSize
                end = pageSize * pageNumber
                return df[start:end]
        except Exception as err:
            print(err)
            return None

    @staticmethod
    def get_transaction_by_any_value(any_value) -> DataFrame:
        """[summary]

        Args:
            any_value (any): any_value is any value to find in DataFrame

        Returns:
            DataFrame: found value
        """
        try:
            df = Transaction.get_transactions_df()
            return df[df.eq(any_value).any(1)]
        except Exception as err:
            print(err)
            return None

    @staticmethod
    def get_preprocessed_transactions(save_csv=False, to_list=True, limit: int = 10000) -> list:
        """[summary]

        Args:
            save_csv (bool, optional): saves DataFrame to csv. Defaults to False.
            to_list (bool, optional): returns a list. Defaults to True.
            limit (int, optional): set's limit of rows to return. Default to 10000.

        Returns:
            list: default
            DataFrame: if to_list=False
        """
        try:
            df = Transaction.get_transactions_df(limit=limit)
            df = df[df.UserId > 0]
            df = df[df.ItemCode > 0]
            df = df[df.NumberOfItemsPurchased > 0]
            df = df[df.CostPerItem > 0]
            df = df[df.ItemDescription.notna()]
            df = df[df.TransactionTime.str[-4:] != '2028']
            if save_csv:
                df.to_csv('./data/preprocessed_transactions.csv')
            if to_list:
                return df.values.tolist()
            else:
                return df
        except Exception as err:
            print(err)
            return None

    @staticmethod
    def get_transactions_by_month(save_csv=False, limit: int = 10000) -> Series:
        """[summary]

        Args:
            save_csv (bool, optional): [description]. Defaults to False.
            limit (int, optional): set's limit of rows to return. Default to 10000.

        Returns:
            Series: [description]
        """
        try:
            df = Transaction.get_preprocessed_transactions(
                to_list=False, limit=limit)
            df.TransactionTime = pd.to_datetime(df.TransactionTime)
            df['month_year'] = pd.to_datetime(
                df.TransactionTime).dt.to_period('M')
            df.sort_values(by=['month_year'], inplace=True)
            Ser = df.groupby('month_year').TransactionId.nunique()
            if save_csv:
                Ser.to_csv('./data/transactions_by_month.csv')
            return Ser
        except Exception as err:
            print(err)
            return None

    @staticmethod
    def get_transactions_by_amount(save_csv=False, limit: int = 10000) -> Series:
        """[summary]

        Args:
            save_csv (bool, optional): [description]. Defaults to False.
            limit (int, optional): set's limit of rows to return. Default to 10000.

        Returns:
            Series: [description]
        """
        try:
            df = Transaction.get_preprocessed_transactions(
                to_list=False, limit=limit)
            Ser = df.groupby('TransactionId').ItemDescription.nunique()
            if save_csv:
                Ser.to_csv('./data/transactions_by_amount.csv')
            return Ser
        except Exception as err:
            print(err)
            return None

    @staticmethod
    def get_transactions_by_cost(save_csv=False, limit: int = 10000, top: int = 10) -> Series:
        """[summary]

        Args:
            save_csv (bool, optional): [description]. Defaults to False.
            limit (int, optional): set's limit of rows to return. Default to 10000.
            top (int, optional): get top transactions. Default to 10

        Returns:
            Series: [description]
        """
        try:
            df = Transaction.get_preprocessed_transactions(
                to_list=False, limit=limit)
            df['total_cost_item'] = df.NumberOfItemsPurchased*df.CostPerItem
            Ser = df.groupby('ItemDescription').total_cost_item.sum()
            Ser.sort_values(ascending=False, inplace=True)
            if save_csv:
                Ser.to_csv('./data/transactions_by_cost.csv', index=False)
            if top:
                return Ser[:top]
            else:
                return Ser
        except Exception as err:
            print(err)
            return None

    @staticmethod
    def get_frequent_itemsets(min_support: float = 0.015,  limit: int = 10000, save_csv=False) -> Series:
        """[summary]

        Args:
            min_support (float, optional): minimal support. Defaults to 0.015.
            limit (int, optional): limit of rows to read. Defaults to 10000.
            save_csv (bool, optional): save result to csv. Defaults to False.

        Returns:
            Series: result
        """
        try:
            df = Transaction.get_preprocessed_transactions(
                to_list=False, limit=limit)

            df_set = df.groupby(['TransactionId', 'ItemDescription']).NumberOfItemsPurchased.sum(
            ).unstack().reset_index().fillna(0).set_index('TransactionId')

            # df_set = df_set.applymap(lambda x: 0 if x <= 0 else 1) # toooooo slowwwww
            df_set = (df_set > 0).astype(np.int8)

            frequent_itemsets = apriori(
                df_set, min_support=min_support, use_colnames=True, low_memory=True)
            frequent_itemsets['itemsets'] = frequent_itemsets['itemsets'].apply(
                tuple)  # convert frozenset to tuple

            if save_csv:
                frequent_itemsets.to_csv(
                    './data/frequent_itemsets.csv', index=False)
            return frequent_itemsets
        except Exception as err:
            print(err)
            return None

    @ staticmethod
    def get_association_rules(min_support: float = 0.015, min_threshold: float = 0.2, metric: str = 'confidence', limit: int = 10000) -> DataFrame:
        """[summary]

        Args:
            min_support (float, optional): minimal support. Defaults to 0.015.
            min_threshold (float, optional): minimal threshold for . Defaults to 0.2.
            metric (str, optional): Metric to evaluate if a rule is of interest. Supported metrics are 'support', 'confidence', 'lift', 'leverage', and 'conviction'. Defaults to 'confidence'.
            limit (int, optional): limit of rows to read. Defaults to 10000.

        Returns:
            DataFrame: result
        """
        try:
            frequent_itemsets = Transaction.get_frequent_itemsets(
                min_support=min_support, limit=limit)
            rules = association_rules(
                frequent_itemsets, metric=metric, min_threshold=min_threshold)
            rules['antecedents'] = rules['antecedents'].apply(tuple)
            rules['consequents'] = rules['consequents'].apply(tuple)
            print(rules.columns)
            return rules.values.tolist()
        except Exception as err:
            print(err)
            return None

    @ staticmethod
    def create_top_cost_transactions_image(image_name: str):
        try:
            df = Transaction.get_transactions_df()
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

    @ staticmethod
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

    @ staticmethod
    def create_transactions_by_month_image(image_name: str):
        try:
            Ser = Transaction.get_transactions_by_month()
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
