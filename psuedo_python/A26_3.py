def A(a,b):
    if a < b:
        return a
    else:
        return A(a-b,b) 


a = 26
b = 3

print(A(a,b))
