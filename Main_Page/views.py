from django.shortcuts import render, redirect
import requests as req
from bs4 import BeautifulSoup


def Main(requests):
	try:
		URL = 'https://www.mohfw.gov.in/'

		page = req.get(URL)

		soup = BeautifulSoup(page.content, 'html.parser')

		content = soup.find(class_="site-stats-count")

		content = content.get_text().split()


		content = [int(i) for i in content if i.isdigit()]

		active=int(content[0])
		cured =int(content[1])
		deaths=int(content[2])
		migrated=int(content[3])
		confirmed = active+cured+deaths+migrated

	except:
		confirmed='N/A'
		active='N/A'
		cured ='N/A'
		deaths='N/A'
		migrated='N/A'


	return render(requests,'index.html',{'confirmed':confirmed, 'active':active, 'cured':cured, 'deaths':deaths, 'migrated':migrated})


def Karnataka(requests):
	try:
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

	except:
		conf_cases='N/A'
		act_cases='N/A'
		rec_cases='N/A'
		deaths='N/A'
		fatality='N/A'


	return render(requests, 'karnataka.html' ,{'conf_cases':conf_cases , 'act_cases':act_cases, 'rec_cases':rec_cases, 'deaths':deaths, 'fatality':fatality })



def Tamilnadu(requests):
	try:
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

	except:
		conf_cases='N/A'
		act_cases='N/A'
		rec_cases='N/A'
		deaths='N/A'
		fatality='N/A'



	return render(requests, 'tamilnadu.html',{'conf_cases':conf_cases, 'act_cases':act_cases, 'rec_cases':rec_cases, 'deaths':deaths, 'fatality':fatality})



def Kerala(requests):
	try:
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

	except:
		conf_cases='N/A'
		act_cases='N/A'
		rec_cases='N/A'
		deaths='N/A'
		fatality='N/A'



	return render(requests, 'kerala.html',{'conf_cases':conf_cases, 'act_cases':act_cases, 'rec_cases':rec_cases, 'deaths':deaths, 'fatality':fatality})



def Andhrapradesh(requests):
	try:
		URL = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Andhra_Pradesh'

		page = req.get(URL)

		soup = BeautifulSoup(page.content, 'html.parser')

		content = soup.find_all('td')

		conf_cases_list = content[7].get_text().split()
		conf_cases = conf_cases_list[0]

		act_cases_list = content[8].get_text().split()
		act_cases = act_cases_list[0]

		rec_cases_list = content[9].get_text().split()
		rec_cases = rec_cases_list[0]

		deaths_list = content[10].get_text().split()
		deaths = deaths_list[0]


		conf = conf_cases.split(',')
		conf = ''.join(conf)

		fatality = (int(deaths)/int(conf))*100
		fatality = str(round(fatality,2))+'%'


	except:
		conf_cases='N/A'
		act_cases='N/A'
		rec_cases='N/A'
		deaths='N/A'
		fatality='N/A'
	
	return render(requests, 'andhrapradesh.html',{'conf_cases':conf_cases, 'act_cases':act_cases, 'rec_cases':rec_cases, 'deaths':deaths, 'fatality':fatality})



def Maharashtra(requests):
	try:
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

		conf = conf_cases.split(',')
		conf = ''.join(conf)

		fatality = (int(deaths)/int(conf))*100

		fatality = round(fatality,2)
		fatality = str(fatality)+'%'

	except:
		conf_cases='N/A'
		act_cases='N/A'
		rec_cases='N/A'
		deaths='N/A'
		fatality='N/A'

	return render(requests, 'maharashtra.html', {'conf_cases':conf_cases, 'act_cases':act_cases, 'rec_cases':rec_cases, 'deaths':deaths, 'fatality':fatality})


def Telangana(requests):
	try:
		URL = 'https://covid19.telangana.gov.in/'

		page = req.get(URL)

		soup = BeautifulSoup(page.content, 'html.parser')

		content = soup.find_all(class_="uagb-column__inner-wrap")

		#content = [int(i) for i in content[2].get_text().split() if i.isdigit()]


		print('\n\n\n\n\n\n',content[5].get_text())

	except:
		conf_cases='N/A'
		act_cases='N/A'
		rec_cases='N/A'
		deaths='N/A'
		fatality='N/A'


	return render(requests, 'telangana.html')



def Delhi(requests):
	URL = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Delhi'

	page = req.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	content = soup.find_all('td')

	conf_cases_list = content[11].get_text().split()
	conf_cases = conf_cases_list[0]

	act_cases = content[12].get_text()


	rec_cases_list = content[13].get_text().split()
	rec_cases = rec_cases_list[0]

	deaths_list = content[14].get_text().split()
	deaths = deaths_list[0]


	fatality_list = content[15].get_text().split()
	fatality = fatality_list[0]


	return render(requests, 'delhi.html', {'conf_cases':conf_cases, 'act_cases':act_cases, 'rec_cases':rec_cases, 'deaths':deaths, 'fatality':fatality})
