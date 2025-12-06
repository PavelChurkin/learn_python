"""
Модуль 7: Объектно-ориентированное программирование (ООП)
==========================================================

Этот модуль охватывает:
- Классы и объекты
- Атрибуты и методы
- Конструктор __init__
- Инкапсуляция
- Наследование
- Полиморфизм
- Специальные методы

Каждая строка кода сопровождается подробным комментарием.
"""

print("=" * 60)  # Печатаем разделитель
print("МОДУЛЬ 7: Объектно-ориентированное программирование")
print("=" * 60)
print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 1: Классы и объекты - основы
# ============================================================================

print("--- Классы и объекты - основы ---")
print()  # Пустая строка

# Класс - это шаблон (чертёж) для создания объектов
# Объект - это экземпляр класса

# Определение простейшего класса
class Dog:
    """Класс, представляющий собаку"""
    pass  # Пустой класс

# Создание объекта (экземпляра класса)
my_dog = Dog()  # Вызываем класс как функцию
print(f"Объект: {my_dog}")  # Выводит адрес в памяти
print(f"Тип: {type(my_dog)}")  # <class '__main__.Dog'>

print()  # Пустая строка

# Класс с атрибутами и методами
class Cat:
    """Класс, представляющий кошку"""

    # Атрибут класса (общий для всех экземпляров)
    species = "Felis catus"  # Научное название вида

    # Конструктор - вызывается при создании объекта
    def __init__(self, name, age):
        """Инициализация объекта"""
        # self - ссылка на текущий объект
        self.name = name  # Атрибут экземпляра - имя
        self.age = age  # Атрибут экземпляра - возраст

    # Метод экземпляра
    def meow(self):
        """Издаёт мяуканье"""
        return f"{self.name} говорит: Мяу!"

    def describe(self):
        """Описывает кошку"""
        return f"{self.name}, {self.age} лет, вид: {self.species}"

# Создаём объекты
cat1 = Cat("Барсик", 3)  # Передаём аргументы в __init__
cat2 = Cat("Мурка", 5)

# Доступ к атрибутам
print(f"cat1.name: {cat1.name}")  # Барсик
print(f"cat2.age: {cat2.age}")  # 5
print(f"Cat.species: {Cat.species}")  # Атрибут класса

# Вызов методов
print(f"cat1.meow(): {cat1.meow()}")  # Барсик говорит: Мяу!
print(f"cat2.describe(): {cat2.describe()}")

print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 2: Атрибуты класса vs атрибуты экземпляра
# ============================================================================

print("--- Атрибуты класса vs атрибуты экземпляра ---")
print()  # Пустая строка

class Counter:
    """Класс со счётчиком экземпляров"""

    count = 0  # Атрибут класса - общий для всех

    def __init__(self, name):
        """Инициализация счётчика"""
        self.name = name  # Атрибут экземпляра - уникальный
        Counter.count += 1  # Увеличиваем общий счётчик

    def get_info(self):
        """Возвращает информацию о счётчике"""
        return f"{self.name}: экземпляр #{Counter.count}"

# Создаём несколько объектов
c1 = Counter("Первый")
print(f"После создания c1: Counter.count = {Counter.count}")  # 1

c2 = Counter("Второй")
print(f"После создания c2: Counter.count = {Counter.count}")  # 2

c3 = Counter("Третий")
print(f"После создания c3: Counter.count = {Counter.count}")  # 3

# Все экземпляры видят общий счётчик
print(f"c1.count: {c1.count}")  # 3
print(f"c2.count: {c2.count}")  # 3

print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 3: Инкапсуляция
# ============================================================================

print("--- Инкапсуляция ---")
print()  # Пустая строка

# Инкапсуляция - скрытие внутренней реализации

class BankAccount:
    """Банковский счёт с защитой данных"""

    def __init__(self, owner, balance=0):
        """Инициализация счёта"""
        self.owner = owner  # Публичный атрибут
        self._balance = balance  # Защищённый атрибут (соглашение)
        self.__pin = "1234"  # Приватный атрибут (name mangling)

    def deposit(self, amount):
        """Внесение средств"""
        if amount > 0:  # Проверка входных данных
            self._balance += amount
            return f"Внесено: {amount}. Баланс: {self._balance}"
        return "Сумма должна быть положительной"

    def withdraw(self, amount):
        """Снятие средств"""
        if amount <= 0:
            return "Сумма должна быть положительной"
        if amount > self._balance:
            return "Недостаточно средств"
        self._balance -= amount
        return f"Снято: {amount}. Баланс: {self._balance}"

    def get_balance(self):
        """Получение баланса (геттер)"""
        return self._balance

    def _internal_method(self):
        """Защищённый метод (условное соглашение)"""
        return "Это внутренний метод"

    def __private_method(self):
        """Приватный метод (name mangling)"""
        return "Это приватный метод"

