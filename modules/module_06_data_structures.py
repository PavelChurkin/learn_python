"""
Модуль 6: Структуры данных
===========================

Этот модуль охватывает:
- Списки (lists)
- Кортежи (tuples)
- Словари (dictionaries)
- Множества (sets)
- Методы и операции для каждой структуры

Каждая строка кода сопровождается подробным комментарием.
"""

print("=" * 60)  # Печатаем разделитель
print("МОДУЛЬ 6: Структуры данных")
print("=" * 60)
print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 1: Списки (Lists)
# ============================================================================

print("--- Списки (Lists) ---")
print()  # Пустая строка

# Список - упорядоченная изменяемая коллекция элементов

# Создание списков
empty_list = []  # Пустой список
numbers = [1, 2, 3, 4, 5]  # Список чисел
mixed = [1, "два", 3.0, True]  # Список с разными типами
nested = [[1, 2], [3, 4], [5, 6]]  # Вложенный список

print(f"Пустой список: {empty_list}")
print(f"Числа: {numbers}")
print(f"Смешанный: {mixed}")
print(f"Вложенный: {nested}")

print()  # Пустая строка

# Доступ к элементам по индексу
fruits = ["яблоко", "банан", "вишня", "дыня", "ежевика"]

print(f"Список: {fruits}")
print(f"fruits[0]: {fruits[0]}")  # Первый элемент
print(f"fruits[2]: {fruits[2]}")  # Третий элемент
print(f"fruits[-1]: {fruits[-1]}")  # Последний элемент
print(f"fruits[-2]: {fruits[-2]}")  # Предпоследний элемент

print()  # Пустая строка

# Срезы (slicing)
print(f"fruits[1:3]: {fruits[1:3]}")  # С 1 по 2 (не включая 3)
print(f"fruits[:3]: {fruits[:3]}")  # Первые 3 элемента
print(f"fruits[2:]: {fruits[2:]}")  # С третьего до конца
print(f"fruits[::2]: {fruits[::2]}")  # Каждый второй элемент
print(f"fruits[::-1]: {fruits[::-1]}")  # Список наоборот

print()  # Пустая строка

# Изменение элементов
colors = ["красный", "зелёный", "синий"]
print(f"До изменения: {colors}")

colors[1] = "жёлтый"  # Заменяем элемент
print(f"После colors[1] = 'жёлтый': {colors}")

colors[0:2] = ["белый", "чёрный", "серый"]  # Заменяем срез
print(f"После colors[0:2] = [...]: {colors}")

print()  # Пустая строка

# Методы списков
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Исходный список: {numbers}")

# Добавление элементов
numbers.append(5)  # Добавляем в конец
print(f"После append(5): {numbers}")

numbers.insert(0, 0)  # Вставляем на позицию 0
print(f"После insert(0, 0): {numbers}")

numbers.extend([3, 5])  # Добавляем несколько элементов
print(f"После extend([3, 5]): {numbers}")

print()  # Пустая строка

# Удаление элементов
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Исходный список: {numbers}")

removed = numbers.pop()  # Удаляем и возвращаем последний
print(f"После pop(): {numbers}, удалён: {removed}")

removed = numbers.pop(2)  # Удаляем элемент по индексу
print(f"После pop(2): {numbers}, удалён: {removed}")

numbers.remove(1)  # Удаляем первое вхождение значения
print(f"После remove(1): {numbers}")

print()  # Пустая строка

# Поиск и подсчёт
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(f"Список: {numbers}")

print(f"numbers.count(5): {numbers.count(5)}")  # Количество вхождений
print(f"numbers.index(9): {numbers.index(9)}")  # Индекс первого вхождения
print(f"5 in numbers: {5 in numbers}")  # Проверка наличия
print(f"len(numbers): {len(numbers)}")  # Длина списка

print()  # Пустая строка

# Сортировка
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Исходный: {numbers}")

numbers.sort()  # Сортировка на месте (изменяет список)
print(f"После sort(): {numbers}")

numbers.sort(reverse=True)  # Сортировка по убыванию
print(f"После sort(reverse=True): {numbers}")

numbers.reverse()  # Разворот списка
print(f"После reverse(): {numbers}")

# sorted() возвращает новый список, не изменяя исходный
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)  # Новый отсортированный список
print(f"original: {original}, sorted(original): {sorted_list}")

print()  # Пустая строка

# Копирование списков
original = [1, 2, 3]
# Поверхностная копия
shallow_copy = original.copy()  # или original[:]  или list(original)
# Глубокая копия (для вложенных списков)
import copy
nested = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(nested)

print(f"original: {original}")
print(f"shallow_copy: {shallow_copy}")
print(f"original is shallow_copy: {original is shallow_copy}")  # False

