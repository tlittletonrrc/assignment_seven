"""This module is for making and running tests to test the input_handler module.
To be able to run the tests use this command in the terminal.
python3 -m unittest tests/test_input_handler.py
"""

__author__ = "Thomas Littleton"
__version__ = "1.0."

import unittest
from unittest import TestCase
from input_handler.input_handler import InputHandler
from unittest.mock import patch, mock_open

class InputHandlerTests(TestCase):
    """Defines the unit tests for the InputHandler class."""

    def setUp(self):
        """This function is invoked before executing a unit test
        function.

        The following class attribute has been provided to reduce the 
        amount of code needed when testing the InputHandler class in 
        the tests that follow.
        
        Example:
            >>> data_processor = DataProcessor(self.FILE_CONTENTS)
        """
        self.FILE_CONTENTS = \
            ("Transaction ID,Account number,Date,Transaction type,"
            + "Amount,Currency,Description\n"
            + "1,1001,2023-03-01,deposit,1000,CAD,Salary\n"
            + "2,1002,2023-03-01,deposit,1500,CAD,Salary\n"
            + "3,1001,2023-03-02,withdrawal,200,CAD,Groceries")

    # Tests for validating transactions
    def test_list_of_transactions_excludes_not_a_numeric_type(self):
        # Returns a list of transactions that excludes records
        # with an amount that is not a numeric type (int or float).

        # Arrange
        file_path = "/input/test_not_numeric.json"

        # Act
        file = [
                {
                    "Transaction ID": 1,
                    "Account number": 1002,
                    "Date": "2023-03-01",
                    "Transaction type": "deposit",
                    "Amount": "a",
                    "Currency": "CAD",
                    "Description": "Salary"
                },
                {
                    "Transaction ID": 2,
                    "Account number": 1002,
                    "Date": "2023-03-01",
                    "Transaction type": "deposit",
                    "Amount": 1800,
                    "Currency": "CAD",
                    "Description": "Salary"
                },
                {
                    "Transaction ID": 3,
                    "Account number": 1001,
                    "Date": "2023-03-02",
                    "Transaction type": "withdrawal",
                    "Amount": 300,
                    "Currency": "CAD",
                    "Description": "Groceries"
                }
                ]
        input = InputHandler(file_path)
        actual = input.data_validation(file)

        # Assert
        expected = [
                {
                    "Transaction ID": 2,
                    "Account number": 1002,
                    "Date": "2023-03-01",
                    "Transaction type": "deposit",
                    "Amount": 1800,
                    "Currency": "CAD",
                    "Description": "Salary"
                },
                {
                    "Transaction ID": 3,
                    "Account number": 1001,
                    "Date": "2023-03-02",
                    "Transaction type": "withdrawal",
                    "Amount": 300,
                    "Currency": "CAD",
                    "Description": "Groceries"
                }
                ]
        self.assertEqual(expected, actual)

    def test_list_of_transactions_excludes_less_then_zero(self):
        # Returns a list of transactions that excludes
        # records with amount less than zero.
        
        # Arrange
        file_path = "input/test_less_then_zero.json"

        # Act
        file = [
                {
                    "Transaction ID": 1,
                    "Account number": 1002,
                    "Date": "2023-03-01",
                    "Transaction type": "deposit",
                    "Amount": -1800,
                    "Currency": "CAD",
                    "Description": "Salary"
                },
                {
                    "Transaction ID": 2,
                    "Account number": 1002,
                    "Date": "2023-03-01",
                    "Transaction type": "deposit",
                    "Amount": 1800,
                    "Currency": "CAD",
                    "Description": "Salary"
                },
                {
                    "Transaction ID": 3,
                    "Account number": 1001,
                    "Date": "2023-03-02",
                    "Transaction type": "withdrawal",
                    "Amount": 300,
                    "Currency": "CAD",
                    "Description": "Groceries"
                }
                ]
        input = InputHandler(file_path)
        actual = input.data_validation(file)

        # Assert
        expected = [
                {
                    "Transaction ID": 2,
                    "Account number": 1002,
                    "Date": "2023-03-01",
                    "Transaction type": "deposit",
                    "Amount": 1800,
                    "Currency": "CAD",
                    "Description": "Salary"
                },
                {
                    "Transaction ID": 3,
                    "Account number": 1001,
                    "Date": "2023-03-02",
                    "Transaction type": "withdrawal",
                    "Amount": 300,
                    "Currency": "CAD",
                    "Description": "Groceries"
                }
                ]
        self.assertEqual(expected, actual)

    def test_list_of_transactions_excludes_invalid_transaction_type(self):
        # Returns a list of transactions that excludes
        # records with an invalid transaction_type.
        # Arrange
        file_path = "input/test_invalid_transaction_type.json"

        # Act
        file = [
                {
                    "Transaction ID": 1,
                    "Account number": 1002,
                    "Date": "2023-03-01",
                    "Transaction type": "a",
                    "Amount": 1800,
        self.FILE_CONTENTS_FOR_TESTS = [{'Transaction ID': '1',
                                        'Account number': '1001',
                                        'Date': '2023-03-01',
                                        'Transaction type': 'deposit',
                                        'Amount': '1000',
                                        'Currency': 'CAD',
                                        'Description': 'Salary'},
                                        {'Transaction ID': '2',
                                         'Account number': '1002',
                                         'Date': '2023-03-01',
                                         'Transaction type': 'deposit',
                                         'Amount': '1500',
                                         'Currency': 'CAD',
                                         'Description': 'Salary'},
                                         {'Transaction ID': '3',
                                          'Account number': '1001',
                                          'Date': '2023-03-02',
                                          'Transaction type': 'withdrawal',
                                          'Amount': '200', 'Currency': 'CAD', 
                                          'Description': 'Groceries'}]

    # test for get file format
    def test_get_file_format(self):
        """Returns the file extension of the file path."""
        # Arrange
        file_path = "file.csv"

        # Act
        input = InputHandler(file_path)

        # Assert
        expected = "csv"
        actual  = input.get_file_format
        
        self.assertEqual = (actual, expected)

    # tests for read csv data
    def test_read_csv_data_file_path_does_not_exist(self):
        """Raises a FileNotFoundError when the file path does not exist to a file."""
        # Arrange
        file_path = "file.jkl"

        # Act
        input = InputHandler(file_path)

        with self.assertRaises(FileNotFoundError) as context:
            input.read_csv_data()

        # Assert
        expected = f"File: {file_path} does not exist."
        actual = str(context.exception)
        self.assertEqual(expected, actual)
    
    def test_read_csv_data_list_of_transaction_from_csv(self):
        """Returns a list containing the transaction data from an existing csv file."""
        # Arrange
        file_contents = self.FILE_CONTENTS
        file_path = "/workspaces/assignment_seven/input/input_data.csv"

        # Act
        
        with patch('builtins.open', mock_open(read_data=file_contents)):
            input = InputHandler(file_path)
            actual = input.read_csv_data()

        # Assert
        expected = self.FILE_CONTENTS_FOR_TESTS
        self.assertEqual(expected, actual)

    # tests for read input data
    def test_read_input_data_list_of_transaction_from_csv(self):
        """Returns a list containing the transaction data from an existing csv file."""
        # Arrange
        file_contents = self.FILE_CONTENTS
        file_path = "/workspaces/assignment_seven/input/input_data.csv"

        # Act
        with patch('builtins.open', mock_open(read_data=file_contents)):
            input = InputHandler(file_path)
            actual = input.read_input_data()

        # Assert
        expected = self.FILE_CONTENTS_FOR_TESTS
        self.assertEqual(expected, actual)

    def test_read_input_data_list_of_transaction_from_json(self):
        """Returns a list containing the transaction data from an existing json file."""
        # Arrange
        file_path = "/workspaces/assignment_seven/input/tests.json"

        # Act
        input = InputHandler(file_path)
        actual = input.read_input_data()

        # Assert
        expected = [
                {
                    "Transaction ID": 1,
                    "Account number": 1001,
                    "Date": "2023-03-01",
                    "Transaction type": "deposit",
                    "Amount": 1200,
                    "Currency": "CAD",
                    "Description": "Salary"
                },
                {
                    "Transaction ID": 2,
                    "Account number": 1002,
                    "Date": "2023-03-01",
                    "Transaction type": "deposit",
                    "Amount": 1800,
                    "Currency": "CAD",
                    "Description": "Salary"
                },
                {
                    "Transaction ID": 3,
                    "Account number": 1001,
                    "Date": "2023-03-02",
                    "Transaction type": "withdrawal",
                    "Amount": 300,
                    "Currency": "CAD",
                    "Description": "Groceries"
                }
                ]
        input = InputHandler(file_path)
        actual = input.data_validation(file)

        # Assert
        expected = [
                {
                    "Transaction ID": 2,
                    "Account number": 1002,
                    "Date": "2023-03-01",
                    "Transaction type": "deposit",
                    "Amount": 1800,
                    "Currency": "CAD",
                    "Description": "Salary"
                },
                {
                    "Transaction ID": 3,
                    "Account number": 1001,
                    "Date": "2023-03-02",
                    "Transaction type": "withdrawal",
                    "Amount": 300,
                    "Currency": "CAD",
                    "Description": "Groceries"
                }
                ]
        self.assertEqual(expected, actual)

    def test_read_input_data_empty_list_if_no_json_or_csv(self):
        """Returns an empty list if the file is not a csv or json file."""
        # Arrange
        file_contents = ""
        file_path = "/workspaces/assignment_seven/input/input_data.csv"

        # Act
        with patch('builtins.open', mock_open(read_data=file_contents)):
            input = InputHandler(file_path)
            actual = input.read_input_data()

        # Assert
        expected = []
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
