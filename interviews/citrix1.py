
# iterate the array with minimum moves. At an index i - you can either move to i+1 or some other index j such that a[i] == a[j]

def minimum_jump(lst):
    cost = dict()

    i = len(lst) - 1

    while i >= 0:
        if lst[i] not in cost:
            cost[lst[i]] = len(lst) - i
        else:
            cost[lst[i]] += 1
        i -= 1

    return cost[lst[0]]


a = [1, 2, 3, 4, 5, 2, 6, 1, 3]

minimum_jump(a)
