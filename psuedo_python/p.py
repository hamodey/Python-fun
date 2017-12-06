def A(a,b):
    if a < b:
        return 0
    else:
        return A(a-b,b) +1


a = 27
b = 5

print(A(a,b))
