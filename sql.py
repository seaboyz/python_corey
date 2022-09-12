from select import select
from employee import Employee
import sqlite3

# conn = sqlite3.connect('test.db')
conn = sqlite3.connect(':memory:')


c = conn.cursor()

c.execute("""
    CREATE TABLE employee(
        first TEXT,
        last TEXT,
        pay INTEGER
    )
""")


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employee VALUES (:first, :last, :pay)",
                  {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employee WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employee SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute(
            "DELETE from employee WHERE first = :first AND last = :last",
            {'first': emp.first, 'last': emp.last})


e1 = Employee('John', 'Doe', 80000)
e2 = Employee('Jane', 'Doe', 90000)

insert_emp(e1)
insert_emp(e2)

emps = get_emps_by_name('Doe')
print(emps)

remove_emp(e1)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(e2, 95000)
emps = get_emps_by_name('Doe')
print(emps)