print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 2: Кортежи (Tuples)
# ============================================================================

print("--- Кортежи (Tuples) ---")
print()  # Пустая строка

# Кортеж - упорядоченная неизменяемая коллекция элементов

# Создание кортежей
empty_tuple = ()  # Пустой кортеж
single = (42,)  # Кортеж с одним элементом (запятая обязательна!)
point = (3, 4)  # Кортеж координат
mixed = (1, "два", 3.0)  # Кортеж с разными типами
without_parens = 1, 2, 3  # Скобки необязательны

print(f"Пустой кортеж: {empty_tuple}")
print(f"Один элемент: {single}, type: {type(single)}")
print(f"Точка: {point}")
print(f"Без скобок: {without_parens}, type: {type(without_parens)}")

print()  # Пустая строка

# Доступ к элементам (как в списках)
coordinates = (10, 20, 30)
print(f"coordinates[0]: {coordinates[0]}")  # 10
print(f"coordinates[-1]: {coordinates[-1]}")  # 30
print(f"coordinates[1:]: {coordinates[1:]}")  # (20, 30)

# Кортеж нельзя изменить!
# coordinates[0] = 5  # ОШИБКА! TypeError

print()  # Пустая строка

# Распаковка кортежей
point = (3, 4, 5)
x, y, z = point  # Распаковка в три переменные
print(f"point: {point} -> x={x}, y={y}, z={z}")

# Распаковка с игнорированием
first, *rest = (1, 2, 3, 4, 5)  # first=1, rest=[2,3,4,5]
print(f"first: {first}, rest: {rest}")

first, *middle, last = (1, 2, 3, 4, 5)  # middle=[2,3,4]
print(f"first: {first}, middle: {middle}, last: {last}")

# Обмен значений через кортежи
a, b = 10, 20
print(f"До обмена: a={a}, b={b}")
a, b = b, a  # Обмен без временной переменной
print(f"После обмена: a={a}, b={b}")

print()  # Пустая строка

# Именованные кортежи (namedtuple)
from collections import namedtuple

# Создаём тип Point с полями x и y
Point = namedtuple("Point", ["x", "y"])

p = Point(3, 4)  # Создаём экземпляр
print(f"Point: {p}")
print(f"p.x: {p.x}, p.y: {p.y}")  # Доступ по имени
print(f"p[0]: {p[0]}, p[1]: {p[1]}")  # Доступ по индексу

print()  # Пустая строка

# Когда использовать кортежи вместо списков:
# - Для неизменяемых данных (координаты, RGB-цвета)
# - Как ключи словарей (списки нельзя использовать как ключи)
# - Для возврата нескольких значений из функции
# - Когда нужна защита от случайного изменения

print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 3: Словари (Dictionaries)
# ============================================================================

print("--- Словари (Dictionaries) ---")
print()  # Пустая строка

# Словарь - коллекция пар ключ-значение

# Создание словарей
empty_dict = {}  # Пустой словарь
person = {"name": "Иван", "age": 30, "city": "Москва"}  # Литерал
from_pairs = dict([("a", 1), ("b", 2)])  # Из списка пар
from_kwargs = dict(x=10, y=20)  # Из именованных аргументов

print(f"person: {person}")
print(f"from_pairs: {from_pairs}")
print(f"from_kwargs: {from_kwargs}")

print()  # Пустая строка

# Доступ к значениям
person = {"name": "Иван", "age": 30, "city": "Москва"}

print(f"person['name']: {person['name']}")  # По ключу
# person['email']  # ОШИБКА! KeyError, если ключа нет

# Безопасный доступ с get()
print(f"person.get('age'): {person.get('age')}")  # 30
print(f"person.get('email'): {person.get('email')}")  # None
print(f"person.get('email', 'нет'): {person.get('email', 'нет')}")  # 'нет'

print()  # Пустая строка

# Добавление и изменение
person = {"name": "Иван", "age": 30}
print(f"До изменений: {person}")

person["city"] = "Москва"  # Добавляем новый ключ
print(f"После добавления city: {person}")

person["age"] = 31  # Изменяем существующий
print(f"После изменения age: {person}")

# update() - обновление несколькими парами
person.update({"email": "ivan@mail.ru", "age": 32})
print(f"После update(): {person}")

print()  # Пустая строка

# Удаление элементов
person = {"name": "Иван", "age": 30, "city": "Москва", "email": "ivan@mail.ru"}
print(f"До удаления: {person}")

del person["email"]  # Удаление по ключу
print(f"После del ['email']: {person}")

age = person.pop("age")  # Удаление с возвратом значения
print(f"После pop('age'): {person}, удалён age: {age}")

