"""
This program implements a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

"""
def main():
    ans = input("What is the answer to the great question of life: ").lower()
    
    if ans == "42" or ans == "fourty-two" or ans == "forty two":
        print("Yes")
    else:
        print("No")
        
main()