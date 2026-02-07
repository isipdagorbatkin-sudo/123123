import os


# Класс для книги
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "доступна"

    def show_info(self):
        return f"'{self.title}' - {self.author} ({self.status})"


# Класс для пользователя
class User:
    def __init__(self, name):
        self.name = name
        self.books = []

    def show_info(self):
        books_count = len(self.books)
        return f"{self.name} (книг: {books_count})"


# Основной класс
class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.load_data()

    def load_data(self):
        # Загружаем книги
        if os.path.exists("books.txt"):
            with open("books.txt", "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        data = line.split(";")
                        if len(data) == 3:
                            book = Book(data[0], data[1])
                            book.status = data[2]
                            self.books.append(book)

        # Загружаем пользователей
        if os.path.exists("users.txt"):
            with open("users.txt", "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        data = line.split(";")
                        if len(data) >= 1:
                            user = User(data[0])
                            self.users.append(user)

    def save_data(self):
        # Сохраняем книги
        with open("books.txt", "w", encoding="utf-8") as f:
            for book in self.books:
                f.write(f"{book.title};{book.author};{book.status}\n")

        # Сохраняем пользователей
        with open("users.txt", "w", encoding="utf-8") as f:
            for user in self.users:
                f.write(f"{user.name}\n")

    def add_book(self):
        title = input("Название книги: ")
        author = input("Автор книги: ")

        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Книга '{title}' добавлена!")

    def remove_book(self):
        print("\nУдалить книгу")

        if not self.books:
            print("Книг нет в библиотеке")
            return

        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book.show_info()}")

        try:
            num = int(input("Номер книги для удаления: "))
            if 1 <= num <= len(self.books):
                removed = self.books.pop(num - 1)
                print(f"Книга '{removed.title}' удалена!")
            else:
                print("Неверный номер!")
        except:
            print("Ошибка ввода!")

    def add_user(self):
        print("\n--- Добавить пользователя ---")
        name = input("Имя пользователя: ")

        new_user = User(name)
        self.users.append(new_user)
        print(f"Пользователь '{name}' добавлен!")

    def show_users(self):
        print("\nВсе пользователи")

        if not self.users:
            print("Пользователей нет")
            return

        for i, user in enumerate(self.users, 1):
            print(f"{i}. {user.show_info()}")

    def show_books(self):
        print("\nВсе книги")

        if not self.books:
            print("Книг нет")
            return

        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book.show_info()}")

    def start(self):
        print("БИБЛИОТЕКА")
        print("Вы вошли как библиотекарь")

        while True:
            print("\nМеню:")
            print("1. Добавить книгу")
            print("2. Удалить книгу")
            print("3. Добавить пользователя")
            print("4. Показать пользователей")
            print("5. Показать книги")
            print("0. Выход")

            choice = input("Выберите: ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.add_user()
            elif choice == "4":
                self.show_users()
            elif choice == "5":
                self.show_books()
            elif choice == "0":
                self.save_data()
                print("Данные сохранены. До свидания!")
                break
            else:
                print("Неверный выбор!")


# Создаем библиотеку и запускаем программу
library = Library()
library.start()