# popitem() удаляет и возвращает последнюю пару (Python 3.7+)
item = person.popitem()
print(f"После popitem(): {person}, удалена пара: {item}")

print()  # Пустая строка

# Перебор словаря
data = {"a": 1, "b": 2, "c": 3}

print("Перебор ключей:")
for key in data:  # или data.keys()
    print(f"  {key}")

print("Перебор значений:")
for value in data.values():
    print(f"  {value}")

print("Перебор пар:")
for key, value in data.items():
    print(f"  {key}: {value}")

print()  # Пустая строка

# Проверка наличия ключа
person = {"name": "Иван", "age": 30}
print(f"'name' in person: {'name' in person}")  # True
print(f"'email' in person: {'email' in person}")  # False

print()  # Пустая строка

# Полезные методы словарей
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

# Объединение словарей (Python 3.9+)
merged = d1 | d2  # Новый словарь
print(f"{d1} | {d2} = {merged}")

# setdefault() - получить или установить значение
person = {"name": "Иван"}
person.setdefault("age", 25)  # Устанавливает, если ключа нет
print(f"После setdefault('age', 25): {person}")
person.setdefault("age", 30)  # Не изменяет, если ключ есть
print(f"После setdefault('age', 30): {person}")

print()  # Пустая строка

# Словарь со значениями по умолчанию
from collections import defaultdict

# Подсчёт слов
text = "яблоко банан яблоко вишня банан яблоко"
word_count = defaultdict(int)  # По умолчанию 0

for word in text.split():
    word_count[word] += 1  # Не нужно проверять наличие ключа

print(f"Подсчёт слов: {dict(word_count)}")

print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 4: Множества (Sets)
# ============================================================================

print("--- Множества (Sets) ---")
print()  # Пустая строка

# Множество - неупорядоченная коллекция уникальных элементов

# Создание множеств
empty_set = set()  # Пустое множество (НЕ {}, это словарь!)
numbers = {1, 2, 3, 4, 5}  # Литерал множества
from_list = set([1, 2, 2, 3, 3, 3])  # Из списка (дубликаты удаляются)

print(f"Пустое множество: {empty_set}")
print(f"numbers: {numbers}")
print(f"from_list (без дубликатов): {from_list}")

print()  # Пустая строка

# Добавление и удаление элементов
fruits = {"яблоко", "банан"}
print(f"Исходное: {fruits}")

fruits.add("вишня")  # Добавляем элемент
print(f"После add('вишня'): {fruits}")

fruits.add("яблоко")  # Дубликат не добавится
print(f"После add('яблоко'): {fruits}")

fruits.update(["дыня", "ежевика"])  # Добавляем несколько
print(f"После update(): {fruits}")

fruits.remove("банан")  # Удаляем элемент (ошибка если нет)
print(f"После remove('банан'): {fruits}")

fruits.discard("груша")  # Удаляем если есть (без ошибки)
print(f"После discard('груша'): {fruits}")

print()  # Пустая строка

# Операции над множествами
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(f"a = {a}")
print(f"b = {b}")

# Объединение (union) - все элементы из обоих множеств
print(f"a | b (объединение): {a | b}")  # или a.union(b)

# Пересечение (intersection) - общие элементы
print(f"a & b (пересечение): {a & b}")  # или a.intersection(b)

# Разность (difference) - элементы из a, которых нет в b
print(f"a - b (разность): {a - b}")  # или a.difference(b)

# Симметрическая разность - элементы, которые есть только в одном
print(f"a ^ b (симм. разность): {a ^ b}")  # или a.symmetric_difference(b)

print()  # Пустая строка

# Проверки подмножеств
small = {1, 2}
big = {1, 2, 3, 4, 5}

print(f"small = {small}")
print(f"big = {big}")

print(f"small <= big (подмножество): {small <= big}")  # True
print(f"small < big (строгое подмножество): {small < big}")  # True
print(f"big >= small (надмножество): {big >= small}")  # True

# Проверка на непространство
print(f"small.isdisjoint({3, 4}): {small.isdisjoint({3, 4})}")  # True, нет общих

print()  # Пустая строка

# Неизменяемое множество (frozenset)
frozen = frozenset([1, 2, 3])  # Нельзя изменять
# frozen.add(4)  # ОШИБКА!

# Можно использовать как ключ словаря
d = {frozen: "значение"}
print(f"Словарь с frozenset: {d}")

print()  # Пустая строка

# Практические применения множеств

# Удаление дубликатов
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(numbers))  # Преобразуем в set и обратно в list
print(f"С дубликатами: {numbers}")
print(f"Уникальные: {unique}")

# Быстрая проверка принадлежности
valid_statuses = {"active", "pending", "completed"}
status = "active"
if status in valid_statuses:  # O(1) вместо O(n) для списка
    print(f"Статус '{status}' допустим")

