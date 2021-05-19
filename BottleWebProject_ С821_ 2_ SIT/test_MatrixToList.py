import methodLogic1
import unittest

class Test_MatrixToList(unittest.TestCase):
    def test_correct_method(self):
        list_tests = [[1,1,1, 1,1,1, 1,1,1], [0,1,1, 1,0,1, 1,1,0], [0,0,1,0, 0,0,1,1, 1,1,0,0, 0,1,0,0], [1,0,1,1, 0,1,1,1, 1,1,1,1, 1,1,1,1], [1,1,1,0,1, 1,1,1,1,1, 1,1,1,1,1, 0,1,1,0,0, 1,1,1,0,1]]
        list_answers = [[1,1, 2,1, 2,2, 3,1, 3,2, 3,3], [2,1, 3,1, 3,2], [3,1, 3,2, 4,2], [1,1, 2,2, 3,1, 3,2, 3,3, 4,1, 4,2, 4,3, 4,4],[1,1, 2,1, 2,2, 3,1, 3,2, 3,3, 4,2, 4,3, 5,1, 5,2, 5,3, 5,5]]
        for i in range(0, len(list_tests)):
            if (methodLogic1.matrixToList(list_tests[i]) != list_answers[i]):
                self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()