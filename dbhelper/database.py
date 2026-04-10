from mysql.connector import MySQLConnection, Error

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = MySQLConnection(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            print("Database connection successful.")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def execute_query(self, query):
        if not self.connection:
            print("No database connection.")
            return None
        
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error executing query: {e}")
            return None

    def login_validation(self, email, passwd):
        query = f"SELECT * FROM users WHERE email='{email}' AND passwd='{passwd}'"
        result = self.execute_query(query)
        print(f"Login validation result: {result}")
        return result is not None and len(result) > 0