def A(a,b):
    if b == 0:
        return a
    else:
        return A(a,b-1) + 1


a = 9
b = 7

print(A(a,b))
