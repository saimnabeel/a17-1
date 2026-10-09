yoo=(int(input("enter any number between 1 and 100: ")))
number=1
print("saim's triangle")
for i in range(1,yoo+1):
    for j in range(1,i+1):
        print(number,end=" ")
        number=number+1
    print()