import sqlite3
from datasource.dto.SmarKeyDto import SmartKeyDto
from utils.DBUtils import DBUtils

DB_NAME = "smartkey.db"


class SmartKeyService:
    table_name = "users"

    def __init__(self):
        self.sqlConnection = sqlite3.connect(DB_NAME)
        self.create_table()

    def create_table(self):
        query = f'''
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            PIN int(4) NOT NULL UNIQUE,
            is_active int(1) NOT NULL
        );        
        '''
        DBUtils.db_execute(self.sqlConnection, query)

    def fetch_users_for_list(self):
        query = f'''
        SELECT * FROM {self.table_name};
        '''
        users = []
        result = DBUtils.db_fetch(self.sqlConnection, query)
        try:
            for item in result:
                user = SmartKeyDto.map_data_from_database(item)
                user_data = str(user.id) + ". " + user.first_name + " " + user.last_name
                users.append(user_data)
            return users
        except Exception as e:
            print(e)
            return None

    def fetch_by_id(self, id):
        query = f'''
            SELECT * FROM `{self.table_name}` WHERE id = {id};'''

        result = DBUtils.db_fetch(self.sqlConnection, query, True)
        try:
            user = SmartKeyDto.map_data_from_database(result)
            return user
        except Exception as e:
            print(e)
            return None

    def update_user(self, id, fname, lname, pin, is_active):
        query = f'''
            UPDATE `{self.table_name}` SET
                first_name = '{fname}',
                last_name = '{lname}',
                PIN = {pin},
                is_active = {is_active}
                WHERE id = {id};'''

        DBUtils.db_execute(self.sqlConnection, query)

    def create_user(self, user: SmartKeyDto):
        query = f'''
            INSERT INTO `{self.table_name}` (
                first_name,
                last_name,
                PIN,
                is_active
            ) VALUES (
                "{user.first_name}",
                "{user.last_name}",
                {user.PIN},
                {user.isActive});'''

        DBUtils.db_execute(self.sqlConnection, query)

    def delete_user(self, id):
        query = f'''
            DELETE FROM `{self.table_name}` WHERE id = {id};'''

        DBUtils.db_execute(self.sqlConnection, query)

    def allow_entry(self, PIN):
        query = f'''
        SELECT * FROM {self.table_name} WHERE PIN = {PIN} AND is_active = 1;
        '''
        result = DBUtils.db_fetch(self.sqlConnection, query, True)
        print(result)
        if result is not None:
            return True, result
        else:
            return False, None
