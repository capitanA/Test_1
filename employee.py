class Employee():
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)

    def apply_raise(self):
        return int(self.pay * self.raise_amount)
