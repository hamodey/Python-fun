def B(a):
    if a == 0:
        return True
    else:
	 c = not B(a-1)
	 return c


b = 7

print(B(b))
