"""
This program prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. It assumes that the user’s input will indeed be in camel case.
"""

def main():
	n = input("camelCase: ")
	print(convert(n))

def convert(n):
	l = list()
	for e in n:
		if e.isupper():
			l.append("_")
			l.append(e.lower())
		else:
			l.append(e)
			
	return "".join(l)

main()