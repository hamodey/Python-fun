def B(a):
    if a == 0 :
        return 1
    else:
        return a * B(a-1)


a = 5

print(B(a))
