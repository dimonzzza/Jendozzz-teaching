#!/usr/bin/env python3
# -*- coding: utf-8 -*-

while True:
	x = raw_input()
	if x == 'quit':
		quit()
	else:
		z = raw_input()
		y = raw_input()
		x = float(x)
		y = float(y)
	if z in ('+','-','*','/','//','%','**'):	
		if z == '+':
			print(x + y)
		elif z == '-':
			print(x - y)
		elif z == '*':
			print(x * y)
		elif z == '/':
			if y != 0:
				print(x / y)
			else:
				print('Деление на ноль!')
		elif z == '//':
			print(x // y)
		elif z == '%':
			print(x % y)
		elif z == '**':
			print(x ** y)
	else:
		print('Неверный знак операции')
	


