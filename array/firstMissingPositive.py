

def solution(A):
    # Implement your solution here
    pass
    for i in range(len(A)):
        if A[i] > 0 and A[i] <= len(A) and A[i] != A[A[i] - 1]:
            # A[i] , A[A[i] - 1] = A[A[i] - 1], A[i]
            temp = A[i]
            A[i] = A[A[i] - 1] 
            A[temp - 1] = temp
            
    
    for i in range(len(A)):
        if A[i] != i + 1:
            return i + 1


    return len(A) + 1
