# All Functions For The Program Are Defined Here

from tabulate import tabulate

def init_interface():
    user  = input('''
    Main menu:             
    1. Admin
    2. Customer
    3. Exit program
                  
Select user type or exit program: ''').title()
    return user    

def auth_admin(credList):
    cred = input("Enter admin credentials: ")
    if cred in credList:
        return True
    else:
        print("\nInvalid credentials")
        return False

def welcome_admin():
    menu = input('''
Welcome to the Book Store                 
                 
    Admin Action:
    1. Show book list
    2. Add book
    3. Update book
    4. Delete book
    5. Sort book list
    6. Return to menu
                 
Enter the menu number that you want to run: ''')
    return menu

def welcome_user():
    menu = input('''
Welcome to the Book Store

Customer Action:
    1. Show book list
    2. Sort book list
    3. Rent book
    4. Return book
    5. Return to menu
                 
Enter the menu number that you want to run: ''')
    return menu

def read_list(bookList):
    while True:
        read_prompt = input('''
    Read Actions:
    1. Show all books
    2. Show book detail
    3. Return to user menu
    Enter read action number: ''')
        if read_prompt == "1":
            show_list(bookList)
        elif read_prompt == "2":
            while True:
                try:
                    readIndex = int(input("\nInput book index to display specific book info (four digit integer): "))
                except:
                    print('\nBook index not found')
                    break
                if readIndex not in [book["index"] for book in bookList]:
                    print("\nBook index not found")
                    break
                for book in bookList:
                    if book["index"] == readIndex:
                        allPrompt = input("Display all fields? (yes/no): ").lower()
                        if allPrompt == "yes":
                            print(f'\n{tabulate([book], headers="keys", tablefmt="pretty")}')
                            break
                        elif allPrompt == "no":
                            readHeaders = input("Which columns would you like to read? (Comma Separated): ").replace(' ','').lower().split(",")
                            try:
                                readEntries = [[book[column] for column in readHeaders] for book in bookList if book["index"] == readIndex]
                            except:
                                print("\nColumn name(s) not found")
                                break
                            print(f'\n{tabulate(readEntries,headers = readHeaders,tablefmt = "pretty")}')
                            break
                        else:
                            print("\nPlease enter a valid input")
                            break
                break
                        
        elif read_prompt == "3":
            break
        else:
            show_menu_error()

def show_list(bookList):
    headers = list(bookList[0].keys())
    entries = [list(entry.values()) for entry in bookList]
    table = tabulate(entries, headers = headers, tablefmt="pretty")
    print(f"\n{table}")

def add_book(bookList):
    while True:
        add_prompt = input('''
    Add Actions:
    1. Add new book
    2. Return to user menu
    Enter create action number: ''')
        if add_prompt == "1":
            while True:
                show_list(bookList)
                try:
                    askIndex = int(input("\nEnter new book index (four digit integer): "))
                except:
                    print("\nInvalid input format")
                    break
                if len(str(askIndex)) != 4:
                    print("\nInvalid integer format")
                    break
                if askIndex in [book["index"] for book in bookList]:
                    print("\nBook index already exists in book list")
                    break
                addTitle = input("Enter book title: ").title()
                addAuthor = input("Enter book author: ").title()
                try:
                    addPages = int(input("Enter page count (int): "))
                except:
                    print("\nInput must be an integer")
                    break
                try:
                    addPeriod = int(input("Enter max rent period in days (int): "))
                except:
                    print("\nInput must be an integer")
                    break
                try:
                    addPrice = int(input("Enter daily rent price (int): "))
                except:
                    print("\nInput must be an integer")
                    break
                addDict = {"index":askIndex,"title":addTitle,"author":addAuthor,"pages":addPages,"allowed_rent_days":addPeriod,"price_per_day":addPrice,"rentable":True,"days_being_rented":0}
                print(f'\n{tabulate([addDict], headers = "keys", tablefmt="pretty")}\n')
                savePrompt = input("Save new book to book list? (yes/no): ").lower()
                if savePrompt == "yes":
                    bookList.append(addDict)
                    show_list(bookList)
                    print("\nBook added into book list")
                elif savePrompt == "no":
                    print("\nBook addition cancelled")
                else:
                    print("\nPlease input a valid response")
                break
        elif add_prompt == "2":
            break
        else:
            show_menu_error()

