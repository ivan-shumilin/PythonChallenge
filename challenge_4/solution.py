def count_bits(number):
    result = '' if number > 0 else '0'
    while number > 0:
        result = str(number % 2) + result
        number = number // 2
    return result.count('1')

