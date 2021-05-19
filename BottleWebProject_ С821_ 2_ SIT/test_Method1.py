import methodLogic1
import unittest

class Test_Method1(unittest.TestCase):
    def test_correct_method(self):
        list_tests1 = [[1,2, 1,4, 2,4, 2,3, 3,4, 5,1, 5,4, 6,2, 6,3],[1,2, 1,4, 2,4, 2,3, 3,4, 5,1, 5,4,], [1,2, 1,4, 2,4, 2,3, 3,4],[1,2, 1,4, 2,4, 2,3], [1,2, 1,4, 2,4, 2,3, 3,4]]
        list_tests2 = [[1,2, 2,3, 3,1],[1,2, 2,3, 3,1],[1,2, 2,3, 3,1],[1,2, 2,3, 3,1],[1,2, 2,3, 3,4, 4,1]]
        list_answers = [[[1,2,4],[1,4,5],[2,3,4],[2,3,6]], [[1,2,4],[1,4,5],[2,3,4]], [[1,2,4],[2,3,4]], [[1,2,4]], [[1,2,3,4]]]
        for i in range(0, len(list_tests1)):
            if (methodLogic1.findFragment(list_tests1[i], list_tests2[i]) != list_answers[i]):
                self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()