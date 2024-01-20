"""
This program prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, it outputs how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
"""

def main():
	amount_due = 50
	print(f'Amount Due: {amount_due}')

	while True:
		coin = int(input("Insert coin: "))
		amount_due = calculate(amount_due, coin)
		if amount_due > 0:
			print(f'Amount Due: {amount_due}')
		else:
			print(f'Change Owed: {abs(amount_due)}')
			break

def calculate(amount_due, coin):
	return amount_due - coin

main()