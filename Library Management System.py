class Library:
    
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def listOfBooks(self):
        print("\nBooks present in this library are : ")
        for book in listOfBooks:
            print(f"* {book}")

    def borrowBook(self, bookName):
        if bookName in listOfBooks:
            print(f"\nYou have been issued {bookName} book. Please keep it safe and return it within 30 days")
            listOfBooks.remove(bookName)
        else:
            print("\nSorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")

    def returnBook(self, bookName):
        listOfBooks.append(bookName)
        print("\nThanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")

class Student:
    def requestBook(self):
        bookName = (input("Enter the name of the book you want to borrow : ")).capitalize()
        return bookName

    def returnBook(self):
        bookName = (input("Enter the name of the book you want to return : ")).capitalize()
        return bookName

if __name__ == "__main__":

    import time

    listOfBooks = ["Python", "Java", "C++", "Javascript"]

    centralLibrary = Library(listOfBooks)
    student = Student()

    while (True):
        welcomeMSG = '''\n====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library\n'''
        print(welcomeMSG)

        a = input("Enter a choice : ")
        try:
            if int(a) == 1:
                centralLibrary.listOfBooks()

            elif int(a) == 2:
                centralLibrary.borrowBook(student.requestBook())

            elif int(a) == 3:
                centralLibrary.returnBook(student.returnBook())

            elif int(a) == 4:
                print("Thank you for visiting Central Library.")
                time.sleep(2)
                exit()

            else:
                print("Invalid Choice!")

        except Exception as e:
            print("Invalid Choice!")
