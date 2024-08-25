print("welcome to tip calclator")
bill=float(input("Enter your bill\n"))
tip=float(input("How much wuld you like to tip 10,12,15\n"))
people=int(input("how many people will split the bill\n"))
bwt=(tip/100)*bill+bill
each=bwt/people
print(f"each persons split is \n{each}")
