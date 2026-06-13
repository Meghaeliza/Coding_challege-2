import math
class employee:
    def __init__(self,name,basic_salary):
        self.name=name
        self.basic_salary=basic_salary
    def calculate_hra(self):
        return math.ceil(self.basic_salary * 0.2)
    def calculate_da(self):
        return math.ceil(self.basic_salary * 0.1)
    def calculate_total_salary(self):
        hra = self.calculate_hra()
        da = self.calculate_da()
        return self.basic_salary + hra + da

            
emp1=employee("Megha",20000)      
emp2=employee("Mitha",30000)
print("The total salary of Megha is",emp1.calculate_total_salary())
print("The total salary of Mitha is",emp2.calculate_total_salary())
