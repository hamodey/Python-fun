def B(a):
    if a == 0:
        return True
    else:
        return !B(a-1)


b = 2

print(B(b))
