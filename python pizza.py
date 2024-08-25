print("welcome")
size=input("what size do you want")
p=input("do you want pepperoni")
cheese=input("do you want extra cheese")
bill=0
if size== 'S':
    bill+=30
elif size=='M':
    bill+=50
elif size=='L':
    bill+=80
if p=='Y':
    bill+=30
elif p=='N':
    bill+=0
if cheese=='Y':
    bill+=30
elif cheese=='N':
    bill+=0
print(f"your final bill is {bill}")

