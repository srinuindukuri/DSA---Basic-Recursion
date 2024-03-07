# U want the function to return the answer, not the parameter...
def Sum(num):
    if num == 1:
        return 1
    return num + Sum(num-1)


num = int(input("Enter the number: "))
print(Sum(num))
