# Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
#
# Найдите сумму всех простых чисел меньше двух миллионов.
import math

dividers = [2]
number = 0

for number in range(3, 2000000, 2):
    status = True
    sqrtNumber = math.ceil(number**0.5)
    for divider in dividers:        
        if divider > sqrtNumber:
            break
        if number % divider == 0:
            status = False
            break
    if status:
        dividers.append(number)

print ("Сумма всех простых чисел меньше двух миллионов =", sum(dividers))