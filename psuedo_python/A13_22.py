def A(a,b):
    if b == 0:
        return a
    else:
        return A(a,b-1) + 1


a = 13
b = 22

print(A(a,b))
