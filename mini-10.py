class singleton():
    instances = {}
    def __new__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__new__(cls)
        return cls.instances[cls]

class MooMoo(singleton):
    def __init__(self, name):
        self.name = name
    def moo(self):
        print("moo!!!", self.name)

a = MooMoo("Meow")
b = MooMoo("Bark")

a.moo()
b.moo()

print(a == b)
