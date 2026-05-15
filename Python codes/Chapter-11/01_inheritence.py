class Employee:
    company = "ITC Infotech"
    
    def __init__(self, name, salary):      # ✅ added __init__
        self.name = name
        self.salary = salary
    
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")  #  fixed self.language → self.salary


class Programmer(Employee):
    company = "ITC Infotech"
    
    def __init__(self, name, salary, language):   #  added __init__ with language
        super().__init__(name, salary)             #  call parent __init__
        self.language = language
    
    def show(self):
        print(f"The name is {self.name} and the language is {self.language}")  #  fixed

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language}")


a = Employee("Nahid", 50000)
b = Programmer("Rakib", 70000, "Python")    #  fixed "programmer" → "Programmer"

a.show()
b.show()
b.showLanguage()
print(a.company, b.company)