# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
# Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
# ###########################################################################################################

# Функция определяющая является ли число палиндромом
def isPalindrome(number):
    originalNumberStr = str(number)
    reversedNumberStr = originalNumberStr[::-1]
    return originalNumberStr == reversedNumberStr


maxPalindrome = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        number = i*j
        if isPalindrome(number) and maxPalindrome < number:
            maxPalindrome = number

print ("Самый большой палиндром, полученный умножением двух трехзначный чисел -", maxPalindrome)
