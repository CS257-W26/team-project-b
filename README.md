# Command Line Arguments
python3 command_line.py --ratio "Japan"

python3 command_line.py --year_co2 "2004"

python3 command_line.py --biofuel "Canada"

# Flask App Routes
python3 flask_app.py

/average/Japan

/ratio/Canada

/year_co2/2004

/biofuel/Argentina

# Usage Statement

Usage: python3 command_line.py [--help]

# Dependecies

unittest: The module unittest was used for the construction of tests

sys: Sys module was used to allow access to command line arguments

io:  The module io was used to handle input/output streams

argparse: argparse module was used to create command lines 

flask: Flask framework was used to write and route web applications

# Extraneous Data 

The columns ISO and population were kept because we plan to use them when we integrate a map into our website. 
The columns country, year, co2, co2_per_capita, energy_per_capita, biofuel_electricity are currently being used in our features.
The column gas_electricity is being integrated as an additional year function because we were interested in pulling this column from our energy_data.

# Front-End Web Design
Scanning: Our wesite enables scanning by having a heading that shows where users can scan for keywords and main pages. Text is also kept brief, with most pages having only a few lines for the user to easily scan through and not be overwhelmed. Page layout also follows a visual hierarchy, with pages having more detailed information towards the bottom

Satisficing: Our website enables satisficing by having noticeable buttons [] that are easy to read and see would be helpful in guiding users while they are searching. 

Muddling Through: Our website enables muddling by having a bar with main pages stays at the top of each page, so users can easily go back to the most significant pages while traversing the website since they can expect where to find them.
