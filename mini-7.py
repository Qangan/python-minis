def deprecated(since = None, will_be_removed = None):
    def deprecat(func):
        def depr(*args, **kwargs):
            name = func.__name__
            if since and will_be_removed:
                print(f"Warning: function {name} is deprecated since version {since}. It will be removed in version {will_be_removed}.")
            elif since:
                print(f"Warning: function {name} is deprecated since version {since}. It will be removed in future versions.")
            elif will_be_removed:
                print(f"Warning: function {name} is deprecated. It will be removed in version {will_be_removed}.")
            else:
                print(f"Warning: function {name} is deprecated. It will be removed in future versions.")
            func(*args, **kwargs)
        return depr
    return deprecat

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
