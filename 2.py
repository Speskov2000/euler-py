# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... 

print ("Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.")
sum = 0

number = 1
previosNumber = number

while number < 4000000:
    if number % 2 == 0:
        sum += number
    temp = number
    number += previosNumber    
    previosNumber = temp
    
print (sum)