def chain(*arrs):
    for arr in arrs:
        yield from arr

def cycle(arr):
    content = []
    for i in arr:
        yield i
        content.append(i)
    while content:
        for i in content:
            yield i

def take(arr, n):
    i = 0
    for j in arr:
        if i < n:
            yield j
            i += 1
        else:
            break

print(list(take(cycle([1,2,3]), 10)))
print(list(chain('goyda', 'medved', [1,2,3], ('test',))))
