# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 20:29:33 2021

@author: USER
"""

import random 
count = 0 
ans = random.randint(1,100)
guess = 0
l = 1
h = 100

while ans != guess:
    print ("請輸入",l,"-",h,"間的整數:",sep="")
    guess = int(input())
    if ans > guess:
        print("請猜大一點")
        l = guess + 1
    if ans < guess:
        print("請猜小一點")
        h = guess - 1
    count += 1
print("猜對了,共猜:",count,"次:")