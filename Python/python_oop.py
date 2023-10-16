# python object oriented programming

# Python classes allows us to logically group data and functions logically
# Its a bluprint which allows use to easily create multiple instances 
# Classes have to main parts: 1) attributes or variables 2) methods or funcitons

class Employee:
    # class varaibles are defined outside constructor
    # They are shared among all instances
    # always best to use class variables to avoid making multiple changes
    total_employees = 0
    raise_amount = 1.5
    def __init__(self, first_name, last_name, pay, company="google"):
        # constructor is used to initialize the attributes
        # these are called instance variables or attributes
        # these variables are unique to each instance
        self.first_name = first_name.upper()
        self.last_name = last_name.upper()
        self.pay = int(pay)
        self.company = company.upper()
        self.email = self.first_name +"."+self.last_name+"@"+self.company+".com"
        Employee.total_employees += 1
    
    def __str__(self):
        # string representaion
        return self.first_name+" "+self.last_name
    
    def __repr__(self):
        # string represention mostly used by developers for debugging
        pass
    
    def apply_raise(self):
        # regular or instance methods, take 'self' or the instance itself as the first argument
        return f"{self} will receive a bonus of {self.pay * self.raise_amount}" # or Employee.raise_amount
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def create_from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() in (5,6):
            return False
        return True

# class vs instances

emp_list = []

emp1 = Employee("james","bond","1500") # unique emp instance 1
emp2 = Employee("gordon","ramsay","150") # unique emp instance 2 
emp_list = [emp1,emp2]

def print_emp_details(emp_list):
    print(f"total_employees: {Employee.total_employees}")
    for  emp in (emp1, emp2):
        print(f"{Employee.__str__(emp)}'s email is {emp.email}")
        print(f"{emp} current raise amount is {emp.raise_amount}")
        print(f"{emp} : {emp.apply_raise()}")
        Employee.set_raise_amt(2.5)
        print(f"{emp.apply_raise()} after change in raise amount to {emp.raise_amount}")
        
    import datetime
    my_day = datetime.date(2016,7,10)
    print(Employee.is_workday(my_day))

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-smith-30000'
emp_str_3 = 'Jane-Doe-90000'

emp_list = [emp_str_1,emp_str_2,emp_str_3]

if __name__ == '__main__':
    # print_emp_details([emp1, emp2])
    new_emp_list = []
    for emp in emp_list:
        new_emp = Employee.create_from_string(emp)
        new_emp_list.append(new_emp)
    
    print_emp_details(new_emp_list)
        
    
    
    
        
