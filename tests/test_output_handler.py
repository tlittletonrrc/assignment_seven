"""Unit tests for the OutputHandler class.
This file contain test cases for verifying the functionality of the OutputHandler class, including intialization, property access, and CSV file writing operations.
"""

__author__ = "Karmjeet Kaur"
__version__ = "1.0"

from unittest import TestCase, main
from unittest.mock import patch, mock_open
from output_handler.output_handler import OutputHandler

class TestOutputHandler(TestCase):
    """Defines the unit tests for the OutputHandler class."""

    def setUp(self):
        """This function is invoked before executing a unit test
        function.

        The following class attributes have been provided to reduce the 
        amount of code needed when creating OutputHandler class objects 
        in the tests that follow.  
        
        Example:
            >>> OutputHandler(self.account_summaries, 
                              self.suspicious_transactions, 
                              self.transaction_statistics)
        """
        self.account_summaries = { 
            "1001": {
                "account_number": "1001", 
                "balance": 50, 
                "total_deposits": 100, 
                "total_withdrawals": 50
            },
            "1002": {
                "account_number": "2", 
                "balance": 200, 
                "total_deposits": 200, 
                "total_withdrawals": 0
            }
        }

        self.suspicious_transactions = [
            {
                "Transaction ID": "1",
                "Account number": "1001",
                "Date": "2023-03-14",
                "Transaction type": "deposit",
                "Amount": 250,
                "Currency": "XRP",
                "Description": "crypto investment"
            }
        ]

        self.transaction_statistics = {
            "deposit": {
                "total_amount": 300, 
                "transaction_count": 2
            }, 
            "withdrawal": {
                "total_amount": 50, 
                "transaction_count": 1
            }
        }

    # Define unit test functions below
    def test_init(self):
        """Test the intialization of OutputHandler object."""
        handler = OutputHandler(
            self.account_summaries,
            self.suspicious_transactions,
            self.transaction_statistics
        )
        self.assertEqual(handler.account_summaries, self.account_summaries)
        self.assertEqual(handler.suspicious_transactions, self.suspicious_transactions)
        self.assertEqual(handler.transaction_statistics, self.transaction_statistics)
    
    def test_account_summaries_property(self):
        """Test the account summaries property returns correct data"""
        handler = OutputHandler(
            self.account_summaries,
            self.suspicious_transactions,
            self.transaction_statistics
        )
        self.asserEqual(handler.account_summaries, self.account_summaries)

    def test_suspicious_transaction_property(self):
        """Test the suspicious_trnasaction property returns correct data."""
        handler = OutputHandler(
            self.account_summaries,
            self.suspicious_transactions,
            self.transaction_statistics
        )
        self.assertEqual(handler.transaction_statistics, self.transaction_statistics)


    @patch('builtins.open', new_callable=mock_open)
    def test_write_account_summaries_to_csv(self, mock_file):
        """Test writting account summaries to CSV file."""
        handler = OutputHandler(
            self.account_summaries,
            self.suspicious_transactions,
            self.transaction_statistics
        )
        handler.write_account_summaries_to_csv('test.csv')
        
        mock_file.assert_called_once_with('test.csv', 'w', newline='')
        # Verify number of calls (header + data rows)
        expected_calls = len(self.account_summaries) + 1
        self.assertEqual(mock_file().write.call_count, expected_calls)

    @patch('builtins.open', new_callable=mock_open)
    def test_write_suspicious_transactions_to_csv(self, mock_file):
        """Test writing suspicious transactions to CSV file."""
        handler = OutputHandler(
            self.account_summaries,
            self.suspicious_transactions,
            self.transaction_statistics
        )
        handler.write_suspicious_transactions_to_csv('test.csv')
        
        mock_file.assert_called_once_with('test.csv', 'w', newline='')
        # Verify number of calls (header + data rows)
        expected_calls = len(self.suspicious_transactions) + 1
        self.assertEqual(mock_file().write.call_count, expected_calls)

    @patch('builtins.open', new_callable=mock_open)
    def test_write_transaction_statistics_to_csv(self, mock_file):
        """Test writing transaction statistics to CSV file."""
        handler = OutputHandler(
            self.account_summaries,
            self.suspicious_transactions,
            self.transaction_statistics
        )
        handler.write_transaction_statistics_to_csv('test.csv')
        
        mock_file.assert_called_once_with('test.csv', 'w', newline='')
        # Verify number of calls (header + data rows)
        expected_calls = len(self.transaction_statistics) + 1
        self.assertEqual(mock_file().write.call_count, expected_calls)


if __name__ == "__main__":
    main()