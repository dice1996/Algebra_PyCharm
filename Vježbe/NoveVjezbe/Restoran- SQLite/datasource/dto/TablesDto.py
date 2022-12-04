

class TablesDto:
    TABLE_NAME = "Tables"

    def __init__(self):
        self.id = None
        self.table_id = None
        self.table_seats = None
        self.table_available = True

    def add_table(self, table_id, table_seats):
        self.table_id = table_id
        self.table_seats = table_seats
