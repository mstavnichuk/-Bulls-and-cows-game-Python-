# Усложненное задание (делать по желанию)

# Реализовать модуль искусственного интеллекта для отгадывания числа
# Функции ИИ:
#  выдать_вариант_числа()
#  получить_количество_быков_и_коров()

# Сделать модуль авто-игры (auto_mastermind):
#   модуль движка загадывает число
#   модуль ИИ отгадывает
#   протокол вопросов-ответов выводить на консоль


from mastermind_engine import generate_number, compare_numbers
from itertools import permutations

generate_number()
digits = []
for i in range(0, 10):
    string = str(i) * 4
    hits = compare_numbers(string)
    print(string, hits)
    if hits['bulls'] != 0:
        digits.append(i)

all_variants = permutations(digits)
for variant in all_variants:
    string = ''
    for _ in range(0, 4):
        string += str(variant[_])
    hits = compare_numbers(string)
    print(string, hits)
    if hits['bulls'] == 4:
        print('Было загадано число ', string)
        break


