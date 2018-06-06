class Employee():
    def __init__(self, name, last_name, money):
        self.name = name
        self.last_name = last_name
        self.money = money

    def give_raise(self, money=5000):
        self.money += money
