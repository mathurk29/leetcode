# https://leetcode.com/problems/time-needed-to-inform-all-employees/


def numOfMinutes(n, headID, manager, informTime):
    children = [[] for i in range(n)]
    for i, m in enumerate(manager):
        if m >= 0:
            children[m].append(i)

    def dfs(i):
        return max([dfs(j) for j in children[i]] or [0]) + informTime[i]

    return dfs(headID)


n = 6
headID = 2
manager = [2, 2, -1, 2, 2, 2]
informTime = [0, 0, 1, 0, 0, 0]


numOfMinutes(n, headID, manager, informTime)
