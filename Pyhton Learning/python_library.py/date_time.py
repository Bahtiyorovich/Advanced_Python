# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 07:12:54 2024

@author: Sherzodbek
"""

import datetime as dt

# datetime
now = dt.datetime.now()
# print(now)
# print(now.hour)
# print(now.minute)
# print(now.seconds)
# print(now.date())
# print(now.time())
# today = dt.date.today()
# print(today)


create_time = dt.time(7, 29, 50)
# print(create_time)


# aksiyaga qancha vaqt qoldi

now_date = dt.date.today()
ramazon = dt.date(2025, 2, 17)

time = ramazon - now_date

print(f"Aksiya tugashiga {time.days} kun qoldi")




























