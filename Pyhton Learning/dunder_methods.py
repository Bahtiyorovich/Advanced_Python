# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 18:21:50 2024

@author: Sherzodbek
"""

class Developer:
    __auth = 0
    def __init__(self, name, trend, exp):
        self.name = name
        self.trend = trend
        self.exp = exp
        Developer.__auth += 1
        
    """obyekt haqidagi tushunarsiz natijani matn ko'rinishida qaytaradi"""
    # def __str__(self):
    #     return f"{self.name}, {self.trend} dasturchisi, {self.exp}-yil tajribaga ega"
    """Tavsiya beriladigan usul __repr__ metodi"""
    def __repr__(self):
        return f"{self.name}, {self.trend} dasturchisi, {self.exp}-yil tajribaga ega"
    
    """__eq__ tenglik metodi"""
    def __eq__(self, x):
        return self.exp == x.exp
    
    """__lt__ kichiklik metodi"""
    def __lt__(self, x):
        return self.exp < x.exp
    
    """__le__ kichik yoki tenglik metodi"""
    def __le__(self, x):
        return self.exp <= x.exp
    
    """__len__ matn uzunligini qaytaradi"""
    def __len__(self):
        return self.name
    
    def get_name(self):
        return self.name
    
    def get_trend(self):
        return self.trend

    def get_exp(self):
        return self.exp
    
    @classmethod
    def get_auth_count(cls):
        return cls.__auth
    
dev1 = Developer("Sherzod", "Python backend", 3)

# print(dev1.get_auth_count())

# print(dev1)


class DevPro:
    """Avtosalon klasi"""
    def __init__(self, name):
        self.name = name
        self.developers = []
        
    def get_dev(self):
        return [dev for dev in self.developers]

    def add_dev(self, *developers):
        for dev in developers:
            if isinstance(dev, Developer):
                self.developers.append(dev)

    def __len__(self):
        return len(self.developers)

    def __getitem__(self, index):
        return self.developers[index]
    
    def __setitem__(self,index, new_dev):
        self.developers[index] = new_dev
    
dev2 = Developer("Ali", "Java", 5)
dev3 = Developer("Jasur", "JavaScript", 4)
dev4 = Developer("Sarvar", "C#", 5)

devPro1 = DevPro("Soft_Skills")

devPro1.add_dev(dev1, dev2, dev3, dev4) 

# print(devPro1.get_dev())
# print(devPro1.__len__())
# print(devPro1.__getitem__(1))
dev5 = Developer("Bek", "Nodejs", 6)
print(devPro1.__setitem__(1,dev5))
print(devPro1.__getitem__(1))

print(devPro1.get_dev())























































































