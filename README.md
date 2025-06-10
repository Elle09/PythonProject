# PythonProject
May 2025 Code:You
Smart Personal Finance Analyzer - Project Checklist


I am aware that I did not complete this project as planned. I have had trouble balancing some life/work issues the past month. 
It's not an excuse but partially a reason. 
I did enjoy the learning materials from this class, and had a fun time applying what I've learned (and learning things a different way than I initially understood) and I am proud of what I did accomplish here.

I still plan to finish this project because I enjoyed it and want the UI working.

Thank you for allowing me to be a part of this class these past few months. Although it makes me sad, I understand I can no longer be apart of the class since I did not complete this project on time. 

Thank you to everyone who contributed their time for me and my peers to learn something new.



Task 1
X> Load Transactions from CSV 
X> Read financial_transactions.csv using csv.DictReader
X> Parse dates using datetime.strptime
X> Make amounts negative for "debit" transactions
X> Handle file not found and data format errors
X> Skip invalid rows and log to errors.txt
X> Print the number of successfully loaded transactions



Task 2

X> Function to add a new transaction with user input
X> Validate input: date format, transaction type, amount
X> Generate unique transaction_id (max ID + 1)
X> Append the new transaction to the list
X> Function to display transactions in a table
X> Use proper formatting for alignment
> Optional: Filter transactions by type
X> Optional: Format dates as "Month Day, Year"



Task 3

X> Function to update an existing transaction
X> Show transactions with numbers using enumerate
X> Let user select and edit a field
X> Validate changes (e.g., correct type, amount)
X> Function to delete a transaction
X> Confirm deletion before removing
> Optional: Update multiple fields in one go
X> Optional: Cancel option for update or delete



Task 4

X> Sum all credits, debits, and transfers
X> Calculate net balance (credits - debits)
> Group and sum by transaction type or customer ID
> Format numbers to two decimal places
X> Optional: Show customer with highest debit
> Optional: Show percentage of each type
> Optional: Analyze transactions for a specific year
X> Optional: Save analysis to analysis.txt



Task 5

X> Save updated transactions to financial_transactions.csv using csv.DictWriter
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

