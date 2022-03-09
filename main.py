from fractions import Fraction as F
import re

#В видите вырожение
#Пример может содержать дроби и целые числа с использованием знака "/"

#ВЫРАЖЕНИЕ
a = "(1+1/2)*2 : 2"

#remove spaces
s = re.sub('\s+', '', a)
s = s.replace(':', '/')
#
s = re.sub(r'(\d+/\d+)', r'F(\1)', s)

res = eval(s)
print(f"{a} = {res}")
print(f"{a} = {eval(str(res))}")

