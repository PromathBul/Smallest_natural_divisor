import os
import time

os.system('cls')

number = int(input('Введите число: '))

start = time.time()

list = [i for i in range(2, number + 1) if number % i == 0]
print(list[0])

end = time.time()
print(end - start)

def search_smallest_divisor(number):
    divisor = 2
    if number % divisor == 0:
            return divisor
    else:
        while number % divisor != 0:
            divisor += 1
        return divisor

start = time.time()

result = search_smallest_divisor(number)
print(result)

end = time.time()
print(end - start)