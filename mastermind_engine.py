from random import randint

def generate_number():
    global number
    number = str(randint(1000, 9999))
    i = 0
    while i <= 3:
        if number.count(number[i]) > 1:
            number = str(randint(1000, 9999))
            i = 0
        else:
            i += 1


def compare_numbers(called_number):
    global bulls
    cows = 0
    bulls = 0
    for i in range(0, 4):
        if number[i] == called_number[i]:
            bulls += 1
        if number.count(called_number[i]) == 1 and number[i] != called_number[i]:
            cows += 1
    print("Быков - ", bulls, ", Коров - ", cows)


def is_game_over():
    return bulls == 4
