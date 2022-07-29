# //   A = [ [“X”, “X”, “X”, “O”, “X”],
# //         [“O”, “O”, “O”, “X”, “O”],
# //         [“O”, “O”, “O”, “O”, “O”],
# //         [“X”, “X”, “O”, “O”, “X”] ] 4*5

# // An X region constitutes of connected X’s.
# // Find number of X regions


# regions are non-inersecting


# // A = [   [“X”, “O”, “O”, “O”, “X”],
# //         [“X”, “O”, “O”, “X”, “O”],
# //         [“X”, “O”, “X”, “O”, “O”],
# //         [“X”, “X”, “O”, “O”, “X”] ] 4*5

region1 = (0, 0), (1, 0)
region2 = (0, 4), (1, 3)


def getXregions(arr):

    visited = [[]]


def dfs(matrix, i, j, visited):

    if visited[i][j]:
        return
