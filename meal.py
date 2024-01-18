"""
This program prompts users for a time and outputs whether it's breakfast time, lunch time or dinner time, else, it outputs nothing at all. 
"""

def main():
    #prompts the user for a time
    time = input("What time is it? ")
    if 7.00 <= convert(time) <= 8.00:
        print("Breakfast time")
    elif 12.00 <= convert(time) <= 13.00:
        print("Lunch time")
    elif 18.00 <= convert(time) <= 19.00:
        print("Dinner time")
    else:
        pass

def convert(time):
    '''
    converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).
    '''
    hour, minute = time.split(":")
    return float(hour) + (float(minute)/60)

if __name__ == "__main__":
    main()




