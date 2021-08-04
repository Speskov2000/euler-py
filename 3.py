# Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?
#################################################################################################################
# Решение подсмотрел.
# import math
# def issimple(a):
#     r=math.ceil(math.sqrt(a))
#     lst=[]
#     for i in range(3,r):
#         if a%i==0:
#             if issimple(i)==[]:lst.append(i)
#     return lst
# r=issimple(600851475143)
# print(r)


#################################################################################################################
# Это работает, но не для больших чисел. Мой код.
import math

def isPrimeFactor(num):
    numSqrt = math.ceil(math.sqrt(num))
    for divider in range(2, numSqrt):
        if num % divider == 0:
            return False
    return True 

mainNumber = 600851475143
number = math.ceil(math.sqrt(mainNumber))
largestPrimeFactor = 1

for divider in range(2, number):
    if mainNumber % divider == 0 and isPrimeFactor(divider):
        largestPrimeFactor = divider
        print (divider)

print ("Наибольший делитель числа 600851475143 равен:", largestPrimeFactor)