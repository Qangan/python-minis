def actually_count_bits(n: int) -> list:
    counter, n_len = 0, 0
    while n > 0:
        counter += n & 1
        n >>= 1
        n_len += 1
    if counter == n_len:
        n_len += 1
    return [counter, n_len]
def get_ones_from_int(n: int) -> int:
    counter = 0
    if n < 0:
        n = ~n
        result = actually_count_bits(n)
        return result[1] - result[0] + 1
    else:
        result = actually_count_bits(n)
        return result[0]
n = int(input("Enter the number: "))
print(get_ones_from_int(n))
