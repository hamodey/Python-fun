import random
y = random.randrange(0,9)
def coinFlip():
    if y >= 5:
        z = 'Tails'
    else:
        z = 'Heads'
    return z
x = coinFlip()
print(x)
