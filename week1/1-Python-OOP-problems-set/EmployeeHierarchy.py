class Employee:

    def __init__(self, __name):
        self.__name = __name

    def getName(self):
        return self.__name


class HourlyEmployee(Employee):

    def __init__(self, __name, hourly_wage):
        super().__init__(__name)
        self.hourly_wage = hourly_wage

    def weeklyPay(self, hours):
        if hours <= 40:
            return hours * self.hourly_wage
        else:
            return hours * 1.5 * self.hourly_wage


class SalariedEmployee(Employee):

    def __init__(self, __name, annual_salary):
        super().__init__(__name)
        self.annual_salary = annual_salary

    def weeklyPay(self, hours):
        return self.annual_salary / 52


class Manager(SalariedEmployee):

    def __init__(self, __name, annual_salary, weekly_bonus):
        super().__init__(__name, annual_salary)
        self.weekly_bonus = weekly_bonus

    def weeklyPay(self, hours):
        return self.annual_salary / 52 + self.weekly_bonus

staff = []
staff.append(HourlyEmployee("Morgan, Harry", 30.0))
staff.append(SalariedEmployee("Lin, Sally", 52000.0))
staff.append(Manager("Smith, Mary", 104000.0, 50.0))
for employee in staff:
    hours = int(input("Hours worked by " + employee.getName() + ": "))
    pay = employee.weeklyPay(hours)
    print("Salary: %.2f" % pay)
