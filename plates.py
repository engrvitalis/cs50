"""
program that prompts the user for a vanity plate and then 
output Valid if meets all of the requirements or Invalid if 
it does not. Assume that any letters in the user’s input 
will be uppercase. Structure your program per the below, 
wherein is_valid returns True if s meets all requirements 
and False if it does not. Assume that s will be a str. 
You’re welcome to implement additional functions for 
is_valid to call (e.g., one function per requirement).
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #No periods, spaces, or punctuation marks are allowed
    return valid_char_count(s) and valid_suffix(s)

def valid_char_count(s):
    #Number of characters must be between 2 and 6.
    print(len(s))
    return 2<=len(s)<=6

def valid_suffix(s):
    #Numbers must come at the end
    #The first number used cannot be a ‘0’
    for c in s[2:]:
        print(c.isdigit(), c != '0', s[s.index(c)], s[s.index(c):])
        if c.isdigit() and s[s.index(c):].isdigit():
             if c != '0':
                return True
        return False

main()