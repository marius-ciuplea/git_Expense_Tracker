import unittest
from unittest.mock import MagicMock
from app.expense_manager import ExpenseManager


class TestExpenseManager(unittest.TestCase):

	def setUp(self):
		# Mock the database connection
		self.mock_db = MagicMock()
		self.mock_cursor = MagicMock()  # Create a separate mock for the cursor
		self.mock_db.cursor.return_value = self.mock_cursor  # Make sure cursor() returns our mock cursor
		self.expense_manager = ExpenseManager(self.mock_db)

	def test_add_expense(self): # Checks that the correct SQL query and parameters are used when adding an expense.
		# Test adding an expense
		amount = 50.0
		category = 'Food'
		description = 'Lunch'

		# Mock the cursor's execute method
		self.mock_cursor.execute = MagicMock()  # Mock execute method on the cursor

		# Call the add_expense method
		self.expense_manager.add_expense(amount, category, description)

		# Normalize expected query to remove extra whitespace and newlines
		expected_query = 'INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)'
		actual_query = self.mock_cursor.execute.call_args[0][0].strip()

		# Normalize the parameter tuple as well
		expected_params = (amount, category, description, '2025-02-12')
		actual_params = self.mock_cursor.execute.call_args[0][1]

		# Assert that the query and parameters are correct
		self.assertEqual(expected_query, actual_query)
		self.assertEqual(expected_params, actual_params)

		# Check if commit was called to save the changes
		self.mock_db.commit.assert_called_once()

	def test_get_expenses(self): # Checks that the expenses are retrieved correctly from the mocked database.
		# Test getting all expenses
		expense_data = [
			(1, 50.0, 'Food', 'Lunch', '2025-02-12'),
			(2, 100.0, 'Transport', 'Bus ticket', '2025-02-12'),
		]

		# Mock the cursor to return the expense_data
		self.mock_cursor.fetchall.return_value = expense_data

		# Call the get_expenses method
		expenses = self.expense_manager.get_expenses()

		# Verify that the get_expenses method returns the correct list of expenses
		self.assertEqual(len(expenses), 2)
		self.assertEqual(expenses[0]['amount'], 50.0)
		self.assertEqual(expenses[1]['category'], 'Transport')
		self.assertEqual(expenses[1]['description'], 'Bus ticket')

	def test_get_expenses_empty(self): # Checks the case when no expenses are available.
		# Test getting expenses when there are none in the database
		self.mock_cursor.fetchall.return_value = []

		# Call the get_expenses method
		expenses = self.expense_manager.get_expenses()

		# Verify that the expenses list is empty
		self.assertEqual(expenses, [])


if __name__ == '__main__':
	unittest.main()

# Mocks help you test the behavior of your code without
# needing to interact with external systems, making tests
# faster, more reliable, and easier to set up