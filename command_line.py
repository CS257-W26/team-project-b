'''
Purpose: Allows user to interact with data with the command line

'''
import argparse
import sys
from ProductionCode.core import Features

def parsing():
    ''''Arguments: none
    Return value: parser
    Purpose: Taking command line inputs to run functions in command_line
    '''
    parser = argparse.ArgumentParser(
        epilog = (
            "Example Commands:\n"
            "python3 command_line.py --ratio Japan\n"
            "python3 command_line.py --year_co2 2004\n"
            "python3 command_line.py --biofuel Canada\n"

        )
    )

    parser.add_argument('-a', '--average', type = str, help= 'Provides')
    parser.add_argument('-r', '--ratio', type = str, help = '')
    parser.add_argument('-y', '--year_co2', type = str, help = '')
    parser.add_argument('-b', '--biofuel', type = str, help = '' )

    return parser

def no_arg():
    no_arg_parser = parsing()

    args = parser.parse_args()

    if len(sys.argv) < 2:
        no_arg_parser.print_help()
        sys.exit(1)

    return args

# def main():
#     '''Arguments: none
#     Return value: none
#     Purpose: Takes command line inputs to run other functions in command_line
#     '''
#     args = sys.argv
#     core = Features()

#     if len(args) == 1:
#         print("Usage: python3 command_line.py [options]")
#     elif len(args) == 3:
#         if args[1] == 'ratio':
#             print (core.ratio(args[2]))
#         if args[1] == 'year_co2':
#             print (core.year_co2(args[2]))
#         if args[1] == 'biofuel':
#             print (core.highest_biofuel_consumption(args[2]))
#     return 'Invalid inputs'

if __name__ == "__main__":
    parsing()
