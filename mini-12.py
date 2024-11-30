def coroutine(f):
    def coroutine_next(*args, **kwargs):
        coroutine_func = f(*args, **kwargs);
        next(coroutine_func)
        return coroutine_func
    return coroutine_next

def storage():
    values = set()
    was_there = False

    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)

@coroutine
def cstorage():
    values = set()
    was_there = False

    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)




st = storage()
try:
    print(st.send(42)) 
    print(st.send(42)) 
except TypeError:
    print("Here is error!")

cst = cstorage()
print(cst.send(42)) 
print(cst.send(42)) 

