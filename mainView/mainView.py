import tkinter as tk


class MainWindow:
    
    def __init__(self, root, db=None, user=None):
        self.root = root
        self.db = db
        self.user = user
        self.current_panel = None
        self.active_button = None
        self._init_window()

    def _init_window(self):
        self.root.title("Экзамен - Главное меню")
        self.root.geometry("900x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#202330")
        
        # Конфигурация колонок и строк
        self.root.columnconfigure(0, minsize=200)  # Левая колонка
        self.root.columnconfigure(1, weight=1)     # Центральная колонка
        self.root.columnconfigure(2, minsize=200)  # Правая колонка
        self.root.rowconfigure(0, weight=1)
        
        # Левая колонка с навигацией
        self.left_column = tk.Frame(self.root, bg="#2a2f3f")
        self.left_column.grid(row=0, column=0, sticky="nsew")
        
        # Центральная колонка с содержимым
        self.center_column = tk.Frame(self.root, bg="#202330")
        self.center_column.grid(row=0, column=1, sticky="nsew")
        
        # Правая колонка с информацией пользователя
        self.right_column = tk.Frame(self.root, bg="#2a2f3f")
        self.right_column.grid(row=0, column=2, sticky="nsew")
        
        self._create_navigation()
        self._create_user_panel()
        self._show_home()

    def _create_navigation(self):
        """Создаёт кнопки навигации в левой панели"""
        self.left_column.columnconfigure(0, weight=1)
        
        nav_title = tk.Label(
            self.left_column,
            text="Меню",
            fg="white",
            bg="#2a2f3f",
            font=("Arial", 12, "bold")
        )
        nav_title.grid(row=0, column=0, sticky="ew", pady=10)
        
        row = 1
        
        # Кнопка для главной страницы
        self._create_nav_button("🏠 Главная", self._show_home, row)
        row += 1
        
        # Кнопка для товаров
        self._create_nav_button("📦 Товары", self._show_goods, row)
        row += 1
        
        # Кнопка для заказов
        self._create_nav_button("🛒 Заказы", self._show_orders, row)
        row += 1
        
        # Кнопка для пользователей
        self._create_nav_button("👥 Пользователи", self._show_users, row)
        row += 1
        
        # Кнопка для поставщиков
        self._create_nav_button("🏭 Поставщики", self._show_suppliers, row)
        row += 1
        
        # Кнопка для выхода
        self._create_nav_button("🚪 Выход", self._logout, row, is_danger=True)

    def _create_nav_button(self, text, command, row, is_danger=False):
        """Создаёт кнопку навигации"""
        btn = tk.Button(
            self.left_column,
            text=text,
            command=command,
            bg="#3a3f4f" if not is_danger else "#5a3a3a",
            fg="white",
            border=0,
            font=("Arial", 10),
            padx=10,
            pady=12,
            activebackground="#4a4f5f" if not is_danger else "#6a4a4a",
            cursor="hand2"
        )
        btn.grid(row=row, column=0, sticky="ew", padx=5, pady=5)

    def _create_user_panel(self):
        """Создаёт панель с информацией о пользователе"""
        if not self.user:
            return
        
        self.right_column.columnconfigure(0, weight=1)
        self.right_column.rowconfigure(0, weight=1)
        self.right_column.rowconfigure(1, weight=0)
        
        # Контейнер для центрирования
        container = tk.Frame(self.right_column, bg="#2a2f3f")
        container.grid(row=0, column=0, sticky="nsew", padx=10, pady=20)
        
        # Иконка профиля (большой кружок с инициалами)
        profile_icon_frame = tk.Frame(container, bg="#292e42", width=80, height=80, relief=tk.RAISED, bd=2)
        profile_icon_frame.pack(expand=False, pady=(0, 15))
        profile_icon_frame.pack_propagate(False)
        
        # Инициалы пользователя
        initials = "".join([word[0].upper() for word in self.user['name'].split() if word])
        initials_label = tk.Label(
            profile_icon_frame,
            text=initials or "U",
            fg="#bb9af7",
            bg="#292e42",
            font=("Arial", 28, "bold")
        )
        initials_label.pack(expand=True)
        
        # Имя пользователя
        name_label = tk.Label(
            container,
            text=self.user['name'],
            fg="white",
            bg="#2a2f3f",
            font=("Arial", 12, "bold"),
            wraplength=180,
            justify=tk.CENTER
        )
        name_label.pack()
        
        # Роль
        role_label = tk.Label(
            container,
            text=self.user['role'],
            fg="#7aa2f7",
            bg="#2a2f3f",
            font=("Arial", 9),
            wraplength=180,
            justify=tk.CENTER
        )
        role_label.pack(pady=(5, 0))
        
        # Почта
        email_label = tk.Label(
            container,
            text=self.user['email'],
            fg="#9099a8",
            bg="#2a2f3f",
            font=("Arial", 8),
            wraplength=180,
            justify=tk.CENTER
        )
        email_label.pack(pady=(3, 0))

    def _clear_center_panel(self):
        """Очищает центральную панель"""
        for widget in self.center_column.winfo_children():
            widget.destroy()

    def _show_home(self):
        """Показывает главную страницу"""
        self._clear_center_panel()
        
        title = tk.Label(
            self.center_column,
            text="Главное меню",
            fg="white",
            bg="#202330",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=20)
        
        welcome_text = tk.Label(
            self.center_column,
            text="Добро пожаловать!\n\nВыберите раздел в левом меню",
            fg="#cccccc",
            bg="#202330",
            font=("Arial", 12),
            justify=tk.CENTER
        )
        welcome_text.pack(pady=40)

    def _show_goods(self):
        """Показывает список товаров"""
        self._clear_center_panel()
        
        title = tk.Label(
            self.center_column,
            text="📦 Товары",
            fg="white",
            bg="#202330",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=10)
        
        # Создаём скроллируемую область
        canvas_frame = tk.Frame(self.center_column, bg="#202330")
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        canvas = tk.Canvas(canvas_frame, bg="#202330", highlightthickness=0)
        scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#202330")
        
        # Конфигурация для правильного заполнения ширины
        scrollable_frame.columnconfigure(0, weight=1)
        
        def on_canvas_configure(event):
            canvas.itemconfig(window_id, width=event.width)
        
        window_id = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.bind("<Configure>", on_canvas_configure)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Загружаем товары из БД
        if self.db:
            goods = self.db.execute_query("""
                SELECT g.id, g.article, g.name, g.description, g.price, 
                       g.photo, g.discount, g.amount
                FROM goods g
            """)
            
            if goods:
                for good in goods:
                    self._create_good_card(scrollable_frame, good)
            else:
                no_goods_label = tk.Label(
                    scrollable_frame,
                    text="Товары не найдены",
                    fg="#999999",
                    bg="#202330",
                    font=("Arial", 11)
                )
                no_goods_label.pack(pady=20)
        else:
            error_label = tk.Label(
                scrollable_frame,
                text="Ошибка подключения к БД",
                fg="#ff6b6b",
                bg="#202330",
                font=("Arial", 11)
            )
            error_label.pack(pady=20)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _create_good_card(self, parent, good):
        """Создаёт карточку товара"""
        good_id, article, name, description, price, photo, discount, amount = good
        
        # Контейнер карточки
        card = tk.Frame(parent, bg="#292e42", relief=tk.FLAT, height=170)
        card.pack(fill=tk.BOTH, expand=True, pady=8, padx=0)
        card.pack_propagate(False)
        
        # Левая часть - картинка (180x170)
        image_frame = tk.Frame(card, bg="#1f2937", width=180, height=170)
        image_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=0)
        image_frame.pack_propagate(False)
        
        # Заглушка для изображения (позже можно добавить реальные картинки)
        image_label = tk.Label(
            image_frame,
            text=f"Photo\n{photo}",
            fg="#7aa2f7",
            bg="#1f2937",
            font=("Arial", 9)
        )
        image_label.pack(expand=True)
        
        # Правая часть - содержимое
        content_frame = tk.Frame(card, bg="#292e42")
        content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=12, pady=10)
        
        # Название товара
        name_label = tk.Label(
            content_frame,
            text=name,
            fg="#c0caf5",
            bg="#292e42",
            font=("Arial", 11, "bold")
        )
        name_label.pack(anchor="w")
        
        # Артикул
        article_label = tk.Label(
            content_frame,
            text=f"Артикул: {article}",
            fg="#7aa2f7",
            bg="#292e42",
            font=("Arial", 9)
        )
        article_label.pack(anchor="w", pady=(2, 0))
        
        # Описание
        if description:
            desc_label = tk.Label(
                content_frame,
                text=description[:40] + ("..." if len(description) > 40 else ""),
                fg="#9099a8",
                bg="#292e42",
                font=("Arial", 9),
                justify=tk.LEFT,
                wraplength=250
            )
            desc_label.pack(anchor="w", pady=(3, 0))
        
        # Нижняя часть - цена и количество
        bottom_frame = tk.Frame(content_frame, bg="#292e42")
        bottom_frame.pack(anchor="w", pady=(8, 0), fill=tk.X)
        
        # Цена
        price_label = tk.Label(
            bottom_frame,
            text=f"Цена: {price} ₽",
            fg="#bb9af7",
            bg="#292e42",
            font=("Arial", 10, "bold")
        )
        price_label.pack(side=tk.LEFT, padx=(0, 20))
        
        # Количество
        amount_label = tk.Label(
            bottom_frame,
            text=f"Кол-во: {amount}",
            fg="#7aa2f7",
            bg="#292e42",
            font=("Arial", 9)
        )
        amount_label.pack(side=tk.LEFT)
        
        # Скидка (если есть)
        if discount and discount > 0:
            discount_label = tk.Label(
                bottom_frame,
                text=f"Скидка: {discount}%",
                fg="#f7768e",
                bg="#292e42",
                font=("Arial", 9, "bold")
            )
            discount_label.pack(side=tk.RIGHT, padx=(0, 0))

    def _show_orders(self):
        """Показывает список заказов"""
        self._clear_center_panel()
        
        title = tk.Label(
            self.center_column,
            text="🛒 Заказы",
            fg="white",
            bg="#202330",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=10)
        
        # Здесь будет список заказов
        info_label = tk.Label(
            self.center_column,
            text="Список заказов из таблицы 'orders'",
            fg="#cccccc",
            bg="#202330",
            font=("Arial", 11)
        )
        info_label.pack(pady=20)

    def _show_users(self):
        """Показывает список пользователей"""
        self._clear_center_panel()
        
        title = tk.Label(
            self.center_column,
            text="👥 Пользователи",
            fg="white",
            bg="#202330",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=10)
        
        # Здесь будет список пользователей
        info_label = tk.Label(
            self.center_column,
            text="Список пользователей из таблицы 'users'",
            fg="#cccccc",
            bg="#202330",
            font=("Arial", 11)
        )
        info_label.pack(pady=20)

    def _show_suppliers(self):
        """Показывает список поставщиков"""
        self._clear_center_panel()
        
        title = tk.Label(
            self.center_column,
            text="🏭 Поставщики",
            fg="white",
            bg="#202330",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=10)
        
        # Здесь будет список поставщиков
        info_label = tk.Label(
            self.center_column,
            text="Список поставщиков из таблицы 'suppliers'",
            fg="#cccccc",
            bg="#202330",
            font=("Arial", 11)
        )
        info_label.pack(pady=20)

    def _logout(self):
        """Выход из приложения"""
        if self.db:
            self.db.disconnect()
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()