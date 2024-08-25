# Дан одномерный массив числовых значений, насчитывающий N элементов. Добавить к
# элементам массива такой новый элемент, чтобы сумма элементов с положительными
# значениями стала бы равна модулю суммы элементов с отрицательными значениями.

numbers = input('Введите последовательность положительных и отрицательных чисел через пробел: ').split()

def balanced_number(numbers):
    numbers = [int(i) for i in numbers]

    positive_numbers = []
    negative_numbers = []

    for number in numbers:
        if number >= 0:
            positive_numbers.append(number)
        else:
            negative_numbers.append(number)
    
    sum_pos = 0
    for number in positive_numbers:
        sum_pos = sum_pos + number

    sum_neg = 0
    for number in negative_numbers:
        sum_neg = sum_neg + abs(number)

    if sum_pos > sum_neg:
        balance = sum_pos - sum_neg
    elif sum_pos < sum_neg:
        balance = sum_neg - sum_pos
    else:
        balance = 0
    
    numbers.append(balance)
    
    print(sum_pos)
    print(sum_neg)
    print('need', balance)
    print(numbers)

balanced_number(numbers)