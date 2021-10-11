'''
   booksdatasourcetest.py
   Chloe Morscheck Xinyan Xiang, 27 September 2021
'''

from booksdatasource import Author, Book, BooksDataSource
import unittest

class BooksDataSourceTester(unittest.TestCase):
    def setUp(self):
        self.data_source = BooksDataSource("books1.csv")

    def tearDown(self):
        pass


## tests for author function

## tests that a unique search returns proper author
    def test_unique_author(self):
        authors = self.data_source.authors("Pratchett")
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author("Pratchett", "Terry"))
    
## tests that default search returns full list in proper order
    def test_case_test_author_default(self):
        authors = self.data_source.authors()
        self.assertTrue(len(authors) == 22)
        self.assertTrue(authors[0] == Author("Austen","Jane"))

## tests that search string with a space character functions properly
    def test_author_space(self):
        authors = self.data_source.authors("a C")
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author("Christie","Agatha"))

## tests that both surname and first name sorting works,
## as well as tests case-insensitivity
    def test_author_sort(self):
        authorsBronte = self.data_source.authors("brontë")
        authorsOr = self.data_source.authors("OR")
        self.assertTrue(authorsBronte[0] == Author("Brontë","Ann"))
        self.assertEqual(authorsOr[0], Author("Morrison","Toni"))
        
# tests for special character
    def test_author_special_character(self):
        authors = self.data_source.authors(".")
        self.assertTrue(authors[0] == Author("Schwab","V.E."))

## tests for books function

## tests that default search returns full list, properly sorted
    def test_books_sort_default(self):
        books = self.data_source.books()
        self.assertTrue(books[0] == Book("1Q84"))
        self.assertTrue(len(books) == 41)
        self.assertTrue(books[40] == Book("Wuthering Heights"))

## tests that sorting by year works
    def test_books_sort_year(self):
        books = self.data_source.books(sort_by="year")
        self.assertTrue(books[0] == Book("The Life and Opinions of Tristram Shandy, Gentleman"))
        self.assertTrue(books[1] == Book("Pride and Prejudice"))
        self.assertTrue(books[2] == Book("Sense and Sensibility"))
        # We are doing multiple things in one test - is there a way
        # to show in the error statement which part errored?

## tests case sensitivity
    def test_books_case(self):
        books = self.data_source.books("beLOVEd")
        self.assertTrue(books[0] == Book("Beloved"))

## tests search string both within words and surrounded by spaces
    def test_books_the(self):
        books = self.data_source.books("the")
        self.assertTrue(len(books) == 13)   

## tests search string with space
    def test_books_space(self):
        books = self.data_source.books("e, t")
        self.assertTrue(books[0] == Book("Fine, Thanks"))

## tests search string with number
    def test_books_number(self):
        books = self.data_source.books("84")
        self.assertTrue(books[0] == Book("1Q84"))
        self.assertTrue(len(books) == 1) 

## tests for books between years function

## tests that default with both years=None behaves properly
    def test_years_both_none(self):
        books = self.data_source.books_between_years()
        self.assertTrue(len(books) == 41) 
        self.assertTrue(books[0] == Book("The Life and Opinions of Tristram Shandy, Gentleman"))
        self.assertTrue(books[1] == Book("Pride and Prejudice"))
        self.assertTrue(books[2] == Book("Sense and Sensibility"))

## tests that start=None behaves properly
    def test_years_start_none(self):
        books = self.data_source.books_between_years(end_year="1759")
        self.assertTrue(len(books) == 1) 
        self.assertTrue(books[0] == Book("The Life and Opinions of Tristram Shandy, Gentleman"))     

## tests that end=None behaves properly
    def test_years_end_none(self):
        books = self.data_source.books_between_years(start_year="2020")
        self.assertTrue(len(books) == 2) 
        self.assertTrue(books[0] == Book("Boys and Sex")) 

## tests that the case when start year and end year are equal
    def test_years_equal(self):
        books = self.data_source.books_between_years(start_year="2020", end_year="2020")
        self.assertTrue(len(books) == 2) 
        self.assertTrue(books[0] == Book("Boys and Sex")) 

## test the case when the order of input years is wrong
    def test_years_wrong_order(self):
        with self.assertRaises(ValueError):
            self.data_source.books_between_years(start_year="2020", end_year="1759")

## test the case when the input year does not correct format   
    def test_years_wrong_input(self):
        with self.assertRaises(TypeError):
            self.data_source.books_between_years(start_year="abc")




if __name__ == "__main__":
    unittest.main()
