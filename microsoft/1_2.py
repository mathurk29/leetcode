def hammingAlgo(binary_number):
    """
    :type n: int
    :rtype: int
    """
    cost = 0
    while binary_number:
        binary_number &= binary_number - 1
        cost += 1
    return cost


def solution(A, B):
    return hammingAlgo(A * B)


solution(3, 7)
