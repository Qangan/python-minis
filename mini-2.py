#mentally ill solve
#print((lambda x, y: ([(x[i], y[i]) for i in range(min(len(x), len(y)))]))(eval('[' + ', '.join(input().split()) + ']'), eval('[' + ', '.join(input().split()) + ']')))

def zip4anything(f, s):
    result = []
    for i in range(min(len(f), len(s))):
        result.append((f[i], s[i]))
    return result


assert(zip4anything([1, 2, 3, 4], [[], ()]) == [(1, []), (2, ())])
assert(zip4anything(['first'], ['goyda', 'meow']) == [('first', 'goyda')])
assert(zip4anything([1, []], ['', {}]) == [(1, ''), ([], {})])
