# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.


def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # result = []
        # count = 0
        # for i in range(n-1,-1,-1):
        #     temp = []
        #     for j in range(n):
        #         temp.append(matrix[n-1-j][count])
        #     result.append(temp)
        #     count += 1
        # matrix[:] = result


        for i in range(n-1):
            for j in range(i + 1 , n):
                matrix[i][j],matrix[j][i] = matrix[j][i] , matrix[i][j]
        for i in range(n):
            matrix[i] = matrix[i][::-1]


        