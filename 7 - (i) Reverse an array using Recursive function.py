# Using Recursive Method
def Reverse(A, start, end):
    if(start >= end):
        return
    A[start], A[end] = A[end], A[start]
    Reverse(A, start+1, end-1)


A = [10, 20, 30, 40, 50]
Reverse(A, 0, 4)
print(A)
