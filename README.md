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

# Code Design Improvements

### Code Smells: Large Class and Long Parameter List 

Page changed: datasource.py

Lines changed: 14-21, 38-45, 61-68

Explanation of refactoring: The previous version of our datasource class was longer than necessary due to helper functions containing general SQL queries, which needed multiple parameters. By removing these helper functions, we removed methods with long parameter lists and shortened our datasource class to only include methods that are necessary.

### Code Smells: Naming Principles for Variables and Improvement of Function (idk change this)

Page changed: core.py

Lines changed: 13-26, 31, 39, 43-50, 85-101

Explanation of refactoring: Initially, variables names for our function arguments lacked appropriate description for what they were. We improved this by changing variables to names like "country" or "year" to provide more context. In addition, after changing our datasource.py, we were able to remove calculate_average function. This shortened our average function and significantly cut down on excessive lines of code in our ratio and biofuel functions, improving the overall readability of our code. 

# Front-End Design Improvements

### Improvement: Expanded Navigation Bar

Usability issue: In the initial front-end version of our website, the navigation bar only included links to the homepage and information page. As a result, users would have to return back to the homepage after navigating to one of the function pages in order to visit a page of a different function. For example, if a user visited the stats page and wanted to explore a different field, they would have to return to the homepage. This creates unnecessary navigation steps and makes exploring and satisficing through the site more difficult.

Page changed: templates/base.html

How we addressed this issue: We expanded the navigation bar to include links to all of our main function pages, a graph page, and a help page. This allows users to easily move between different features of the website without needing to return to the homepage, making the navigation more fluid and improving the operability of our website. The help page also offers added clarity on how to use the main function pages, supporting users who are scanning through and want to quickly understand the website's system.

## Improvement: Added Information and Improved Visual Hierarchy for Homepage

Usability issue: In the initial front-end version of our website, the homepage contained minimal background information on the purpose of the website and how to navigate the function pages. There were only two brief lines addressing the goal of the website and one vague instruction line that directed users to enter a value for one of the search boxes. There were also functions missing from the homepage, and in general, a weak visual hierarchy that made scanning difficult for users.

Page changed: templates/homepage.html, static/style.css

How we addressed this issue: We revised the styling of the homepage by adding labels in the HTML template, which created distinct sections to allow for separate styling. Additional background information was also included to inform the user about the website. This resulted in the general information about the site being formatted with larger text at the top of the page and the search boxes spread out at the bottom of the page.

the instructions emphasized by using a box-shadow, 
This allowed different sections to be styled seperately from one another,
