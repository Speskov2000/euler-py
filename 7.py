# Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13.
# Очевидно, что 6-е простое число - 13.
# Какое число является 10001-м простым числом?

# Массив с простыми числами, на которые будем делить будущие перебираемые числа
dividers = [2]
indexNumber = 1
number = 3
while True:
    counter = 0
    for divider in dividers:
        if number % divider == 0:            
            counter += 1
            break
    if counter == 0:
        dividers.append(number)
        indexNumber += 1

    if indexNumber == 10001:
        break
    number += 1

print("Простое число под номером 10001 -", number)