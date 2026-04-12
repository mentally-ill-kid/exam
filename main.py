import tkinter as tk
from dbhelper.database import Database
from loginView.loginView import LoginWindow


def main():
    """Инициализация и запуск приложения."""
    root = tk.Tk()
    
    # Конфигурация базы данных
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "eJx6985OK6Y7gX",
        "database": "testing"
    }
    
    db = Database(**db_config)
    db.connect()
    
    # Инициализация окна логина с передачей БД
    login_window = LoginWindow(root, db)
    
    root.mainloop()
    
    # Закрытие соединения с БД при завершении
    db.disconnect()


if __name__ == "__main__":
    main()