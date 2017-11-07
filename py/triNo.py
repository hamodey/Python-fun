n = int(input("Input a number: "))
for i in range(1, n+1):
    print("triangular number - ", int((i+1)*2))


p_in = input("mamamamamamammmammma: ")

def palidrom(input_):
    if input_ == input_[::-1]:
        return True
    else:
        return False
print(palidrom(p_in))
