#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
while True:
	command = str(input())
	if command == 'q':
		quit()
	if command == '..':
		os.chdir('..')
	if command in ('listdir','cd','mkdir','rename','remove','cwd'):
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
	else:
		print('Неизвестная команда')
