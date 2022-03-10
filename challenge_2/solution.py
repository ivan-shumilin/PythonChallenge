# Определяем функцию для вычисления факториала
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


def triangle(row_number):
    numbers_count = row_number + 1
    line = []
    for i in range(numbers_count):
        # Для вычисления числа заданной строки используем формулу
        # расчёта биноминальных коэффициентов С(n, k) = n! / (k! * (n - k)!)
        line.append(fact(row_number) / (fact(i) * fact(row_number - i)))
    return line