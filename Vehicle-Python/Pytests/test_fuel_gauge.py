import sys

sys.path.insert(0, "../ADTs")
from Calculators import FuelConsump  # noqa E402 (linting exemption)


def test_base_case():
    test_gauge = FuelConsump(30.0, 15.0)
    print("Expected: 50.0")
    print("Actual Result: " + str(test_gauge.calculateFuelPercentage()))
    assert test_gauge.calculateFuelPercentage() == 50.0


def test_zero_over_full():
    test_gauge = FuelConsump(30.0, 0)
    print("Expected: 0.0")
    print("Actual Result: " + str(test_gauge.calculateFuelPercentage()))
    assert test_gauge.calculateFuelPercentage() == 0.0


def test_zero_over_zero():
    test_gauge = FuelConsump(0.0, 0.0)
    print("Expected: 0.0")
    print("Actual Result: " + str(test_gauge.calculateFuelPercentage()))
    assert test_gauge.calculateFuelPercentage() == 0.0


def test_negative_over_full():
    test_gauge = FuelConsump(30.0, -15.0)
    print("Expected: 0.0")
    print("Actual Result: " + str(test_gauge.calculateFuelPercentage()))
    assert test_gauge.calculateFuelPercentage() == 0.0


def test_side_case():
    test_gauge = FuelConsump(30.0, 25.8)
    print("Expected: 86.0")
    print("Actual Result: " + str(test_gauge.calculateFuelPercentage()))
    assert test_gauge.calculateFuelPercentage() == 86.0


def test_half_over_zero():
    test_gauge = FuelConsump(0.0, 30.0)
    print("Expected: 0.0")
    print("Actual Result: " + str(test_gauge.calculateFuelPercentage()))
    assert test_gauge.calculateFuelPercentage() == 0.0


def test_extra_over_full():
    test_gauge = FuelConsump(30.0, 45.0)
    print("Expected: 100.0")
    print("Actual Result: " + str(test_gauge.calculateFuelPercentage()))
    assert test_gauge.calculateFuelPercentage() == 100.0


def test_full_over_full():
    test_gauge = FuelConsump(30.0, 30.0)
    print("Expected: 100.0")
    print("Actual Result: " + str(test_gauge.calculateFuelPercentage()))
    assert test_gauge.calculateFuelPercentage() == 100.0


def test_full_over_negative():
    test_gauge = FuelConsump(-15.0, 30.0)
    print("Expected: 0.0")
    print("Actual Result: " + str(test_gauge.calculateFuelPercentage()))
    assert test_gauge.calculateFuelPercentage() == 0.0


test_base_case()
print("")
test_zero_over_full()
print("")
test_zero_over_zero()
print("")
test_negative_over_full()
print("")
test_side_case()
print("")
test_half_over_zero()
print("")
test_extra_over_full()
print("")
test_full_over_full()
print("")
test_full_over_negative()
