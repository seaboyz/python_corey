import logging

logging.basicConfig(level=logging.INFO,
                    filename='employee.log',
                    format='%(asctime)s:%(levelname)s:%(message)s')


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        logging.info(f"Created Employee: {self.fullname} - {self.email}")

    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"


emp_1 = Employee('John', 'Smith', 50000)
emp_2 = Employee('Jane', 'Doe', 60000)