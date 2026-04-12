import tkinter as tk


class MainWindow:
    """Главное окно приложения."""
    
    def __init__(self, root):
        """
        Конструктор главного окна.
        
        Args:
            root: Основное окно Tkinter
        """
        self.root = root
        self._init_window()

    def _init_window(self):
        """Инициализация главного окна."""
        self.root.title("Экзамен - Главное меню")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#202330")
        self.root.rowconfigure(0, weight=1)
        
        # Заголовный лейбл
        title_label = tk.Label(
            self.root,
            text="Главное меню",
            fg="white",
            bg="#202330",
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()