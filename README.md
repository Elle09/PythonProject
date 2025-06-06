# PythonProject
May 2025 Code:You
Smart Personal Finance Analyzer - Project Checklist



Task 1
> Load Transactions from CSV
> Read financial_transactions.csv using csv.DictReader
> Parse dates using datetime.strptime
> Make amounts negative for "debit" transactions
> Handle file not found and data format errors
> Skip invalid rows and log to errors.txt
> Print the number of successfully loaded transactions



Task 2

> Function to add a new transaction with user input
> Validate input: date format, transaction type, amount
> Generate unique transaction_id (max ID + 1)
> Append the new transaction to the list
> Function to display transactions in a table
> Use proper formatting for alignment
> Optional: Filter transactions by type
> Optional: Format dates as "Month Day, Year"



Task 3

> Function to update an existing transaction
> Show transactions with numbers using enumerate
> Let user select and edit a field
> Validate changes (e.g., correct type, amount)
> Function to delete a transaction
> Confirm deletion before removing
> Optional: Update multiple fields in one go
> Optional: Cancel option for update or delete



Task 4

> Sum all credits, debits, and transfers
> Calculate net balance (credits - debits)
> Group and sum by transaction type or customer ID
> Format numbers to two decimal places
> Optional: Show customer with highest debit
> Optional: Show percentage of each type
> Optional: Analyze transactions for a specific year
> Optional: Save analysis to analysis.txt



Task 5

> Save updated transactions to financial_transactions.csv using csv.DictWriter
> Convert date objects to string before writing
> Generate a financial summary report in report.txt
> Optional: Add timestamp to the report filename
> Optional: Back up the original CSV before saving
> Optional: Include transaction date range in the report
> Handle file writing errors gracefully
> Main Program Integration
> Create a main menu loop with options (1–9)
> Load transactions before allowing other operations
> Organize code into separate functions and a module (e.g., finance_utils.py)
> Test each function individually
> Ensure user-friendly prompts and error messages



Deliverables

> Python script or Jupyter notebook
> Sample financial_transactions.csv with 20+ records
> Output files: updated CSV and report.txt
> README file with setup and usage instructions

