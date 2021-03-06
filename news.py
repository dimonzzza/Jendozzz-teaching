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

result_list = []

for i in range(len(last_news[:29])):
	dictionary = {'name': last_news[i].getText(),'point': points[i].getText()}
	result_list.append(dictionary)

def sort_by_point(i):
	return dictionary['point']
result_list.sort(key = sort_by_point)

print(result_list)

	

