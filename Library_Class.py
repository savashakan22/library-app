from datetime import datetime
import pandas as pd
from os.path import isfile
import numpy as np

class Library:
    """Used for adding students to the log and managing their books. 
        Method:     Member.__init__()                                   -> Initializes the library DataFrame
                    Member.addbook(name, lastname, bookno, bookname)    -> Adds book on a student register
                    Member.returnbook(name, lastname, bookno, bookname) -> Changes the book to Return = 1 on the given register
                    Member.showbooks(name, lastname)                    -> Shows the books on the register with the "Return = 0"
                    """
    
    def __init__(self, file_name):
        self.library_log = pd.DataFrame(columns= ['Date', 'Hour', 'Name', 'Lastname', 'Booknumber', 'Bookname', 'Return'])
        self.file_name = file_name

        if isfile(self.file_name):
            self.library_log = pd.read_csv(self.file_name)

        else:
            self.library_log.to_csv(self.file_name, index = False)

        
        
    def add_book(self, name, lastname, bookno, bookname):
        """Adds book to the register's name, also adds the date and the hour"""
        
        library_append = pd.DataFrame({
                                    'Date':             [str(datetime.now().strftime('%d-%m-%Y'))],
                                    'Hour':             [str(datetime.now().strftime('%H:%M:%S'))],
                                    'Name':             [name],
                                    'Lastname':         [lastname],
                                    'Booknumber':       [bookno],
                                    'Bookname':         [bookname],
                                    'Return':           [0]})
        self.library_log = pd.concat([self.library_log, library_append])


    def show_book(self, name, lastname):
        """Returns the students books as a dataframe"""
        
        #Matching the name and the lastname and getting the boolean pandas array
        name_matching = np.logical_and(self.library_log["Name"] == name, self.library_log['Lastname'] == lastname)
        name_matching = np.logical_and(name_matching, self.library_log['Return'] == 0)

        member_books = self.library_log.loc[name_matching, ['Date', 'Hour', 'Booknumber', 'Bookname']]
        
        return member_books if not member_books.empty else "No books found for the student"


    def return_book(self, name, lastname, bookno):
        """Used for returning a student's unreturned book"""

        #Serially matching the bookno, name, lastname and return = 0
        book_matching = np.logical_and(self.library_log['Booknumber'] == bookno , self.library_log['Return'] == 0)
        name_matching = np.logical_and(self.library_log['Lastname'] == lastname, self.library_log['Name'] == name)
        full_match = np.logical_and(book_matching, name_matching)
        
        self.library_log.loc[full_match, 'Return'] = 1        
        
