# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 13:20:30 2024

@author: HP
"""
#4
qarzdorlar = ['Salim 4500', 'Jalil 2250', 'Sardor 4450', 'Otabek 9760', 'Asilbek 3150']
katta_qarzdorlar = []

for qarzdor in qarzdorlar:
    ism, qarz = qarzdor.split()
    qarz = int(qarz)
    if qarz >= 2500:
        katta_qarzdorlar.append(qarzdor)

print(katta_qarzdorlar)
