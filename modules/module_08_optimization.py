"""
Модуль 8: Советы по оптимизации производительности
====================================================

Этот модуль охватывает:
- Выбор правильных структур данных
- Оптимизация циклов
- Профилирование кода
- Использование встроенных функций
- Кэширование и мемоизация
- Работа с большими данными
- Общие рекомендации

Каждая строка кода сопровождается подробным комментарием.
"""

import time  # Для измерения времени выполнения
from functools import lru_cache  # Для кэширования

print("=" * 60)  # Печатаем разделитель
print("МОДУЛЬ 8: Советы по оптимизации производительности")
print("=" * 60)
print()  # Пустая строка

# ============================================================================
# Вспомогательная функция для измерения времени
# ============================================================================

def measure_time(func, *args, iterations=1000, **kwargs):
    """
    Измеряет среднее время выполнения функции.

    Args:
        func: Функция для измерения
        *args: Позиционные аргументы для функции
        iterations: Количество повторений для усреднения
        **kwargs: Именованные аргументы для функции

    Returns:
        tuple: (результат, среднее_время_в_мс)
    """
    start = time.perf_counter()  # Точный таймер
    for _ in range(iterations):
        result = func(*args, **kwargs)
    end = time.perf_counter()
    avg_time = (end - start) / iterations * 1000  # В миллисекундах
    return result, avg_time

# ============================================================================
# РАЗДЕЛ 1: Выбор правильных структур данных
# ============================================================================

print("--- Выбор правильных структур данных ---")
print()  # Пустая строка

# Совет 1: Используйте set для проверки принадлежности вместо list
print("Совет 1: set vs list для проверки принадлежности")

# Создаём данные для тестирования
test_list = list(range(10000))  # Список из 10000 элементов
test_set = set(test_list)  # Множество из тех же элементов
search_value = 9999  # Значение для поиска

# Измеряем поиск в списке - O(n)
def search_in_list():
    return search_value in test_list

# Измеряем поиск в множестве - O(1)
def search_in_set():
    return search_value in test_set

_, list_time = measure_time(search_in_list, iterations=10000)
_, set_time = measure_time(search_in_set, iterations=10000)

print(f"  Поиск в list: {list_time:.4f} мс")
print(f"  Поиск в set:  {set_time:.4f} мс")
print(f"  set быстрее в {list_time/set_time:.1f} раз")

print()  # Пустая строка

# Совет 2: Используйте dict для поиска по ключу
print("Совет 2: dict vs list для поиска по ключу")

# Поиск в списке кортежей - O(n)
users_list = [(i, f"user_{i}") for i in range(1000)]

def find_in_list_of_tuples(user_id):
    for uid, name in users_list:
        if uid == user_id:
            return name
    return None

# Поиск в словаре - O(1)
users_dict = {i: f"user_{i}" for i in range(1000)}

def find_in_dict(user_id):
    return users_dict.get(user_id)

_, list_time = measure_time(find_in_list_of_tuples, 999, iterations=10000)
_, dict_time = measure_time(find_in_dict, 999, iterations=10000)

print(f"  Поиск в list of tuples: {list_time:.4f} мс")
print(f"  Поиск в dict:           {dict_time:.4f} мс")
print(f"  dict быстрее в {list_time/dict_time:.1f} раз")

print()  # Пустая строка

# Совет 3: Используйте deque для операций в начале списка
print("Совет 3: deque vs list для операций в начале")

from collections import deque

# Вставка в начало списка - O(n)
def insert_to_list():
    lst = []
    for i in range(1000):
        lst.insert(0, i)  # Вставка в начало
    return lst

# Вставка в начало deque - O(1)
def insert_to_deque():
    dq = deque()
    for i in range(1000):
        dq.appendleft(i)  # Вставка в начало
    return dq

_, list_time = measure_time(insert_to_list, iterations=100)
_, deque_time = measure_time(insert_to_deque, iterations=100)

print(f"  Вставка в начало list:  {list_time:.4f} мс")
print(f"  Вставка в начало deque: {deque_time:.4f} мс")
print(f"  deque быстрее в {list_time/deque_time:.1f} раз")

print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 2: Оптимизация циклов
# ============================================================================

print("--- Оптимизация циклов ---")
print()  # Пустая строка

# Совет 4: Используйте генераторы списков вместо циклов
print("Совет 4: List comprehension vs обычный цикл")

# Обычный цикл
def squares_loop():
    result = []
    for i in range(1000):
        result.append(i ** 2)
    return result

# Генератор списка
def squares_comprehension():
    return [i ** 2 for i in range(1000)]

