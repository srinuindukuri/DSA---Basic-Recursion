def num(n):
    if (n < 1):
        return
    else:
        print(n)
        num(n-1)


n = int(input("Enter the number: "))
num(n)
