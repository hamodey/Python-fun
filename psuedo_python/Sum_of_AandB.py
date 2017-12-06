def A(a,b):
    if b == 0:
        return a
    else:
        return A(a,b-1) + 1


a = 27
b = 5

print(A(a,b))
