import unittest

def student_score(score):
    if score < 0:
        return "Invalid"
    elif 0 <= score < 50:
        return "Failed"
    elif 50 <= score < 65:
        return "Passed"
    elif 65 <= score < 75:
        return "Good"
    elif 75 <= score < 85:
        return "V.Good"
    elif 85 <= score < 100:
        return "Excellent"
    elif score >= 100:
        return "In"

class TestEvaluateStudentScore(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.testedString = student_score(75)
        print('Setup ',cls.testedString)

    @classmethod
    def tearDownClass(cls) -> None:
        print('Tear down ',cls.testedString)

    def test_valid_score_failed(self):
        self.assertEqual(student_score(20), "Failed")

    def test_valid_score_passed(self):
        self.assertEqual(student_score(60), "Passed")

class TestEvaluateStudentScore2(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.testedString = student_score(100)
        print('Setup ',cls.testedString)

    @classmethod
    def tearDownClass(cls) -> None:
        print('Tear down ',cls.testedString)

    def test_invalid_score_negative(self):
        self.assertEqual(student_score(-10), "Invalid")

    def test_invalid_score_high(self):
        self.assertEqual(student_score(120), "In")


if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestEvaluateStudentScore)
    suite1.beforeAll = TestEvaluateStudentScore.setUpClass
    suite1.afterAll = TestEvaluateStudentScore.tearDownClass

    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestEvaluateStudentScore2)
    suite2.beforeAll = TestEvaluateStudentScore2.setUpClass
    suite2.afterAll = TestEvaluateStudentScore2.tearDownClass

    mySuite = unittest.TestSuite([suite1, suite2])

    runner = unittest.TextTestRunner()
    runner.run(mySuite)
