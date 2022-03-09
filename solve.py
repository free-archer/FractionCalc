from fractions import Fraction as F
import re

#В видите вырожение
#Пример может содержать дроби и целые числа с использованием знака "/" без пробела
#Между знаками и числами должен быть обязательно пробел

#ВЫРАЖЕНИЕ
a = "1+1/2*2"

#ПРОГРАММА
a = re.sub('\s+', '', a)
l = re.findall('(\d+/\d+|\d+|\d+\.\d+)([-*+:])', a)
e = re.findall('(\d+/\d+|\d+|\d+\.\d+)$', a)
mainlist = l + e
print(mainlist)

s = ''
for i in mainlist:
    if isinstance(i, tuple):
        val = i[0]
        if i[1] == ':':
            znak = '/'
        else:
            znak = i[1]

    else:
        val = i
        znak = ''

    s = s + f'F("{val}"){znak}'

res = eval(s)
print(f"{a} = {res}")
print(f"{a} = {eval(str(res))}")

