'''
Purpose: Allows user to interact with data with the command line

'''
import argparse
import sys
from ProductionCode.core import Features
from ProductionCode.data_handling import Data_Handler

def set_parser():
    ''''Arguments: none
    Return value: parser
    Purpose: Taking command line inputs to run functions in command_line
    '''
    core = Features()
    handler = Data_Handler()

    handler.load_data('Data/dummy_data.csv')

    parser = argparse.ArgumentParser(
        epilog = (
            "Example Commands:\n"
            "python3 command_line.py --ratio Japan\n"
            "python3 command_line.py --year_co2 2004\n"
            "python3 command_line.py --biofuel Canada\n"

        ) , 
        usage = 'command_line [options]'
    )

    parser.add_argument('-a', '--average', type = str, help= 'Provides')
    parser.add_argument('-r', '--ratio', type = str, help = '')
    parser.add_argument('-y', '--year_co2', type = str, help = '')
    parser.add_argument('-b', '--biofuel', type = str, help = '' )

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
    else:
        args = parser.parse_args()
        if args.ratio:
            final_data = handler.set_data('Data/dummy_data.csv', args.ratio)
            print(core.ratio(final_data))

        elif args.average:
            final_data = handler.set_data('Data/dummy_data.csv', args.average)
            print(core.average(final_data))

        elif args.biofuel:
            final_data = handler.set_data('Data/dummy_energy_data.csv', args.biofuel)
            print(core.highest_biofuel(final_data))

if __name__ == "__main__":
    set_parser()

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
