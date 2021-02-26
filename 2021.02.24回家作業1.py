# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


number = int(input("請輸入次數:"))
for i in range(1,number+1):
    if i % 2 == 0:
        print(i)
print("偶數")
for i in range (1,number+1):
    if i % 2 == 1:
        print(i)
print("奇數")