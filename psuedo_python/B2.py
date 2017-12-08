def B(a):
    if a == 0:
        return 1
    else:
        return a * B(a-1)


b = 2

print(B(b))
