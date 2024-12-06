"""REQUIRED MODULE DOCUMENTATION
"""

__author__ = ""
__version__ = ""

import csv
import json
from os import path

class InputHandler:
    """REQUIRED: CLASS DOCSTRING
    """

    def __init__(self, file_path: str):
        """REQUIRED: METHOD DOCSTRING
        """
        self.__file_path = file_path

    @property
    def file_path(self) -> str:
        """REQUIRED: METHOD DOCSTRING
        """
        return self.__file_path

    def get_file_format(self) -> str:
        """REQUIRED: METHOD DOCSTRING
        """
        return self.__file_path.split(".")[-1]

    def read_input_data(self) -> list:
        """REQUIRED: METHOD DOCSTRING
        """
        transactions = []
        file_format = self.get_file_format()
        
        if file_format == "csv":
            transactions =  self.read_csv_data()
        elif file_format == "json":
            transactions = self.read_json_data()
        return transactions

    def read_csv_data(self) -> list:
        """REQUIRED: METHOD DOCSTRING
        """
        if not path.isfile(self.__file_path):
            raise FileNotFoundError(f"File: {self.__file_path} does not exist.")

        transactions = []

        with open(self.__file_path, "r") as input_file:
            reader = csv.DictReader(input_file)
            for row in reader:
                transactions.append(row)
            
        return transactions
            
    def read_json_data(self) -> list:
        """REQUIRED: METHOD DOCSTRING
        """
        # Research the json.load function so that you 
        # understand the format of the data once it is
        # placed into input_data
        if not path.isfile(self.__file_path):
            raise FileNotFoundError(f"File: {self.__file_path} does not exist.")

        with open(self.__file_path, "r") as input_file:
            transactions = json.load(input_file)

        return transactions

    def data_validation(self) -> list:
        """checks to see if the amount or the transaction type
        is a valid value. ex if amount is less then 0.
        
        Args:
            transaction (list): The list of all transactions.
            valid_transaction (list): The list of all valid
            transactions.

        Returns:
            valid_transaction: A list of all valid transactions.
        """
        transaction = self.read_input_data()
        valid_transaction = []

        for transactions in transaction:

            if isinstance(transactions["Amount"], (int, float)):
                amount = int(transactions["Amount"])
                if amount > 0:
                    transaction_type = ["deposit", "withdrawal", "transfer"]
                    if transactions["Transaction type"] in transaction_type:
                        valid_transaction.append(transactions)

        return valid_transaction
    