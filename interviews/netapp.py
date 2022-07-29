

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# m * n


def spiralTraversal(matrix):
    '''
        A func to traverse the arry spirally
    '''
    result = []

    # row
    m = len(matrix)

    # col
    n = len(matrix[0])

    # boundary = (row_boundary, col_boundary)

    left_boundary = [0, 0]
    right_boundary = [m-1, n-1]  # 2,2

    while left_boundary != right_boundary:

        i = left_boundary[0]
        j = left_boundary[1]
        result.append(matrix[i][j])

        # increment my left boundary
        left_boundary[0] += 1
        left_boundary[1] += 1

        while j < right_boundary[1]:  # 1 -> 2
            j += 1
            result.append(matrix[i][j])

        while i < right_boundary[0]:  # 1 -> 2
            result.append(matrix[i][j])
            i += 1

        while j >= left_boundary[1]:
            result.append(matrix[i][j])
            j -= 1

        while i >= left_boundary[0]:
            i -= 1
            result.append(matrix[i][j])

        # decrement my right boundary
        right_boundary[1] -= 1
        right_boundary[0] -= 1

        return result


print(spiralTraversal(matrix))


# i = 0, j = 0 , result = [matrix(0,0)]
# j from 1 to  2 result = [ matrix(0,0), matrix(0,1), matrix(0,2)]
# i from 1 to 2
#   result = [ matrix(0,0), matrix(0,1), matrix(0,2), matrix(1,2), matrix(2,2)]
# j from 1 to 0 result = result + [matrix(2,1), matrix(2,0)]
# i from 1 to 0 result = result + [matrix(1,0), matrix(0,0)]
