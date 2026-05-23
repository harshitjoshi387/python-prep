class employee:
    company="itc"
    name="default name"
    def show(self):
        print(f"the name of the Employee is {self.name} and the company is {self.company}")

class coder:
    language="python"
    def printLanguage(self):
        print(f"out of all the language here is your language:{self.language}")


class programmer(employee, coder):
    company="itc infotech"
    def showLanguage(self):
        print(f"the name is {self.company}and he is good with {self.language}language")


a=employee()
b=programmer()
b.show()
b.printLanguage()
b.showLanguage()