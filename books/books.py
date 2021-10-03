'''
    booksdatasource.py
    Chloe Morscheck and Xinyan Xiang, 2 Oct 2021
'''

from booksdatasource import Author, Book, BooksDataSource

import argparse

# some colors we need for our outputs
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[31m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_parsed_arguments():
    parser = argparse.ArgumentParser(add_help=False, description='Search and sort books and authors.')
    parser.add_argument('-t', '--title', const = "None", nargs='?') 
    parser.add_argument('-a', '--author', nargs='?', const="None") 
    parser.add_argument('-y', '--year', nargs='?', const="None") 
    parser.add_argument('-s', nargs=1, default='title', choices=['year', 'title'])
    parser.add_argument('-h', "--help", action = "store_true", dest="hi")
    parser.add_argument('-v', '--version', action='version', version = '%(prog)s 1.0, Chloe Morscheck and Xinyan Xiang, CS 257, Oct 2, 2021')
    parsed_arguments = parser.parse_args()
    return parsed_arguments



def main():
    arguments = get_parsed_arguments()
    if arguments.hi:
        f = open("usage.txt", "r")
        file_contents = f.read()
        print(file_contents)
        f.close
    BooksDataSourceObject = BooksDataSource("books1.csv")  
    list1 = []

    if arguments.title:
        if arguments.title == "None":
            print(bcolors.WARNING + "Note: Since you did not specify any strings for books, here are all books in this database." + bcolors.ENDC)
            list1 = BooksDataSourceObject.books(sort_by=arguments.s[0])
            BooksDataSourceObject.display_books(list1)
        else:
            list1 = BooksDataSourceObject.books(search_text=arguments.title, sort_by=arguments.s[0])
            BooksDataSourceObject.display_books(list1)
    if arguments.author:
        if arguments.author == "None":
            print(bcolors.WARNING + "Note: Since you did not specify any strings for authors , here are all authors in this database." + bcolors.ENDC)
            list1 = BooksDataSourceObject.authors()
            BooksDataSourceObject.display_authors(list1)
        else: 
            list1 = BooksDataSourceObject.authors(search_text=arguments.author)
            BooksDataSourceObject.display_authors(list1)
    if arguments.year:
        if arguments.year == "None":
            print(bcolors.WARNING + "Note: Since you did not specify any years for authors , here are all authors in this database." +  bcolors.ENDC)
            list1 = BooksDataSourceObject.books_between_years()
        elif "-" in arguments.year:
            yearList = arguments.year.split(" ")
            if len(yearList) == 3:             
                list1 = BooksDataSourceObject.books_between_years(start_year = yearList[0], end_year = yearList[2])
            else:
                if yearList[0].isdigit(): 
                    list1 = BooksDataSourceObject.books_between_years(start_year = yearList[0])
                else:
                    list1 = BooksDataSourceObject.books_between_years(end_year = yearList[1])
        else: 
            list1 = BooksDataSourceObject.books_between_years(start_year = arguments.year, end_year = arguments.year)        
        BooksDataSourceObject.display_books(list1)




if __name__ == '__main__':
    main()