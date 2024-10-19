# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:42:39 2024

@author: Sherzodbek
"""

import unittest
from word_list import wordTitle

class WordTitleTest(unittest.TestCase):
    def test_word_title(self):
        self.assertEqual(wordTitle(['ali', 'vali']), ['Ali', 'Vali'])
        
        
unittest.main()
        
        
        
        
        
    