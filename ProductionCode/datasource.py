'''module records imported to work with Database'''
import records
import ProductionCode.psql_config as config

class DataSource:
    '''Purpose:Class that grabs info from table'''

    def __init__ (self):
        connect = f"postgresql://{config.USER}:{config.PASSWORD}@localhost:5432/{config.DATABASE}"
        self.db = records.Database(connect)

    def get_country (self,country):
        '''Arguments: self, data, country
        Purpose: Gets the data from a specific country
        Return: A csv
        '''
        result = self.db.query(f"SELECT * FROM co2_data WHERE country = '{country}'")
        return result.export('csv')

    def get_year (self,data,year):
        '''Arguments: self, data, year
        Purpose: Gets the data for a specific year
        Return: A csv
        '''
        result = self.db.query(f'SELECT country, year, co2 FROM {data} WHERE years = {year}')
        return result.export('csv')

if __name__ == "__main__":
    ds = DataSource()
    print(ds.get_country())