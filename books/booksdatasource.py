#!/usr/bin/env python3
'''
    booksdatasource.py
    Chloe Morscheck and Xinyan Xiang, 11 Oct 2021
'''

import csv

class Author:
    def __init__(self, surname="", given_name="", birth_year=None, death_year=None):
        self.surname = surname
        self.given_name = given_name
        self.birth_year = birth_year
        self.death_year = death_year

    def __eq__(self, other):
        ''' For simplicity, we're going to assume that no two authors have the same name. '''
        return self.surname == other.surname and self.given_name == other.given_name
    
    # Credits to Simon and Anders for the __str__ and __repr__ ideas
    
    def __str__(self):
        return self.given_name + " " + self.surname
    
    def __repr__(self):
        return self.__str__() 

    def get_fullname(self):
        return self.given_name + " " + self.surname

    def get_name(self):
        return self.surname + ", " + self.given_name

class Book:
    def __init__(self, title="", publication_year=None, authors=[]):
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
    
    def __str__(self):
        return self.title + " by " + str(self.authors) + ", published in " + str(self.publication_year)
    
    def __repr__(self):
        return self.__str__()

    def get_title(self):
        return self.title
    
    def get_pub_year(self):
        return int(self.publication_year)

class BooksDataSource:
    def __init__(self, books_csv_file_name):
        self.books_list = []
        self.authors_list = []
        filename = books_csv_file_name
        with open(filename, "r") as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                # Check for author
                # Do the book checker
                book_new = Book(row[0],int(row[1]),[])
                author_string_list = row[2].split(" and ")
                for author_string in author_string_list:
                    author_vars = author_string.split(" ")
                    author_surname = author_vars[-2]
                    if (len(author_vars) == 4):
                        author_firstname = author_vars[0] + " " + author_vars[1]
                    else:
                        author_firstname = author_vars[0]
                    added = False
                    for author in self.authors_list:
                        if (author == Author(author_surname, author_firstname)):
                            book_new.authors.append(author)
                            added = True
                        
                    # if author is not yet created, create and add to list
                    # NOTE birth and death yesars currently not recorded
                    if added == False:
                        author_new = Author(author_surname, author_firstname)
                        self.authors_list.append(author_new)
                        book_new.authors.append(author_new)
                self.books_list.append(book_new)

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
        search_list = []
        if search_text == None:
            return self.author_sort(self.authors_list)
        else:
            search_text = search_text.lower()
            for author in self.authors_list:
                if search_text in author.get_fullname().lower():
                    search_list.append(author)
        return self.author_sort(search_list)

    def books(self, search_text=None, sort_by="title"):
        ''' Returns a list of all the Book objects in this data source whose
            titles contain (case-insensitively) search_text. If search_text is None,
            then this method returns all of the books objects.

            The list of books is sorted in an order depending on the sort_by parameter:

                "year" -- sorts by publication_year, breaking ties with (case-insenstive) title
                "title" -- sorts by (case-insensitive) title, breaking ties with publication_year
                default -- same as "title" (that is, if sort_by is anything other than "year"
                            or "title", just do the same thing you would do for "title")
        '''
        search_list = []
        if search_text == None:
            search_list = self.books_list
        else:
            search_text = search_text.lower()
            for book in self.books_list:
                if search_text in book.get_title().lower():
                    search_list.append(book)

        if sort_by == "title":
            search_list = self.book_sort(search_list)
        elif sort_by == "year":
            search_list = self.year_sort(search_list)
        return search_list


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
        
        search_list = []
        if start_year == None and end_year == None:
            return self.year_sort(self.books_list)
        
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

        for book in self.books_list:
            if book.get_pub_year() <= end_year and book.get_pub_year() >= start_year:
                search_list.append(book)

        return self.year_sort(search_list)

    def display_books(self, books):
        for book in books:
            author_string = book.authors[0].get_fullname()
            if len(book.authors) == 2:
                author_string = author_string + " and " + book.authors[1].get_fullname()
            print(book.title + " by " + author_string + ", published in " + str(book.get_pub_year()))
        pass


    def display_authors(self, authors):
        for author in authors:
            print(author.get_fullname())
            for book in self.books_list:
                for author_of_book in book.authors:
                    if author == author_of_book:
                        print("  -  " + book.get_title() + " published in " + str(book.get_pub_year()))
        pass

    def author_sort(self, authors):
        authors = sorted(authors, key=Author.get_name)
        return authors

    def book_sort(self, books):
        books = sorted(books, key=Book.get_title)
        return books

    def year_sort(self, books):
        books = sorted(books, key=Book.get_pub_year)
        return books