# Использование
account = BankAccount("Иван", 1000)

print(f"Владелец: {account.owner}")  # Публичный атрибут
print(f"Баланс через метод: {account.get_balance()}")  # 1000

print(account.deposit(500))  # Внесено: 500. Баланс: 1500
print(account.withdraw(200))  # Снято: 200. Баланс: 1300
print(account.withdraw(2000))  # Недостаточно средств

# Доступ к защищённым атрибутам (технически возможен, но не рекомендуется)
print(f"account._balance: {account._balance}")  # Работает, но не рекомендуется

# Приватные атрибуты преобразуются в _ClassName__attribute
# print(account.__pin)  # ОШИБКА! AttributeError
print(f"account._BankAccount__pin: {account._BankAccount__pin}")  # Работает

print()  # Пустая строка

# Свойства (properties) - элегантный способ контроля доступа
class Temperature:
    """Класс для работы с температурой"""

    def __init__(self, celsius=0):
        """Инициализация температуры в Цельсиях"""
        self._celsius = celsius  # Внутреннее хранение в Цельсиях

    @property
    def celsius(self):
        """Геттер для температуры в Цельсиях"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Сеттер для температуры в Цельсиях"""
        if value < -273.15:  # Абсолютный ноль
            raise ValueError("Температура не может быть ниже -273.15°C")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Геттер для температуры в Фаренгейтах"""
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Сеттер для температуры в Фаренгейтах"""
        self.celsius = (value - 32) * 5/9  # Используем сеттер celsius

# Использование свойств
temp = Temperature(25)
print(f"Цельсий: {temp.celsius}°C")  # 25°C
print(f"Фаренгейт: {temp.fahrenheit}°F")  # 77.0°F

temp.celsius = 30  # Используем сеттер
print(f"После изменения: {temp.celsius}°C = {temp.fahrenheit}°F")

temp.fahrenheit = 100  # Устанавливаем в Фаренгейтах
print(f"100°F = {temp.celsius:.1f}°C")  # 37.8°C

print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 4: Наследование
# ============================================================================

print("--- Наследование ---")
print()  # Пустая строка

# Наследование позволяет создавать новые классы на основе существующих

# Базовый класс (родительский)
class Animal:
    """Базовый класс животного"""

    def __init__(self, name, age):
        """Инициализация животного"""
        self.name = name  # Имя животного
        self.age = age  # Возраст животного

    def speak(self):
        """Издаёт звук (будет переопределён в подклассах)"""
        return "Животное издаёт звук"

    def describe(self):
        """Описывает животное"""
        return f"{self.name}, возраст: {self.age}"

# Производный класс (дочерний)
class Dog(Animal):
    """Класс собаки, наследует от Animal"""

    def __init__(self, name, age, breed):
        """Инициализация собаки"""
        super().__init__(name, age)  # Вызываем конструктор родителя
        self.breed = breed  # Добавляем новый атрибут - порода

    def speak(self):
        """Переопределяем метод родителя"""
        return f"{self.name} говорит: Гав!"

    def fetch(self):
        """Новый метод, специфичный для собаки"""
        return f"{self.name} приносит мяч"

# Ещё один производный класс
class Cat(Animal):
    """Класс кошки, наследует от Animal"""

    def speak(self):
        """Переопределяем метод родителя"""
        return f"{self.name} говорит: Мяу!"

    def purr(self):
        """Новый метод, специфичный для кошки"""
        return f"{self.name} мурлычет"

# Использование
dog = Dog("Бобик", 3, "Лабрадор")
cat = Cat("Мурка", 5)

print(f"dog.describe(): {dog.describe()}")  # Унаследованный метод
print(f"dog.speak(): {dog.speak()}")  # Переопределённый метод
print(f"dog.breed: {dog.breed}")  # Новый атрибут
print(f"dog.fetch(): {dog.fetch()}")  # Новый метод

print()

