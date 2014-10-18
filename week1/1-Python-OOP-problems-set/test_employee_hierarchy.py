import unittest

from EmployeeHierarchy import Employee, HourlyEmployee, SalariedEmployee, Manager


class EmployeeHierarchyTest(unittest.TestCase):

    def test_get_employee_name(self):
        new_employee = Employee('Stoyan')
        self.assertEqual('Stoyan', new_employee.getName())

    def test_hourly_employee_weekly_pay(self):
        new_hourly_employee = HourlyEmployee('Stoyan', 20)
        self.assertEqual(new_hourly_employee.weeklyPay(20), 400)
        self.assertEqual(new_hourly_employee.weeklyPay(50), 3000)

    def test_salaried_employee_weekly_pay(self):
        new_salaried_employee = SalariedEmployee('Ivan', 52000)
        self.assertEqual(new_salaried_employee.weeklyPay(), 1000)

    def test_manager_weekly_pay(self):
        new_manager = Manager('Mourinho', 104000, 100)
        self.assertEqual(new_manager.weeklyPay(), 2600)

if __name__ == '__main__':
    unittest.main()
