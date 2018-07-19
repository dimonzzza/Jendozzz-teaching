#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
while True:
	command = str(input())
	if command == 'q':
		quit()
	if command in ('listdir','cd','mkdir','rename','remove','cwd','edit','open','..'):
		if command == 'listdir': 
			print(os.listdir('.'))
		elif command == 'cd':
			os.chdir(input())
		elif command == 'mkdir':
			os.mkdir(input())
		elif command == 'rename':
			old = input()
			new = input()
			os.renames(old, new) 
		elif command == 'remove':
			os.rmdir(input())
		elif command == 'cwd':
			print(os.getcwd())
		elif command == 'edit':
			my_file = open(input(), "a")
			my_file.write(input())
			my_file.close()
		elif command == 'open':
			my_file = open(input())
			my_string = my_file.read()
			print(my_string)
			my_file.close()
		elif command == '..':
			os.chdir('..')
	else:
		print('Неизвестная команда')