print(f"cat.describe(): {cat.describe()}")  # Унаследованный метод
print(f"cat.speak(): {cat.speak()}")  # Переопределённый метод
print(f"cat.purr(): {cat.purr()}")  # Новый метод

# Проверка наследования
print(f"\nisinstance(dog, Dog): {isinstance(dog, Dog)}")  # True
print(f"isinstance(dog, Animal): {isinstance(dog, Animal)}")  # True
print(f"issubclass(Dog, Animal): {issubclass(Dog, Animal)}")  # True

print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 5: Множественное наследование
# ============================================================================

print("--- Множественное наследование ---")
print()  # Пустая строка

# Python поддерживает множественное наследование

class Flyable:
    """Миксин для летающих объектов"""

    def fly(self):
        """Летит"""
        return f"{self.name} летит"

class Swimmable:
    """Миксин для плавающих объектов"""

    def swim(self):
        """Плывёт"""
        return f"{self.name} плывёт"

class Duck(Animal, Flyable, Swimmable):
    """Утка - наследует от Animal, Flyable и Swimmable"""

    def speak(self):
        """Переопределяем метод"""
        return f"{self.name} говорит: Кря!"

# Использование
duck = Duck("Дональд", 2)
print(f"duck.describe(): {duck.describe()}")  # От Animal
print(f"duck.speak(): {duck.speak()}")  # Переопределённый
print(f"duck.fly(): {duck.fly()}")  # От Flyable
print(f"duck.swim(): {duck.swim()}")  # От Swimmable

# MRO - порядок разрешения методов
print(f"\nMRO (Method Resolution Order):")
print(Duck.__mro__)  # Порядок поиска методов

print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 6: Полиморфизм
# ============================================================================

print("--- Полиморфизм ---")
print()  # Пустая строка

# Полиморфизм - возможность объектов разных классов
# иметь одинаковый интерфейс

class Shape:
    """Базовый класс геометрической фигуры"""

    def area(self):
        """Вычисляет площадь (абстрактный метод)"""
        raise NotImplementedError("Подклассы должны реализовать этот метод")

    def perimeter(self):
        """Вычисляет периметр (абстрактный метод)"""
        raise NotImplementedError("Подклассы должны реализовать этот метод")

class Rectangle(Shape):
    """Прямоугольник"""

    def __init__(self, width, height):
        """Инициализация прямоугольника"""
        self.width = width
        self.height = height

    def area(self):
        """Площадь прямоугольника"""
        return self.width * self.height

    def perimeter(self):
        """Периметр прямоугольника"""
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Круг"""

    def __init__(self, radius):
        """Инициализация круга"""
        self.radius = radius

    def area(self):
        """Площадь круга"""
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Периметр (длина окружности)"""
        import math
        return 2 * math.pi * self.radius

class Triangle(Shape):
    """Треугольник"""

    def __init__(self, a, b, c):
        """Инициализация треугольника по трём сторонам"""
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        """Площадь по формуле Герона"""
        s = (self.a + self.b + self.c) / 2  # Полупериметр
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def perimeter(self):
        """Периметр треугольника"""
        return self.a + self.b + self.c

# Полиморфное поведение
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Triangle(3, 4, 5)
]

print("Вычисление площадей и периметров:")
for shape in shapes:  # Единообразная обработка разных фигур
    print(f"  {shape.__class__.__name__}:")
    print(f"    Площадь: {shape.area():.2f}")
    print(f"    Периметр: {shape.perimeter():.2f}")

print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 7: Специальные (магические) методы
# ============================================================================

print("--- Специальные (магические) методы ---")
print()  # Пустая строка

class Vector:
    """Класс вектора с перегрузкой операторов"""

    def __init__(self, x, y):
        """Инициализация вектора"""
        self.x = x
        self.y = y

    def __repr__(self):
        """Формальное строковое представление"""
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        """Неформальное строковое представление"""
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        """Сложение векторов: v1 + v2"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Вычитание векторов: v1 - v2"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Умножение на скаляр: v * n"""
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        """Умножение справа: n * v"""
        return self * scalar  # Используем __mul__

    def __eq__(self, other):
        """Сравнение на равенство: v1 == v2"""
        return self.x == other.x and self.y == other.y

    def __abs__(self):
        """Модуль вектора: abs(v)"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __len__(self):
        """Размерность вектора: len(v)"""
        return 2

    def __getitem__(self, index):
        """Доступ по индексу: v[0], v[1]"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Индекс должен быть 0 или 1")

    def __iter__(self):
        """Итерация по вектору: for x in v"""
        yield self.x
        yield self.y

