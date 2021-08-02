print ("Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.")

# step = 1
# for number in range(0, 10, step):
#     step = number
#     sum += number
#     print (number)


number = 1
previosNumber = number

while number < 100:
    print (number)
    temp = number
    number += previosNumber    
    previosNumber = temp
    

print (sum)