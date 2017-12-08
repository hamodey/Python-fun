def A(a,b):
    if b == 0:
        return 1
    else:
        return A(a,b-1) * a


a = 10
b = 2

print(A(a,b))
