import math

"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(s: list) -> list:
    a = []
    for i in s:
        a.append(i**2)
    return a
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def check_odd (n: int) -> bool:
    if n%2 == 0:
        return True
    else:
        return False

def check_prime (n: int) -> bool:
    counter = 0
    #print("n=", n)
    for i in range (1, n+1):
        if n % i == 0:
            counter+=1
            #print(i, " counter = ", counter)
    if counter > 2:
        return False
    else:
        return True

def filter_numbers(s: list, id) -> list:
    a = []
    if id == "ODD":
        for i in s:
            if check_odd(i) == True:
                a.append(i)
        return a
    elif id == "EVEN":
        for i in s:
            if check_odd(i) == False:
                a.append(i)
        return a
    elif id == "PRIME":
        for i in s:
            if check_prime(i) == True:
                a.append(i)
        return a
    else:
        print("Nothing successfull")
        return a

    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
//    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
//    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """


s = [1, 2, 5, 8, 13, 15, 27, 81, 100]
print(power_numbers(s))
print(filter_numbers(s, "ODD"))
print(filter_numbers(s, "EVEN"))
print(filter_numbers(s, "PRIME"))