'''
    booksdatasource.py
    Chloe Morscheck and Xinyan Xiang, 11 Oct 2021
'''

from booksdatasource import Author, Book, BooksDataSource

import argparse

# some colors we need for our outputs
class bcolors:
    OKGREEN = "\033[0;32m"
    WARNING = "\033[31m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

def get_parsed_arguments():
    ''' Create an ArgumentParser object and fill it with information about command lines 
        utilized by this program arguments.
    '''
    parser = argparse.ArgumentParser(add_help=False, description="Search and sort books and authors.")
    parser.add_argument("-t", "--title", const = "empty", nargs="?") 
    parser.add_argument("-a", "--author", nargs="?", const="empty") 
    parser.add_argument("-y", "--year", nargs="?", const="empty") 
    parser.add_argument("-s", "--startyear", nargs=1, default="empty")
    parser.add_argument("-e", "--endyear", nargs=1, default="empty")
    parser.add_argument("-bs", "--booksort", nargs=1, default="title", choices=["year", "title"])
    parser.add_argument("-h", "--help", action = "store_true", dest="help_me")
    parser.add_argument("-v", "--version", action="version", version = "%(prog)s 2.0, Chloe Morscheck and Xinyan Xiang, CS 257, Oct 2, 2021")
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def main():
    arguments = get_parsed_arguments()
    filename = "books1.csv"
    books_data_source = BooksDataSource(filename)  
    books_list = []

    # When the user types the help flag (-h): print the command-line documentation 
    if arguments.help_me:
        f = open("usage.txt", "r")
        file_contents = f.read()
        print(file_contents)
        f.close

    # When the user types the title flag (-t) and / or the book sorting flag (-bs)
    if arguments.title:
        if arguments.title == "empty":
            print(f"{bcolors.WARNING}Note: Since you did not specify any strings for books, here are all books in this database. {bcolors.ENDC}")
            search_text=None
        else:
            search_text = arguments.title
        books_list = books_data_source.books(search_text=search_text, sort_by=arguments.booksort[0])
        books_data_source.display_books(books_list)

    # When the user types the author flag (-a)
    if arguments.author:
        if arguments.author == "empty":
            print(f"{bcolors.WARNING}Note: Since you did not specify any strings for authors, here are all authors in this database. {bcolors.ENDC}")
            search_text=None
        else: 
            search_text=arguments.author
        books_list = books_data_source.authors(search_text=search_text)
        books_data_source.display_authors(books_list)

    # When the user types the year flag (-y) and / or the date flags (-s and and -e )
    if arguments.year:
        if arguments.startyear == "empty":
            startyear = None
        else:
            startyear = arguments.startyear[0]
        if arguments.endyear =="empty":
            endyear = None
        else:
            endyear = arguments.endyear[0]   
        if startyear == None and endyear == None:
            print(f"{bcolors.WARNING}Note: Since you did not specify any strings for years, here are all books in this database. {bcolors.ENDC}")
            
        books_list = books_data_source.books_between_years(startyear, endyear)       
        books_data_source.display_books(books_list)


if __name__ == "__main__":
    main()