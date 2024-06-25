# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 13:13:20 2024

@author: HP
"""
# 1-m
def aniqlagich(s):
    # Bo'sh ro'yxat 
    result = []

    # ism va familiyani 
    parts = s.split()

    # Jinsi
    if len(parts) >= 3:
        if parts[-3].endswith('a') or parts[-3].endswith('va'):
            jinsi = "ayol"
        else:
            jinsi = "erkak"
    else:
        jinsi = "erkak"

    # Jinsini 
    result.append(jinsi)

    
    if len(parts) >= 1:
        result.append(parts[0])
    if len(parts) >= 2:
        result.append(parts[-3])
    if len(parts) >= 3:
        result.append(parts[-2])
    if len(parts) >= 4:
        result.append(parts[-1])
    
    return result


s = "Diyora Axmedova Najmiddin qizi"
print(aniqlagich(s))  # ["ayol", "Diyora", "Axmedova"]

s = "Valixon Muxtorov Xamidjon og'li"
print(aniqlagich(s))  # ["erkak", "Valixon", "Muxtorov"]

s = "Xamidov Behruzbek Valixon og'li"
print(aniqlagich(s))  # ["erkak", "Behruzbek", "Xamidov"]