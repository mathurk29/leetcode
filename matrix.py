def input_matrix():
    """How to take matrix input from terminal"""
    rows, cols = [int(x) for x in input().split()]  # give row, col
    matrix = []
    for _ in range(rows):
        row = input()
        matrix.append(list(row))