_, loop_time = measure_time(squares_loop, iterations=1000)
_, comp_time = measure_time(squares_comprehension, iterations=1000)

print(f"  Обычный цикл:           {loop_time:.4f} мс")
print(f"  List comprehension:     {comp_time:.4f} мс")
print(f"  comprehension быстрее в {loop_time/comp_time:.2f} раз")

print()  # Пустая строка

# Совет 5: Избегайте вызова len() в условии цикла
print("Совет 5: Оптимизация условия цикла")

data = list(range(1000))

# Неоптимально: len() вызывается на каждой итерации
def loop_with_len():
    i = 0
    result = 0
    while i < len(data):  # len() вызывается каждый раз
        result += data[i]
        i += 1
    return result

# Оптимально: len() вычисляется один раз
def loop_with_cached_len():
    i = 0
    result = 0
    length = len(data)  # Вычисляем один раз
    while i < length:
        result += data[i]
        i += 1
    return result

# Ещё лучше: используем for
def loop_with_for():
    result = 0
    for item in data:  # Итератор эффективнее
        result += item
    return result

# Лучше всего: используем sum()
def loop_with_sum():
    return sum(data)  # Встроенная функция

_, len_time = measure_time(loop_with_len, iterations=1000)
_, cached_time = measure_time(loop_with_cached_len, iterations=1000)
_, for_time = measure_time(loop_with_for, iterations=1000)
_, sum_time = measure_time(loop_with_sum, iterations=1000)

print(f"  while с len() в условии: {len_time:.4f} мс")
print(f"  while с кэшированным len: {cached_time:.4f} мс")
print(f"  for:                     {for_time:.4f} мс")
print(f"  sum():                   {sum_time:.4f} мс")

print()  # Пустая строка

# Совет 6: Используйте локальные переменные
print("Совет 6: Локальные vs глобальные переменные")

global_list = list(range(100))

# С глобальной переменной
def sum_global():
    total = 0
    for i in global_list:  # Доступ к глобальной переменной
        total += i
    return total

# С локальной переменной
def sum_local():
    local_list = global_list  # Копируем ссылку в локальную переменную
    total = 0
    for i in local_list:  # Доступ к локальной переменной быстрее
        total += i
    return total

_, global_time = measure_time(sum_global, iterations=10000)
_, local_time = measure_time(sum_local, iterations=10000)

print(f"  Глобальная переменная: {global_time:.4f} мс")
print(f"  Локальная переменная:  {local_time:.4f} мс")
print(f"  Локальная быстрее в {global_time/local_time:.2f} раз")

print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 3: Использование встроенных функций
# ============================================================================

print("--- Использование встроенных функций ---")
print()  # Пустая строка

# Совет 7: Используйте встроенные функции
print("Совет 7: Встроенные функции vs ручная реализация")

numbers = list(range(1000))

# Ручной поиск максимума
def manual_max():
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

# Встроенная функция max()
def builtin_max():
    return max(numbers)

_, manual_time = measure_time(manual_max, iterations=1000)
_, builtin_time = measure_time(builtin_max, iterations=1000)

print(f"  Ручной поиск max: {manual_time:.4f} мс")
print(f"  Встроенный max(): {builtin_time:.4f} мс")
print(f"  Встроенный быстрее в {manual_time/builtin_time:.2f} раз")

print()  # Пустая строка

# Совет 8: Используйте join() для конкатенации строк
print("Совет 8: join() vs конкатенация строк")

words = ["слово"] * 1000

# Конкатенация через += (создаёт новую строку каждый раз)
def concat_plus():
    result = ""
    for word in words:
        result += word  # O(n) на каждую итерацию
    return result

# Использование join() (одно выделение памяти)
def concat_join():
    return "".join(words)  # O(n) всего

_, plus_time = measure_time(concat_plus, iterations=100)
_, join_time = measure_time(concat_join, iterations=100)

print(f"  Конкатенация +=: {plus_time:.4f} мс")
print(f"  join():          {join_time:.4f} мс")
print(f"  join() быстрее в {plus_time/join_time:.2f} раз")

print()  # Пустая строка

# Совет 9: Используйте map() и filter() для простых преобразований
print("Совет 9: map()/filter() vs циклы")

numbers = list(range(1000))

# Цикл для возведения в квадрат
def squares_loop():
    return [x**2 for x in numbers]

# map() для возведения в квадрат
def squares_map():
    return list(map(lambda x: x**2, numbers))

_, loop_time = measure_time(squares_loop, iterations=1000)
_, map_time = measure_time(squares_map, iterations=1000)

