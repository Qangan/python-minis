#mentally ill solve
#print((lambda x: {val: (tuple(filter(lambda z: x[z] == val, x)) if list(x.values()).count(val) > 1 else list(filter(lambda y: x[y] == val, x))[0]) for val in x.values()})({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}))

def reverse_dict(source):
    result = {}
    for val in source.values():
        if len(tuple(filter(lambda x: source[x] == val, source.keys()))) > 1:
            result[val] = tuple(filter(lambda v: source[v] == val, source))
        else:
            result[val] = list(filter(lambda v: source[v] == val, source))[0]
    return result


assert(reverse_dict({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}) == {97832: ("Ivanov", "Kuznecov"), 55521: "Petrov"})
assert(reverse_dict({"Goyda": "goyda", "Test1": "goyda", "skillissue": 123}) == {"goyda": ("Goyda", "Test1"), 123: "skillissue"})
try:
    assert(reverse_dict({420: 1337, "@Huawei": "Excelsior", []: "nonhashable"}) == {"Excelsior": "@Huawei", 1337: 420, "nonhashable": ([])})
except Exception as err:
    print("It breaks on unhashable types")
