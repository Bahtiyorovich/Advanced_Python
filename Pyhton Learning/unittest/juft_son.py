# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:00:49 2024

@author: Sherzodbek
"""

def juft_son(arr):
    """berilgan sonlar ro'yxatidan juft sonlarni ajratib oluvchi funksiya"""
    
    juft = []
    
    for son in arr:
        if son % 2 == 0:
            juft.append(son)
        elif type(son) is float:
            continue
        else:
            "ro'yxatda juft sonlar mavjud emas"
        
    return juft
