import tkinter as tk
from tkinter import messagebox
from dbhelper.database import Database


class LoginWindow:
    """Окно входа пользователя."""
    
    def __init__(self, root, database):
        """
        Конструктор окна логина.
        
        Args:
            root: Основное окно Tkinter
            database: Экземпляр класса Database
        """
        self.root = root
        self.db = database
        self.login_entry = None
        self.password_entry = None
        self._init_window()

    def _init_window(self):
        """Инициализация интерфейса."""
        self.root.title("Экзамен")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#202330")
        
        # Настройка сетки
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(2, weight=1)

        # Основной фрейм
        frame = tk.Frame(self.root, bg="#202330")
        frame.grid(row=1, column=1, sticky="nsew")
        frame.columnconfigure(0, minsize=220)

        # Поле "Логин"
        tk.Label(frame, text="Логин", fg="white", bg="#202330") \
            .grid(row=0, column=0, sticky="w", pady=(10, 5))
        
        self.login_entry = tk.Entry(frame)
        self.login_entry.grid(row=1, column=0, sticky="ew", padx=10)

        # Поле "Пароль"
        tk.Label(frame, text="Пароль", fg="white", bg="#202330") \
            .grid(row=2, column=0, sticky="w", pady=(15, 5))
        
        self.password_entry = tk.Entry(frame, show="*")
        self.password_entry.grid(row=3, column=0, sticky="ew", padx=10)

        # Кнопка "Войти"
        tk.Button(frame, text="Войти", command=self._on_login_click) \
            .grid(row=4, column=0, sticky="ew", padx=10, pady=(20, 5))

        # Кнопка "Войти как гость"
        tk.Button(frame, text="Войти как гость", command=self._on_guest_click) \
            .grid(row=5, column=0, sticky="ew", padx=10)

    def _on_login_click(self):
        """Обработка клика кнопки входа."""
        login = self.login_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not login or not password:
            messagebox.showwarning("Ошибка", "Пожалуйста, введите все данные")
            return
        
        if self.db.login_validation(login, password):
            messagebox.showinfo("Успех", f"Добро пожаловать, {login}!")
            # TODO: Открыть главное окно
        else:
            messagebox.showerror("Ошибка", "Невернные учетные данные")

    def _on_guest_click(self):
        """Обработка клика запуска как гость."""
        messagebox.showinfo("Гость", "Добро пожаловать как гость!")
        # TODO: Открыть главное окно в режиме гостя


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