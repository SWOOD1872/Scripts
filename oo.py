# With thanks to Corey Schafer: https://www.youtube.com/user/schafer5

import datetime

class Employee:

    # Class Variable
    company = 'Company'

    def __init__(self, forename, surname, department, salary):
        self.forename = forename
        self.surname = surname
        self.department = department
        self.salary = float(salary)
        self.email = f'{self.forename}.{self.surname}@{Employee.company}.com'

    def fullname(self):
        return f'{self.forename} {self.surname}'
    
    def monthlypay(self):
        return '%.2f' % round((self.salary / 12), 2)

    # Alternative / Additional Constructor
    @classmethod
    def from_string(cls, s):
        forename, surname, department, salary = s.split('-')
        return cls(forename, surname, department, float(salary))
    
    # Static Method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


e1 = Employee('John', 'Doe', 'Engineering', 22500)
print(e1.fullname(), e1.monthlypay(), e1.email, sep=', ')

print()

e2 = Employee('Jane', 'Doe', 'Engineering', 25000)
print(e2.fullname(), e2.monthlypay(), e2.email, sep=', ')

print()

e3 = Employee('Wally', 'West', 'Runner', '32000')
print(e3.fullname(), e3.monthlypay(), e3.email, sep=', ')

print()

e4 = Employee.from_string('Bruce-Wayne-Vigilante-500000')
print(e4.fullname(), e4.monthlypay(), e4.email, sep=', ')

print()

d = datetime.date(2019, 4, 27)
print(Employee.is_workday(d))