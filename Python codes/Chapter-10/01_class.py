class Employee:
    language = "Py" # This is a class attribute
    salary = 120000


nahid = Employee()
nahid.name = "Nahid" # This is an instance attribute
print(nahid.name, nahid.language, nahid.salary)

ifti = Employee()
ifti.name = "Farhan Ifti"
print(ifti.name, ifti.salary, ifti.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class