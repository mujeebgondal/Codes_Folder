while True :  
    num=int(input("enter a number : "))
    r=int(input("give a number to which you want to write table :"))
    t=1
    while t<= r:
        print(f"{num}*{t}={num*t}")
        t=t+1
    a=input("do you want another table (yes/no)")
    if a =='yes' :
        continue
    elif a == 'no':
        break
    else :
        print("invalid input")