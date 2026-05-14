class Employee:
    language = "Python" # This is a class attribute
    salary = 120000


nahid = Employee()
nahid.language = "Javascript" # This is an instance attribute
print(nahid.language, nahid.salary)
