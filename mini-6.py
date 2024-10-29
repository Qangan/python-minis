def flatten(ll, depth=None):
    def unpack_list(l):
        if type(l) == list:
            return l
        else:
            return [l]
    if depth == None:
        while sum(map(lambda x: type(x) == list, ll)) != 0:
            ll = [unpack_list(i)[j] for i in ll for j in range(len(unpack_list(i)))]
        return ll
    else:
        for i in range(depth):
             ll = [unpack_list(i)[j] for i in ll for j in range(len(unpack_list(i)))]
        return ll
print(flatten([1,2,3,[1,[2,3]]], depth=0))