print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 5: Сравнение структур данных
# ============================================================================

print("--- Сравнение структур данных ---")
print()  # Пустая строка

print("""
┌─────────────┬────────────┬───────────────┬────────────┬─────────────┐
│  Структура  │ Упорядочен │  Изменяемый   │ Уникальные │   Индексы   │
├─────────────┼────────────┼───────────────┼────────────┼─────────────┤
│   list      │     Да     │      Да       │     Нет    │     Да      │
│   tuple     │     Да     │     Нет       │     Нет    │     Да      │
│   dict      │  Да(3.7+)  │      Да       │  Ключи-да  │   По ключу  │
│   set       │    Нет     │      Да       │     Да     │     Нет     │
│ frozenset   │    Нет     │     Нет       │     Да     │     Нет     │
└─────────────┴────────────┴───────────────┴────────────┴─────────────┘

Когда использовать:
• list   - упорядоченная коллекция с возможными дубликатами
• tuple  - неизменяемая коллекция (координаты, записи БД)
• dict   - связь ключ-значение, быстрый поиск по ключу
• set    - уникальные элементы, проверка принадлежности
""")

print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 6: Практические примеры
# ============================================================================

print("--- Практические примеры ---")
print()  # Пустая строка

# Пример 1: Подсчёт частоты слов
def word_frequency(text):
    """Подсчитывает частоту слов в тексте"""
    words = text.lower().split()  # Разбиваем на слова
    frequency = {}  # Словарь для подсчёта

    for word in words:
        # Убираем знаки препинания
        word = word.strip(".,!?:;\"'")
        if word:  # Пропускаем пустые строки
            frequency[word] = frequency.get(word, 0) + 1

    return frequency

text = "Привет мир! Привет Python. Python - это круто, мир!"
freq = word_frequency(text)
print("Частота слов:")
for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    print(f"  {word}: {count}")

print()  # Пустая строка

# Пример 2: Инвертированный индекс
def create_inverted_index(documents):
    """Создаёт инвертированный индекс для поиска по документам"""
    index = {}  # слово -> список документов

    for doc_id, text in enumerate(documents):
        words = set(text.lower().split())  # Уникальные слова документа
        for word in words:
            if word not in index:
                index[word] = set()  # Используем set для уникальности
            index[word].add(doc_id)

    return index

documents = [
    "Python язык программирования",
    "Java тоже язык программирования",
    "Python прост в изучении"
]

index = create_inverted_index(documents)
print("Инвертированный индекс:")
for word, docs in sorted(index.items()):
    print(f"  '{word}' -> документы {docs}")

# Поиск документов, содержащих слово
search_word = "python"
if search_word in index:
    print(f"\nДокументы со словом '{search_word}': {index[search_word]}")

print()  # Пустая строка

# Пример 3: Группировка данных
from collections import defaultdict

def group_by_key(items, key_func):
    """Группирует элементы по ключу"""
    groups = defaultdict(list)  # Автоматически создаёт пустые списки

    for item in items:
        key = key_func(item)  # Вычисляем ключ группировки
        groups[key].append(item)  # Добавляем в группу

    return dict(groups)

# Группируем людей по первой букве имени
people = ["Алексей", "Анна", "Борис", "Андрей", "Виктор", "Анастасия"]
grouped = group_by_key(people, lambda name: name[0])

print("Группировка по первой букве:")
for letter, names in sorted(grouped.items()):
    print(f"  {letter}: {names}")

print()  # Пустая строка

# Пример 4: Объединение данных
def merge_dicts(*dicts):
    """Объединяет несколько словарей"""
    result = {}
    for d in dicts:
        result.update(d)  # Каждый следующий перезаписывает
    return result

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d3 = {"a": 10, "e": 5}  # 'a' перезапишется

merged = merge_dicts(d1, d2, d3)
print(f"merge_dicts({d1}, {d2}, {d3})")
print(f"Результат: {merged}")

print()  # Пустая строка

# ============================================================================
# ИТОГИ МОДУЛЯ 6
# ============================================================================

print("=" * 60)  # Печатаем разделитель
print("ИТОГИ МОДУЛЯ 6: Структуры данных")
print("=" * 60)
print("""
Вы изучили:
✓ Списки: создание, индексация, срезы, методы
✓ Кортежи: неизменяемость, распаковка, namedtuple
✓ Словари: ключи и значения, методы, defaultdict
✓ Множества: уникальность, операции (union, intersection)
✓ Сравнение структур данных и их применение
✓ Практические примеры: частота слов, индексация, группировка
""")
print("Переходите к Модулю 7: Объектно-ориентированное программирование")
print("=" * 60)
