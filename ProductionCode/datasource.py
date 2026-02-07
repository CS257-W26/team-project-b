import records

import ProductionCode.psql_config as config

class DataSource:

    def __init__ (self):
        connect = f"postgresql://{config.USER}:{config.PASSWORD}@localhost:5432/{config.DATABASE}"
        self.db = records.Database(connect)

    def 