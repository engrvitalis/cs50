"""
This program prompts the user for input and then outputs that same input, 
replacing each space with ... (i.e., three periods).

"""

def main():
	inp = input("Enter a sentence: ")
	playback(inp)

def playback(sentence):
	print(sentence.replace(" ", "..."))

main()