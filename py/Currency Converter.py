name = (input("Enter your name : "))
print ("Hello " + name)

import datetime
print("The current date and time is: ")
print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

def menu():
    print("-" * 30)
    print("Ahmed's Currency converter")
    print("-" * 30)


def  getChoice(message, options):

    choice = input(message + " : ").lower()
    while choice not in options:
        choice = input("Try again : ")
    return choice



def getAmount():
    amount = -1
    while amount < 0:
        try:
            amount = round(float(input("Please enter your amount : ")),2)
        except ValueError:
            print("Try again")
    return amount
        

converter = { 'po' : 1,
              'eu' : 1.5,
              'do' : 2,
              'ye' : 120, }


currencyOptions = ['po','eu','do','ye']

menuChoice = ""

while menuChoice != 'qu':

    menu()

    menuChoice = getChoice("Would you like to [co]nvert, [ed]it rates or [qu]it?", ['co','ed','qu'])

    if menuChoice == 'co':
        
        currencyIn = getChoice("Convert from [po]unds, [eu]ros, [do]llars or [ye]n", currencyOptions)
        amountIn = getAmount()

        currencyOut = getChoice("Convert to [po]unds, [eu]ros, [do]llars or [ye]n", currencyOptions)

        amountOut = round(amountIn * (converter['po'] / converter[currencyIn]) * converter[currencyOut],2)
        print(amountIn,currencyIn," = ",amountOut, currencyOut)

    elif menuChoice == 'ed':

        print("Today £1 is worth : ")
        for currency in converter:
            print("  ", converter[currency], currency)
        
        currencyToChange = getChoice("Which currency rate to set?", currencyOptions)

        newRate = getAmount()
    
        converter[currencyToChange] = newRate
