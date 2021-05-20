import methodLogic3
import unittest 


class Test_Method3(unittest.TestCase):
    def test_correct_method(self):
        matrix = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0,  1, 0, 1, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0]]
        result = ["None", "[2, 1, 4, 3, 2]", "None", "None", "[2, 1, 6, 4, 5, 3, 2]"]
       
        for i in range(len(matrix)):
            if(methodLogic3.findEuler(methodLogic3.split(methodLogic3.matrixToList(matrix[i]))) == result[i]):
                self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()


