def A(a,b):
    if a == 0:
        return 0
    else:
        return A(a-1,b) + b


a = 6
b = 2
print(A(a,b))
