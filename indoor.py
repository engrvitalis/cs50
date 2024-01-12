"""
Project title:	Indoor
Description:	This program prompts the user for input and then outputs that same input
in lowercase with punctuation and whitespace outputted unchanged.
Programmer:	Nnamdi Vitalis Ewuzie
Date:		12/02/2024.

"""

def main():
	inp = input("Enter your sentence: ")
	print(indoor(inp))

def indoor(sentence):
    return sentence.lower()

main()
