# At this point there are two methods in the subclass

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def get_job_title(self):
        return "Manager"
    
    def get_work(self):
        return "I manage a department"
    
class Attendant(Employee):
    def get_job_title(self):
        return "Station Attendant"
    
    def get_work(self):
        return "I fill up cars with gasoline"
    

employee = [Manager("Anand", 2000),
            Attendant("Vikash", 1800),
            Attendant("Bali", 1900)]

for e in employee:
    print(f"{e.name}, ${e.salary}, {e.get_job_title()}")
    print(e.get_work())
    print()
    


