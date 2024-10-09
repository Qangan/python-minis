def actually_count_bits(n: int) -> tuple:
    counter, n_len = 0, 0
    while n > 0:
        counter += n & 1
        n >>= 1
        n_len += 1
    if counter == n_len:
        n_len += 1
    return counter, n_len
def get_ones_from_int(n: int) -> int:
    if n < 0:
        n = ~n
        result, n_len = actually_count_bits(n)
        return n_len - result + 1
    else:
        result, _ = actually_count_bits(n)
        return result
n = int(input("Enter the number: "))
print(get_ones_from_int(n))
