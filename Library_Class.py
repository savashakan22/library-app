# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 19:01:02 2019

@author: turkf
"""

from datetime import datetime
import pandas as pd
from os.path import isfile
import numpy as np

library_log = pd.DataFrame(columns= ['Date', 'Hour', 'Name', 'Lastname', 'Booknumber', 'Bookname', 'Return'])

if isfile('Library_log.csv'):
    library_log = pd.read_csv('Library_log.csv')

else:
    library_log.to_csv('Library_log.csv')
    

class Member:
    """Used for adding students to the log and managing their books. 
        Method:     Member.__init__(name, lastname)     -> Lets you do change on a register with the matching name
                    Member.addbook(bookno, bookname)    -> Adds book on a student register
                    Member.returnbook(bookno, bookname) -> Changes the book to Return = 1 on the given register
                    Member.showbooks()                  -> Shows the books on the register with the "Return = 0"
                    """
    
    
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        
        
    def addbook(self, bookno, bookname):
        """Adds book to the register's name, also adds the date and the hour"""
        
        global library_log
        library_append = pd.DataFrame({
                                    'Date':             [str(datetime.now().strftime('%d-%m-%Y'))],
                                    'Hour':             [str(datetime.now().strftime('%H:%M:%S'))],
                                    'Name':             [self.name],
                                    'Lastname':         [self.lastname],
                                    'Booknumber':       [bookno],
                                    'Bookname':         [bookname],
                                    'Return':           [0]})
        library_log = pd.concat([library_log, library_append])
        library_log.to_csv("Library_log.csv")


    def showbook(self):
        """Returns the students books as a dataframe"""
        
        isim_es = np.logical_and(library_log["Name"] == self.name, library_log['Lastname'] == self.lastname)

        kg1 = library_log.loc[np.logical_and(isim_es, library_log['Return'] == 0), ['Date', 'Hour', 'Booknumber', 'Bookname'] ]
        
        return kg1


    def returnbook(self, bookno):
        """Used for returning a student's unreturned book"""
        
        a = library_log['Booknumber'] == bookno
        b = np.logical_and(a, library_log['Name'] == self.name)
        c = np.logical_and(b, library_log['Return'] == 0)
        d = np.logical_and(c, library_log['Lastname'] == self.lastname)
        
        library_log.loc[c, 'Return'] = 1
        
        library_log.to_csv("Library_log.csv")
        