print(f"  List comprehension: {loop_time:.4f} мс")
print(f"  map():              {map_time:.4f} мс")
# Примечание: для простых операций comprehension часто быстрее

print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 4: Кэширование и мемоизация
# ============================================================================

print("--- Кэширование и мемоизация ---")
print()  # Пустая строка

# Совет 10: Используйте lru_cache для кэширования результатов
print("Совет 10: lru_cache для мемоизации")

# Числа Фибоначчи без кэширования
def fib_no_cache(n):
    if n <= 1:
        return n
    return fib_no_cache(n-1) + fib_no_cache(n-2)

# Числа Фибоначчи с кэшированием
@lru_cache(maxsize=None)  # Кэшируем все результаты
def fib_cached(n):
    if n <= 1:
        return n
    return fib_cached(n-1) + fib_cached(n-2)

# Сравнение (используем маленькое n для no_cache, т.к. он очень медленный)
start = time.perf_counter()
result1 = fib_no_cache(30)
no_cache_time = (time.perf_counter() - start) * 1000

start = time.perf_counter()
result2 = fib_cached(30)
fib_cached.cache_clear()  # Очищаем кэш для честного сравнения
cached_time = (time.perf_counter() - start) * 1000

print(f"  fib(30) без кэша:  {no_cache_time:.2f} мс")
print(f"  fib(30) с кэшем:   {cached_time:.4f} мс")
print(f"  С кэшем быстрее в {no_cache_time/cached_time:.0f} раз")

# Для больших значений кэш критически важен
fib_cached.cache_clear()
start = time.perf_counter()
result = fib_cached(100)  # Было бы невозможно без кэша
cached_time = (time.perf_counter() - start) * 1000
print(f"  fib(100) с кэшем:  {cached_time:.4f} мс, результат: {result}")

print()  # Пустая строка

# Совет 11: Ручное кэширование для сложных случаев
print("Совет 11: Ручное кэширование")

# Кэш для хранения результатов
_cache = {}

def expensive_calculation(x):
    """Имитация дорогой операции"""
    if x in _cache:  # Проверяем кэш
        return _cache[x]

    # Дорогое вычисление
    time.sleep(0.001)  # Имитируем задержку
    result = x ** 2 + x * 3 + 1

    _cache[x] = result  # Сохраняем в кэш
    return result

# Первый вызов - вычисление
start = time.perf_counter()
result1 = expensive_calculation(42)
first_time = (time.perf_counter() - start) * 1000

# Второй вызов - из кэша
start = time.perf_counter()
result2 = expensive_calculation(42)
cached_time = (time.perf_counter() - start) * 1000

print(f"  Первый вызов (вычисление): {first_time:.2f} мс")
print(f"  Второй вызов (из кэша):    {cached_time:.4f} мс")

print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 5: Работа с генераторами
# ============================================================================

print("--- Работа с генераторами ---")
print()  # Пустая строка

# Совет 12: Используйте генераторы для экономии памяти
print("Совет 12: Генераторы vs списки")

import sys

# Список занимает много памяти
def get_squares_list(n):
    return [x**2 for x in range(n)]

# Генератор создаёт значения по требованию
def get_squares_generator(n):
    return (x**2 for x in range(n))

n = 10000

list_squares = get_squares_list(n)
gen_squares = get_squares_generator(n)

print(f"  Размер списка:     {sys.getsizeof(list_squares)} байт")
print(f"  Размер генератора: {sys.getsizeof(gen_squares)} байт")

# Генератор можно итерировать только один раз!
# Если нужно многократное использование - создайте список

print()  # Пустая строка

# Совет 13: Используйте itertools для эффективных итераций
print("Совет 13: Использование itertools")

import itertools

# chain - объединение нескольких итерируемых объектов
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

# Неэффективно: создаёт новый список
combined_list = list1 + list2 + list3

# Эффективно: создаёт итератор
combined_iter = itertools.chain(list1, list2, list3)
print(f"  chain: {list(combined_iter)}")

# islice - срез для итераторов
big_range = range(1000000)
first_five = list(itertools.islice(big_range, 5))
print(f"  islice: {first_five}")

