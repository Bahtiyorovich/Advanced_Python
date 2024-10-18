# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 21:58:20 2024

@author: Sherzodbek
"""

"""variableni json formatiga o'tkazish"""
import json

x = 10
x_json = json.dumps(x)

y = 5.5
y_json = json.dumps(y)

m = True

m_json = json.dumps(m)


sonlar = (11, 15, 17)
sonlay_json = json.dumps(sonlar)


person = {
      "name":"Aliyev Vali",
      "yosh": 28,
      "oila":True,
      "farzandlar": ("Ahmad", "Bonu"),
      "alergiya": None,
      "dorilar":[
           {"nomi":"Analgin", "miqdori":0.5},
           {"nomi":"Panadol", "miqdori":1.2}
       ]
}



person_json = json.dumps(person, indent=4)
print(person_json)





# json.load()
# Bu funksiya JSON fayllarning tarkibini Pythonga yuklab olish uchun ishlatiladi.

# filename = 'bemor.json'
# with open(filename) as f:
#     bemor = json.load(f)
    
# print(type(bemor))
















































