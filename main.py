# Expense Tracker Application

expenses = []

while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Expense
    if choice == "1":

        expense_name = input("Enter Expense Name: ")
        expense_amount = float(input("Enter Expense Amount: "))

        expense = {
            "name": expense_name,
            "amount": expense_amount
        }

        expenses.append(expense)

        print("✅ Expense Added Successfully")

    # View Expenses
    elif choice == "2":

        if len(expenses) == 0:
            print("No Expenses Found")

        else:
            print("\nExpense Records")

            for expense in expenses:

                print(
                    f"Expense: {expense['name']} | "
                    f"Amount: ₹{expense['amount']}"
                )

    # View Total Expense
    elif choice == "3":

        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"\n💰 Total Expense: ₹{total}")

    # Exit
    elif choice == "4":

        print("Thank You")
        break

    else:
        print("❌ Invalid Choice")