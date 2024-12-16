class singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MooMoo(metaclass=singleton):
    def __init__(self, name):
        self.name = name
    def moo(self):
        print("moo!!!", self.name)

class BarkBark(metaclass=singleton):
    def __init__(self, name):
        self.name = name
    def bark(self):
        print("bark!!!", self.name)


a = MooMoo("Meow")
b = MooMoo("Bark")  

c = BarkBark("Z")
z = BarkBark("K")  

print(c.name)  

a.moo()  
b.moo()  

c.bark()  
z.bark()  

print(a == b)  
