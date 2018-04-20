class Employee:
    "This deals with basic employment"
    total_employees = 0
    upgrade = 5
    
    def __init__(self, first, last, race, age, pay):
        self.first = first
        self.last = last
        self.race = race
        self.age = age
        self.pay = pay
        Employee.total_employees += 1

    def apply_raise(self):
        self.pay = self.pay + (self.pay * (Employee.upgrade/100))

    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    @fullname.setter
    def fullname(self, newName):
        first, last = newName.split(" ")
        self.first, self.last = first, last
        
        



class Developer(Employee):
    "This deals with developer roles"
    upgrade = 15


    def __init__(self, first, last, race, age, pay, prog_lang):
        super().__init__(first, last, race, age, pay)
        self.prog_lang = prog_lang



class Manager(Employee):
    "This deals with management roles"


    def __init__(self, first, last, race, age, pay, employees = None):
        super().__init__(first, last, race, age, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employees(self, emps):
        [self.employees.append(char) for char in emps if char not in self.employees]
        
    def remove_employees(self, emps):
        [self.employees.remove(char) for char in emps if char in self.employees]
    
    def print_employees(self):
        print(f"{self.first} has a total of {len(self.employees)} employees:")
        for char in self.employees:
            print("---->", char.fullname())
    

