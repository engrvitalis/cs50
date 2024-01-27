"""
This program prompts the user for a vanity plate and then
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
    return valid_char_count(s) and valid_prefix(s) and valid_suffix(s)

def valid_prefix(s):
    #must start with at least two letters
    return s[:2].isalpha()

def valid_char_count(s):
    #may contain a maximum of 6 characters (letters or numbers)
    #and a minimum of 2 characters.
    return 2<=len(s)<=6

def valid_suffix(s):
    #Numbers cannot be used in the middle of a plate;
    #they must come at the end.
    #The first number used cannot be a ‘0’.”
    for c in s[2:]:
        if c.isalpha():
            continue
        else:
            if c.isdigit():
                # check if c is not 0 and remaining integers.
                try:
                    return c != "0" and int(s[s.index(c):])
                except:
                    return False
    return True

main()
