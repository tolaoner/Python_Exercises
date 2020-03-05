'''Write a Python program to get the top stories from Google news.'''
from urllib import request as request
#from urllib import parse as parse
from bs4 import BeautifulSoup as soup
url_page=request.urlopen('https://news.google.com/?hl=en-US&gl=US&ceid=US:en')
xml_page=url_page.read()
url_page.close()
soup_page=soup(xml_page,"html.parser")
top_news=soup_page.findAll('a',{'class':'DY5T1d'})
top_links=soup_page('article', {'class':'MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne'})
pub_time=soup_page('time',{'class':'WW6dff uQIVzc Sksgp'})
title_list=[]
link_list=[]
pub_list=[]
for news in top_news:
	title_list.append(news.text)
for links in top_links:
	x=len(links['jslog'])
	link_list.append(links['jslog'][9:x-13])
for times in pub_time:
	pub_list.append(times.text)
news_list=[list(a) for a in zip(title_list, link_list, pub_list)]
for news in news_list:
	print('TITLE:',news[0],'\n','LINK:',news[1],'\n','Published:',news[2])