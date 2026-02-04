# User Stories:

As a user interested in climate change, I can look up individual countries' top biofuel consumption information so that I can form a more comprehensive view of the world. The acceptance test can be found in the Tests folder, where the test_command_line.py checks that the user input of a country outputs the highest biofuel value, and the function for highest_biofuel is checked in test_core.py.

As a user interested in climate change, I can find the ratio of co2 per capita to energy consumption per capita of a country to know how much a country emits co2 compared to how much energy it uses on average. The acceptance test can be found in the Tests folder, where test_command_line.py checks that the user input of a country outputs a float average, and the function for ratio is checked in test_core.py

As a user interested in climate change, I want to compare CO2 emissions between each country in the dataset in a specific year so that I can learn more about how they compare to one another. The acceptance test can be found in the Tests folder, where test_command_line.py checks that the user input of a year displays the correct countries and values, and the function for year_co2 is checked in test.core.py.
