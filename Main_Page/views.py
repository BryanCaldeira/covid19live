from django.shortcuts import render, redirect
import requests as req
from bs4 import BeautifulSoup


def Main(requests):
	URL = 'https://www.mohfw.gov.in/'

	page = req.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	content = soup.find(class_="site-stats-count")

	content = content.get_text().split()


	content = [int(i) for i in content if i.isdigit()]

	active=content[0]
	cured =content[1]
	deaths=content[2]
	migrated=content[3]

		
	return render(requests,'index.html',{'active':active, 'cured':cured, 'deaths':deaths, 'migrated':migrated})


def Karnataka(requests):
	URL = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Karnataka'

	page = req.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	content = soup.find_all('td')

	conf_cases_list = content[9].get_text().split()
	conf_cases = conf_cases_list[0]

	act_cases = content[10].get_text()

	rec_cases_list = content[11].get_text().split()
	rec_cases = rec_cases_list[0]

	deaths_list = content[12].get_text().split()
	deaths = deaths_list[0]

	fatality = content[13].get_text()[:2]

	return render(requests, 'karnataka.html' ,{'conf_cases':conf_cases , 'act_cases':act_cases, 'rec_cases':rec_cases, 'deaths':deaths, 'fatality':fatality })



def Tamilnadu(requests):
	URL = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Tamil_Nadu'

	page = req.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	content = soup.find_all('td')

	conf_cases_list = content[7].get_text().split()
	conf_cases = conf_cases_list[0]

	act_cases_list = content[8].get_text().split('[')
	act_cases = act_cases_list[0]

	rec_cases_list = content[9].get_text().split()
	rec_cases = rec_cases_list[0]

	deaths_list = content[10].get_text().split()
	deaths = deaths_list[0]

	fatality = content[11].get_text()


	return render(requests, 'tamilnadu.html',{'conf_cases':conf_cases, 'act_cases':act_cases, 'rec_cases':rec_cases, 'deaths':deaths, 'fatality':fatality})



def Kerala(requests):
	URL = 'https://dashboard.kerala.gov.in/'

	page = req.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	content = soup.find_all(class_="inner")

	conf_cases_list = content[0].get_text().split()
	conf_cases = conf_cases_list[0]

	act_cases_list = content[1].get_text().split()
	act_cases = act_cases_list[0]

	rec_cases_list = content[2].get_text().split()
	rec_cases = rec_cases_list[0]

	deaths_list = content[3].get_text().split()
	deaths = deaths_list[0]

	fatality = deaths_list[2]

	print('\n\n\n\n\n\n\n',deaths_list)

	return render(requests, 'kerala.html',{'conf_cases':conf_cases, 'act_cases':act_cases, 'rec_cases':rec_cases, 'deaths':deaths, 'fatality':fatality})



def Andhrapradesh(requests):
	URL = 'http://hmfw.ap.gov.in/covid_dashboard.aspx'

	page = req.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	content = soup.find_all('td')

	conf_cases_list = content[1].get_text().split()
	conf_cases = conf_cases_list[2]

	act_cases_list = content[3].get_text().split()
	act_cases = act_cases_list[2]

	rec_cases_list = content[5].get_text().split()
	rec_cases = rec_cases_list[2]

	deaths_list = content[8].get_text().split()
	deaths = deaths_list[1]

	fatality = (int(deaths)/int(conf_cases))*100

	fatality = round(fatality,2)
	fatality = str(fatality)+'%'
	
	return render(requests, 'andhrapradesh.html',{'conf_cases':conf_cases, 'act_cases':act_cases, 'rec_cases':rec_cases, 'deaths':deaths, 'fatality':fatality})



def Maharashtra(requests):
	URL = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Maharashtra'

	page = req.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	content = soup.find_all('td')

	conf_cases_list = content[8].get_text().split()
	conf_cases = conf_cases_list[0]

	act_cases_list = content[9].get_text().split()
	act_cases = act_cases_list[0]

	rec_cases_list = content[10].get_text().split()
	rec_cases = rec_cases_list[0]

	deaths_list = content[11].get_text().split()
	deaths = deaths_list[0]

	conf_cases = conf_cases.split(',')
	conf_cases = ''.join(conf_cases)

	fatality = (int(deaths)/int(conf_cases))*100

	fatality = round(fatality,2)
	fatality = str(fatality)+'%'

	return render(requests, 'maharashtra.html', {'conf_cases':conf_cases, 'act_cases':act_cases, 'rec_cases':rec_cases, 'deaths':deaths, 'fatality':fatality})


def Telangana(requests):
	URL = 'https://covid19.telangana.gov.in/'

	page = req.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	content = soup.find_all(class_="uagb-column__inner-wrap")

	#content = [int(i) for i in content[2].get_text().split() if i.isdigit()]


	print('\n\n\n\n\n\n',content[5].get_text())


	return render(requests, 'telangana.html')