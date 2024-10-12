# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 20:27:37 2024

@author: Sherzodbek
"""

"""fayllar bilan ishlash, faylni ochish ichini o'qish"""

with open('files_txt/salom.txt') as file:
    word = file.read()
    
# print(word)

# print(word.upper())



filename = 'files_txt/talabalar.txt'
with open(filename) as file:
    talabalar = file.readlines()

# print(talabalar)

talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)


"""fayl yaratish va ichiga matn yozish"""
faylnomi = 'new_file.txt'
ism = 'Bernard Show'
tyil = 2005

with open(faylnomi, 'w') as file:
    file.write(ism + '\n')
    file.write(str(tyil))

with open(faylnomi, 'a') as file:
    file.write('\n Omadbek Baxtiyorov \n')
    file.write('2023')

with open('new_file.txt') as file:
    text = file.read()
    
print(text)
    









































