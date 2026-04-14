import tkinter as tk
from tkinter import messagebox
from dbhelper.database import Database
from mainView.mainView import MainWindow


class LoginWindow:
    
    def __init__(self, root, database):
        self.root = root
        self.db = database
        self.login_entry = None
        self.password_entry = None
        self._init_window()

    def _init_window(self):
        self.root.title("Экзамен")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#202330")
        
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(2, weight=1)

        frame = tk.Frame(self.root, bg="#202330")
        frame.grid(row=1, column=1, sticky="nsew")
        frame.columnconfigure(0, minsize=220)

        tk.Label(frame, text="Логин", fg="white", bg="#202330") \
            .grid(row=0, column=0, sticky="w", pady=(10, 5))
        
        self.login_entry = tk.Entry(frame)
        self.login_entry.grid(row=1, column=0, sticky="ew", padx=10)

        tk.Label(frame, text="Пароль", fg="white", bg="#202330") \
            .grid(row=2, column=0, sticky="w", pady=(15, 5))
        
        self.password_entry = tk.Entry(frame, show="*")
        self.password_entry.grid(row=3, column=0, sticky="ew", padx=10)

        tk.Button(frame, text="Войти", command=self._on_login_click) \
            .grid(row=4, column=0, sticky="ew", padx=10, pady=(20, 5))

        tk.Button(frame, text="Войти как гость", command=self._on_guest_click) \
            .grid(row=5, column=0, sticky="ew", padx=10)

    def _on_login_click(self):
        login = self.login_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not login or not password:
            messagebox.showwarning("Ошибка", "Пожалуйста, введите все данные")
            return
        
        user = self.db.login_validation(login, password)
        if user:
            self._open_main_window(user)
        else:
            messagebox.showerror("Ошибка", "Невернные учетные данные")

    def _on_guest_click(self):
        guest_user = {
            "id": 0,
            "name": "Гость",
            "email": "guest@example.com",
            "role": "guest"
        }
        self._open_main_window(guest_user)

    def _open_main_window(self, user):
        self.root.destroy()
        main_root = tk.Tk()
        main_window = MainWindow(main_root, self.db, user)
        main_root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    db = Database(
        host="localhost",
        user="root",
        password="eJx6985OK6Y7gX",
        database="testing"
    )
    db.connect()
    LoginWindow(root, db)
    root.mainloop()
    db.disconnect()