# Использование
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")  # (3, 4) - __str__
print(f"repr(v1) = {repr(v1)}")  # Vector(3, 4) - __repr__
print(f"v1 + v2 = {v1 + v2}")  # (4, 6) - __add__
print(f"v1 - v2 = {v1 - v2}")  # (2, 2) - __sub__
print(f"v1 * 2 = {v1 * 2}")  # (6, 8) - __mul__
print(f"3 * v1 = {3 * v1}")  # (9, 12) - __rmul__
print(f"v1 == v2: {v1 == v2}")  # False - __eq__
print(f"abs(v1) = {abs(v1)}")  # 5.0 - __abs__
print(f"len(v1) = {len(v1)}")  # 2 - __len__
print(f"v1[0] = {v1[0]}, v1[1] = {v1[1]}")  # 3, 4 - __getitem__

print("Итерация по v1:")
for coord in v1:  # __iter__
    print(f"  {coord}")

print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 8: Классовые и статические методы
# ============================================================================

print("--- Классовые и статические методы ---")
print()  # Пустая строка

class Date:
    """Класс для работы с датой"""

    def __init__(self, year, month, day):
        """Инициализация даты"""
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        """Строковое представление"""
        return f"{self.day:02d}.{self.month:02d}.{self.year}"

    @classmethod
    def from_string(cls, date_string):
        """
        Классовый метод - альтернативный конструктор.
        cls - это ссылка на класс, а не на экземпляр.
        """
        day, month, year = map(int, date_string.split("."))
        return cls(year, month, day)  # Создаём экземпляр класса

    @classmethod
    def today(cls):
        """Классовый метод - создаёт дату сегодняшнего дня"""
        import datetime
        today = datetime.date.today()
        return cls(today.year, today.month, today.day)

    @staticmethod
    def is_valid_date(year, month, day):
        """
        Статический метод - не имеет доступа к self или cls.
        Работает как обычная функция, но логически связана с классом.
        """
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        # Упрощённая проверка
        return True

    def days_until(self, other):
        """Обычный метод экземпляра"""
        import datetime
        d1 = datetime.date(self.year, self.month, self.day)
        d2 = datetime.date(other.year, other.month, other.day)
        return (d2 - d1).days

# Использование обычного конструктора
d1 = Date(2024, 12, 31)
print(f"Обычный конструктор: {d1}")

# Использование классового метода как альтернативного конструктора
d2 = Date.from_string("15.01.2025")
print(f"Из строки: {d2}")

# Использование классового метода today()
today = Date.today()
print(f"Сегодня: {today}")

# Использование статического метода
print(f"Is 2024-02-30 valid? {Date.is_valid_date(2024, 2, 30)}")  # True (упрощённая проверка)
print(f"Is 2024-13-01 valid? {Date.is_valid_date(2024, 13, 1)}")  # False

# Обычный метод
print(f"Дней до {d1}: {today.days_until(d1)}")

print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 9: Абстрактные классы
# ============================================================================

print("--- Абстрактные классы ---")
print()  # Пустая строка

