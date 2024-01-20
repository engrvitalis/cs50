"""
This program prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""

def main():
	x = input("Input: ")
	remove_vowel(x)

def remove_vowel(n):
	for c in n:
		if c in ['a', 'e', 'i', 'o', 'u']:
			continue
		else:
			print(c, end="")

main()