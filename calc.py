#!/usr/bin/env python3

while True:
	x, z, y = raw_input().split() 
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
			print(x / y)
		elif z == '//':
			print(x // y)
		elif z == '%':
			print(x % y)
		elif z == '**':
			print(x ** y)



