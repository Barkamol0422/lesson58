def tail(n,num):
    if n>num:
        return
    print(n)
    tail(n+1,num)
n=int(input("enter a number: "))
tail(1,n)