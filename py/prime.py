
def isPrime():
    n = int(input("Input n value:"))
    x = 2
    prime = False
    for i in range(1, n):
        if x < n:
            if n%x == 0:
                prime = False
            else:
                x += 1
        else:
            prime = True
    if prime:
        print("This is a prime no.")
    else:
        print("Not a prime")
#
while True:
    isPrime()
