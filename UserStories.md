# User Stories:

# Feature 1
As a user interested in climate change, I can look up individual countries' top biofuel consumption information so that I can form a more comprehensive view of the world. 

Acceptance test: 
- test_command_line.py 
    - test_arg_biofuel checks that the user input of a country outputs the highest biofuel value. 
- test_core.py
    - test_highest_biofuel and test_biofuel_edge tests the core function highest_biofuel

# Feature 2
As a user interested in climate change, I can find the ratio of co2 per capita to energy consumption per capita of a country to know how much a country emits co2 compared to how much energy it uses on average.

Acceptance test: 
- test_command_line.py
    - test_arg_ratio checks if user input of a country outputs the correct ratio
    - test_arg_average checks if user input of a country outputs correct average co2 emissions
- test_core.py
    - test_ratio checks core function ratio
    - test_average checks core function average

# Feature 3
As a user interested in climate change, I want to compare CO2 emissions between each country in the dataset in a specific year so that I can learn more about how they compare to one another. 

Acceptance Test:
- test_command_line.py
    - test_arg_year_co2 checks that the user input of a year displays the correct countries and values
- test_core.py
    - test_year_co2 tests core function year_co2
