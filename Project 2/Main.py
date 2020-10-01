from Contact import Contact
""" Program made by Tristan Carlo Jara"""
contactList = list()

def main():
    """Main function of the program"""
    menu()

def menu():
    """A simple options menu for the user of the program"""
    print("******************Simple Contact Tracing Program For Business Establishments****************")
    print("These are your options: ")
    print("1. Add customer details ")
    print("2. Show list of customers ")
    print("3. Exit the program ")
    choice = input("Enter a number [1-3]: ")
    choice = int(choice)
    if choice == 1:
        addCurrent()
    elif choice == 2:
        showCustomers()
    elif choice == 3:
        print(" ")
        print("**********Thank you for using the program***********")
        SystemExit(0)
    else:
        print("Sorry wrong input, try again")
        menu()

def addCurrent():
    """This function will add people to a list of customers"""
    global contact, addAnother
    while True:
        lName = input("Enter last name of person: ")
        fName = input("Enter first name of person: ")
        contactNum = input("Enter contact number: ")
        barangay = input("Enter the barangay of the person: ")
        contact = contactList.append(Contact(lName, fName, contactNum, barangay))
        print("Customer Added!")
        addAnother = input("Add another customer? [Yes/No]: ")
        if addAnother == "Yes":
            addAnother = True
            addCurrent()
        elif addAnother == "No":
            addAnother = False
            menu()


def showCustomers():
    """This function will show the list of customers or people"""
    print(" ")
    print("**************List of Customers****************")
    print(" ")
    for index in range(len(contactList)):
        print(contactList[index].lastName + " , " + contactList[index].firstName + " , " + contactList[
            index].contactNo + " , " +
              contactList[index].barangay)
        print(" ")
        print("**********************************************")
        menu()

main()




