#Main Program

import functions as f
import collection as c

bookList = c.bookList
credList = c.credList

while True:

    user = f.init_interface()

    if user == "Admin" or user == "1":
        if f.auth_admin(credList):
            while True:
                
                menu = f.welcome_admin()

                if menu == "1":
                    f.read_list(bookList)

                elif menu == "2":
                    f.add_book(bookList)

                elif menu == "3":
                    f.update_list(bookList)

                elif menu == "4":
                    f.delete_book(bookList)
                
                elif menu == "5":
                    f.sort_list(bookList)

                elif menu == "6":
                    break

                else:
                    f.show_menu_error()

        else:
            continue

    elif user == "Customer" or user == "2":
        while True:

            menu = f.welcome_user()

            if menu == "1":
                f.read_list(bookList)
            
            elif menu =="2":
                f.sort_list(bookList)

            elif menu == "3":
                f.rent_book(bookList)

            elif menu == "4":
                f.return_book(bookList)

            elif menu == "5":
                break

            else:
                f.show_menu_error()
    
    elif user == "Exit" or user == "3":
        break

    else:
        f.show_user_error()