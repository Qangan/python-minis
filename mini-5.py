def specialize(f, *args, **kwargs):
    def ret_function(*ret_args):
        given_args = args + ret_args
        return f(*given_args, **kwargs)
    return ret_function

def mult_sum(*args):
    result = sum(args)
    return result

def summ(x, y):
    return x + y

plus_two = specialize(summ, y = 2)
multi_sum = specialize(mult_sum, 1, 2, 3, 4, 5, 6, 7)

assert(plus_two(1) == summ(1, y = 2))
assert(multi_sum(8) == mult_sum(1,2,3,4,5,6,7,8))
assert((x := specialize(summ, y=2))(1) == 3)
