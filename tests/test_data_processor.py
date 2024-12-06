"""
Test suite for financial transaction processing.

Validates the core functionality of the DataProcessor class including:
- Account balance tracking
- Suspicious activity monitoring
- Transaction analytics

"""

__author__ = "sandeep kaur"
__version__ = "1.0."

import unittest
from unittest import TestCase
from data_processor.data_processor import DataProcessor

class TestDataProcessor(TestCase):
    """Defines the unit tests for the DataProcessor class."""

    def setUp(self):
        """This function is invoked before executing a unit test
        function.

        The following class attribute has been provided to reduce the 
        amount of code needed when creating DataProcessor class objects 
        in the tests that follow.  
        
        Example:
            >>> data_processor = DataProcessor(self.transactions)
        """
        self.transactions = [
            {
                "Transaction ID": "1",
                "Account number": "1001",
                "Date": "2023-03-01",
                "Transaction type": "deposit",
                "Amount": 1000,
                "Currency": "CAD",
                "Description": "Salary"
            }, 
            {
                "Transaction ID": "2",
                "Account number": "1002",
                "Date": "2023-03-01",
                "Transaction type": "deposit",
                "Amount": 1500,
                "Currency": "CAD",
                "Description": "Salary"
            }
        ]

def test_update_account_summary_deposit(self):
        """Test account summary updates for deposit transactions."""
        processor = DataProcessor([])
        deposit_transaction = {
            "Transaction ID": "3",
            "Account number": "1003",
            "Transaction type": "deposit",
            "Amount": 2000,
            "Currency": "CAD"
        }
        
        processor.update_account_summary(deposit_transaction)
        account_summary = processor.account_summaries["1003"]
        
        self.assertEqual(account_summary["balance"], 2000)
        self.assertEqual(account_summary["total_deposits"], 2000)
        self.assertEqual(account_summary["total_withdrawals"], 0)

def test_update_account_summary_withdrawal(self):
        """Test account summary updates for withdrawal transactions."""
        processor = DataProcessor([])
        withdrawal_transaction = {
            "Transaction ID": "4",
            "Account number": "1004",
            "Transaction type": "withdrawal",
            "Amount": 500,
            "Currency": "CAD"
        }
        
        processor.update_account_summary(withdrawal_transaction)
        account_summary = processor.account_summaries["1004"]
        
        self.assertEqual(account_summary["balance"], -500)
        self.assertEqual(account_summary["total_deposits"], 0)
        self.assertEqual(account_summary["total_withdrawals"], 500)

def test_check_suspicious_transactions_large_amount(self):
        """Test detection of transactions exceeding threshold."""
        processor = DataProcessor([])
        large_transaction = {
            "Transaction ID": "5",
            "Account number": "1005",
            "Amount": DataProcessor.LARGE_TRANSACTION_THRESHOLD + 1000,
            "Currency": "CAD"
        }
        
        processor.check_suspicious_transactions(large_transaction)
        self.assertIn(large_transaction, processor.suspicious_transactions)

def test_check_suspicious_transactions_uncommon_currency(self):
        """Test detection of transactions with uncommon currencies."""
        processor = DataProcessor([])
        crypto_transaction = {
            "Transaction ID": "6",
            "Account number": "1006",
            "Amount": 1000,
            "Currency": "XRP"
        }
        
        processor.check_suspicious_transactions(crypto_transaction)
        self.assertIn(crypto_transaction, processor.suspicious_transactions)

def test_check_suspicious_transactions_normal(self):
        """Test handling of normal transactions."""
        processor = DataProcessor([])
        normal_transaction = {
            "Transaction ID": "7",
            "Account number": "1007",
            "Amount": 1000,
            "Currency": "CAD"
        }
        
        processor.check_suspicious_transactions(normal_transaction)
        self.assertEqual(len(processor.suspicious_transactions), 0)

def test_update_transaction_statistics(self):
        """Test transaction statistics tracking."""
        processor = DataProcessor([])
        test_transaction = {
            "Transaction ID": "8",
            "Account number": "1008",
            "Transaction type": "deposit",
            "Amount": 3000,
            "Currency": "CAD"
        }
        
        processor.update_transaction_statistics(test_transaction)
        stats = processor.transaction_statistics["deposit"]
        
        self.assertEqual(stats["total_amount"], 3000)
        self.assertEqual(stats["transaction_count"], 1)

if __name__ == "__main__":
    unittest.main()
