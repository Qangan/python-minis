from functools import wraps

def deprecated(func=None, *, since=None, will_be_removed=None):
    
    if func is None:
        return lambda f: deprecated(f, since=since, will_be_removed=will_be_removed)
    
    @wraps(func)
    def deprecat(*args, **kwargs):
        name = func.__name__
        since_message = f'Warning: function {name} is deprecated since version {since}. '
        nosince_message = f'Warning: function {name} is deprecated. '
        iwbrm = "It will be removed in "
        ftr = "future versions."
        vers = f"version {will_be_removed}"
        
        if since and will_be_removed:
            print(since_message + iwbrm + vers)
        elif since:
            print(since_message + iwbrm + ftr)
        elif will_be_removed:
            print(nosince_message + iwbrm + vers)
        else:
            print(nosince_message + iwbrm + ftr)
            
        return func(*args, **kwargs)
    return deprecat

@deprecated
def printiz(arg, arg2):
    print(arg, arg2)
printiz(1, arg2 = ())

@deprecated()
def printi_with_no_args(arg, arg2):
    print(arg, arg2)
printi_with_no_args(1, arg2 = ())

@deprecated(since = '1.2.0')
def printi_with_since(arg, arg2):
    print(arg, arg2)
printi_with_since(arg = 'SINCE', arg2 = ''.join(['1','.2']))    

@deprecated(will_be_removed = 'alpha 2.1')
def printi_with_wbr(arg, arg2):
    print(arg, arg2)
printi_with_wbr("alpha 2.1", 'will remove this')

@deprecated(since = '1.2.0', will_be_removed = 'alpha 2.1')
def printi_with_both(arg, arg2):
    print(arg, arg2)
printi_with_both('since 1.2.0', 'in alpha 2.1')
