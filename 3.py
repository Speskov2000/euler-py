# Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?
########################################################################################

import math


# Функция для определения простоты числа
def isPrimeFactor(num):
    numSqrt = math.ceil(math.sqrt(num))
    for divider in range(2, numSqrt):
        if num % divider == 0:
            return False
    return True


mainNumber = 600851475143
number = math.ceil(math.sqrt(mainNumber))
largestPrimeFactor = 1  # Наибольший простой делитель

# Нахождение половины делителей (до корня)
allDividers = []
for divider in range(2, number):
    if mainNumber % divider == 0:
        allDividers.append(divider)

temporaryDividers = allDividers.copy()

# Нахождение второй половины делителей (после корня)
for divider in temporaryDividers:
    allDividers.append(int(mainNumber / divider))

#упорядочивание
allDividers.sort()

# Нахождение максимального простого делителя
for i in allDividers:
    if isPrimeFactor(i):
        largestPrimeFactor = i

print("Наибольший делитель числа 600851475143 равен:", largestPrimeFactor)
