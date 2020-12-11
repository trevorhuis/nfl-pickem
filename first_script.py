def collect_input():
	x = input("Input: ")
	return x


def income_input(incomes):
	print("Please enter an income or 'next' to move to expenses")
	user_input = collect_input()
	while user_input != "next":
		incomes.append(int(user_input))
		user_input = collect_input()
	return incomes


def expenses_input(expenses):
	print("Please enter an expense or 'next' to move to summary")
	user_input = collect_input()
	while user_input != "next":
		expenses.append(int(user_input))
		user_input = collect_input()
	return expenses
	
def result(dif):
	if dif > 0:
		return "You are " + str(dif) + " in the black."
	else:
		return "You are " + str(dif) + "in the red."


def main():
	expenses = []
	incomes = []

	print("This is a program to calculate your budget!")
	income_total = sum(income_input(incomes))
	expenses_total = sum(expenses_input(expenses))
	print("Your income is:  %s" % (income_total))
	print("Your expenses are:  %s" % (expenses_total))
	print(result( income_total - expenses_total ))


main()

