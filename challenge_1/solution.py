NUMERALS = {  # noqa: WPS407
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1,
}


def descending(pair):
    return -pair[1]


def to_roman(number):
    result = ''
    for roman, arabic in sorted(NUMERALS.items(), key=descending):
        repetitions_count = number // arabic
        number -= arabic * repetitions_count
        result += roman * repetitions_count
    return result


def to_arabic(number):  # noqa: WPS210
    numbers = []
    for char in number:
        numbers.append(NUMERALS[char])
    # Сдвиг чисел с повтором последнего
    # Пример: [1,2,3,4] -> [2,3,4,4]
    shifted_numbers = numbers[1:] + numbers[-1:]
    result = 0
    for previous, current in zip(numbers, shifted_numbers):
        if previous >= current:
            result += previous
        else:
            result -= previous
    if to_roman(result) != number:
        return False
    return result