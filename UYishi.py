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
        if parts[-2].endswith('a') or parts[-2].endswith('ha'):
            jinsi = "erkak"
        else:
            jinsi = "erkak"
    else:
        jinsi = "erkak"

    # Jinsini 
    result.append(jinsi)

    
    if len(parts) >= 1:
        result.append(parts[0])
    if len(parts) >= 2:
        result.append(parts[-1])

    
    return result


s = "Shukrullo Turgunov"
print(aniqlagich(s))  # ["erkak", "Shukrullo", "Turgunov"]

s = "Valixon Muxtorov"
print(aniqlagich(s))  # ["erkak", "Valixon", "Muxtorov"]

s = "Xamidov Behruzbek"
print(aniqlagich(s))  # ["erkak", "Behruzbek", "Xamidov"]