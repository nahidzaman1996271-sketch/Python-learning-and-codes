class Employee:
    language = "Python" # This is a class attribute
    salary = 120000

    def __init__(self): # dunder method which is automatically called
        self.name = nahid
        self.salary = self.salary
        self.language = self.language
        print("I am creating an object")
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

nahid = Employee("Nahid", 130000, "Javascript")
nahid.name = "Nahid"
print(nahid.name, nahid.salary, nahid.language)        

# nahid = Employee()