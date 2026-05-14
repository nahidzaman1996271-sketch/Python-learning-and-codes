class Employee:
    language = "Python" # This is a class attribute
    salary = 120000
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

nahid = Employee()
nahid.language = "Javascript" # This is an instance attribute
# harry.getInfo()
Employee.getInfo(nahid)