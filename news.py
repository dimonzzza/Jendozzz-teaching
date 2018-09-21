#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import bs4
import sys

try:
	site = requests.get('https://news.ycombinator.com')
except EnvironmentError:
	print('not connection')
	sys.exit()

parse = bs4.BeautifulSoup(site.text, "html.parser")
last_news = parse.select(".title .storylink")
points = parse.select(".subtext .score")

print('Последние новости news.ycombinator.com:')

if len(sys.argv) == 2:
	last = int(sys.argv[1])
	last_news = last_news[:last]
if len(sys.argv) == 3:
	first = int(sys.argv[1])
	last = int(sys.argv[2])
	last_news = last_news[first:last]

a = last_news + points
result_list = []

for i in range(len(a)):
	dictionary = {'name': last_news[i],'point': points[i]}
	result_list.append(dictionary)

print(result_list)

	

