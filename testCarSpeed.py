import unittest

def car_speed(speed):
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
    def setUpClass(cls) -> None:
        cls.testedString = car_speed(70)
        print('Setup ',cls.testedString)

    @classmethod
    def tearDownClass(cls) -> None:
        print('Tear down ',cls.testedString)

    def test_valid_speed_low(self):
        self.assertEqual(car_speed(0), "Low")

    def test_valid_speed_normal(self):
        self.assertEqual(car_speed(60), "Normal")

class TestEvaluateCarSpeed2(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.testedString = car_speed(220)
        print('Setup ',cls.testedString)

    @classmethod
    def tearDownClass(cls) -> None:
        print('Tear down ',cls.testedString)

    def test_invalid_speed_negative(self):
        self.assertEqual(car_speed(-10), "Invalid")

    def test_invalid_speed_high(self):
        self.assertEqual(car_speed(300), "Invalid")


if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestEvaluateCarSpeed)
    suite1.beforeAll = TestEvaluateCarSpeed.setUpClass
    suite1.afterAll = TestEvaluateCarSpeed.tearDownClass

    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestEvaluateCarSpeed2)
    suite2.beforeAll = TestEvaluateCarSpeed2.setUpClass
    suite2.afterAll = TestEvaluateCarSpeed2.tearDownClass

    mySuite = unittest.TestSuite([suite1, suite2])

    runner = unittest.TextTestRunner()
    runner.run(mySuite)
