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
        """Initialize test data fixtures."""
        # Arrange - Test data setup
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

    def test_init(self):
        """Test the initialization of OutputHandler object."""
        # Arrange - Using setUp data
        
        # Act - Create handler instance
        handler = OutputHandler(
            self.account_summaries,
            self.suspicious_transactions,
            self.transaction_statistics
        )

        # Assert - Verify correct initialization
        self.assertEqual(handler.account_summaries, self.account_summaries)
        self.assertEqual(handler.suspicious_transactions, self.suspicious_transactions)
        self.assertEqual(handler.transaction_statistics, self.transaction_statistics)

    def test_account_summaries_property(self):
        """Test the account_summaries property returns correct data."""
        # Arrange - Create handler with test data
        handler = OutputHandler(
            self.account_summaries,
            self.suspicious_transactions,
            self.transaction_statistics
        )

        # Act - Access property
        result = handler.account_summaries

        # Assert - Verify property returns correct data
        self.assertEqual(result, self.account_summaries)

    def test_suspicious_transactions_property(self):
        """Test the suspicious_transactions property returns correct data."""
        # Arrange - Setup handler
        handler = OutputHandler(
            self.account_summaries,
            self.suspicious_transactions,
            self.transaction_statistics
        )

        # Act - Access property
        result = handler.suspicious_transactions

        # Assert - Verify property value
        self.assertEqual(result, self.suspicious_transactions)

    def test_transaction_statistics_property(self):
        """Test the transaction_statistics property returns correct data."""
        # Arrange - Initialize handler
        handler = OutputHandler(
            self.account_summaries,
            self.suspicious_transactions,
            self.transaction_statistics
        )

        # Act - Access property
        result = handler.transaction_statistics

        # Assert - Verify property value
        self.assertEqual(result, self.transaction_statistics)

    @patch('builtins.open', new_callable=mock_open)
    def test_write_account_summaries_to_csv(self, mock_file):
        """Test writing account summaries to CSV file."""
        # Arrange - Create handler and mock file
        handler = OutputHandler(
            self.account_summaries,
            self.suspicious_transactions,
            self.transaction_statistics
        )

        # Act - Write to CSV
        handler.write_account_summaries_to_csv('test.csv')
        
        # Assert - Verify file operations
        mock_file.assert_called_once_with('test.csv', 'w', newline='')
        expected_calls = len(self.account_summaries) + 1
        self.assertEqual(mock_file().write.call_count, expected_calls)

    @patch('builtins.open', new_callable=mock_open)
    def test_write_suspicious_transactions_to_csv(self, mock_file):
        """Test writing suspicious transactions to CSV file."""
        # Arrange - Setup handler with test data
        handler = OutputHandler(
            self.account_summaries,
            self.suspicious_transactions,
            self.transaction_statistics
        )

        # Act - Execute CSV write operation
        handler.write_suspicious_transactions_to_csv('test.csv')
        
        # Assert - Verify write operations
        mock_file.assert_called_once_with('test.csv', 'w', newline='')
        expected_calls = len(self.suspicious_transactions) + 1
        self.assertEqual(mock_file().write.call_count, expected_calls)

    @patch('builtins.open', new_callable=mock_open)
    def test_write_transaction_statistics_to_csv(self, mock_file):
        """Test writing transaction statistics to CSV file."""
        # Arrange - Initialize handler with test data
        handler = OutputHandler(
            self.account_summaries,
            self.suspicious_transactions,
            self.transaction_statistics
        )

        # Act - Perform CSV write
        handler.write_transaction_statistics_to_csv('test.csv')
        
        # Assert - Verify file writing behavior
        mock_file.assert_called_once_with('test.csv', 'w', newline='')
        expected_calls = len(self.transaction_statistics) + 1
        self.assertEqual(mock_file().write.call_count, expected_calls)


if __name__ == "__main__":
    main()