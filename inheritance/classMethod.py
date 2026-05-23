class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"the value of class attribute is {cls.a}")


e= Employee()
e.a=45
e.show()