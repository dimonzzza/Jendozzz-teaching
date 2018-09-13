#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, bs4
site=requests.get('https://news.ycombinator.com/')
parse=bs4.BeautifulSoup(site.text, "html.parser")
latest_news=parse.select(".title .storylink")
print('Последние новости news.ycombinator.com:')
for i in range(len(latest_news)):
	print(i, latest_news[i].getText())

