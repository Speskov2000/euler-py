# Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?

import math
def issimple(a):
    r=math.ceil(math.sqrt(a))
    lst=[]
    for i in range(3,r):
        if a%i==0:
            if issimple(i)==[]:
                lst.append(i)
    return lst

dividers=issimple(26)
max = dividers
for divider in dividers:
    if divider < max:
        max = divider

print (max)





# Это работает, но не для больших чисел.
# def isPrimeFactor(number):    
#     for divider in range(2, number):
#         if number%divider==0:return False
#     return True 

# largestPrimeFactor = 1
# for i in range(1, 600851475144):
#     if 600851475143 % i == 0:
#         if isPrimeFactor(i):
#             largestPrimeFactor = i

# print ("Наибольший делитель числа 600851475143 равен:", largestPrimeFactor)