def test_correct_input_file(name):
    k = True
    try:
        read_file(name)
    except ValueError:
        k = False
    return k


def read_file(name):
    f = open(name, 'rt')
    spisok = list(map(int, f.read().split()))
    return spisok


def sum_numb(mas):
    summa = 0
    for i in range(len(mas)):
        summa += mas[i]
    return summa


def prod_numb(mas):
    prod_n = 1
    for i in range(len(mas)):
        prod_n *= mas[i]
    return prod_n


def min_numb(mas):
    mas.sort()
    min_n = mas[0]
    return min_n


def max_numb(mas):
    mas.sort()
    max_n = mas[-1]
    return max_n


name_file = 'Homework3/test.txt'
if test_correct_input_file(name_file):
    sp = read_file(name_file)
    try:
        s = sum_numb(sp)
        pr = prod_numb(sp)
        mx = max_numb(sp)
        mn = min_numb(sp)
        print(f'Сумма чисел: {s}; Произведение чисел: {pr}; Максимум: {mx}; Минимум: {mn}')
    except OverflowError:
        print("Числа в файле слишком большие")
else:
    print('В файле присутствуют значения не типа int')
