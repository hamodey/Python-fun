on = True
def sumTo():
    n = int(input("enter n: "))
    while n > 0:
        z = n - 1
        print(n, "+", z)
        n = n - 1
    y = z + n
    print(y)
    return z

def  getChoice(message, options):

    choice = input(message + " : ").lower()
    while choice not in options:
        choice = input("Try again : ")
    return choice
menuOptions = ['q']

def main():
    sumTo()
#    menuChoice = getChoice("press q to quit anytime", menuOptions)
#    if menuChoice == 'q':
#        on = False

main()

