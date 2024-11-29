"""This module is for getting the file format then putting that file if it is
a csv or a json and put it into a dictionary.
"""

__author__ = "Thomas Littleton"
__version__ = "1.0."

import csv
import json
from os import path

class InputHandler:
    """This class is for validation for the input of the files which is the input.
    """

    def __init__(self, file_path: str):
        """Initializes a new instance of the InputHandler class.
        """
        self.__file_path = file_path

    @property
    def file_path(self) -> str:
        """Gets the file path of the InputHandler.

        Returns:
            __file_path: The file path of the InputHandler.
        """
        return self.__file_path

    def get_file_format(self) -> str:
        """Gets the file path of the InputHandler.

        Returns:
            __file_path.split: The file path formatted of the InputHandler.
        """
        return self.__file_path.split(".")[-1]

    def read_input_data(self) -> list:
        """Reads the file and put it into a variable.
        
        It checks to see it is a csv or a json file then reads that file into
        a variable then returns that variable.

        Returns:
            transactions: the variable that holds the file.
        """
        transactions = []
        file_format = self.get_file_format()
        
        if file_format == "csv":
            transactions =  self.read_csv_data()
        elif file_format == "json":
            transactions = self.read_json_data()
        return transactions

    def read_csv_data(self) -> list:
        """Reads the file and put it into a variable.
        
        Returns:
            transactions: the variable that holds the file.
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
        """Reads the file and put it into a variable.
        
        Returns:
            transactions: the variable that holds the file.
        """
        # Research the json.load function so that you 
        # understand the format of the data once it is
        # placed into input_data
        if not path.isfile(self.__file_path):
            raise FileNotFoundError(f"File: {self.__file_path} does not exist.")

        with open(self.__file_path, "r") as input_file:
            transactions = json.load(input_file)

        return transactions
