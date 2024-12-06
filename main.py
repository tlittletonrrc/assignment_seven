"""This module is the starting point for the financial data
 processing application. It handles the tasks of reading, 
 processing, and displaying financial transaction data, and it also has features to
 filter data based on specific account requirements.

Key Functions:
- Reads transaction data from CSV files
- Processes financial records for analysis
- Generates detailed reports and statistics
- Logs processing activities and important events
"""

__author__ = "Thomas Littleton, Karmjeet Kaur, Sandeep Kaur"
__version__ = "1.0."

from os import path
from input_handler.input_handler import InputHandler
from data_processor.data_processor import DataProcessor
from output_handler.output_handler import OutputHandler

def main() -> None:
    """Main function to read input data, process it, and write the 
    results to output files.

    - Reads input data from a CSV file using InputHandler.
    - Processes the data using DataProcessor.
    - Writes the processed data to CSV and JSON files using 
    OutputHandler.
    -  Filters account summaries based on specified criteria.
    - Exports filtered data to a separate CSV file.
    """

    # Retrieves the directory name of the current script or module file.
    current_directory = path.dirname(path.abspath(__file__))

    # Joins the current directory, the relative path to the input folder 
    # and the filename to create a complete path to the file.
    input_file_path = path.join(current_directory, "input/input_data.csv")

    input_handler = InputHandler(input_file_path)
    transactions = input_handler.read_input_data()

    # Create log file path
    log_file_path = path.join(current_directory, "output/fdp_team_1.log")  # Replace 1 with your team number

    # Initialize DataProcessor with logging configuration

    data_processor = DataProcessor(transactions,
    logging_level="INFO",
        logging_format="%(asctime)s - %(levelname)s - %(message)s",
        log_file=log_file_path
    )
    processed_data = data_processor.process_data()


    account_summaries = processed_data["account_summaries"]
    suspicious_transactions = processed_data["suspicious_transactions"]
    transaction_statistics = processed_data["transaction_statistics"]
    output_handler = OutputHandler(account_summaries, 
                                   suspicious_transactions, 
                                   transaction_statistics)

    # Joins the current directory, the relative path to the output 
    # folder and the filename to create a complete path to each of the 
    # output files.
    file_prefix = "output_data"
    filenames = [
        "account_summaries", 
        "suspicious_transactions", 
        "transaction_statistics"
    ]

    file_path = {}

    for filename in filenames:
        file_path[filename] = path.join(current_directory,
                                        f"output/{file_prefix}_{filename}.csv")

    output_handler.write_account_summaries_to_csv(file_path["account_summaries"])
    output_handler.write_suspicious_transactions_to_csv(file_path["suspicious_transactions"])
    output_handler.write_transaction_statistics_to_csv(file_path["transaction_statistics"])

# Add filtering functionality here
    filtered_filename = "fdp_filter_team_1.csv"  # Replace 1 with your team number
    file_path["filtered_accounts"] = path.join(current_directory,
                                             f"output/{filtered_filename}")

    # Apply filtering to identify high-value accounts (balance >= 5000)
    filtered_accounts = output_handler.filter_account_summaries("balance", 5000, True)

    # Write filtered results to CSV
    output_handler.write_filtered_summaries_to_csv(
        filtered_accounts, 
        file_path["filtered_accounts"]
    )

if __name__ == "__main__":
    main()
