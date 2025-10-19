# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.


def setZeroes(matrix) :
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        rows_track = [0] * rows
        cols_track = [0] * cols
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0 :
                    rows_track[i] = -1
                    cols_track[j] = -1
        for i in range(rows):
            for j in range(cols):
                if rows_track[i] == -1 :
                    matrix[i][j] = 0
                if cols_track[j] == -1 :
                    matrix[i][j] = 0        
                

        