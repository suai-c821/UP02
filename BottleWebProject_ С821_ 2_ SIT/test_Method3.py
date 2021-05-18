import unittest 
import methodLogic3

class Test_test_1(unittest.TestCase):
    def testMethod(self):
        graph = [[0,1, 1,2, 2,3, 3,1], [2, 1, 2, 2, 3, 3], [1, 1, 2, 2, 3, 1, 3, 2, 3, 3, 4, 1, 4, 2, 4, 3], [1, 1, 2, 1, 2, 2, 3, 2], [1, 1, 2, 2, 3, 2]]
        result = ["graph has a Euler cycle", "graph is not Eulerian", "graph has a Euler path", "graph has a Euler path", "graph is not Eulerian"]
        for i in range(len(graph)):
            if(methodLogic3.matrixToList(graph[i]) == result[i]):
                self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()


