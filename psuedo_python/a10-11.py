def A(a,b):
    if b == 0:
        return 0
    else:
        return A(a,b-1) +a


a = 10
b = 11

print(A(a,b))
