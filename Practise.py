def Reverse(A, Start, End):
    if (Start >= End):
        return
    A[Start], A[End] = A[End], A[Start]
    Reverse(A, Start+1, End-1)

A = [10, 20, 30, 40]
Reverse(A, 0, 3)
print(A)