def linear(n,num):
    if (n<1 or n>num):
        return
    print(n)
    linear(n-1,num)
    print(n)
n=int(input("Enter a number: "))
linear(n,n)