def update_list(bookList):
    while True:
        update_prompt = input('''
    Update Actions:
    1. Update book info
    2. Return to user menu
    Enter update action number: ''')
        if update_prompt == "1":
            while True:
                show_list(bookList)
                try:
                    udtIndex = int(input("\nEnter book index you want to update: "))
                except:
                    print("\nPlease enter a valid response")
                    break
                if udtIndex not in [book["index"] for book in bookList]:
                    print("\nBook index not found")
                    break
                for book in bookList:
                    if book["index"] == udtIndex:
                        print(f'\n{tabulate([book], headers = "keys", tablefmt="pretty")}')
                        contUpdate = input(f'\nUpdate {book["title"]}? (yes/no): ').lower()
                        if contUpdate == "no":
                            print("\nBook update cancelled")
                            break
                        elif contUpdate != "yes":
                            print("\nPlease enter a valid response")
                            break
                        udtColumns = input("Which columns would you like to update? (Comma Separated): ").replace(' ','').lower().split(",")
                        try:
                            for column in udtColumns:
                                book[column]
                        except:
                            print("\nColumn name(s) not found")
                            break
                        for column in udtColumns:
                            if column == "index":
                                print("'index' cannot be updated")
                                continue
                            elif column == "rentable":
                                answer = input("Invert book 'rentable' status? (yes/no): ").lower()
                                if answer == "yes":
                                    book[column] = not column
                                elif answer == "no":
                                    continue
                                else:
                                    print(f"Invalid input, '{column}' will not be updated")
                                    continue
                            elif isinstance(book[column],int):
                                try:
                                    udtValue = int(input(f"Enter new value for {column} (int): "))
                                except:
                                    print(f"Invalid input, '{column}' will not be updated")
                                    continue
                                book[column] = udtValue
                            else:
                                udtValue = input(f"Enter new value for {column}: ").title()
                                book[column] = udtValue
                        print(f'\n{tabulate([book], headers = "keys", tablefmt="pretty")}\n')
                        break
                break
        elif update_prompt == "2":
            break
        else:
            show_menu_error()

def delete_book(bookList):
    while True:
        delete_prompt = input('''
    Delete Actions:
    1. Delete existing book
    2. Return to user menu
    Enter delete action number: ''')
        if delete_prompt == "1":
            while True:
                show_list(bookList)
                try:
                    dltIndex = int(input("\nEnter book index you want to delete: "))
                except:
                    print("\nPlease enter a valid response")
                    break
                if dltIndex not in [book["index"] for book in bookList]:
                    print("\nBook index not found!")
                    break
                for book in bookList:
                    if book["index"] == dltIndex:
                        print(f'\n{tabulate([book], headers = "keys", tablefmt="pretty")}')
                        rmvPrompt = input("\nDelete book from book list? (yes/no) ").lower()
                        if rmvPrompt == "yes":
                            bookList.remove(book)
                            show_list(bookList)
                            print(f"\n{book['title']} deleted from book list")
                            break
                        elif rmvPrompt == "no":
                            print("\nBook deletion canceled")
                            break
                        else:
                            print("\nPlease enter a valid response")
                            break
                dltDecide = input("\nDelete another book from book list? (yes/no): ").lower()
                if dltDecide == "yes":
                    continue
                elif dltDecide != "no":
                    print("\nPlease enter a valid response")
                    break
                else:
                    print("\nBook deletion completed")
                break
        elif delete_prompt == "2":
            break
        else:
            show_menu_error()

def sort_list(bookList):
    while True:
        sort_prompt = input('''
    Sort Actions:
    1. Sort book list
    2. Return to user menu
    Enter sort action number: ''') 
        if sort_prompt == "1":
            while True:
                show_list(bookList)
                column = input('\nEnter column name you would like to sort by: ').lower()
                try:
                    bookList[0][column]
                except:
                    print("\nColumn name not found")
                    break
                order = input('Sort from highest to lowest value? (yes/no): ').lower()
                if order == 'yes':
                    order = True
                    bookList.sort(key=lambda x: x[column], reverse = order)
                    show_list(bookList)
                    break
                elif order == 'no':
                    order = False
                    bookList.sort(key=lambda x: x[column], reverse = order)
                    show_list(bookList)
                    break
                else:
                    print("\nPlease enter a valid response")
                    break
        elif sort_prompt == "2":
            break
        else:
            show_menu_error()

