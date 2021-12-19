from tz3 import sum_numb, prod_numb, min_numb, max_numb, read_file, name_file
from random import randint
from math import prod
from time import time


def random_mas(length, min_n, max_n):
    result = []
    for i in range(length):
        result.append(randint(min_n, max_n))
    return result


def test_sum_numb():
    if test_correct_input_file():
        massiv = read_file(name_file)
    else:
        massiv = random_mas(10, 0, 100)
    assert sum(massiv) == sum_numb(massiv)


def test_prod_numb():
    if test_correct_input_file():
        massiv = read_file(name_file)
    else:
        massiv = random_mas(10, 0, 100)
    assert prod(massiv) == prod_numb(massiv)


def test_min_numb():
    if test_correct_input_file():
        massiv = read_file(name_file)
    else:
        massiv = random_mas(10, 0, 100)
    assert min(massiv) == min_numb(massiv)


def test_max_numb():
    if test_correct_input_file():
        massiv = read_file(name_file)
    else:
        massiv = random_mas(10, 0, 100)
    assert max(massiv) == max_numb(massiv)


def test_time():
    start_time = time()
    massiv = random_mas(10, 0, 100)
    sum_numb(massiv)
    prod_numb(massiv)
    max_numb(massiv)
    min_numb(massiv)
    end_time = time()
    time_1 = end_time - start_time
    start_time = time()
    massiv = random_mas(10000, 0, 100)
    sum_numb(massiv)
    prod_numb(massiv)
    max_numb(massiv)
    min_numb(massiv)
    end_time = time()
    time_2 = end_time - start_time
    assert (time_2 > time_1)


def test_correct_input_file():
    k = True
    try:
        read_file(name_file)
    except ValueError:
        k = False
    return k
