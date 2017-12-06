def A(a):
    if a == 0:
        return 1
    else:
        return a * A(a-1)


a = 8


print(A(a))
