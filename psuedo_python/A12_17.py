def A(a,b):
    if a == 0:
        return 0
    else:
        return A(a-1,b) + b


a = 12
b = 17

print(A(a,b))
