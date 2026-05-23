class Employee:
    def __init__(self):
        print("i am the constructor of employee")
    a=1
class Programmer(Employee):
     def __init__(self):
        print("i am the constructor of Programmer")
     b=2

class Manager(Programmer):
     def __init__(self):
        super().__init__()
        print("i am the constructor of Manager")

     c=3


# o=Employee()
# print(o.a)
m=Manager()
print(m.c)