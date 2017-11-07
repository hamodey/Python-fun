

def main(): # def makes it a menu so the user can chose what to do i.e "Quit" etc
    print("*** Ahmed's AddressBook ***")
    my_data = load("AhmedsAddressBook.csv")
    if my_data == []:
        print("No data found")
        return
    while 1:
        print("1:search by surname\n2: search by month of birth\nq: quit.""")
        choice= input("How would you like to search?: ")# This line is used to put in an input so the name can be what the user wants it to be
        if choice == 'q':
            break
        elif choice == '1':
            search_name(my_data)
        elif choice == '2':
            search_date(my_data)
        else:
            print("Unrecognised choice.")

def search_date(data):
    """Takes the data and searches by date."""#This line above searches in the data used "AddressBook.csv" 
    print("\nSearch by month of birth.")#This line allows the user to input the birth to search the .csv file
    print("Press 'Enter' to return to main menu.")
    while 1:

        month = (input("Month: "))#This line represents what the user inputs and searches it

        if month == "":
            return

        try:
            month = int(month)
            if month < 1 or month > 12:#this line is used to show only 12 months because it not possible to go over 12 or uner 1 of course
                raise ValueError
            else:
                display(list(filter(lambda x: int(x[6].split('/')[1]) == month, data)), "month only")
        except ValueError:
            print("Month must be an integer between 1 and 12.")#
            continue

def display(results, fields = "all"):
    """Takes a list of results and prints them out neatly."""
    n = len(results) #This will display the results of the input that is chosen by the user
    if n == 0:
        print("No matches found.")
        return
    if fields == "month only":
        print("Search results:")
        for a in results:
            print("\t" + a[1] + " " + a[0])
        return
    for i, a in enumerate(results, 1):
        print("\nSearch Results (" + str(i) + " of " + str(n) + "):\n")
        print("Name:\t\t" + a[1] + " " + a[0])
        print("Address:\t" + a[2] + ", " + a[3] + ", " + a[4] + '.')
        print("Telephone:\t" + a[5])
        print("Date of Birth:\t" + a[6])
        print("Email:\t\t" + a[7])
        print("\n \nPress 'Enter' to return to main menu")


def search_name(data):
    
    """Takes the list of data and searches by name."""
    print("\nSearch by surname.")
    print("Press 'Enter' to return to main menu.")
    while 1:

        name = input("Name: ").lower()     #changes the string into lowercase
        
        if name == "":
            return
    
        try:
            name = int(name)
            if name == int(name):
                print("Must be 'letters' no numbers accepted.")
                raise ValueError
            display(list(filter(lambda x: x[0].lower() == name, data)))

        except ValueError:
    
            display(list(filter(lambda x: x[0].lower() == name, data)))
        
        #Filter only allows 'Name and Data' and constructs a list for it. The lambda is an anonymous function
                     
def display(results, fields = "all"):
    """Takes a list of results and prints them out neatly."""
    n = len(results) #This will display the results of the input that is chosen by the user
    if n == 0:
        print("No matches found.")
        return
    if fields == "name only":
        print("Search results:")
        for a in results:
            print("\t" + a[1] + " " + a[0])
        return
    for i, a in enumerate(results, 1):
        print("\nSearch Results (" + str(i) + " of " + str(n) + "):\n")
        print("Name:\t\t" + a[1] + " " + a[0])
        print("Address:\t" + a[2] + ", " + a[3] + ", " + a[4] + '.')
        print("Telephone:\t" + a[5])
        print("Date of Birth:\t" + a[6])
        print("Email:\t\t" + a[7])
        print("\n \nPress 'Enter' to return to main menu")
    
        
def load(filename):#This loads the file that is being used
    """Takes a filename. Reads data from the address book, if found."""
    try:
        f = open(filename, 'r')
        # List shows all the results in a list form
        # explain how the how each line of the file is made into a list.

        data = [line.split(',') for line in f] ###
        f.close()
    except IOError: ###
        data = []
    return data
    
if __name__ == "__main__": ###
    main()
