from tkinter import *
from dbhelper.database import Database

#bg=#202330

class Login_window:
    def init_window():
        root = Tk()
        root.title("exam_test")
        root.geometry("400x600")
        root.resizable(False, False)
        root.configure(bg="#202330")
        root.rowconfigure(0, weight=1)

        root.rowconfigure(2, weight=1)
        root.columnconfigure(0, weight=1)
        root.columnconfigure(2, weight=1)

        frame = Frame(root, bg="#202330")
        frame.grid(row=1, column=1, sticky="nsew")

        frame.columnconfigure(0, minsize=220)

        Label(frame, text="Логин", fg="white", bg="#202330")\
            .grid(row=0, column=0, sticky="w", pady=(10, 5))

        login_entry = Entry(frame)
        login_entry.grid(row=1, column=0, sticky="ew", padx=10)

        Label(frame, text="Пароль", fg="white", bg="#202330")\
            .grid(row=2, column=0, sticky="w", pady=(15, 5))

        password_entry = Entry(frame, show="*")
        password_entry.grid(row=3, column=0, sticky="ew", padx=10)

        Button(frame, text="Войти", command=lambda: Database.login_validation(login_entry, password_entry))\
            .grid(row=4, column=0, sticky="ew", padx=10, pady=(20, 5))

        Button(frame, text="Войти как гость")\
            .grid(row=5, column=0, sticky="ew", padx=10)

        root.mainloop()
        
if __name__ == "__main__": Login_window.init_window()