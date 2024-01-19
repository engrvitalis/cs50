"""
This program prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. It assumes that the user’s input will indeed be in camel case.
"""

def main():
	n = input("camelCase: ")
	convert(n)

def convert(n):
	for e in n:
		if e.isupper():
			print(f'_{e.lower()}', end="")
		else:
			print(e, end="")

main()