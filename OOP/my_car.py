from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.increement_odemeter(500)
my_new_car.read_odemeter()

my_new_car.increement_odemeter(100)
my_new_car.read_odemeter()