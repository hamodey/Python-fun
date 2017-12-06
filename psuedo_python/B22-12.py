def A(a,b):
    if b == 0:
        return a
    else:
        return A(a-1,b-1)


a = 22
b = 12

print(A(a,b))
