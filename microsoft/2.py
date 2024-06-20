# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S, C):
    """
    :type S: string
    :type C: List
    :rtype: int
    """

    # no identical letters
    if len(S) == len(set(S)):
        return 0

    cost = 0

    i = 0
    while i < len(S) - 1:

        j = i + 1

        # if immediate right is not identical than skip
        if S[j] != S[i]:
            i = j
            continue

        # move j to right most letter identical to S[i]
        while j < len(S) - 1 and S[j + 1] == S[i]:
            j += 1

        # i to j is now the window of letters identical to S[i] - skip the highest cost
        cost += sum(C[i : j + 1]) - max(C[i : j + 1])

        i = j + 1

    return cost


# solution('abccbd', [0,1,2,3, 4, 5])
# solution('aabbcc', [1,2,1,2,1,2])
# solution('aaaa', [3, 4, 5, 6])
solution("ababa", [10, 5, 10, 5, 10])
