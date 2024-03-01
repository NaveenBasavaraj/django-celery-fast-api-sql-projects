class Employee:
    def __init__(self, name:str, role:str, age:int, salary:int):
        self.name:str = name
        self.role:str = role
        self.age:int = age
        self.salary:int = salary
 
    def get_age(self) -> int:
        return self.age
    
    def get_salary(self)-> int:
        return self.salary
    
    def get_role(self)-> str:
        return self.role
    
    def get_name(self)-> str:
        return self.name

class Manager(Employee):
    def __init__(self, name:str, role:str, age:int, salary:int, sub_role:str):
        super().__init__(name, role, age, salary)
        self.sub_role:str = sub_role
    
    def get_sub_role(self)-> str:
        return self.sub_role + '' + self.get_role()

if __name__ == "__main__":
    # emp1 = Employee(name='emp', role='dev', age=12, salary=100)
    # print(f'name: {emp1.get_name()} age:{emp1.get_age()}')
    
    mang1 = Manager(name='mang1', role='dev', age='12', salary=100, sub_role='senior')
    print(f'name and role: {mang1.get_sub_role()}')



