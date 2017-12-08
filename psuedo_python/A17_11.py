def A(a,b):
    if b == 0:
        return a
    else:
        return A(a-1,b-1)


a = 17
b = 11

print(A(a,b))
