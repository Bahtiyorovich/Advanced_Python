# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 20:18:31 2024

@author: Sherzodbek
"""

import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_full_name(self):
       name = get_full_name("Sherzod", "Yoqubov", "Baxtiyorovich")
       self.assertEqual(name, "Sherzod Baxtiyorovich Yoqubov")
       
    def test_name(self):
        name = get_full_name("Sherzod", "Yoqubov")
        self.assertEqual(name, "Sherzod Yoqubov")
        
        
unittest.main()  
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       