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



    # Generate a report with the expenses
    # generate_expense_report(expenses)  # Uncomment if you want to generate a report

    # Delete an expense

    # expense_manager.delete_expenses([3])

    # Print the list of expenses
    print("Expenses List:")
    for expense in expenses:
        print(f"ID: {expense['id']}, Amount: {expense['amount']}, "
              f"Category: {expense['category']}, Description: {expense['description']}, Date: {expense['date']}")
    # expense_manager.add_expense(200, 'Food', 'Dinner')
    # expense_manager.add_expense(250, 'Bills', 'Electricity')

if __name__ == "__main__":
    main()