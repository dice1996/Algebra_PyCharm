from datasource.dto.DrinksDto import DrinksDto
from utils.DBUtils import DBUtils


class DrinksService:
    def __init__(self, sqlConnection):
        self.sqlConnection = sqlConnection
        self.create_drinks_table()

    def create_drinks_table(self):
        query = f'''
            CREATE TABLE IF NOT EXISTS {DrinksDto.TABLE_NAME} (
                id integer PRIMARY KEY AUTOINCREMENT,
                name text,
                price float,
                drink_type text
);'''
        row_id = DBUtils.execute_query(self.sqlConnection, query)

    def add_drink_item(self, name, price, dt):
        query = f'''
                    INSERT INTO {DrinksDto.TABLE_NAME} (name, price, drink_type)
                    VALUES ("{name}", {price}, "{dt}");

                '''
        row_id = DBUtils.execute_query(self.sqlConnection, query)

    def fetch_drink_items(self):
        query = f'''
            SELECT * FROM {DrinksDto.TABLE_NAME};
        '''
        drinks = DBUtils.fetch_data(self.sqlConnection, query)
        drinks_list = []
        for item in drinks:
            drinks_item = DrinksDto.map_data_from_database(item)
            drinks_list.append(drinks_item)
        return drinks_list