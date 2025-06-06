import csv
from datetime import datetime

transactions = []
errors = []
tx_info = ["transaction_id", "date", "customer_id", "amount", "type", "description"]


def load_transactions(filename="financial_transactions.csv"):

    with open("financial_transactions.csv", "r") as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [
            name.strip() for name in reader.fieldnames  # removes that blank space!
        ]  # .fieldnames notes!

        for row in reader:

            tx_id = row.get("transaction_id", "Unknown")
            missing_info = False

            for (
                info
            ) in tx_info:  # error handling for missing fields in transaction info
                if info not in row or not row[info].strip():
                    error_msg = f"Transaction (ID #{tx_id})information missing: 'info'"
                    print(
                        f"PROBLEM!! Transaction (ID #{tx_id}) skipped - transaction information missing: '{info}'"
                    )
                    errors.append({"transaction_id": tx_id, "error_message": error_msg})

                    missing_info = True
                    break

            if missing_info:
                continue

            try:

                transaction_id = int(
                    row["transaction_id"]
                )  # changing data type for transactions to int

                date_str = row["date"]
                date = datetime.strptime(
                    date_str, "%Y-%m-%d"
                ).date()  # correcting date format

                customer_id = int(
                    row["customer_id"]
                )  # changing data type from strin to int

                amount_str = row["amount"]
                amount = float(amount_str)  # change from string to float
                if row["type"] == "debit":
                    amount = -amount

                tx_type = row["type"]  # stays a string

                description = row["description"]  # stays a string

                transaction = {
                    "transaction_id": transaction_id,
                    "date": date,
                    "customer_id": customer_id,
                    "amount": amount,
                    "type": tx_type,
                    "description": description,
                }

                transactions.append(transaction)


            except ValueError as e:
                error_msg = f"ValueError: {e}"
                tx_id = row.get("transaction_id", "Unknown")
                print(
                    f"PROBLEM!! Transaction (ID #{tx_id}) skipped due to ValueError. Error message: {e}"
                )
                errors.append({"transaction_id": tx_id, "error_message": error_msg})

            except KeyError as e:
                error_msg = f"KeyError: {e}"
                tx_id = row.get("transaction_id", "Unknown")
                print(
                    f"PROBLEM!! Transaction (ID #{tx_id}) skipped due to KeyError. Error message: {e}"
                )
                errors.append({"transaction_id": tx_id, "error_message": error_msg})

            except FileNotFoundError as e:
                error_msg = f"FileNotFoundError: {e}"
                tx_id = row.get("transaction_id", "Unknown")
                print(
                    f"PROBLEM!! Transaction (ID #{tx_id}) skipped due to FileNotFoundError. Error message: {e}"
                )
                errors.append({"transaction_id": tx_id, "error_message": error_msg})


        with open("errors.csv", "w", newline="") as error_file:
            fieldnames = ["transaction_id", "error_message"]
            writer = csv.DictWriter(error_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(errors)

    # remember to keep this OUTSIDE of your loop!
    for tx in transactions[:50]:
        print(tx)


def add_transaction(transactions):

    try:

        date_str = input("Enter date (YYY-MM-DD): ")
        date = datetime.strptime(date_str, "%Y-%m-%d").date()

        customer_id = int(input("Enter customer ID: "))

        amount = float(input("Enter transaction amount: "))

        tx_type = input("Enter transaction type (credit/debit/transfer: ").lower() # .lower() removes case sensitivity in check 
        if tx_type not in [
            "credit",
            "debit",
            "transfer" 
        ]:

            print(
                "Invalid transaction type. Must be either credit, debit, or transfer."
            )
            return

        description = input("Enter transaction description: ")

        if transactions:
            transaction_id = max(tx["transaction_id"] for tx in transactions) + 1
        else:
            transaction_id = 1

        if tx_type == "debit":
            amount = -amount

        new_tx = {
            "transaction_id": transaction_id,
            "date": date,
            "customer_id": customer_id,
            "amount": amount,
            "type": tx_type,
            "description": description,
        }

        transactions.append(new_tx) # WHY ARE YOU WHITE UGH
        print("Transaction added!")

    except ValueError as e:
        print(f"Input error: {e}")


def view_transactions(transactions):
    print(f"{'ID':<4} | {'Date':<12} | {'Customer':<8} | {'Amount':<10} | {'Type':<8} | Description") # fixed nested quotes??
    print("-" * 75)

    for tx in transactions: 
        date_str = tx["date"].strftime("%b %d, %Y")
        amount_str = f"{tx['amount']:.2f}"

        print(f"{tx['transaction_id']:<4} | {date_str:<12} | {tx['customer_id']:<8} | {amount_str:<10} | {tx['type']:<8} | {tx['description']}")



def update_transaction(transactions):

    if len(transactions) == 0:
        print("No transactions to update")
        return
    
    count = 1
    for tx in transactions:
        print(str(count) + ". " + str(tx["transaction_id"]) + " | " + str(tx["date"]) + " | " + str(tx["customer_id"]) + " | " + str(tx["amount"]) + " | " + str(tx["type"]) + " | " + tx["description"])
        count +=1

    choice = input("Enter the number of the transaction you want to update (or type 'cancel' to quit): ")
    if choice.lower() == "cancel":
        print("Updates cancelled")
        return
    
    index = int(choice) - 1
    if index < 0 or index >= len(transactions):
        print("Update cancelled")
        return
    
    tx = transactions[index]
    print("What do you want to update? (date, customer_id, amount, type, description)")
    
    field = input("Field: ").lower()
    if field not in ["date", "customer_id", "amount", "type", "description"]:
        print("Invalid field")
        return

    new_value = input("Enter new value: ")

    if field == "date":
        tx["date"] = datetime.strptime(new_value, "%Y-%m-%d").date()
    
    elif field == "customer_id":
        tx["customer_id"] = int(new_value)
    
    elif field == "amount":
        amount = float(new_value)
        if tx["type"] == "debit":
            amount = -abs(amount)
        else:
            amount = abs(amount)
        tx["amount"] = amount
    
    elif field == "type":
        if new_value not in ["credit", "debit", "transfer"]:
            print("Invalid transaction type")
            return
        tx["type"] = new_value
    
    else:
        tx["description"] = new_value

    print("Transaction updated successfully!")



def delete_transaction(transactions):
    if len(transactions) == 0:
        print("No transaction to delete")
        return
    
    count = 1
    for tx in transactions:
        print(str(count) + ". " + str(tx["transaction_id"]) + " | " + str(tx["date"]) + " | " + str(tx["customer_id"]) + " | " + str(tx["amount"]) + " | " + str(tx["type"]) + " | " + tx["description"])
        count += 1

    choice = input("Enter the number of the transaction you want to delete (or type 'cancel' to quit): ")
    if choice.lower() == "cancel":
        print("Delete cancelled")
        return
    
    try:
        index = int(choice) - 1
        if index < 0 or index >= len(transactions):
            print("Invalid input, deletion cancelled")
            return 
    except ValueError:
        print("Invalid input, deletion cancelled")
        return


    tx = transactions[index]
    print("Your selection:")
    print(str(tx["transaction_id"]) + " | " + str(tx["date"]) + " | " + str(tx["customer_id"]) + " | " + str(tx["amount"]) + " | " + str(tx["type"]) + " | " + tx["description"])
    
    confirm = input("Are you sure you want to delete this transaction? once deleted it can no longer be retrieved. (yes/no): ").lower()
    if confirm == "yes":
        del transactions[index]
        print("Transaction deleted")
    else:
        print("Deletion cancelled")



    
def save_transactions(filename="financial_transactions.csv"):
    with open(filename, "w", newline="") as file:
        fieldnames = ["transaction_id", "date", "customer_id", "amount", "type", "description"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for tx in transactions:
            writer.writerow({
                "transaction_id": tx["transaction_id"],
                "date": tx["date"].strftime("%Y-%m-%d"),
                "customer_id": tx["customer_id"],
                "amount": f"{abs(tx['amount']):.2f}",
                "type": tx["type"],
                "description": tx["description"]
            })






























