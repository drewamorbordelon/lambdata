class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__ (self, first, last, pay):
        self.first = str(first)  # instance variables
        self.last = str(last)    #  here
        self.email = first + '.' + last + '@company.com'
        self.pay = int(pay)      #  here

        Employee.num_of_emps += 1   # NOTICE: no self here
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


# creating different types of employees (dev and mang)
class Developer(Employee):
    raise_amt = 1.10

    def __init__ (self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = str(prog_lang)


    # @classmethod
    # def set_raise_amt(cls, amount):  # cls is for a class method -->similar to self
    #     cls.raise_amt = smount




dev_1 = Developer('Drew', 'Bordelon', 100000, 'Python')
dev_2 = Developer('Test', 'User', 70000, 'Java')

print(dev_1.email)
print(dev_1.prog_lang)

# emp_1 = Employee('Drew', 'Bordelon', 100000)
# emp_2 = Employee('Test', 'User', 70000)

# Employee.set_raise_amount(1.05)

# emp_1.fullname()       #  These 2 lines of code do the same thing!
# print(Employee.fullname(emp_1))

print(dev_1.email)
print(dev_2.email)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

# print(emp_1.__dict__)  # does not contain raise_amount()
# print(Employee. __dict__)  #  Contains the rais_amount() attribute?

# Employee.raise_amount = 1.04
# emp_1.raise_amount = 1.05
print(Employee.raise_amt)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

print(Employee.num_of_emps)

# emp_1.first = 'Drew'
# emp_1.last = 'Bordelon'
# emp_1.email = 'dabordel@gmail.com'
# emp_1.pay = 100000

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'test.user@gmail.com'
# emp_2.pay = 70000



# if __name__ == "__main__":
#     print(emp_1.email)
#     print(emp_1.fullname())

#     print(emp_2.email)
#     print(emp_2.fullname())

#     print(emp_1.pay)
#     emp_1.apply_raise()
#     print(emp_1.pay)

