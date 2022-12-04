from datasource.dto.FoodDto import FoodDto
from utils.DBUtils import DBUtils


class FoodService:
    def __init__(self, sqlConnection):
        self.sqlConnection = sqlConnection
        self.create_food_table()

    def create_food_table(self):
        query = f'''
            CREATE TABLE IF NOT EXISTS {FoodDto.TABLE_NAME} (
	            id integer PRIMARY KEY AUTOINCREMENT,
                name text,
                price float
);'''
        row_id = DBUtils.execute_query(self.sqlConnection, query)

    def add_food_item(self, name, price):
        query = f'''
            INSERT INTO {FoodDto.TABLE_NAME} (name, price)
            VALUES ("{name}", {price});
        
        '''
        row_id = DBUtils.execute_query(self.sqlConnection, query)

    def fetch_food_items(self):
        query = f'''
            SELECT * FROM {FoodDto.TABLE_NAME};
        '''
        food = DBUtils.fetch_data(self.sqlConnection, query)
        food_list = []
        for item in food:
            food_item = FoodDto.map_data_from_database(item)
            food_list.append(food_item)
        return food_list