# groupby - группировка последовательных элементов
data = [("a", 1), ("a", 2), ("b", 3), ("b", 4), ("a", 5)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(f"  groupby '{key}': {list(group)}")

print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 6: Оптимизация работы со строками
# ============================================================================

print("--- Оптимизация работы со строками ---")
print()  # Пустая строка

# Совет 14: Используйте f-строки вместо format() или %
print("Совет 14: f-строки vs format() vs %")

name = "Алексей"
age = 30

def format_percent():
    return "Имя: %s, Возраст: %d" % (name, age)

def format_method():
    return "Имя: {}, Возраст: {}".format(name, age)

def format_fstring():
    return f"Имя: {name}, Возраст: {age}"

_, percent_time = measure_time(format_percent, iterations=10000)
_, format_time = measure_time(format_method, iterations=10000)
_, fstring_time = measure_time(format_fstring, iterations=10000)

print(f"  % форматирование: {percent_time:.4f} мс")
print(f"  .format():        {format_time:.4f} мс")
print(f"  f-строка:         {fstring_time:.4f} мс")

print()  # Пустая строка

# Совет 15: Используйте str методы вместо регулярных выражений для простых операций
print("Совет 15: str методы vs регулярные выражения")

import re

text = "Hello, World! Hello, Python!"

# Регулярное выражение
def count_with_regex():
    return len(re.findall("Hello", text))

# Строковый метод
def count_with_str():
    return text.count("Hello")

_, regex_time = measure_time(count_with_regex, iterations=10000)
_, str_time = measure_time(count_with_str, iterations=10000)

print(f"  re.findall():  {regex_time:.4f} мс")
print(f"  str.count():   {str_time:.4f} мс")
print(f"  str метод быстрее в {regex_time/str_time:.2f} раз")

print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 7: Профилирование кода
# ============================================================================

print("--- Профилирование кода ---")
print()  # Пустая строка

# Совет 16: Используйте профилировщик для поиска узких мест
print("Совет 16: Использование cProfile")

import cProfile
import pstats
import io

def function_to_profile():
    """Функция для профилирования"""
    result = []
    for i in range(1000):
        result.append(i ** 2)
    return sum(result)

# Создаём профилировщик
profiler = cProfile.Profile()
profiler.enable()  # Включаем профилирование

# Выполняем код
for _ in range(100):
    function_to_profile()

profiler.disable()  # Выключаем профилирование

# Выводим статистику
stream = io.StringIO()
stats = pstats.Stats(profiler, stream=stream)
stats.sort_stats("cumulative")  # Сортируем по общему времени
stats.print_stats(5)  # Выводим топ-5

print("  Результат профилирования (топ-5):")
for line in stream.getvalue().split('\n')[:10]:
    if line.strip():
        print(f"  {line}")

print()  # Пустая строка

# Совет 17: Используйте timeit для точных измерений
print("Совет 17: Использование timeit")

import timeit

# timeit автоматически выполняет множество итераций
list_comp_time = timeit.timeit("[x**2 for x in range(100)]", number=10000)
map_time = timeit.timeit("list(map(lambda x: x**2, range(100)))", number=10000)

print(f"  List comprehension: {list_comp_time:.4f} секунд")
print(f"  map():              {map_time:.4f} секунд")

print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 8: Общие рекомендации
# ============================================================================

print("--- Общие рекомендации ---")
print()  # Пустая строка

print("""
╔══════════════════════════════════════════════════════════════════╗
║                    СОВЕТЫ ПО ОПТИМИЗАЦИИ                        ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  СТРУКТУРЫ ДАННЫХ:                                               ║
║  • Используйте set для проверки принадлежности (O(1) vs O(n))   ║
║  • Используйте dict для поиска по ключу                         ║
║  • Используйте deque для операций в начале/конце                ║
║  • Выбирайте правильную структуру под задачу                    ║
║                                                                  ║
║  ЦИКЛЫ:                                                          ║
║  • Предпочитайте list comprehensions                             ║
║  • Кэшируйте len() и другие вычисления вне цикла                ║
║  • Используйте локальные переменные вместо глобальных           ║
║  • Избегайте ненужных операций внутри цикла                     ║
║                                                                  ║
║  ВСТРОЕННЫЕ ФУНКЦИИ:                                             ║
║  • sum(), max(), min(), len() - быстрее ручной реализации       ║
║  • join() - для конкатенации строк                               ║
║  • sorted() с key - для сортировки                               ║
║  • any(), all() - для проверки условий                           ║
║                                                                  ║
║  КЭШИРОВАНИЕ:                                                    ║
║  • @lru_cache - для чистых функций с повторяющимися вызовами    ║
║  • Ручное кэширование - для сложных случаев                     ║
║  • Предвычисление - если данные известны заранее                ║
║                                                                  ║
║  ПАМЯТЬ:                                                         ║
║  • Генераторы - для обработки больших данных                    ║
║  • itertools - для эффективных итераций                          ║
║  • __slots__ - для уменьшения памяти объектов                   ║
║                                                                  ║
║  ПРОФИЛИРОВАНИЕ:                                                 ║
║  • cProfile - для поиска узких мест                              ║
║  • timeit - для точного измерения времени                        ║
║  • memory_profiler - для анализа памяти                          ║
║                                                                  ║
║  ГЛАВНОЕ ПРАВИЛО:                                                ║
║  "Преждевременная оптимизация - корень всех зол"                ║
║  Сначала напишите работающий код, потом оптимизируйте           ║
║  только там, где это действительно нужно!                       ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
""")

print()  # Пустая строка

# ============================================================================
# РАЗДЕЛ 9: Практические примеры оптимизации
# ============================================================================

print("--- Практические примеры оптимизации ---")
print()  # Пустая строка

# Пример 1: Удаление дубликатов с сохранением порядка
print("Пример 1: Удаление дубликатов")

data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8]

