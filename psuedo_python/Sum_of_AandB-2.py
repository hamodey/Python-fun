def A(a,b):
    if a == 0:
        return b
    else:
        return A(a-1,b+1) 


a = 27
b = 5

print(A(a,b))
