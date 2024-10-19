# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:01:22 2024

@author: Sherzodbek
"""

import unittest
from juft_son import juft_son

class JuftSonTest(unittest.TestCase):
    def test_juft_son(self):
        self.assertEqual(juft_son([1,7,8, 0, 5.5]), [8, 0])
        
unittest.main()