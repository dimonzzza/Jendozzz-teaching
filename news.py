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
latest_news = parse.select(".title .storylink")

print('Последние новости news.ycombinator.com:')
for i in range(len(latest_news)):
	print(i+1, latest_news[i].getText())

