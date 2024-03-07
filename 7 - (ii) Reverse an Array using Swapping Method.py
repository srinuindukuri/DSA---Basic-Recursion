# Using Swapping Method
def Reverse(A, start, end):
    while(start < end):
        A[start], A[end] = A[end], A[start]
        start = start + 1
        end = end - 1


A = [10, 20, 30, 40, 50]
Reverse(A, 0, 4)
print(A)
