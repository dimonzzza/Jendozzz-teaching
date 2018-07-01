#!/usr/bin/env python3

while True:
	x, z, y = raw_input().split() 
	x = float(x)
	y = float(y)
	if z in ('+','-','*','/'):	
		if z == '+':
			x = x + y
		elif z == '-':
			x = x - y
		elif z == '*':
			x = x * y
		elif z == '/':
			x = x / y
		print(x)



ляляляля тополя проверка связи
