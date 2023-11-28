import test_vehicle
from vehicle import Car, Motorcycle

car = Car(company="Toyota", model="Camry", year_release=2022)
test_vehicle.test_car_is_vehicle_instance(car)
test_vehicle.test_car_has_4_wheels(car)
test_vehicle.test_car_test_drive_speed(car)

motorcycle = Motorcycle(company="Harley-Davidson", model="Sportster", year_release=2022)
test_vehicle.test_motorcycle_has_2_wheels(motorcycle)
test_vehicle.test_motorcycle_test_drive_speed(motorcycle)
test_vehicle.test_motorcycle_park_speed(motorcycle)

print("Все тесты успешно пройдены!")
