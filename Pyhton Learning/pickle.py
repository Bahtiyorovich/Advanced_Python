# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 21:26:08 2024

@author: Sherzodbek
"""
"""pickle faylga yaratish"""
import pickle

# jiyan1 = {'ism':'Hayotbek', 'familya':'Baxtiyorjonov', 'yosh':3}
# jiyan2 = {'ism':'Omadbek', 'familya':'Baxtiyorjonov', 'yosh':1.5}

# with open('info.pkl', 'wb') as file:
#     pickle.dump(jiyan1, file)
#     pickle.dump(jiyan2, file)
    
"""pickle faylni o'qish"""

with open('info.pkl', 'rb') as file:
    jiyan1 = pickle.load(file)
    jiyan2 = pickle.load(file)
    
print(jiyan1)
print(jiyan2)