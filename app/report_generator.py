import matplotlib.pyplot as plt

def generate_expense_report(expenses):
	categories = [expense['category'] for expense in expenses]
	amounts = [expense['amount'] for expense in expenses]

	plt.figure(figsize=(10, 6))
	plt.pie(amounts, labels=categories, autopct='%1.1f%%')
	plt.title('Expense Categories Breakdown')
	plt.show()