# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
# Какое самое маленькое число делится нацело на все числа от 1 до 20?

dividend = 1

# Поиск числа
while True:
    status = True
    for divider in range(1, 21):
        if dividend % divider != 0:
            status = False
            break
    if status:
        break
    dividend += 1

# Проверка значения
for divider in range(1, 21):
    print(dividend, "делить на", divider, "равно:", dividend / divider)

print("Наименьшее число, нацело делящееся на все числа от 1 до 20:",
      dividend)  # 232792560
