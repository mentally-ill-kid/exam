import tkinter as tk
from dbhelper.database import Database
from loginView.loginView import LoginWindow


def main():
    root = tk.Tk()
    
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "eJx6985OK6Y7gX",
        "database": "testing"
    }
    
    db = Database(**db_config)
    db.connect()
    
    login_window = LoginWindow(root, db)
    
    root.mainloop()
    
    db.disconnect()


if __name__ == "__main__":
    main()