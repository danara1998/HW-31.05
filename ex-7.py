# Напишите программу, в которой возвращаются домены из списка e-mail адресов.
import re
emails = input('Введите email адреса через пробел: ').split()
pattern = r'@'
for email in emails:
    domen = re.split(pattern, email)
    print(domen[1])