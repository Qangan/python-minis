#mentally ill solve
#print((lambda x: [list(map(float, i.strip().split())) for i in x.split("|")])(input())[int(input())][int(input())])

def matrix(string_matrix):
    result = []
    for i in string_matrix.split('|'):
        result.append(list(map(float, i.strip().split()))) # converting to float list from splitting stripped string
    return result

assert(matrix("1 2 | 2 3.33333")[1][1] == 3.33333)
assert(matrix("1")[0][0] == 1)
assert(matrix("1 2 3 4 5 | 1 2 3 4 5 | 1 2 0 0 0")[2][4] == 0)

