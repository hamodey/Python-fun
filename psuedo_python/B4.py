def B(a):
    if a == 0:
        return 0
    else:
        return B(a-1) + a * a


a = 4

print(B(a))
