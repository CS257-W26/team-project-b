'''
Purpose: Allows user to interact with data with the command line
'''
import argparse
import sys
from ProductionCode.core import Features

core = Features()

def set_parser():
    ''''Arguments: none
    Return value: parser
    Purpose: Setting up the parser with arguments
    '''

    parser = argparse.ArgumentParser(
        epilog = (
            "Example Commands:\n"
            "python3 command_line.py --ratio Japan\n"
            "python3 command_line.py --year_co2 2004\n"
            "python3 command_line.py --biofuel Canada\n"
        ),
        usage = 'command_line [--help]'
    )

    parser.add_argument('-a', '--average', type = str,
    help= 'Calculates avg co2 of a country')
    parser.add_argument('-r', '--ratio', type = str,
    help = 'Provides co2 and co2 per capita ratio')
    parser.add_argument('-y', '--year_co2', type = str,
    help = 'co2 emissions of all countries for a year')
    parser.add_argument('-b', '--biofuel', type = str,
    help = 'Finds the top biofuel consumption of a country')

    return parser

def main():
    '''Arguments: None
    Purpose: Handles command line user input
    Return: None
    '''
    parser = set_parser()

    if len(sys.argv) == 1:
        print("Usage: python3 command_line.py [--help]")
    else:
        args = parser.parse_args()
        if args.ratio:
            print(core.ratio(args.ratio))

        elif args.average:
            print(core.average(args.average))

        elif args.biofuel:
            print(core.highest_biofuel(args.biofuel))

        elif args.year_co2:
            print(core.year_co2(args.year_co2))

if __name__ == "__main__":
    main()
