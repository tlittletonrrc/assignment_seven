"""
Financial Transaction Data Processing Module

This module provides functionality for processing financial transaction data,
including account tracking, suspicious activity detection, and statistical analysis.
"""

import logging
__author__ = "sandeep kaur"
__version__ = "1.0."

import logging


class DataProcessor:
    """
    Financial transaction data processing and analysis class.
    
    This class processes transaction records to:
    - Track account balances and transaction totals
    - Detect suspicious transactions
    - Generate transaction statistics
    - Calculate average transaction amounts
    """

    LARGE_TRANSACTION_THRESHOLD = 10000
    """
    Amount threshold above which transactions are flagged as suspicious.
    """

    UNCOMMON_CURRENCIES = ["XRP", "LTC"]
    """
    List of currency codes considered uncommon or high-risk.
    """

    def __init__(self, transactions: list,logging_level: str = "WARNING",
                 logging_format: str = "%(asctime)s - %(levelname)s - %(message)s",
                 log_file:str=""
                 ):
        """
        Initialize the processor with transaction data.
        
        Args:
            transactions: List of transaction dictionaries to process
            logging_level: The level of severity for logging (default: WARNING)
            logging_format: Format string for log messages (default: timestamp-level-message format)
            log_file: File path for log output (default: empty string for console output)
            """
        self.__transactions = transactions
        self.__account_summaries = {}
        self.__suspicious_transactions = []
        self.__transaction_statistics = {}


# Configure logging
        numeric_level = getattr(logging, logging_level.upper())
        if log_file:
            logging.basicConfig(filename=log_file, 
                              level=numeric_level,
                              format=logging_format)
        else:
            logging.basicConfig(level=numeric_level,
                              format=logging_format)

    @property
    def input_data(self) -> list:
        """
        Get the original transaction data.
        
        Returns:
            List of transaction dictionaries
        """
        return self.__transactions
    
    @property
    def account_summaries(self) -> dict:
        """
        Get the processed account summaries.
        
        Returns:
            Dictionary of account-level transaction summaries
        """
        return self.__account_summaries
    
    @property
    def suspicious_transactions(self) -> list:
        """
        Get flagged suspicious transactions.
        
        Returns:
            List of transactions that met suspicious criteria
        """
        return self.__suspicious_transactions
    
    @property
    def transaction_statistics(self) -> dict:
        """
        Get transaction type statistics.
        
        Returns:
            Dictionary of transaction statistics by type
        """
        return self.__transaction_statistics

    def process_data(self) -> dict:
        """
        Process all transactions and generate summary data.
        
        Performs complete data processing including:
        - Account summary updates
        - Suspicious transaction checks
        - Statistical calculations
        
        Returns:
            Dictionary containing all processed data results
        """
        for transaction in self.__transactions:
            self.update_account_summary(transaction)
            self.check_suspicious_transactions(transaction)
            self.update_transaction_statistics(transaction)

        return {
            "account_summaries": self.__account_summaries,
            "suspicious_transactions": self.__suspicious_transactions,
            "transaction_statistics": self.__transaction_statistics
        }

    def update_account_summary(self, transaction: dict) -> None:
        """
        Update account summary with new transaction.
        
        Updates account balance and transaction totals based on
        transaction type (deposit/withdrawal).
        
        Args:
            transaction: Dictionary containing transaction details
        """
        account_number = transaction["Account number"]
        transaction_type = transaction["Transaction type"]
        amount = float(transaction["Amount"])

        if account_number not in self.__account_summaries:
            self.__account_summaries[account_number] = {
                "account_number": account_number,
                "balance": 0,
                "total_deposits": 0,
                "total_withdrawals": 0
            }

        if transaction_type == "deposit":
            self.__account_summaries[account_number]["balance"] += amount
            self.__account_summaries[account_number]["total_deposits"] += amount
        elif transaction_type == "withdrawal":
            self.__account_summaries[account_number]["balance"] -= amount
            self.__account_summaries[account_number]["total_withdrawals"] += amount

    def check_suspicious_transactions(self, transaction: dict) -> None:
        """
        Check if transaction meets suspicious criteria.
        
        Flags transactions that:
        - Exceed LARGE_TRANSACTION_THRESHOLD
        - Use currencies in UNCOMMON_CURRENCIES
        
        Args:
            transaction: Dictionary containing transaction details
        """
        amount = float(transaction["Amount"])
        currency = transaction["Currency"]

        if amount > self.LARGE_TRANSACTION_THRESHOLD \
            or currency in self.UNCOMMON_CURRENCIES:
            self.__suspicious_transactions.append(transaction)

    def update_transaction_statistics(self, transaction: dict) -> None:
        """
        Update statistical totals for transaction type.
        
        Maintains running totals of:
        - Total amount by transaction type
        - Transaction count by type
        
        Args:
            transaction: Dictionary containing transaction details
        """
        transaction_type = transaction["Transaction type"]
        amount = float(transaction["Amount"])

        if transaction_type not in self.__transaction_statistics:
            self.__transaction_statistics[transaction_type] = {
                "total_amount": 0,
                "transaction_count": 0
            }

        self.__transaction_statistics[transaction_type]["total_amount"] += amount
        self.__transaction_statistics[transaction_type]["transaction_count"] += 1

    def get_average_transaction_amount(self, transaction_type: str) -> float:
        """
        Calculate average transaction amount for specified type.
        
        Args:
            transaction_type: Type of transaction to calculate average for
            
        Returns:
            Average amount per transaction, or 0 if no transactions exist
        """
        total_amount = self.__transaction_statistics[transaction_type]["total_amount"]
        transaction_count = self.__transaction_statistics[transaction_type]["transaction_count"]
    
        return 0 if transaction_count == 0 else total_amount / transaction_count