from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Абстрактный базовый класс транспортного средства"""

    def __init__(self, brand, model):
        """Инициализация транспорта"""
        self.brand = brand
        self.model = model

    @abstractmethod
    def start(self):
        """Абстрактный метод - должен быть реализован в подклассах"""
        pass

    @abstractmethod
    def stop(self):
        """Абстрактный метод - должен быть реализован в подклассах"""
        pass

    def info(self):
        """Обычный метод - наследуется подклассами"""
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    """Конкретный класс автомобиля"""

    def start(self):
        """Реализация абстрактного метода"""
        return f"{self.info()}: Двигатель заведён"

    def stop(self):
        """Реализация абстрактного метода"""
        return f"{self.info()}: Двигатель заглушен"

class Bicycle(Vehicle):
    """Конкретный класс велосипеда"""

    def start(self):
        """Реализация абстрактного метода"""
        return f"{self.info()}: Начинаем крутить педали"

    def stop(self):
        """Реализация абстрактного метода"""
        return f"{self.info()}: Остановились"

# Нельзя создать экземпляр абстрактного класса
# vehicle = Vehicle("Generic", "Brand")  # ОШИБКА! TypeError

# Можно создать экземпляры конкретных классов
car = Car("Toyota", "Camry")
bike = Bicycle("Giant", "Escape")

print(car.start())  # Toyota Camry: Двигатель заведён
print(car.stop())   # Toyota Camry: Двигатель заглушен
print(bike.start()) # Giant Escape: Начинаем крутить педали
print(bike.stop())  # Giant Escape: Остановились

print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 10: Практический пример - система управления библиотекой
# ============================================================================

print("--- Практический пример: Библиотека ---")
print()  # Пустая строка

class Book:
    """Класс книги"""

    def __init__(self, title, author, isbn):
        """Инициализация книги"""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True  # Доступна ли книга

    def __str__(self):
        """Строковое представление"""
        status = "доступна" if self.is_available else "на руках"
        return f"'{self.title}' ({self.author}) - {status}"

    def __eq__(self, other):
        """Сравнение по ISBN"""
        return self.isbn == other.isbn

class Member:
    """Класс читателя библиотеки"""

    def __init__(self, name, member_id):
        """Инициализация читателя"""
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # Список взятых книг

    def borrow(self, book):
        """Взять книгу"""
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            return f"{self.name} взял книгу '{book.title}'"
        return f"Книга '{book.title}' недоступна"

    def return_book(self, book):
        """Вернуть книгу"""
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            return f"{self.name} вернул книгу '{book.title}'"
        return f"У {self.name} нет книги '{book.title}'"

    def __str__(self):
        """Строковое представление"""
        return f"{self.name} (ID: {self.member_id})"

class Library:
    """Класс библиотеки"""

    def __init__(self, name):
        """Инициализация библиотеки"""
        self.name = name
        self.books = []  # Каталог книг
        self.members = []  # Список читателей

    def add_book(self, book):
        """Добавить книгу в каталог"""
        self.books.append(book)
        return f"Книга '{book.title}' добавлена в библиотеку"

    def register_member(self, member):
        """Зарегистрировать читателя"""
        self.members.append(member)
        return f"Читатель {member.name} зарегистрирован"

    def find_book(self, title):
        """Найти книгу по названию"""
        for book in self.books:
            if title.lower() in book.title.lower():
                return book
        return None

    def available_books(self):
        """Получить список доступных книг"""
        return [book for book in self.books if book.is_available]

# Демонстрация
library = Library("Городская библиотека")

# Добавляем книги
book1 = Book("Война и мир", "Л.Н. Толстой", "978-5-17-090123-4")
book2 = Book("Преступление и наказание", "Ф.М. Достоевский", "978-5-17-090124-5")
book3 = Book("Мастер и Маргарита", "М.А. Булгаков", "978-5-17-090125-6")

print(library.add_book(book1))
print(library.add_book(book2))
print(library.add_book(book3))

# Регистрируем читателей
member1 = Member("Иван Петров", "M001")
member2 = Member("Анна Сидорова", "M002")

print(library.register_member(member1))
print(library.register_member(member2))

print()

# Операции с книгами
print(member1.borrow(book1))  # Иван берёт "Войну и мир"
print(member2.borrow(book1))  # Анна пытается взять ту же книгу
print(member2.borrow(book2))  # Анна берёт другую книгу

print()

# Список доступных книг
print("Доступные книги:")
for book in library.available_books():
    print(f"  {book}")

print()

# Возврат книги
print(member1.return_book(book1))  # Иван возвращает книгу

print()

# Обновлённый список доступных книг
print("Доступные книги после возврата:")
for book in library.available_books():
    print(f"  {book}")

print()  # Пустая строка

# ============================================================================
# ИТОГИ МОДУЛЯ 7
# ============================================================================

print("=" * 60)  # Печатаем разделитель
print("ИТОГИ МОДУЛЯ 7: Объектно-ориентированное программирование")
print("=" * 60)
print("""
Вы изучили:
✓ Классы и объекты - основы ООП
✓ Атрибуты класса vs атрибуты экземпляра
✓ Инкапсуляция и свойства (@property)
✓ Наследование и super()
✓ Множественное наследование и MRO
✓ Полиморфизм - единый интерфейс для разных классов
✓ Специальные методы (__init__, __str__, __add__ и др.)
✓ Классовые (@classmethod) и статические (@staticmethod) методы
✓ Абстрактные классы (ABC)
✓ Практический пример: система библиотеки
""")
print("Переходите к Модулю 8: Советы по оптимизации производительности")
print("=" * 60)
