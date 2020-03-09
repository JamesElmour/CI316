# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Input number 1:")
num1 = int(input())

print("\nInput number 2:")
num2 = int(input())

num3 = 0

# Get sign of num2, to prevent problems with negative multiplication
sign = -1 if num2 < 0 else 1 if num2 > 0 else 0

for i in range(abs(num2)):
    num3 = num3 + (num1 * sign)
    
print(num1, " x ", num2, " = ", num3)