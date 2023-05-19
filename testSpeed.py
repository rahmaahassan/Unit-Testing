import unittest

def evaluate_car_speed(speed):
    if speed < 0:
        return "Invalid"
    elif 0 <= speed < 40:
        return "Low"
    elif 40 <= speed < 120:
        return "Normal"
    elif 120 <= speed < 200:
        return "High"
    elif 200 <= speed < 220:
        return "V.High"
    elif speed >= 220:
        return "Invalid"

class TestEvaluateCarSpeed(unittest.TestCase):
    @classmethod
    def beforeAll(cls):
        print("Setup for Test Suite 1 - Valid Speed Levels")

    @classmethod
    def afterAll(cls):
        print("Teardown for Test Suite 1 - Valid Speed Levels")

    def test_valid_speed_low(self):
        self.assertEqual(evaluate_car_speed(0), "Low")

    def test_valid_speed_normal(self):
        self.assertEqual(evaluate_car_speed(60), "Normal")

class TestEvaluateCarSpeed2(unittest.TestCase):
    @classmethod
    def beforeAll(cls):
        print("Setup for Test Suite 2 - Invalid Speed Levels")

    @classmethod
    def afterAll(cls):
        print("Teardown for Test Suite 2 - Invalid Speed Levels")

    def test_invalid_speed_negative(self):
        self.assertEqual(evaluate_car_speed(-10), "Invalid")

    def test_invalid_speed_high(self):
        self.assertEqual(evaluate_car_speed(300), "Invalid")


if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestEvaluateCarSpeed)
    suite1.beforeAll = TestEvaluateCarSpeed.beforeAll
    suite1.afterAll = TestEvaluateCarSpeed.afterAll

    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestEvaluateCarSpeed2)
    suite2.beforeAll = TestEvaluateCarSpeed2.beforeAll
    suite2.afterAll = TestEvaluateCarSpeed2.afterAll

    mySuite = unittest.TestSuite([suite1, suite2])

    runner = unittest.TextTestRunner()
    runner.run(mySuite)
