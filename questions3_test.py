# question3_test.py
import unittest
import question   # imports student code

class TestQuizQuestions(unittest.TestCase):

    def test_question3(self):
        self.assertTrue(quiz.question3(21))
        self.assertTrue(quiz.question3(42))
        self.assertFalse(quiz.question3(9))
        self.assertFalse(quiz.question3(14))
        self.assertFalse(quiz.question3(10))


if __name__ == "__main__":
    unittest.main()
