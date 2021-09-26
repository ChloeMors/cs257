'''
   booksdatasourcetest.py
   Jeff O, 24 September 2021
'''

import booksdatasource
import unittest

class BooksDataSourceTester(unittest.TestCase):
    def setUp(self):
        self.data_source = booksdatasource.BooksDataSource('books1.csv')

    def tearDown(self):
        pass

    def test_unique_author(self):
        authors = self.data_source.authors('Pratchett')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Pratchett', 'Terry'))
    
    def test_case_test_author_default(self):
        authors = self.data_source.authors()
        self.assertTrue(len(authors) == 22)
        self.assertTrue(authors[0] == Author('Austen','Jane'))

    def test_author_space(self):
        authors = self.data_source.authors('a C')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Christie','Agatha'))

    def test_author_sort(self):
        authors1 = self.data_source.authors('brontë')
        authors2 = self.data_source.authors('OR')
        # self.assertTrue(len(authors) == 1)
        self.assertTrue(authors1[0] == Author('Brontë','Ann'))
        self.assertEqual(authors2[0], Author('Morrison','Toni'))
        
# V.E. schwab check 
    def test_author_special_character(self):
        authors1 = self.data_source.authors('.')
        self.assertTrue(authors1[1] == Author('Schwab','V.E.'))

# default case test 
# "a C" agatha christie
# breaking ties ann bronte before charlotte bronte 
# pratchett and Pratchett equal 
# "OR" should be peggy orenstein, toni morrison, tommy orange
# init assert length is ??
# V.E. schwab check 

# sort by year
# sort by title/default
# default length 41
# case sensitive test
# "the"
# "e, t" assert that the list is length one and that its the correct book
# "84"

# both none
# start none
# end none
# inclusive start check
# inclusive end check
# one year check 1996 - check sort
# wrong order years
# word rather than number error



if __name__ == '__main__':
    unittest.main()
