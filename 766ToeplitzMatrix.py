"""
    A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
    Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
    1234
    5123
    9512
    In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]", and in each diagonal all elements are the same, so the answer is True.


"""
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
            :type matrix: List[List[int]]
            :rtype: bool
        """

#       if matrix[-1][1] != matrix[-2][0]:
#           return false
        for i in range(1, len(matrix)):
            if matrix[i-1][:len(matrix[j]) - 1] != matrix[i][1:]:
                 return False
        return True

