class Person(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


class Customer(Person):
    def is_employee(self):
        return False


class Employee(Person):
    def is_employee(self):
        return True
        
            
    

# PYTHONPATH=.py.test tests/test_customers.py::CustomerTestCase::test_if_are_employee
# PYTHONPATH=.py.test tests/test_board.py::BoardTestCase::test_make_move_on_board