import records

import ProductionCode.psql_config as config

class DataSource:

    def __init__ (self):
        connect = f"postgresql://{config.USER}:{config.PASSWORD}@localhost:5432/{config.DATABASE}"
        self.db = records.Database(connect)

    def get_country (self,data,country):
        result = self.db.query(f'SELECT * FROM {data} WHERE country = {country}')
        return result.export('csv')

    def get_year (self,data,year):
        result = self.db.query(f'SELECT * FROM {data} WHERE years = {year}')
        return result.export('csv')