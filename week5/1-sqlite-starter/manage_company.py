import sqlite3


db = sqlite3.connect('company.db')
db.row_factory = sqlite3.Row
cursor = db.cursor()


def get_command():
    return input('Enter command>').split(' ')


def list_employees():
    cursor.execute('''
        SELECT id, name, position FROM employees
        ''')
    employees = cursor.fetchall()
    for employee in employees:
        print(
            "{} - {} - {}".format(
                employee['id'], employee['name'], employee['position'])
        )


def monthly_spending():
    cursor.execute('''
        SELECT SUM(monthly_salary) AS sum FROM employees
        ''')
    return cursor.fetchone()['sum']


def yearly_spending():
    cursor.execute('''
        SELECT SUM(yearly_bonus) AS bonus FROM employees
        ''')
    bonus = cursor.fetchone()['bonus']
    monthly = monthly_spending()
    total_yearly_spending = 12 * monthly + bonus
    return total_yearly_spending


def add_employee():
    name = input("name>")
    monthly_salary = input("monthly_salary>")
    yearly_bonus = input("yearly_bonus>")
    position = input("position>")
    employee = (name, monthly_salary, yearly_bonus, position)
    cursor.execute('''
        INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
        VALUES(?,?,?,?)''', employee)
    db.commit()


def delete_employee(id_):
    deleted_empoyee = cursor.execute('''
        SELECT name FROM employees WHERE id = ?
        ''', (id_, ))
    deleted_empoyee = deleted_empoyee.fetchone()
    print('{} was deleted.'.format(deleted_empoyee['name']))
    cursor.execute('''
        DELETE FROM employees WHERE id = ?
        ''', (id_, ))
    db.commit()


def update_employee(id_):
    name = input("name>")
    monthly_salary = input("monthly_salary>")
    yearly_bonus = input("yearly_bonus>")
    position = input("position>")
    employee = (name, monthly_salary, yearly_bonus, position, id_)
    cursor.execute('''
        UPDATE employees SET name = ?, monthly_salary = ?, yearly_bonus = ?,
        position = ? WHERE id = ?''', employee)


def main():
    while True:
        full_command = get_command()
        command = full_command[0]
        if command == 'exit':
            print('Goodbye')
            return
        elif command == 'list_employees':
            list_employees()
        elif command == 'monthly_spending':
            print('The company is spending ${} every month'.format(
                monthly_spending()))
        elif command == 'yearly_spending':
            print('The company is spending ${} every year!'.format(
                yearly_spending()))
        elif command == 'add_employee':
            add_employee()
        elif command == 'delete_employee':
            id_ = full_command[1]
            delete_employee(id_)
        elif command == 'update_employee':
            id_ = full_command[1]
            update_employee(id_)
        else:
            print('Wrong command!')


if __name__ == '__main__':
    main()
