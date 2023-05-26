def solution(A):
    # Implement your solution here K
    pass
    for i in range(len(A)):
        if A[i] > 0 and A[i] <= len(A) :#and A[i] != A[A[i] - 1]:
            # A[i] , A[A[i] - 1] = A[A[i] - 1], A[i]
            temp = A[i]
            A[i] = A[A[i] - 1] 
            A[temp - 1] = temp
            
    print("For Testcase - ")
    print(A)
    print("Answer is:")
    
    for i in range(len(A)):
        if A[i] != i + 1:
            return i + 1

    return len(A) + 1

testcases = [

    [0],
    [-1],
    [-1,-2],
    [0, -1,-2],
    [1],
    [2],
    [3],
    [0,1],
    [0,2],
    [23,345345,6575678,0]

]

for testcase in testcases:
    solution(testcase)