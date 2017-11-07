def gcd(m,n):
    #m = int(input("Enter m:"))
    #n = int(input("Enter n:"))
    if m < n:
        m, n = n, m
    while n != 0:
        m1 = m % n
        m = n
        n = m1
    print("The Greatest Common Divisor is:",m)
    return m

def decToBase(n,b):
    arr = []
    while n > 0:
        r = n % b
        #mystr = print(r, end="")
        arr.insert(0,r)
        d = int(n/b)
        n = d
    print(arr)
    mystr = ''
    for i in arr:
        i = str(i)
        mystr += i
    print(mystr)
    return mystr
    
gcd(10,3)

decToBase(123,2)
