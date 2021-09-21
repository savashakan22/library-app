# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 19:01:02 2019

@author: turkf
"""

from datetime import datetime
import pandas as pd
from os.path import isfile
import numpy as np

kitapliklog = pd.DataFrame({
        'Date':             [],
        'Hour':             [],
        'Name':             [],
        'Lastname':         [],
        'Booknumber':       [],
        'Bookname':         [],
        'Teslim':           []
                                })

if isfile('Kutuphane.csv'):
    kitapliklog = pd.read_csv('Kutuphane.csv')

else:
    kitapliklog.to_csv('Kutuphane.csv')
    

class Uye:
    """Kutuphane arşivine üye atamayı ve üye işlemlerini yönetir. 
        Komutlar:   Uye.__init__(name, lastname) -> İsmi verilen kayıt adına işlem yapar
                    Uye.kitapal(kitapno, kitapad) -> Öğrenci adına 'Teslim = 0' lı kitap kaydeder
                    Uye.kitapteslim(kitapno, kitapad) -> Öğrencinin adına kayıtlı bir kitabı 'Teslim = 1' yapar.
                    Uye.kitapgoster() -> Öğrenciye kayıtlı Teslim = 0 olan kitapları return()'lar.
                    """
    
    
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        
        
    def kitapal(self, kitapno, kitapad):
        """Öğrencinin adına kitap ekler, aynı zamanda tarih ve saati de kaydeder"""
        
        global kitapliklog
        kitapliklog = kitapliklog.append(pd.DataFrame({
                                    'Date':             [str(datetime.now().strftime('%d-%m-%Y'))],
                                    'Hour':             [str(datetime.now().strftime('%H:%M:%S'))],
                                    'Name':             [self.name],
                                    'Lastname':         [self.lastname],
                                    'Booknumber':       [kitapno],
                                    'Bookname':         [kitapad],
                                    'Teslim':           [0]
                                        }))
        
        kitapliklog.to_csv("Kutuphane.csv")


    def kitapgoster(self):
        """Öğrencinin teslim edilmemiş kitaplarını gösterir"""
        
        isim_es = np.logical_and(kitapliklog["Name"] == self.name, kitapliklog['Lastname'] == self.lastname)

        kg1 = kitapliklog.loc[np.logical_and(isim_es, kitapliklog['Teslim'] == 0), ['Date', 'Hour', 'Booknumber', 'Bookname'] ]
        
        return kg1


    def kitapteslim(self, kitapno, kitapad):
        """Öğrencinin teslim edilmemiş kitaplarını teslim etmesine yarar"""
        
        a = np.logical_and(kitapliklog['Booknumber'] == kitapno, kitapliklog['Bookname'] == kitapad)
        b = np.logical_and(a, kitapliklog['Name'] == self.name)
        c = np.logical_and(b, kitapliklog['Teslim'] == 0)
        d = np.logical_and(c, kitapliklog['Lastname'] == self.lastname)
        
        kitapliklog.loc[c, 'Teslim'] = 1
        
        kitapliklog.to_csv("Kutuphane.csv")
        
