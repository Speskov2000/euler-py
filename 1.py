print ("Найдите сумму всех чисел меньше 1000, кратных 3 или 5.")

sum = 0

# number = 1
# while number < 1000:
#     if number % 3 == 0 or number % 5 == 0:
#         sum += number    
#     number += 1

for number in range(1000):
    if number % 3 == 0 or number % 5 == 0:
        sum += number

print ("Сумма равна:", sum)