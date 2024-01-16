"""
This project implements a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

"""

def main():
    inp = input("Hello, enter your greeting: ").strip().lower()
    
    if inp.startswith("hello"):
        print(f"${0}")
    elif inp.startswith("h"):
        print(f"${20}")
    else:
        print(f"${100}")
    
main()