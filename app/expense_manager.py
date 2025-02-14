import sqlite3
from datetime import datetime

class ExpenseManager:
	def __init__(self, database):
		# Initialize with a connection to the database
		self.database = database

	def add_expense(self, amount, category, description):

		# Get current date and time for the expense entry
		date = datetime.now().strftime('%Y-%m-%d')

		query = '''INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)'''

	# Execute the query with the provided data
		cursor = self.database.cursor()
		try:
			cursor.execute(query, (amount, category, description, date))
			self.database.commit() # Save the changes to the database
		finally:
			cursor.close() # Close the cursor after the query is executed

	def get_expenses(self):
		"""Retrieve all expenses from the database"""
		query = '''SELECT id, amount, category, description, date FROM expenses'''

		cursor =self.database.cursor()

		try:
			cursor.execute(query)
			expenses = cursor.fetchall() # Fetch all rows from the result

			# Return the expenses as a list of dictionaries for easier handling
			expense_list = []
			for expense in expenses:
				expense_list.append({
					'id':expense[0],
					'amount': expense[1],
					'category': expense[2],
					'description': expense[3],
					'date': expense[4]
				})
			return expense_list
		finally:
			cursor.close()  # Ensure the cursor is closed after the operation

	def update_expense(self, expense_id, amount=None, category=None, description=None):
		"""Update an existing expense entry in the database"""

		# Ensure at least one field is being updated
		if amount is None and category is None and description is None:
			print("⚠️ No updates provided.")
			return False

		# Build the query dynamically
		updates = []
		values = []

		if amount is not None:
			updates.append("amount = ?")
			values.append(amount)
		if category is not None:
			updates.append("category = ?")
			values.append(category)
		if description is not None:
			updates.append("description = ?")
			values.append(description)

		values.append(expense_id)  # ID goes at the end

		query = f"UPDATE expenses SET {', '.join(updates)} WHERE id = ?"

		cursor = self.database.cursor()
		try:
			cursor.execute(query, tuple(values))
			self.database.commit()
			print(f"✅ Expense with ID {expense_id} updated successfully.")
			return cursor.rowcount > 0
		except Exception as e:
			print(f"⚠️ Error updating expense: {e}")
			return False
		finally:
			cursor.close()

	def delete_expenses(self, expense_ids):
		if not expense_ids:
			print("⚠️ No expense IDs provided for deletion.")
			return False

		query = f"DELETE FROM expenses WHERE id IN ({', '.join(['?'] * len(expense_ids))})"
		print(f"Generated SQL Query: {query}")  # 🔍 Debugging line

		cursor = self.database.cursor()
		try:
			cursor.execute(query, tuple(expense_ids))
			self.database.commit()
			print(f"🛠️ Deleted {cursor.rowcount} expenses.")
			return cursor.rowcount > 0
		except Exception as e:
			print(f"⚠️ Error deleting expenses: {e}")
			return False
		finally:
			cursor.close()
