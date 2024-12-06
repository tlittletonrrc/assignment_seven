"""REQUIRED MODULE DOCUMENTATION
"""

__author__ = ""
__version__ = ""

import unittest
from unittest import TestCase
from input_handler.input_handler import InputHandler

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

if __name__ == "__main__":
    unittest.main()