# Неоптимально: O(n²)
def remove_duplicates_slow(lst):
    result = []
    for item in lst:
        if item not in result:  # O(n) проверка
            result.append(item)
    return result

# Оптимально: O(n)
def remove_duplicates_fast(lst):
    seen = set()  # O(1) проверка
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Ещё короче с dict (Python 3.7+ сохраняет порядок)
def remove_duplicates_dict(lst):
    return list(dict.fromkeys(lst))

_, slow_time = measure_time(remove_duplicates_slow, data, iterations=1000)
_, fast_time = measure_time(remove_duplicates_fast, data, iterations=1000)
_, dict_time = measure_time(remove_duplicates_dict, data, iterations=1000)

print(f"  Медленный способ: {slow_time:.4f} мс")
print(f"  Быстрый способ:   {fast_time:.4f} мс")
print(f"  Через dict:       {dict_time:.4f} мс")

print()  # Пустая строка

# Пример 2: Подсчёт элементов
print("Пример 2: Подсчёт элементов")

from collections import Counter

text = "hello world hello python hello world python programming"
words = text.split()

# Ручной подсчёт
def count_manual(lst):
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    return counts

# С использованием Counter
def count_counter(lst):
    return dict(Counter(lst))

_, manual_time = measure_time(count_manual, words, iterations=10000)
_, counter_time = measure_time(count_counter, words, iterations=10000)

print(f"  Ручной подсчёт: {manual_time:.4f} мс")
print(f"  Counter:        {counter_time:.4f} мс")

print()  # Пустая строка

# Пример 3: Проверка анаграмм
print("Пример 3: Проверка анаграмм")

def are_anagrams_sort(s1, s2):
    """Проверка через сортировку - O(n log n)"""
    return sorted(s1.lower()) == sorted(s2.lower())

def are_anagrams_counter(s1, s2):
    """Проверка через Counter - O(n)"""
    return Counter(s1.lower()) == Counter(s2.lower())

s1 = "listen"
s2 = "silent"

_, sort_time = measure_time(are_anagrams_sort, s1, s2, iterations=10000)
_, counter_time = measure_time(are_anagrams_counter, s1, s2, iterations=10000)

print(f"  Через сортировку: {sort_time:.4f} мс, результат: {are_anagrams_sort(s1, s2)}")
print(f"  Через Counter:    {counter_time:.4f} мс, результат: {are_anagrams_counter(s1, s2)}")

print()  # Пустая строка

# ============================================================================
# ИТОГИ МОДУЛЯ 8
# ============================================================================

print("=" * 60)  # Печатаем разделитель
print("ИТОГИ МОДУЛЯ 8: Советы по оптимизации производительности")
print("=" * 60)
print("""
Вы изучили:
✓ Выбор правильных структур данных (set, dict, deque)
✓ Оптимизацию циклов и использование comprehensions
✓ Использование встроенных функций (sum, max, join)
✓ Кэширование с @lru_cache и ручное кэширование
✓ Работу с генераторами и itertools
✓ Оптимизацию работы со строками
✓ Профилирование с cProfile и timeit
✓ Практические примеры оптимизации
""")
print("=" * 60)
print()
print("ПОЗДРАВЛЯЕМ! Вы завершили курс Python!")
print()
print("Теперь вы знаете:")
print("  • Основы синтаксиса Python")
print("  • Работу с данными и переменными")
print("  • Условия и циклы")
print("  • Функции и их возможности")
print("  • Структуры данных")
print("  • Объектно-ориентированное программирование")
print("  • Приёмы оптимизации кода")
print()
print("Продолжайте практиковаться и изучать Python!")
print("=" * 60)
