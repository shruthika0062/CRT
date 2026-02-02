for i in range(1, 11):
    if i == 5:
       continue
    print(i,end= " ")
    else:
        print("Loop completed")

#password retry example:

p1 = "abc123"
for i in range(3):
    p2=input("Enter password: ")
    if p1==p2:
        print("Access successful")
        break
else:
    print("Account locked")
