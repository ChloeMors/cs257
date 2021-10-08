'''
    booksdatasource.py
    Chloe Morscheck and Xinyan Xiang, 11 Oct 2021
'''
'''
Comments from people:
range of 0-2021 for default years - is this okay?
more comments to explain what is going on 
revise args 
year string stuff
books init and magic numbers - look at andersshenholm
search in getName and get fullname for author search

revise main
revise and use __str__ and __repr__ functions
hardcoded filename
list1 in main - Xinyan
string formatting  - Xinyan
dont use "none" as default  - Xinyan
redo usage
display functions: I wrote a display authors 2 - we might want to rethink where these functions go
 - should they be functions in the author class?

done:
snake case - chloe
double quotes - chloe
probably can delete lines 65-68 in booksdatasource
added str and repr functinos but Im not sure theyre right, and I didnt use them anywhere
'''
from booksdatasource import Author, Book, BooksDataSource

import argparse

# some colors we need for our outputs
class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[31m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

def get_parsed_arguments():
    parser = argparse.ArgumentParser(add_help=False, description="Search and sort books and authors.")
    parser.add_argument("-t", "--title", const = "None", nargs="?") 
    parser.add_argument("-a", "--author", nargs="?", const="None") 
    parser.add_argument("-y", "--year", nargs="?", const="None") 
    parser.add_argument("-s", nargs=1, default="title", choices=["year", "title"])
    parser.add_argument("-h", "--help", action = "store_true", dest="hi")
    parser.add_argument("-v", "--version", action="version", version = "%(prog)s 1.0, Chloe Morscheck and Xinyan Xiang, CS 257, Oct 2, 2021")
    parsed_arguments = parser.parse_args()
    return parsed_arguments



def main():
    arguments = get_parsed_arguments()
    if arguments.hi:
        f = open("usage.txt", "r")
        file_contents = f.read()
        print(file_contents)
        f.close
    books_data_source = BooksDataSource("books1.csv")  
    list1 = []

    if arguments.title:
        if arguments.title == "None":
            print(bcolors.WARNING + "Note: Since you did not specify any strings for books, here are all books in this database." + bcolors.ENDC)
            list1 = books_data_source.books(sort_by=arguments.s[0])
            books_data_source.display_books(list1)
        else:
            list1 = books_data_source.books(search_text=arguments.title, sort_by=arguments.s[0])
            books_data_source.display_books(list1)
    if arguments.author:
        if arguments.author == "None":
            print(bcolors.WARNING + "Note: Since you did not specify any strings for authors , here are all authors in this database." + bcolors.ENDC)
            list1 = books_data_source.authors()
            books_data_source.display_authors(list1)
        else: 
            list1 = books_data_source.authors(search_text=arguments.author)
            books_data_source.display_authors(list1)
    if arguments.year:
        if arguments.year == "None":
            print(bcolors.WARNING + "Note: Since you did not specify any years for authors , here are all authors in this database." +  bcolors.ENDC)
            list1 = books_data_source.books_between_years()
        elif "-" in arguments.year:
            year_list = arguments.year.split(" ")
            if len(year_list) == 3:             
                list1 = books_data_source.books_between_years(start_year = year_list[0], end_year = year_list[2])
            else:
                if year_list[0].isdigit(): 
                    list1 = books_data_source.books_between_years(start_year = year_list[0])
                else:
                    list1 = books_data_source.books_between_years(end_year = year_list[1])
        else: 
            list1 = books_data_source.books_between_years(start_year = arguments.year, end_year = arguments.year)        
        books_data_source.display_books(list1)




if __name__ == "__main__":
    main()