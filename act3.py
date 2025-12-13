def numbers(n,num):
    if (n>num):
        return
    numbers(n+1,num)
    print(n)
n=int(input("enter a number: "))
numbers(1,n)