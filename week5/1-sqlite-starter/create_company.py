import sqlite3

db = sqlite3.connect('company.db')
db.row_factory = sqlite3.Row
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY, name TEXT,
    monthly_salary INTEGER, yearly_bonus INTEGER, position TEXT)
    ''')
emloyee_Ivan = ("Ivan Ivanov", 5000, 10000, "Software Developer")
emloyee_Rado = ("Rado Rado", 500, 0, "Technical Support Intern")
employee_Ivo = ("Ivo Ivo", 10000, 100000, "CEO")
employee_Petar = ("Petar Petrov", 3000, 1000, "Marketing Manager")
employee_Maria = ("Maria Georgieva", 8000, 10000, "COO")
cursor.execute('''
    INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
    VALUES(?,?,?,?)''', emloyee_Ivan)
cursor.execute('''
    INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
    VALUES(?,?,?,?)''', emloyee_Rado)
cursor.execute('''
    INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
    VALUES(?,?,?,?)''', employee_Ivo)
cursor.execute('''
    INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
    VALUES(?,?,?,?)''', employee_Petar)
cursor.execute('''
    INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
    VALUES(?,?,?,?)''', employee_Maria)
db.commit()
