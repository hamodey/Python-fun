def A(a,b):
    if a == b:
        return 0
    else:
        return A(a-1,b) +1


a = 15
b = 5

print(A(a,b))
