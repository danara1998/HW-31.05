# Напишите программу, в которой извлекаются слова, начинающиеся на гласную букву.
import re
text = input('Введите любой текст кириллицей: ').split()
pattern = r'[]*[а,о,у,э,ы,я,ё,ю,е,и,А,О,У,Э,Ы,Я,Ё,Ю,Е,И][а-я]\S*'

for word in text:
    match = re.fullmatch(pattern, word)
    if match is not None:
        print(word)