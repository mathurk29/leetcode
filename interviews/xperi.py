# Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.

# Input: intervals = [[1,3],[2,6],[5,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

def mergeInterval(input):

    result = []
    i = 0
    base = input[i]
    while i < len(input) - 1 :
        comparison = input[i+1]

        if base[1] > comparison[0]: # 10 > 2


            if base[1] < comparison[1]:  #  10 < 6
                base = [base[0], comparison[1]]
                i = i + 1
            
            else: 
                i = i + 2

        result.append(base)


    return result


input = [[1, 10], [2, 6]]
input = [[1, 10], [2, 6], [4,15], [6,13], [12,20], [22,25], [27,28], [30,35], [32,40] ]
mergeInterval(input)


# Output: [[1,6],[8,10],[15,18]]
