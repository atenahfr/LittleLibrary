'''
This program is meant to manage a library system that helps all the users 
to first of all add books to this library if they wish to donate.
Then it should have the ability to display all the books that exists in this library for the users to know their options. 
Users also should be able to find their desired book by its title. 
And at last, people can both check in and check out books.
It may seem like a simple program to code but for a book lover and someone who wishes to 
work in a library one day, it's like getting one step closer to the dream
'''

#adding books to this library 
def add_book(library, book):
#library= it's the list representing the library (list)
#book= it's the title of the book that will be added (string)
    library.append(book)

def existing_books(library):
#library here displays all the existing books (list)
#At this point the enumerate function can be used to iterate through the sequence of the library
#and keep track of the index of each element
        if not library:
            print("The library is still empty.")
        else:
            print("Here is the list of the books in this library: ")
            for index, book in enumerate(library, start=1):
                print(f"{index}. {book}")
#moving on to the searching feature, so that the user can find their desired book by either it's title
def search_book(library, title):
#library: it's the list representing the library.
#title: to search for the book title or author) 
#Returns: a list of matching books.
    matches = []
    for book in library:
        if title.lower() in book.lower():
            matches.append(book)
    return matches
# in order for people to be able to to use this program to check out a book: 
def check_out(library, entitle):
#library: the list representing the library.
#entitle: the book to be checked out. (string)
    if entitle in library:
        library.remove(entitle)
        print(f"Book '{entitle}' is checked out successfully. Thank you!")
    else:
        print(f"Book '{entitle}' is not available in the library at the moment. Please come back later.")
#To check in a book:
def check_in(library, entitle):
#library: The list representing the library.
#entitle: The title of the book to be checked in.
    library.append(entitle)
    print(f"Book '{entitle}' checked in successfully. Appreciated!")

def main():
    # Initializing an empty library
    library = []

    # Adding books to the library
    add_book(library, "Crime and punishment")
    add_book(library, "The catcher in the rye")
    add_book(library, "Flowers for Algernon")
    add_book(library, "The song of Achilles")
    add_book(library, "The book thief")
    add_book(library, "Kafka on the shore")
    add_book(library, "Les Miserables")

      # Asking the user for input
    user_input = input("Enter a book title or author, or specify a book to check in or write 'add' if you want to donate your book: ")

    # Converting user input to lowercase
    user_input_lower = user_input.lower()

    # If user wants to add a book
    if user_input_lower == "add":
        new_book = input("Enter the title of the book you want to add: ")
        add_book(library, new_book)
        print(f"Book '{new_book}' added to the library.")

    # If user specifies a book to check out
    if user_input_lower.startswith("check out "):
        title = user_input[10:]  # Extracting the title from user input
        check_out(library, title)

    # If user specifies a book to check in
    elif user_input_lower.startswith("check in "):
        title = user_input[9:]  # Extracting the title from user input
        check_in(library, title)

    # Otherwise, searching for a specific book or author
    else:
        search_results = search_book(library, user_input_lower)
        if search_results:
            print("The book is available in the library.")
            check_option = input("Do you want to check out this book? (yes/no): ")
            if check_option.lower() == "yes":
               check_out(library, search_results[0])  # Assuming the first search result is the desired book
        else:
            print("The book is not available in the library.")
            existing_books(library)

if __name__ == "__main__":
    main()

#This progrm as much as our knowledge in programin with python allows, illustrated a simple library system
#in which users are able to add books, see available books, search for a book, check out, and check in a book.
#The program includes functions, loops, if statements, and string comparisons.
#The comments are added throughout the code to better explaine the program's functionality.
