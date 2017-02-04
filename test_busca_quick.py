import unittest
from original import *

class TestBinarySearchQuick(unittest.TestCase):

    '''
        The quick sort just does order with elements of collection int
    '''

    #Aplication of the algorithm of binary search with sorted collection and return the index of value searched
    def test_binarySearch(self):
        self.assertEqual(buscaBinariaIndice([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(buscaBinariaIndice([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(buscaBinariaIndice([1, 2, 3, 4, 5], 5), 4)

        self.assertEqual(buscaBinariaIndice([1, 2, 3, 4], 2), 1)
        self.assertEqual(buscaBinariaIndice([1, 2, 3, 4], 3), 2)
        self.assertEqual(buscaBinariaIndice([1, 2, 3, 4], 4), 3)

    def test_repeated_elements(self):
        self.assertEqual(buscaBinariaIndice([3, 3, 3], 2), -1)
        self.assertEqual(buscaBinariaIndice([3, 3, 3], 3), 1)
        self.assertEqual(buscaBinariaIndice([3, 3, 3, 4], 4), 3)

    def test_limits_in_collection(self):
        order = [1, 4, 8, 3, 1, 2]
        quickSort(order, 0, len(order)-1)
        self.assertEqual([1, 1, 2, 3, 4, 8], order)

        lista1 = [1, 4, 2, 7, 3, 4]
        quickSort(lista1, 1, 3)
        self.assertEqual(lista1, [1, 2, 4, 7, 3, 4])

        lista2 = []
        quickSort(lista2, 0, 0)
        self.assertEqual(lista2, [])

        lista3 = [1, 4, 2, 7, 3, 4]
        quickSort(lista3, -1, 3)
        self.assertEqual(lista3, lista3)

        lista3 = [1, 4, 2, 7, 3, 4]
        quickSort(lista3, 0, 0)
        self.assertEqual(lista3, lista3)

        lista3 = [1, 4, 2, 7, 3, 4]
        quickSort(lista3, 0, 6)
        self.assertEqual(lista3, lista3)

    def test_not_in_list(self):
        self.assertEqual(buscaBinariaIndice([1, 3, 5, 6], 2), -1)
        self.assertEqual(buscaBinariaIndice([1, 3, 5, 6], -1), -1)
        self.assertEqual(buscaBinariaIndice([1, 2.5, 3, 5, 6], 2.4), -1)
        self.assertEqual(buscaBinariaIndice([-8, -4, -3, -2, 1], 2), -1)
        self.assertEqual(buscaBinariaIndice([1.2, 1.4, 1.5, 1.9], 2), -1)
        self.assertEqual(buscaBinariaIndice(['a', 'b', 'c', 'd', 'f'], 'e'), -1)
        self.assertEqual(buscaBinariaIndice(['cat', 'dog', 'horse', 'pig', 'zebra'], 'bird'), -1)

    def test_binarySearch_negatives(self):
        self.assertEqual(buscaBinariaIndice([-8, -4, -3, -2, 1], -2), 3)
        self.assertEqual(buscaBinariaIndice([-8, -4, -3, -2, 1], -8), 0)
        self.assertEqual(buscaBinariaIndice([-8, -4, -3, -2, 1], -4), 1)

    def test_binarySearch_float(self):
        self.assertEqual(buscaBinariaIndice([1.2, 1.4, 1.5, 1.9], 1.4), 1)
        self.assertEqual(buscaBinariaIndice([1.2, 1.4, 1.5, 1.9], 1.9), 3)
        self.assertEqual(buscaBinariaIndice([1.2, 1.4, 1.5, 1.9], 1.2), 0)
        self.assertEqual(buscaBinariaIndice([1.2, 1.4, 1.5, 1.9], 1.5), 2)

    def test_binarySearch_string(self):
        self.assertEqual(buscaBinariaIndice(['a', 'b', 'c', 'd', 'f'], 'a'), 0)
        self.assertEqual(buscaBinariaIndice(['a', 'b', 'c', 'd', 'f'], 'f'), 4)
        self.assertEqual(buscaBinariaIndice(['a', 'b', 'c', 'd', 'f'], 'c'), 2)

        self.assertEqual(buscaBinariaIndice(['cat', 'dog', 'horse', 'pig', 'zebra'], 'cat'), 0)
        self.assertEqual(buscaBinariaIndice(['cat', 'dog', 'horse', 'pig', 'zebra'], 'zebra'), 4)
        self.assertEqual(buscaBinariaIndice(['cat', 'dog', 'horse', 'pig', 'zebra'], 'horse'), 2)
        self.assertEqual(buscaBinariaIndice(['cat', 'dog', 'horse', 'pig', 'zebra'], 'dog'), 1)

    '''
        Test quick and after aplication of the algorithm binary search
    '''
    def quick_BinarySearch(self):
        order = [1, 7, 2, 6, 7]
        quickSort(order, 0, len(order)-1)
        self.assertEqual(order, [1, 2, 6, 7, 7])
        self.assertEqual(buscaBinariaIndice(order, 3), -1)
        self.assertEqual(buscaBinariaIndice(order, 2), 1)
        self.assertEqual(buscaBinariaIndice(order, 7), 3)

        negatives = [-1, -5, -3, 6, -11]
        quickSort(negatives, 0, len(negatives)-1)
        self.assertEqual(negatives, sorted(negatives))
        self.assertEqual(buscaBinariaIndice(negatives, -1), 4)
        self.assertEqual(buscaBinariaIndice(negatives, 1), -1)
        self.assertEqual(buscaBinariaIndice(negatives, -11), 0)

        floats = [1.2, 5, 2.3, 2]
        quickSort(floats, 0, len(floats)-1)
        self.assertEqual(floats, sorted(floats))



if __name__ == '__main__':
    unittest.main()
