import time

from datasource.dto.TablesDto import TablesDto
from utils.DBUtils import DBUtils
import random


class TablesService:
    def __init__(self, sqlConnection):
        self.sqlConnection = sqlConnection
        self.create_table_of_tables()
        self.check_for_tables()

    def create_table_of_tables(self):
        query = f'''
            CREATE TABLE IF NOT EXISTS {TablesDto.TABLE_NAME} (
                id integer PRIMARY KEY AUTOINCREMENT,
                table_id text,
                table_seats integer,
                table_available numeric
);'''
        row_id = DBUtils.execute_query(self.sqlConnection, query)

    def create_one_table(self, table_id, table_seats):
        query = f'''
            INSERT INTO {TablesDto.TABLE_NAME} (table_id, table_seats, table_available)
            VALUES ("{table_id}", "{table_seats}", 1);
        '''
        row_id = DBUtils.execute_query(self.sqlConnection, query)

    def check_for_tables(self):
        query = f'''
            SELECT * FROM {TablesDto.TABLE_NAME}
            where id = 1;
        '''
        data = DBUtils.fetch_data(self.sqlConnection, query, True)
        if data:
            pass
        else:
            self.add_random_tables()

    def add_random_tables(self):
        counter = 1
        for _ in range(1, 10):
            t_name = "Table " + str(counter)
            t_seats = random.randint(2, 6)
            self.create_one_table(t_name, t_seats)
            counter += 1
