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
            print("✓ Соединение с БД установлено.")
            return True
        except Error as e:
            print(f"✗ Ошибка подключения: {e}")
            return False

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("✓ Соединение с БД закрыто.")

    def execute_query(self, query, params=None):
        if not self.connection:
            print("✗ Нет соединения с БД.")
            return None
        
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params or ())
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"✗ Ошибка выполнения запроса: {e}")
            return None
        finally:
            if cursor:
                cursor.close()

    def login_validation(self, email, password):
        query = "SELECT id, email, name, role FROM users WHERE email = %s AND passwd = %s"
        result = self.execute_query(query, (email, password))
        
        if result and len(result) > 0:
            user_id, user_email, user_name, user_role = result[0]
            print(f"✓ Вход выполнен: {user_email}")
            return {
                "id": user_id,
                "email": user_email,
                "name": user_name,
                "role": user_role
            }
        else:
            print("✗ Неверные учетные данные.")
            return None

    def get_all_goods(self):
        query = """
            SELECT g.id, g.article, g.name, g.description, g.price, 
                   g.photo, g.discount, g.amount
            FROM goods g
        """
        return self.execute_query(query)

    def get_all_orders(self):
        query = """
            SELECT o.id, o.user_id, u.name as user_name, o.date, 
                   os.status, o.total_sum
            FROM orders o
            LEFT JOIN users u ON o.user_id = u.id
            LEFT JOIN `order-status` os ON o.id = os.id
        """
        return self.execute_query(query)

    def get_all_users(self):
        query = "SELECT id, name, email, role FROM users"
        return self.execute_query(query)

    def get_all_suppliers(self):
        query = "SELECT id, name FROM suppliers"
        return self.execute_query(query)