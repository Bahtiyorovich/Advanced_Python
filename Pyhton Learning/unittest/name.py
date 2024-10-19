# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 20:13:47 2024

@author: Sherzodbek
"""

def get_full_name(ism, familya, otasi = ''):
    if otasi:
       return f"{ism} {otasi} {familya}".title()
    else:
       return f"{ism} {familya}".title()