'''
Purpose: Allows user to interact with data with the command line

'''
import argparse
import sys
from ProductionCode.core import Features
from ProductionCode.data_handling import DataHandler

def main():
    ''''Arguments: none
    Return value: parser
    Purpose: Taking command line inputs to run functions in command_line
    '''
    core = Features()
    handler = DataHandler()

    handler.load_data('Data/dummy_data.csv')

    parser = argparse.ArgumentParser(
        epilog = (
            "Example Commands:\n"
            "python3 command_line.py --ratio Japan\n"
            "python3 command_line.py --year_co2 2004\n"
            "python3 command_line.py --biofuel Canada\n"
        ),
        usage = 'command_line [options]'
    )

    parser.add_argument('-a', '--average', type = str,
    help= 'Calculates avg co2 of a country')
    parser.add_argument('-r', '--ratio', type = str,
    help = 'Provides co2 and co2 per capita ratio')
    parser.add_argument('-y', '--year_co2', type = str,
    help = 'co2 emissions of all countries for a year')
    parser.add_argument('-b', '--biofuel', type = str,
    help = 'Finds the top biofuel consumption of a country')

    if len(sys.argv) == 1:
        print("Usage: python3 command_line.py [options]")
    else:
        args = parser.parse_args()
        if args.ratio:
            data1 = handler.set_data('Data/dummy_data.csv', args.ratio, 3)
            data2 = handler.set_data('Data/dummy_energy_data.csv', args.ratio, 3)
            print(core.ratio(data1, data2))

        elif args.average:
            final_data = handler.set_data('Data/dummy_data.csv', args.average, 2)
            print(core.average(final_data))

        elif args.biofuel:
            final_data = handler.set_data('Data/dummy_energy_data.csv', args.biofuel, 2)
            print(core.highest_biofuel(final_data))

if __name__ == "__main__":
    main()
