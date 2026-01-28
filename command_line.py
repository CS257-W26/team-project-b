'''
Purpose: Allows user to interact with data with the command line

'''
import csv
import sys

def main():
    '''Arguments: none
    Return value: none
    Purpose: Takes command line inputs to run other functions in command_line
    '''
    args = sys.argv

    if len(args) == 1:
        print("Usage: python3 command_line.py [options]")
    elif len(args) == 3:
        if args[1] == 'ratio':
            print (ratio(args[2]))
        if args[1] == 'year_co2':
            print (year_co2(args[2]))
        if args[1] == 'biofuel':
            print (highest_biofuel_consumption(args[2]))
    return 'Invalid inputs'

if __name__ == "__main__":
    main()
