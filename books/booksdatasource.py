#!/usr/bin/env python3
'''
    booksdatasource.py
    Chloe Morscheck and Xinyan Xiang, 2 September 2021
'''

import csv

class Author:
    def __init__(self, surname='', given_name='', birth_year=None, death_year=None):
        self.surname = surname
        self.given_name = given_name
        self.birth_year = birth_year
        self.death_year = death_year

    def __eq__(self, other):
        ''' For simplicity, we're going to assume that no two authors have the same name. '''
        return self.surname == other.surname and self.given_name == other.given_name

    def getFullname(self):
        return self.given_name + " " + self.surname

    def getName(self):
        return self.surname + ", " + self.given_name

class Book:
    def __init__(self, title='', publication_year=None, authors=[]):
        ''' Note that the self.authors instance variable is a list of
            references to Author objects. '''
        self.title = title
        self.publication_year = publication_year
        self.authors = authors

    def __eq__(self, other):
        ''' We're going to make the excessively simplifying assumption that
            no two books have the same title, so "same title" is the same
            thing as "same book". '''
        return self.title == other.title
    
    def getTitle(self):
        return self.title
    
    def getPubYear(self):
        return int(self.publication_year)

class BooksDataSource:
    def __init__(self, books_csv_file_name):
        self.booksList = []
        self.authorsList = []
        filename = "books1.csv"
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                # Check for author
                # Do the book checker
                bookObj = Book(row[0],int(row[1]),[])
                authorStringList = row[2].split(" and ")
                for authorString in authorStringList:
                    authorVars = authorString.split(" ")
                    authorSurname = authorVars[-2]
                    if (len(authorVars) == 4):
                        authorFirstname = authorVars[0] + authorVars[1]
                    else:
                        authorFirstname = authorVars[0]
                    if len(self.authorsList) == 0:
                        newAuthor = Author(authorSurname, authorFirstname)
                        self.authorsList.append(newAuthor)
                        bookObj.authors.append(newAuthor)
                    added = False
                    for authorsObj in self.authorsList:
                        if (authorsObj == Author(authorSurname, authorFirstname)):
                            bookObj.authors.append(authorsObj)
                            added = True
                        
                    # if author is not yet created, create and add to list
                    # NOTE birth and death yesars currently not recorded
                    if added == False:
                        newAuthor = Author(authorSurname, authorFirstname)
                        self.authorsList.append(newAuthor)
                        bookObj.authors.append(newAuthor)
                self.booksList.append(bookObj)

        ''' The books CSV file format looks like this:

                title,publication_year,author_description

            For example:

                All Clear,2010,Connie Willis (1945-)
                "Right Ho, Jeeves",1934,Pelham Grenville Wodehouse (1881-1975)

            This __init__ method parses the specified CSV file and creates
            suitable instance variables for the BooksDataSource object containing
            a collection of Author objects and a collection of Book objects.
        '''
        pass

    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Brontë comes before Charlotte Brontë).
        '''
        searchList = []
        if search_text == None:
            return self.author_sort(self.authorsList)
        else:
            search_text = search_text.lower()
            for author in self.authorsList:
                if search_text in author.getFullname().lower():
                    searchList.append(author)
        return self.author_sort(searchList)

    def books(self, search_text=None, sort_by='title'):
        ''' Returns a list of all the Book objects in this data source whose
            titles contain (case-insensitively) search_text. If search_text is None,
            then this method returns all of the books objects.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                'title' -- sorts by (case-insensitive) title, breaking ties with publication_year
                default -- same as 'title' (that is, if sort_by is anything other than 'year'
                            or 'title', just do the same thing you would do for 'title')
        '''
        searchList = []
        if search_text == None:
            searchList = self.booksList
        else:
            search_text = search_text.lower()
            for book in self.booksList:
                if search_text in book.getTitle().lower():
                    searchList.append(book)

        if sort_by == 'title':
            searchList = self.book_sort(searchList)
        elif sort_by == 'year':
            searchList = self.year_sort(searchList)
        return searchList


        # make new empty list
        # put books with search text in list
        # if sorting is specified - sort

    def books_between_years(self, start_year=None, end_year=None):
        ''' Returns a list of all the Book objects in this data source whose publication
            years are between start_year and end_year, inclusive. The list is sorted
            by publication year, breaking ties by title (e.g. Neverwhere 1996 should
            come before Thief of Time 1996).

            If start_year is None, then any book published before or during end_year
            should be included. If end_year is None, then any book published after or
            during start_year should be included. If both are None, then all books
            should be included.
        '''
        # define a range, error check
        # make new empty list
        # books with valid publication date in range get added to list
        # sort by year
        
        searchList = []
        if start_year == None and end_year == None:
            return self.year_sort(self.booksList)
        
        if start_year == None:
            start_year = 0
        elif start_year.isdigit() == False:
            raise TypeError("Year input is not a number")
        else:
            start_year = int(start_year)
        if end_year == None:
            end_year = 2021
        elif end_year.isdigit() == False:
            raise TypeError("Year input is not a number")
        else:
            end_year = int(end_year)
        
        if start_year > end_year:
            raise ValueError("Wrong order of year")



        for book in self.booksList:
            if book.getPubYear() <= end_year and book.getPubYear() >= start_year:
                searchList.append(book)

        return self.year_sort(searchList)

    def display_books(self, books):
        for book in books:
            print(book.title + " " + str(book.publication_year))
        pass

    def display_authors(self, authors):
        for author in authors:
            print(author.getFullname())
        pass

    def author_sort(self, authors):
        authors = sorted(authors, key=Author.getName)
        return authors

    def book_sort(self, books):
        books = sorted(books, key=Book.getTitle)
        return books

    def year_sort(self, books):
        books = sorted(books, key=Book.getPubYear)
        return books


def main():
    BooksDataSourceObject = BooksDataSource("books1.csv")
    BooksDataSourceObject.display_books(BooksDataSourceObject.books("e, t"))
    #BooksDataSourceObject.display_books(BooksDataSourceObject.books_between_years())

main()