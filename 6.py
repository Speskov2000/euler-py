# Сумма квадратов первых десяти натуральных чисел равна
# 12 + 22 + ... + 102 = 385
# Квадрат суммы первых десяти натуральных чисел равен
# (1 + 2 + ... + 10)2 = 552 = 3025
# Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет 3025 − 385 = 2640.
# Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.

def getSum():
    sum = 0
    for naturalNum in range(1,101):
        sum += naturalNum
    return sum

def getSumOfTheSquares():
    sumOfTheSquares = 0
    for naturalNum in range(1,101):
        sumOfTheSquares += naturalNum**2
    return sumOfTheSquares


sumOfTheSquares = getSumOfTheSquares()
squareOfTheSum = getSum()**2
difference = squareOfTheSum - sumOfTheSquares

print("Сумма квадратов первых 100 натуральных числе =", sumOfTheSquares)
print("Квадрат суммы первых 100 натуральных числе =", squareOfTheSum)
print("Разность между квадратом суммы и суммой квадратов =", difference)