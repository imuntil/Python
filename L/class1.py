class Restaurant():
    def __init__(self, name, type):
        self.restaurant_name = name
        self.culsine_type = type

    def describe_restaurant(self):
        print(self.restaurant_name, self.culsine_type)

    def open_restaurant(self):
        print('{} is opening'.format(self.restaurant_name))


res = Restaurant('lanzhou', 'zhong')
res.describe_restaurant()
res.open_restaurant()

# print(dir(res))


class Car():
    """模拟汽车"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印汽车里程的信息"""
        print('This car has {} miles on it.'.format(self.odometer_reading))

    def update_odometer(self, mileage):
        """
        更新里程
        禁止将里程回调
        """
        if (self.odometer_reading < mileage):
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, mileage):
        """将里程增加制定的值"""
        if not isinstance(mileage, (int, float)):
            raise TypeError('mileage must be number')
        if mileage <= 0:
            print('mileage must be > 0')
            return
        self.odometer_reading += mileage


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(20)
# my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(11)
# my_new_car.increment_odometer('10')
# my_new_car.increment_odometer(-1)
my_new_car.read_odometer()


class Battery():
    """电瓶"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印电瓶容量"""
        print('This car has a {}-kWh battery'.format(self.battery_size))

    def get_range(self):
        """打印电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = 'this car can go approximately {} miles on a full charge'.format(
            range)
        print(message)


class ElectricCar(Car):
    """电动汽车"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    #     self.battery_size = 70

    # def describe_battery(self):
    #     """打印电瓶容量"""
    #     print("This car has a {}-kWh battery".format(self.battery_size))


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print('.......................................')


class IceCreamStand(Restaurant):
    """冰淇淋小店"""

    def __init__(self, name):
        super().__init__(name, 'ice')
        self.flavors = ['ama', 'kara', 'suppai', 'syoppai']


my_ice_res = IceCreamStand('lal')
my_ice_res.describe_restaurant()
my_ice_res.open_restaurant()
print(my_ice_res.flavors)