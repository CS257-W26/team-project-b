'''module records imported to work with Database'''
import records
import ProductionCode.psql_config as config

class DataSource:
    '''Purpose:Class that grabs info from table'''

    def __init__ (self):
        connect = f"postgresql://{config.USER}:{config.PASSWORD}@localhost:5432/{config.DATABASE}"
        self.db = records.Database(connect)

    def get_country (self,data,country):
        '''Arguments: self, data, country
        Purpose: Helper function for get_country_co2 and get_country_energy 
        to get the data for a specific year
        Return: A csv
        '''
        result = self.db.query(f"SELECT * FROM {data} WHERE country = '{country}'")
        return result.export('csv')

    def get_country_co2 (self,country):
        '''Arguments: self, country
        Purpose: Gets the data from a specific country from co2_data
        Return: A csv
        '''
        return self.get_country('co2_data', country)
    
    def get_country_energy (self,country):
        '''Arguments: self, country
        Purpose: Gets the data from a specific country from energy_data
        Return: A csv
        '''
        return self.get_country('energy_data', country)

    def get_year (self,data,year):
        '''Arguments: self, data, year
        Purpose: Helper function for get_year_co2 and get_year_energy 
        to get the data for a specific year
        Return: A csv
        '''
        result = self.db.query(f'SELECT country, year, co2 FROM {data} WHERE years = {year}')
        return result.export('csv')

    def get_year_co2 (self, year):
        '''Arguments: self, year
        Purpose: Gets the data for a specific year from co2_data
        Return: A csv
        '''
        return ('co2_data',year)
    
    def get_year_energy (self, year):
        '''Arguments: self, year
        Purpose: Gets the data for a specific year from energy_data
        Return: A csv
        '''
        return ('energy_data',year)
    
    def get_value (self,data,col,country):
        '''Arguments: self, country
        Purpose: Helper function for other functions that get specific values
        from a specified dataset
        Return: A csv
        '''
        result = self.db.query(f'SELECT {col} FROM {data} WHERE country = {country}')
        return result.export('csv')

    def get_biofuel (self, country):
        '''Arguments: self, country
        Purpose: Gets the biofuel_consumption data from energy_data for a specified country
        Return: A csv
        '''
        return self.get_value('energy_data', 'biofuel_consumption', country)

    def get_co2_per_capita (self, country):
        '''Arguments: self, country
        Purpose: Gets the co2_per_capita data from co2_data for a specified country
        Return: A csv
        '''
        return self.get_value('co2_data','co2_per_capita',country)
    
    def get_energy_per_capita (self, country):
        '''Arguments: self, year
        Purpose: Gets the energy_per_capita data from energy_data for a specified country
        Return: A csv
        '''
        return self.get_value('energy_data','energy_per_capita',country)

if __name__ == "__main__":
    ds = DataSource()
    print(ds.get_country())