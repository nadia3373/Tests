import pytest
from vehicle import Vehicle

def test_car_is_vehicle_instance(car):
    assert isinstance(car, Vehicle)

def test_car_has_4_wheels(car):
    assert car.num_wheels == 4

def test_car_test_drive_speed(car):
    car.test_drive()
    assert car.speed == 60

def test_car_park_speed(car):
    car.test_drive()
    car.park()
    assert car.speed == 0

def test_motorcycle_has_2_wheels(motorcycle):
    assert motorcycle.num_wheels == 2

def test_motorcycle_test_drive_speed(motorcycle):
    motorcycle.test_drive()
    assert motorcycle.speed == 75

def test_motorcycle_park_speed(motorcycle):
    motorcycle.test_drive()
    motorcycle.park()
    assert motorcycle.speed == 0
