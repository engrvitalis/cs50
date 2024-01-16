"""
This project implements a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z.

x is an integer
y is +, -, *, or /
z is an integer

"""

def main():
	inp = input("Expression: ")
	operator = inp[inp.find(" ")+1]

	match operator:
		case "+":
			print(float(inp[:inp.find(" ")]) + float(inp[inp.find(" ")+3:]))
		case "-":
			print(float(inp[:inp.find(" ")]) - float(inp[inp.find(" ")+3:]))
		case "*":
			print(float(inp[:inp.find(" ")]) * float(inp[inp.find(" ")+3:]))
		case "/":
			print(float(inp[:inp.find(" ")]) / float(inp[inp.find(" ")+3:]))
		case _:
			print("Wrong input")

main()