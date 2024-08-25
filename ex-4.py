# Дан список чисел (содержащий не менее двух элементов). Найдите в нем два 
# ближайших друг к другу числа (то есть два числа с наименьшей разностью).
# Выведите эти числа в порядке не убывания.
# Используйте встроенную сортировку языка Python. Решение должно иметь сложность 
# встроенной сортировки + O(n).

list_A = input('Введите последовательность чисел через пробел: ').split()
list_A = [int(i) for i in list_A]
list_A.sort(reverse=True)

def two_nearest_numbers(list_A):
    differences = []
    result = []
    for index in range(len(list_A) - 1): 
        dif = list_A[index] - list_A[index + 1]
        differences.append(dif)
    differences.sort()
 
    for index in range(len(list_A) - 1):
        dif = list_A[index] - list_A[index + 1]
        if dif == differences[0]:
            result.append([list_A[index + 1], list_A[index]])
    return result

resultat = two_nearest_numbers(list_A)
print(resultat)