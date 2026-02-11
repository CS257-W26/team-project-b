'''
Purpose: Allows user to interact with data with the command line
'''
import argparse
import sys
from ProductionCode.core import Features
from ProductionCode.data_handling import DataHandler

co2_data = 'Data/owid-co2-data-trimmed.csv'
energy_data = 'Data/owid-energy-data-trimmed.csv'
wanted_columns = [8,9]
core = Features()
handler = DataHandler()

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
            data1 = handler.set_data(co2_data,args.ratio,wanted_columns[0],0)
            data2 = handler.set_data(energy_data,args.ratio,wanted_columns[1],0)
            print(core.ratio(data1, data2))

        elif args.average:
            final_data = handler.set_data(co2_data,args.average,wanted_columns[0],0)
            print(core.average(final_data))

        elif args.biofuel:
            final_data = handler.set_data(energy_data,args.biofuel,wanted_columns[1],0)
            print(core.highest_biofuel(final_data))

        elif args.year_co2:
            print(core.year_co2(args.year_co2,handler.load_data(co2_data),wanted_columns[0]))

if __name__ == "__main__":
    main()
