'''module records imported to work with Database'''
import records
import ProductionCode.psql_config as config

# ds = DataSource()

class DataSource:
    '''Purpose:Class that grabs info from table'''

    def __init__ (self):
        connect = f"postgresql://{config.USER}:{config.PASSWORD}@localhost:5432/{config.DATABASE}"
        self.db = records.Database(connect)

    def get_country_co2 (self, country):
        '''Arguments: self, country
        Purpose: Gets all the related data of a specific country from co2_data
        Return: A csv
        '''
        result = self.db.query(f"SELECT * FROM co2_data WHERE country = '{country}'")
        return result.export('csv')

    def get_country_energy (self, country):
        '''Arguments: self, country
        Purpose: Gets all the related data of a specific country from energy_data
        Return: A csv
        '''
        result = self.db.query(
            f"SELECT * FROM energy_data WHERE country = '{country}'"
        )
        return result.export('csv')

    def get_year_co2 (self, year):
        '''Arguments: self, year
        Purpose: Gets the data for a specific year from co2_data
        Return: A csv
        '''
        result = self.db.query(f"SELECT country, year, co2 FROM co2_data WHERE year = '{year}'")
        return result.export('csv')

    def get_year_energy (self, year):
        '''Arguments: self, year
        Purpose: Gets the data for a specific year from energy_data
        Return: A csv
        '''
        result = self.db.query(
            f"SELECT country, year, gas_electricity FROM energy_data WHERE year = '{year}'"
        )
        return result.export('csv')

    def get_biofuel (self, country):
        '''Arguments: self, country
        Purpose: Gets the biofuel_electricity data from energy_data for a specified country
        Return: A csv
        '''
        result = self.db.query(f"SELECT MAX(biofuel_electricity) FROM energy_data WHERE country = '{country}'")
        return result.export('csv')

    def get_average_co2_per_capita (self, country):
        '''Arguments: self, country
        Purpose: Gets the average co2_per_capita data from energy_data for a specified country
        Return: A csv
        '''
        result = self.db.query(f"SELECT AVG(co2_per_capita) FROM co2_data WHERE country = '{country}'")
        return result[0].export('csv')

    def get_average_energy_per_capita (self, country):
        '''Arguments: self, country
        Purpose: Gets the average energy_per_capita data from energy_data for a specified country
        Return: A csv
        '''
        result = self.db.query(f"SELECT AVG(energy_per_capita) FROM energy_data WHERE country = '{country}'")
        return result[0].export('csv')

    def get_average_co2 (self, country):
        '''Arguments: self, country
        Purpose: Gets the average co2 data from energy_data for a specified country
        Return: A csv
        '''
        result = self.db.query(f"SELECT AVG(co2) FROM co2_data WHERE country = '{country}'")
        return result[0].export('csv')

if __name__ == "__main__":
    ds = DataSource()
