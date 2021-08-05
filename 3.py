# Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?
########################################################################################

import math

# Функция для определения простоты
def isPrimeFactor(num):
    numSqrt = math.ceil(math.sqrt(num))
    for divider in range(2, numSqrt):
        if num % divider == 0:
            return False
    return True 

mainNumber = 600851475143
number = math.ceil(math.sqrt(mainNumber))
largestPrimeFactor = 1 # Наибольший просто делитель

# Нахождение половины простых делителей (до корня)
allDividers = []
for divider in range(2, number):
    if mainNumber % divider == 0 and isPrimeFactor(divider):        
        allDividers.append(divider)

temporaryDividers = allDividers.copy()

# Проверка потенциальной второй половины делителей на простоту (после корня)
for divider in temporaryDividers:
    allDividers.append(int(mainNumber/divider))
allDividers.sort()

# Нахождение максимального простого делителя
for i in allDividers:
    if isPrimeFactor(i) and i > largestPrimeFactor:
        largestPrimeFactor = i

print ("Наибольший делитель числа 600851475143 равен:", largestPrimeFactor)