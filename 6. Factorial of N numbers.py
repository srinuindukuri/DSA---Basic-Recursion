# U should not write num == 0, if u write num == 0, then it returns 0. Because 0 x anything is 0.
def Factorial(num):
    if num == 1:
        return 1
    return num * Factorial(num-1)


num = int(input("Enter the number: "))
print(Factorial(num))
