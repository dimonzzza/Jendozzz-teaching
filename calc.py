#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
while True:
	x = input()
	if x == 'quit':
		quit()
	elif x == 'x!':
		fac = int(input())
		print('факториал числа', math.factorial(fac))
		continue
	else:
		mark = input()
		y = input()
		x, y = float(x), float(y)
	if mark in ('+','-','*','/','//','%','**'):	
		if mark == '+':
			print(x + y)
		elif mark == '-':
			print(x - y)
		elif mark == '*':
			print(x * y)
		elif mark == '/':
			if y != 0:
				print(x / y)
			else:
				print('Деление на ноль!')
		elif mark == '//':
			print(x // y)
		elif mark == '%':
			print(x % y)
		elif mark == '**':
			print(x ** y)
	else:
		print('Неверный знак операции')
	


