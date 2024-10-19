# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:42:36 2024

@author: Sherzodbek
"""

def wordTitle(arr):
    """ro'yxatdagi har bir elementning birinchi harfini kattada chiqaruvchi funksiya"""
    words = []
    
    for word in arr:
        words.append(word.title())
        
    return words

