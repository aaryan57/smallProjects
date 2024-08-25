def add(n1,n2):
    print(n1+n2)
def multiply(n1,n2):
    print(n1*n2)
def subtract(n1,n2):
    print(n1-n2)
def divide(n1,n2):
    print(n1/n2)
choice=1
while choice:
    n1=int(input("enter first number\n"))
    op=input("enter operation\n")
    n2=int(input("enter second number\n"))
    print(f"{n1}{op}{n2}=\n")
    if op=='+':
        add(n1,n2)
    elif op=='-':
        subtract(n1,n2)
    elif op=='*':
        multiply(n1,n2)
    elif op=='/':
        divide(n1,n2)
    else:
        print("error")
    n=input("press y to continue n to exit\n")
    if n=='y':
        choice+=1

    elif n=='n':
        choice=0
    else:
        print("rnter valid choice")
