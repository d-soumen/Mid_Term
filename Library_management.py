class Library:
    book_list=[]
    @classmethod
    def entry_book(cls,book):
        cls.book_list.append(book)

class Book:
    def __init__(self,book_id,title,author,availability):
        self.__book_id=book_id
        self.__title=title
        self.__author=author
        self.__availability=availability

    def borrow_book(self):
        if self.__availability:
            self.__availability=False
            print(f"{self.__title} has been borrowed succesfully.")
        else:
            print(f"{self.__title} is not available for borrowing.")
    
    def return_book(self):
        self.__availability=True
        print(f"{self.__title} has been returned successfully.")
    
    def view_book_info(self):
        print(f"Book ID: {self.__book_id}")
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Availability: {'Available' if self.__availability else 'Not Available'}")
        print("===================================")
    
    def get_book_id(self):
        return self.__book_id
    

b1=Book(101,"Python Programming","John Doe",True)
b2=Book(102,"Data Science","Jane Smith",True)               
b3=Book(103,"Machine Learning","Alice Johnson",True)
b4=Book(104,"Artificial Intelligence","Bob Brown",True)
b5=Book(105,"Deep Learning","Charlie Davis",True)
b6=Book(106,"Web Development","Eve White",True)
b7=Book(107,"Database Management","Frank Green",True)
b8=Book(108,"Statistics","Grace Black",True)
b9=Book(109,"Computer Vision","Hannah Blue",True)
b10=Book(110,"Natural Language Processing","Ivy Yellow",True)


Library.entry_book(b1)
Library.entry_book(b2)
Library.entry_book(b3)
Library.entry_book(b4)
Library.entry_book(b5)
Library.entry_book(b6)
Library.entry_book(b7)
Library.entry_book(b8)
Library.entry_book(b9)
Library.entry_book(b10)



while True:
    print("\nView all books:press 1")
    print("Borrow a book:press 2")
    print("Return a book:press 3")
    print("Exit:press 4")
    choice=int(input("Enter your choice(1-4): "))
    if choice==1:
        print("Book Information:")
        for book in Library.book_list:
            book.view_book_info()
    elif choice==2:
        try:
            book_id=int(input("Enter the book ID to borrow: "))
            for book in Library.book_list:
                if book.get_book_id()==book_id:
                    book.borrow_book()
                    break
            else:
                print("Book not found.")
        except ValueError:
            print("Invalid input. Please enter a valid book ID.")
    
    elif choice==3:
        try:
            book_id=int(input("Enter the book ID to return: "))
            for book in Library.book_list:
                if book.get_book_id()==book_id:
                    book.return_book()
                    break
            else:
                print("Book not found.")
        except ValueError:
            print("Invalid input. Please enter a valid book ID.")
    
    elif choice==4:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

