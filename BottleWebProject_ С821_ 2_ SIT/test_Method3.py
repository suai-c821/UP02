import unittest 
import methodLogic3

class Test_test_1(unittest.TestCase):
    def testMethod(self):
        graph = [0,1, 1,2, 2,3, 3,1]
        result = "graph has a Euler cycle"
        if(methodLogic3.matrixToList(methodLogic3.createGraph(70,3)) == result):
            self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()


