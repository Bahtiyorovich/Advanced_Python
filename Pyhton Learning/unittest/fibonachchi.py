# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:13:49 2024

@author: Sherzodbek
"""

import math

def is_fibonacci_number(n):
    # To'liq kvadratni aniqlash uchun yordamchi funksiya
    def is_perfect_square(x):
        s = int(math.sqrt(x))
        return s * s == x

    # 5*n^2 + 4 yoki 5*n^2 - 4 to'liq kvadratmi, tekshiramiz
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)
