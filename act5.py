def negative():
    number=int(input())
    if number<0:
        print("Number -ve")
        return
    else:
        print("Number +ve")
        negative()
negative()
    
