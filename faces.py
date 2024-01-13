"""
Description: This function accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text returned unchanged.

Programmer: Nnamdi Vitalis Ewuzie

"""


def main():
    inp = input("Enter a string: ")
    print(convert(inp))

def convert(string):
    string = string.replace(":)", "🙂")
    string = string.replace(":(", "🙁")
    return string
    
main()
