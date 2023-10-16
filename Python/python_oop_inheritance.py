from python_oop import Employee

class Developer(Employee):
    # we can re-initiate inherited class variable
    raise_amount = 3
    def __init__(self, first_name, last_name, pay, prog_lang="dos"):
        super().__init__(first_name, last_name, pay)
    
dev1 = Developer(first_name="Jason",last_name="Mason",pay=3000,prog_lang="py")

print(dev1.company)


class Manager(Employee):
    pass