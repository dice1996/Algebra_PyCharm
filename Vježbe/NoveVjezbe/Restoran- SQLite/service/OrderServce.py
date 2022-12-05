from datasource.dto.OrdersDto import OrdersDto
from utils.DBUtils import DBUtils
from utils.Utils import Utils as utl


class OrdersService:
    def __init__(self, sqlConnection):
        self.sqlConnection = sqlConnection
        self.create_orders_table()

    def create_orders_table(self):
        query = f'''
        CREATE TABLE IF NOT EXISTS {OrdersDto.TABLE_NAME} (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    food_list text,
                    drinks_list text,
                    price float,
                    seats integer,
                    payment integer,
                    jir text
);'''
        DBUtils.execute_query(self.sqlConnection, query)

    def add_order(self, food_list, drinks_list):
        price = utl.create_receipt(food_list, drinks_list)
        item: OrdersDto = OrdersDto().add_order(food_list, drinks_list, price)
        query = f'''
                    INSERT INTO {OrdersDto.TABLE_NAME} (food_list, drinks_list, price, payment)
                    VALUES ("{food_list}", "{drinks_list}", {price}, "None");
                '''
        row_id = DBUtils.execute_query(self.sqlConnection, query)
        return price, row_id

    def fetch_open_orders(self, paid = False):
        query1 = f'''
                    SELECT * FROM {OrdersDto.TABLE_NAME}
                    WHERE payment = "None";
                '''

        query2 = f'''
                            SELECT * FROM {OrdersDto.TABLE_NAME}
                            WHERE payment != "None";
                        '''
        if paid:
            orders = DBUtils.fetch_data(self.sqlConnection, query2)
        else:
            orders = DBUtils.fetch_data(self.sqlConnection, query1)
        orders_list = []
        for item in orders:
            order_item = OrdersDto.map_data_from_database(item)
            orders_list.append(order_item)
        return orders_list

    def order_payment(self, id, payment, jir):
        query = f'''
                UPDATE {OrdersDto.TABLE_NAME}
                SET payment = "{payment}", jir = "{jir}"
                WHERE id = {id}
        '''
        DBUtils.execute_query(self.sqlConnection, query)