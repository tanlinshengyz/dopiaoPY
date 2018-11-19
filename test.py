#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests,sys

def writer(name, path, text):
    write_flag = True
    with open(path, 'a', encoding='utf-8') as f:
        f.write(name + '\n')
        f.writelines(text)
        f.write('\n\n')

if __name__ == '__main__':
	# headers = {'User-Agent': 'BaiduSipder'}
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'}
	target = 'http://www.biqukan.com/1_1094/5403177.html'
	req = requests.get(url=target,headers=headers)
	# print(req.text)
	html = req.text
	bf = BeautifulSoup(html, "lxml")
	texts = bf.find_all('div', class_ = 'showtxt')
	texts = texts[0].text.replace('\xa0'*8,'\n\n')
	# print(texts)
	writer('一张', '永恒.txt', texts)
	sys.stdout.write("  已下载部分")
	sys.stdout.flush()
	print('《永恒》下载完成')
