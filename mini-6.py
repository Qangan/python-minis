def flatten(ll, depth=-1):
    if depth != 0:
        flattened = []
        for l in ll:
            if isinstance(l, list):
                flattened.extend(flatten(l, depth-1))
            else:
                flattened.append(l)
        ll = flattened
    return ll

assert(flatten([1,2,3,[1,[2,[3]]]]) == [1,2,3,1,2,3])
assert(flatten([1,2,3,[1,[2,[3]]]], depth=0) == [1,2,3,[1,[2,[3]]]])
assert(flatten([1,2,3,[1,[2,[3]]]], depth=1) == [1,2,3,1,[2,[3]]])
assert(flatten([1,2,3,[1,[2,[3]]]], depth=2) == [1,2,3,1,2,[3]])
assert(flatten([1,2,3,[1,[2,[3]]]], depth=3) == [1,2,3,1,2,3])
assert(flatten([1,2,3,[1,[2,[3]]]], depth=100000) == [1,2,3,1,2,3])
