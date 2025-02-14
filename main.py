from app.database import create_table, connect_db
from app.expense_manager import ExpenseManager
from app.report_generator import generate_expense_report

def main():
    # Ensure the database table is created (if not already)
    create_table()

    # Establish connection to the database and create an ExpenseManager instance
    expense_manager = ExpenseManager(connect_db())

    # Get all expenses using the ExpenseManager's get_expenses method
    expenses = expense_manager.get_expenses()

    # Add expenses
    # expense_manager.add_expense(200, 'Food', 'Dinner')
    # expense_manager.add_expense(250, 'Bills', 'Electricity')


    # Update the amount and category
    #expense_manager.update_expense(6, amount=150, category="Food")

    # Update only the description
    # expense_manager.update_expense(6, description="Breakfast")

    # Try updating without passing any parameters (should warn the user)
    # expense_manager.update_expense(6)


    # Delete an expense
    # expense_manager.delete_expenses([3])

    # Generate a report with the expenses
    # generate_expense_report(expenses)  # Uncomment if you want to generate a report

    # Print the list of expenses
    print("Expenses List:")
    for expense in expenses:
        print(f"ID: {expense['id']}, Amount: {expense['amount']}, "
              f"Category: {expense['category']}, Description: {expense['description']}, Date: {expense['date']}")


if __name__ == "__main__":
    main()