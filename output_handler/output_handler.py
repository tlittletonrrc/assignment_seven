"""OutputHndeler Module 
This module manages the writting of processed financial data to CSV files.
It handles account summaries, suspicious transactions, and transaction statistic.
"""

__author__ = "Karmjeet Kaur"
__version__ = "1.0"

import csv

class OutputHandler:
    """A class responsible for writting of processed financial data to CSV files.
    This class handles three main types of output:
    Account summaries 
    Suspicious transactions 
    Transaction statistics 

    """

    def __init__(self, account_summaries: dict, 
                       suspicious_transactions: list, 
                       transaction_statistics: dict):
        """Initialize  the OutputHandler with processed financial data.
        Args:
           account_summaries: Dictionary of account financial summaries
           suspicious_trnsactions: List of flagged transactions
           transaction_statistics: Dictionary of transaction type statistics
        """
        self.__account_summaries = account_summaries
        self.__suspicious_transactions = suspicious_transactions
        self.__transaction_statistics = transaction_statistics
    
    @property
    def account_summaries(self) -> dict:
        """Get the account summaries dictionary.
        Returns:
            Dictionary containing account level financial summaries
        """
        return self.__account_summaries
    
    @property
    def suspicious_transactions(self) -> list:
        """Get the suspacious transaction list.
        Returns:
            List of transactions flagged for review
        """
        return self.__suspicious_transactions
    
    @property
    def transaction_statistics(self) -> dict:
        """Get the transaction statistics dictionary.
        Returns:
            Dictionary containing transaction type statistics
        """
        return self.__transaction_statistics

    def write_account_summaries_to_csv(self, file_path: str) -> None:
        """Write account summaries to a CSV file.
         Creates a CSV with columns:
        - Account number
        - Balance
        - Total Deposits
        - Total Withdrawals

        Args:
            file_path: Location where CSV file will be created

        """
        with open(file_path, "w", newline="") as output_file:
            writer = csv.writer(output_file)
            writer.writerow([
                "Account number", 
                "Balance", 
                "Total Deposits", 
                "Total Withdrawals"
            ])

            for account_number, summary in self.__account_summaries.items():
                writer.writerow([
                    account_number,
                    summary["balance"],
                    summary["total_deposits"],
                    summary["total_withdrawals"]
                ])

    def write_suspicious_transactions_to_csv(self, file_path: str) -> None:
        """Write suspicious transactions to a CSV file.

        Creates a CSV with columns:
        - Transaction ID
        - Account number
        - Date
        - Transaction type
        - Amount
        - Currency
        - Description

        Args:
            file_path: Location where CSV file will be created
        """
        with open(file_path, "w", newline="") as output_file:
            writer = csv.writer(output_file)
            writer.writerow([
                "Transaction ID", 
                "Account number", 
                "Date", 
                "Transaction type", 
                "Amount", 
                "Currency", 
                "Description"
            ])

            for transaction in self.__suspicious_transactions:
                writer.writerow([
                    transaction["Transaction ID"],
                    transaction["Account number"],
                    transaction["Date"],
                    transaction["Transaction type"],
                    transaction["Amount"],
                    transaction["Currency"],
                    transaction["Description"]
                ])

    def write_transaction_statistics_to_csv(self, file_path: str) -> None:
        """ Write transaction statistics to a CSV file.

        Creates a CSV with columns:
        - Transaction type
        - Total amount
        - Transaction count

        Args:
            file_path: Location where CSV file will be created
        """        
        with open(file_path, "w", newline="") as output_file:
            writer = csv.writer(output_file)
            writer.writerow([
                "Transaction type", 
                "Total amount", 
                "Transaction count"
            ])

            for transaction_type, statistic in self.__transaction_statistics.items():
                writer.writerow([
                    transaction_type,
                    statistic["total_amount"],
                    statistic["transaction_count"]
                ])

    def filter_account_summaries(self, filter_field: str, filter_value: int, filter_mode: bool) -> list:
        """Filter account summaries based on specified criteria.
        
        Args:
            filter_field: Field to filter on ('balance', 'total_deposits', or 'total_withdrawals')
            filter_value: Value to compare against
            filter_mode: True for >= comparison, False for <= comparison
        
        Returns:
            List of filtered account summaries
        """
        filtered_data = []
        
        for account_number, summary in self.__account_summaries.items():
            field_value = summary[filter_field]
            
            if filter_mode and field_value >= filter_value:
                filtered_summary = summary.copy()
                filtered_summary['account_number'] = account_number
                filtered_data.append(filtered_summary)
            elif not filter_mode and field_value <= filter_value:
                filtered_summary = summary.copy()
                filtered_summary['account_number'] = account_number
                filtered_data.append(filtered_summary)
                
        return filtered_data

    def write_filtered_summaries_to_csv(self, filtered_data: list, file_path: str) -> None:
        """Write filtered account summaries to a CSV file.
        
        Args:
            filtered_data: List of filtered account summaries
            file_path: Location where CSV file will be created
        """
        with open(file_path, "w", newline="") as output_file:
            writer = csv.writer(output_file)
            writer.writerow([
                "Account number",
                "Balance",
                "Total Deposits",
                "Total Withdrawals"
            ])
            
            for summary in filtered_data:
                writer.writerow([
                    summary["account_number"],
                    summary["balance"],
                    summary["total_deposits"],
                    summary["total_withdrawals"]
                ])