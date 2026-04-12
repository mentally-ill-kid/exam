from mysql.connector import MySQLConnection, Error


class Database:
    """Класс для управления соединением с БД MySQL."""
    
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """Установить соединение с БД."""
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
        """Закрыть соединение с БД."""
        if self.connection:
            self.connection.close()
            print("✓ Соединение с БД закрыто.")

    def execute_query(self, query, params=None):
        """Выполнить SQL запрос с параметризацией для защиты от инъекций."""
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
        """Проверить учетные данные пользователя (параметризованный запрос)."""
        query = "SELECT id, email FROM users WHERE email = %s AND passwd = %s"
        result = self.execute_query(query, (email, password))
        
        if result and len(result) > 0:
            print(f"✓ Вход выполнен: {email}")
            return True
        else:
            print("✗ Неверные учетные данные.")
            return False