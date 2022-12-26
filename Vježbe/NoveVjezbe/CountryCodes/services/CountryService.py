from datasource.dto.Country import CountryDto
from utils.DBUtils import DBUtils
import sqlite3

DB_NAME = "country.db"

class CountryService():

    table_name = 'country'

    def __init__(self):
        self.sqlConnection = sqlite3.connect(DB_NAME)
        self.create_table()


    def create_table(self):
        query = f'''
            CREATE TABLE IF NOT EXISTS `{self.table_name}` (
            `id` INTEGER NOT NULL,
            `name` TEXT NOT NULL,
            `mcc` INTEGER NOT NULL unique,
            europe INTEGER NOT NULL,
            PRIMARY KEY (`id`)
            );
        '''
        DBUtils.db_execute(self.sqlConnection, query)

    def insert_data(self, data: CountryDto):
        query = f'''
        INSERT INTO `{self.table_name}` (name, mcc, europe)
        VALUES ("{data.name}", {data.mcc}, {data.europe});
        '''
        DBUtils.db_execute(self.sqlConnection, query)

    def fetch_by_mcc(self, mcc):
        query = f'''
            SELECT * FROM `{self.table_name}` WHERE mcc = {mcc};'''

        result = DBUtils.db_fetch(self.sqlConnection, query, True)
        try:
            country = CountryDto.map_data_from_database(result)
            return country
        except Exception as e:
            print(e)
            return None

    def prefill_database(self):
        self.insert_data(CountryDto().create_country("Croatia", 385, 1))
        self.insert_data(CountryDto().create_country("Albania", 276, 1))
        self.insert_data(CountryDto().create_country("Argentina", 722, 0))
        self.insert_data(CountryDto().create_country("Brazil", 724, 0))
        self.insert_data(CountryDto().create_country("Canada", 302, 0))
        self.insert_data(CountryDto().create_country("Germany", 262, 1))
        self.insert_data(CountryDto().create_country("Hungary", 216, 1))
        self.insert_data(CountryDto().create_country("United States of America", 311, 0))
        self.insert_data(CountryDto().create_country("United Kingdom", 234, 1))

    def fetch_all(self):
        query = f'''
            SELECT * FROM `{self.table_name}`;'''
        lista = []
        result = DBUtils.db_fetch(self.sqlConnection, query)
        try:
            for item in result:
                country = CountryDto.map_data_from_database(item)
                lista.append(country)
            return lista
        except Exception as e:
            print(e)
            return None

    def update_country(self, id, name, mcc, is_Europe):
        query = f'''
        UPDATE `{self.table_name}`
        SET `name` = '{name}',
        `mcc` = {mcc},
        `europe` = {is_Europe}
        WHERE id = {id};'''

        DBUtils.db_execute(self.sqlConnection, query)

    def delete_country(self, id):
        query = f'''
        DELETE FROM `{self.table_name}`
        WHERE id = {id};'''

        DBUtils.db_execute(self.sqlConnection, query)