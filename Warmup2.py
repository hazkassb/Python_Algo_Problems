# DAY THREE ASSIGNMENT

'''
    1. (The Person, Student, Employee, Faculty, and Staff classes) Design a class named
        Person and its two subclasses named Student and Employee.
        Make Faculty and Staff subclasses of Employee.
'''


class Person:

    def __init__(self, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def __repr__(self):
        return 'Person ' + str(self.name)


class Student(Person):
    def __init__(self, status, name, address, phone_number, email):
        super().__init__(name, address, phone_number, email)
        self.status = status

    def __repr__(self):
        return 'Student ' + str(self.name)


class Employee(Person):
    def __init__(self, office, salary, date_hired, name, address, phone_number, email):
        super().__init__(name, address, phone_number, email)
        self.office = office
        self.salary = salary
        self.date_hired = date_hired

    def __repr__(self):
        return 'Employee ' + str(self.name)


class Faculty(Employee):
    def __init__(self, office_hours, rank, office, salary, date_hired, name, address, phone_number, email):
        super().__init__(office, salary, date_hired, name, address, phone_number, email)
        self.office_hours = office_hours
        self.rank = rank

    def __repr__(self):
        return 'Faculty ' + str(self.name)


class Staff(Employee):
    def __init__(self, name, address, phone_number, email, title, office, salary, date_hired):
        super().__init__(office, salary, date_hired, name, address, phone_number, email)
        self.title = title

    def __repr__(self):
        return 'Staff ' + str(self.name)


person = Person('Hamza', 'NC', '91283758', 'me@gmail.com')
student = Student('senior', 'Hamza', 'NC', '91283758', 'me@gmail.com')
employee = Employee("my_office", "my_salary", "my_date_hired", "my_name", "my_address", "my_phone_number", "my_email")
faculty = Faculty("my_office_hours", "my_rank", "my_office", "my_salary", "my_date_hired", "my_name", "my_address",
                  "my-phone_number", "my_email")
staff = Staff("my_name", "my_address", "my_phone_number", "my_email", "my_title", "my_office", "my_salary",
              "my_date_hired")

print(person)
print(student)
print(employee)
print(faculty)

# print('name is:', employee.)

'''
    2. Store all created Person, Student, Employee, Faculty, and Staff in a dictionary
        for examples: a,b,c... are correspondent objects
        data = {
            'Person': [a, b],
            'Student': [c, d, e],
            'Faculty': [f,g],
            'Staff': [h,k],
            'Employee': [l,m,m,o,p],
        }
        
        Create methods to get all Students, Employees, Faculties and Staffs as generators
'''


def collector(a_dict, obj):
    list_of_values = list()
    class_name = obj.__class__.__name__
    if a_dict.get(class_name) is not None:
        list_of_values = a_dict.get(class_name)

    list_of_values.append(obj)
    if class_name == "Person":
        a_dict.update({"Person": list_of_values})
    elif class_name == "Student":
        a_dict.update({"Student": list_of_values})
    elif class_name == "Faculty":
        a_dict.update({"Faculty": list_of_values})
    elif class_name == "Staff":
        dict.update({"Staff": list_of_values})
    elif class_name == "Employee":
        dict.update({"Employee": list_of_values})


# Test
a_dict_ = dict()
person1 = Person('Hamza1', 'NC', '91283758', 'me@gmail.com')
student1 = Student('senior2', 'Hamza', 'NC', '91283758', 'me@gmail.com')
employee1 = Employee("my_office3", "my_salary", "my_date_hired", "my_name", "my_address", "my_phone_number", "my_email")
faculty1 = Faculty("my_office_hours4", "my_rank", "my_office", "my_salary", "my_date_hired", "my_name", "my_address",
                   "my-phone_number5", "my_email")
staff1 = Staff("my_name", "my_address6", "my_phone_number", "my_email", "my_title", "my_office", "my_salary",
               "my_date_hired")
person2 = Person('Hamza', 'NC', '912837587', 'me@gmail.com')
student2 = Student('senior', 'Hamza', 'N8C', '91283758', 'me@gmail.com')
employee2 = Employee("my_office9", "my_salary", "my_date_hired", "my_name", "my_address", "my_phone_number", "my_email")
faculty2 = Faculty("my_office_hoursw", "my_rank", "my_office", "my_salary", "my_date_hired", "my_name", "my_address",
                   "my-phone_numbere", "my_email")
staff2 = Staff("my_name", "my_address23", "my_phone_number", "my_email", "my_title", "my_office", "my_salary",
               "my_date_hired")
person3 = Person('Hamza', 'NC21', '91283758', 'me@gmail.com')
student3 = Student('senior', 'Hamzagfs', 'NC', '91283758', 'me@gmail.com')
employee3 = Employee("my_officewr", "my_salary", "my_date_hired", "my_name", "my_address", "my_phone_number", "my_email")
faculty3 = Faculty("my_office_hoursv43", "my_rank", "my_office", "my_salary", "my_date_hired", "my_name", "my_address",
                   "my-phone_number23", "my_email")
staff3 = Staff("my_name", "my_addresssqeqw3434", "my_phone_number", "my_email", "my_title", "my_office", "my_salary",
               "my_date_hired")

a_list = [person1, person2, person3, student1, student2, student3, employee1, employee2, employee3, faculty1, faculty2,
          faculty3, staff1, staff2, staff3]

for val in a_list:
    collector(a_dict_, val)

print(a_dict_)




'''
    3. Create a generator that yields "n" random numbers between a low and high number
        (that are inputs). Note: Use the random library.
'''

import random

def gen_random(low, high, n):
    for i in range(n + 1):
        yield random.randint(low, high)


l = gen_random(1, 10, 12)
for x in l:
    print(x)



'''
    4. Display prime numbers from n1 to n2 using iterators and generators.
        Write two python programs using both iterators and generators.
'''


def is_prime(n):
    for i in range(2, int((n ** 0.5)) + 1):
        if n % i == 0:
            return False
    return True


def getPrimes(n1, n2):
    """Generators"""
    while n1 < n2:
        if is_prime(n1):
            yield n1
        n1 += 1


class IterPrimes:
    """Iterators"""

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def __iter__(self):
        return self

    def __next__(self):
        val = self.n1

        if self.n1 > self.n2:
            raise StopIteration

        self.n1 += 1

        if is_prime(val):
            return val

        return


# Genrators
l = list(getPrimes(30, 200))
print(l)

print()

# Iterators
p = IterPrimes(30, 200)

list_primes = [v for v in p if v is not None]
print(list_primes)
