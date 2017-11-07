x = int(input("enter x:"))
y = int(input("enter y:"))
z = int(input("enter z:"))

if x > y:
    if x > z:
        print(x, "is the largest")

    else:
        print(z, "is the largest")
else:
    if y > z:
        print(y, "is the largest")
    else:
        print(z, "is the largest")

