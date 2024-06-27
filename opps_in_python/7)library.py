# write a library class with no_of_books and books as two instance 
#variables.write a program to create a library from this library class
# and show how you can print all books,add a book and get no of books using 
# different methods 

# class library:
#     no_of_books = 0
#     def __init__(self,book_name):
#         self.book_name = book_name
#         library.no_of_books+=1
#     def add_books(self):
#         print(f"the added book is{self.book_name}")
#     def print_all_books(self):
#         print(f"the added books are {self.book_name} and the total no of books are {self.no_of_books} ")

        
# obj1 = library("coding")
# obj2 = library("python")
# obj1.add_books()
# obj1.print_all_books()
# obj2.add_books()
# obj2.print_all_books()

class library:
    def __init__(self):
        self.nobooks = 0
        self.books = []
    def addbook(self,book):
        self.books.append(book)
        self.nobooks = len(self.books)
    def showinfo(self):
        print(f"the library has {self.nobooks} books. the books are ")
        for book in self.books:
            print(book)
l1 = library()
l1.addbook("coding")
l1.addbook("python")
l1.showinfo()