def rent_book(bookList):
    while True:
        rent_prompt = input('''
    Rent Actions:
    1. Rent from book list
    2. Return to user menu
    Enter rent action number: ''') 
        if rent_prompt == "1":
            show_list(bookList)
            for book in bookList:
                book["currently_rented"] = False
            while True:
                rent = int(input("\nEnter book index that you want to rent: "))
                found = False
                for book in bookList:
                    if book["index"] == rent and book["rentable"] == True:
                        found = True
                        rentprd = int(input(f"Enter rent period in days for {book['title']}: "))
                        if rentprd > book['allowed_rent_days']:
                            print(f"Max rent period exceeded, you can rent {book['title']} for up to {book['allowed_rent_days']} days")
                        elif rentprd <= 0:
                            print("The amount of days that you want to rent the book for must exceed zero")
                        else:
                            book["days_being_rented"], book["rentable"], book["currently_rented"] = rentprd, False, True
                    elif book["index"] == rent and book["rentable"] == False:
                        found = True
                        print(f"\n{book['title']} is not rentable at the moment\n")
                if found == False:
                    print("\nPlease enter a valid book index\n")
                headers = list(bookList[0].keys())
                entries = [list(entry.values()) for entry in bookList]
                # print out title, days rented, price_per_day columns
                rentHeader = [headers[i] for i in [1, 7, 5]]
                # input entries that are rented in this transaction loop (currently_rented == True)
                rentEntry = [[entry[i] for i in [1, 7, 5]] for entry in entries if entry[8] == 1]
                table = tabulate(rentEntry, headers = rentHeader, tablefmt = "pretty")
                if rentEntry:
                    print(table)
                decision = input("Would you like to rent anything else? (yes/no): ").lower()
                if decision == "no":
                    billHeader = rentHeader
                    billHeader.append("Total Price")
                    billEntry = rentEntry
                    #calculate total price for each rented book by multiplying days rented with price_per_day
                    for entry in billEntry:
                        entry.append(entry[1]*entry[2])
                    bill = tabulate(billEntry, headers = billHeader, tablefmt = "pretty")
                    if billEntry:
                        print(bill)
                    fintotal = 0
                    for book in bookList:
                        if book["currently_rented"] == True:
                            fintotal += book['days_being_rented']*book['price_per_day']
                    if fintotal == 0:
                        print("\nYou did not rent any books")
                        for book in bookList:
                            del book["currently_rented"]                
                        break
                    while True:
                        print(f'Total amount that must be paid = {fintotal}')
                        payamt = int(input("Enter payment amount: "))
                        if (payamt < fintotal):
                            print(f"Your payment is short by {fintotal-payamt}")
                        else:
                            print(f"\nThank you for your payment!\nYour change: {payamt-fintotal}")
                            break
                    for book in bookList:
                        del book["currently_rented"]
                    break
                elif decision != "yes":
                    print("Please enter a valid input")
        elif rent_prompt == "2":
            break
        else:
            show_menu_error()

def return_book(bookList):
    while True:
        return_prompt = input('''
    Return Actions:
    1. Return rented book
    2. Return to user menu
    Enter return action number: ''') 
        if return_prompt == "1":
            while True:
                show_list(bookList)
                if all([book["rentable"] for book in bookList]):
                    print("\nNo books can be returned at the moment")
                    break
                try:
                    rtnIndex = int(input("\nEnter book index that you want to return: "))
                except:
                    print("\nPlease input a valid index")
                    break
                if rtnIndex not in [book['index'] for book in bookList]:
                    print("\nBook index not found")
                    break
                for book in bookList:
                    if book["index"] == rtnIndex and book["rentable"] == False:
                        try:
                            rtnDays = int(input(f"Enter amount of days {book['title']} has been rented: "))
                        except:
                            print("\nPlease enter a valid input")
                            break
                        if rtnDays < 0:
                            print("\nInvalid amount of days")
                            break
                        rtnPayment = (book["days_being_rented"]-rtnDays)*book["price_per_day"]
                        if rtnPayment < 0:
                            print("You have returned the book late\nPlease also pay the penalty fee if you have exceeded the max rent period (Equal to price_per_day per day exceeded)")
                            #equation below calculates late fee exceeding allowed_rent_days
                            penaltyFee = max(rtnDays,book["allowed_rent_days"])*book["price_per_day"]-book["allowed_rent_days"]*book["price_per_day"]
                            ttlPay = abs(rtnPayment)+penaltyFee
                            print(f'Amount that must be paid = outstanding amount: {abs(rtnPayment)} + penalty fee: {penaltyFee} = {ttlPay}')
                            try:
                                latePmt = int(input("Enter payment amount: "))
                            except:
                                print("\nInvalid payment input")
                                break
                            if (latePmt < ttlPay):
                                print(f"Your payment is short by {ttlPay-latePmt}")
                            else:
                                print(f"\nThank you for returning our book!\nYour change: {latePmt-ttlPay}\n")
                                book["rentable"], book["days_being_rented"] = True, 0
                                break
                        elif rtnPayment > 0:
                            print(f'Outstanding amount that will be returned: {rtnPayment}\nThank you for returning our book!')
                            book["rentable"], book["days_being_rented"] = True, 0
                            break
                        else:
                            print("Thank you for returning our book!")
                            book["rentable"], book["days_being_rented"] = True, 0
                            break
                    elif book["index"] == rtnIndex and book["rentable"] == True:
                        print("\nCannot return books which are available for rent")
                break
        elif return_prompt == "2":
            break
        else:
            show_menu_error()


def show_menu_error():
    print("\nPlease input a valid menu number!")

def show_user_error():
    print("\nInvalid input. Please input Admin/Customer/Exit or 1/2/3\n")
