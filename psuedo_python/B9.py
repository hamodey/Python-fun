def B(a):
    if a == 0:
        return 0
    else:
        return B(a-1) + 1


a = 9

print(B(a))
