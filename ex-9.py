# Напишите программу, в которой разбивается строка по нескольким разделителям.
import re
str_ = input('Введите строку: ')

pattern = r'[.,;:]\s'

result = re.split(pattern, str_)
print(result)