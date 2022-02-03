# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = 'A'


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = 'B'


# class C(B, A):# try this
class C(A, B):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name)  # first inheritance


c = C()
c.showprops()
