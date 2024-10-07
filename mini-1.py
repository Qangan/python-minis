from math import *
def get_ones_from_int(n: int) -> int:
    counter = 0
    if n < 0:
        n = ~n
        for i in range(31):
            counter += ((n & (1 << i)) > 0)
        counter = 1 + (floor(log2(n)) + 1) - counter # один за знаковый бит, длина битового представления [log2 n] + 1
    else:
        for i in range(31):
            counter += ((n & (1 << i)) > 0)
    return counter
n = int(input("Enter the number: "))
print(get_ones_from_int(n))
     
