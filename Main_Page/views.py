from django.shortcuts import render
import requests as req
from bs4 import BeautifulSoup


# Index Page Contents
def Main(requests):
    try:
        # GOV page for COVID-19
        URL = 'https://www.mohfw.gov.in/'
        page = req.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        content = soup.find(class_="site-stats-count")
        content = content.get_text().split()

        # Check if the scrapped data isdigit
        content = [int(i) for i in content if i.isdigit()]

        active = int(content[0])    # Active Cases count
        cured = int(content[1])     # Cured Cases count
        deaths = int(content[2])    # Death count
        migrated = int(content[3])  # Migrated Cases count

        # Calculating the total confirmed Cases
        confirmed = active+cured+deaths+migrated

        # Calculation of fatality rate
        rate = '{:.2%}'.format(deaths/confirmed)

        # Adding ',' to the thousands values
        confirmed = '{:,}'.format(confirmed)
        active = '{:,}'.format(active)
        cured = '{:,}'.format(cured)
        deaths = '{:,}'.format(deaths)

    except:
        # If some error occurs just display N/A
        confirmed = ' N/A '
        active = ' N/A '
        cured = ' N/A '
        deaths = ' N/A '
        migrated = 'N/A'
        rate = ' N/A '

    # return the rendered page
    return render(requests, 'index.html', {'confirmed': confirmed, 'active': active, 'cured': cured, 'deaths': deaths, 'migrated': migrated, 'rate': rate})


# Karnataka Page Contents
def Karnataka(requests):
    try:
        # Wikipedia page of COVID-19 for Karnataks State
        URL = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Karnataka'
        page = req.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        content = soup.find_all('td')

        # Extracting the values
        conf_cases = int((content[10].get_text().split()[0]).replace(
            ',', ''))  # Confirmed Cases count
        # Active Cases count
        act_cases = content[11].get_text().split()[0]
        # Recovered Cases count
        rec_cases = content[12].get_text().split()[0]
        deaths = int((content[13].get_text().split()[0]
                      ).replace(',', ''))      # Death count
        # Calculating Fatality rate
        fatality = '{:.2%}'.format(deaths/conf_cases)

        # Adding ',' to the thousands place
        conf_cases = '{:,}'.format(conf_cases)
        deaths = '{:,}'.format(deaths)

    except:
        # If some error occurs just display N/A
        conf_cases = 'N/A'
        act_cases = 'N/A'
        rec_cases = 'N/A'
        deaths = 'N/A'
        fatality = 'N/A'

    # return the rendered page
    return render(requests, 'karnataka.html', {'conf_cases': conf_cases, 'act_cases': act_cases, 'rec_cases': rec_cases, 'deaths': deaths, 'fatality': fatality})


# TamilNadu Page Contents
def Tamilnadu(requests):
    try:
        # Wikipedia page of COVID-19 for Tamil Nadu State
        URL = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Tamil_Nadu'
        page = req.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        content = soup.find_all('td')

        conf_cases = int((content[15].get_text().split()[0]).replace(
            ',', ''))      # Confirmed Cases count
        act_cases = int(''.join(
            [elem for elem in content[16].get_text().split()[0] if elem.isdigit()]))    # Active Cases count
        rec_cases = content[17].get_text().split()[0]   # Recovered Cases Count
        deaths = int((content[18].get_text().split()[0]
                      ).replace(',', ''))  # Death Count

        fatality = '{:.2%}'.format(deaths/conf_cases)  # Fatality Rate

        # Adding ',' to the thousands place
        conf_cases = '{:,}'.format(conf_cases)
        act_cases = '{:,}'.format(act_cases)
        deaths = '{:,}'.format(deaths)

    except:
        # If some error occurs just display N/A
        conf_cases = 'N/A'
        act_cases = 'N/A'
        rec_cases = 'N/A'
        deaths = 'N/A'
        fatality = 'N/A'

    # return the rendered page
    return render(requests, 'tamilnadu.html', {'conf_cases': conf_cases, 'act_cases': act_cases, 'rec_cases': rec_cases, 'deaths': deaths, 'fatality': fatality})


# Kerala Page Contents
def Kerala(requests):
    try:
        # GOV page of COVID-19 for Kerala State
        URL = 'https://dashboard.kerala.gov.in/'
        page = req.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        content = soup.find_all(class_="inner")

        conf_cases = int(content[0].get_text().split()[0])  # Confirmed Cases
        act_cases = int(content[1].get_text().split()[0])   # Active Cases
        rec_cases = int(content[2].get_text().split()[0])   # Recovered Cases
        deaths = int(content[3].get_text().split()[0])      # Deaths

        # Fatality Rate
        fatality = '{:.2%}'.format(deaths/conf_cases)

        # Adding ',' to thousands place
        conf_cases = '{:,}'.format(conf_cases)
        act_cases = '{:,}'.format(act_cases)
        rec_cases = '{:,}'.format(rec_cases)

    except:
        # If some error occurs just display N/A
        conf_cases = 'N/A'
        act_cases = 'N/A'
        rec_cases = 'N/A'
        deaths = 'N/A'
        fatality = 'N/A'

    # return the rendered page
    return render(requests, 'kerala.html', {'conf_cases': conf_cases, 'act_cases': act_cases, 'rec_cases': rec_cases, 'deaths': deaths, 'fatality': fatality})


# AndhraPradesh Page Contents
def Andhrapradesh(requests):
    try:
        # Wikipedia page of COVID-19 for AndhraPradesh State
        URL = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Andhra_Pradesh'
        page = req.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        content = soup.find_all('td')

        # Confirm Cases count
        conf_cases = int((content[7].get_text().split()[0]).replace(',', ''))
        act_cases = content[8].get_text().split()[0]    # Active Cases count
        rec_cases = content[9].get_text().split()[0]    # Recovered Cases count
        deaths = int(content[10].get_text().split()[0])  # death count

        # Fatality Rate
        fatality = '{:.2%}'.format(deaths/conf_cases)

        # Adding ',' to thousands place
        conf_cases = '{:,}'.format(conf_cases)

    except:
        # If some error occurs just display N/A
        conf_cases = 'N/A'
        act_cases = 'N/A'
        rec_cases = 'N/A'
        deaths = 'N/A'
        fatality = 'N/A'

    # return the rendered page
    return render(requests, 'andhrapradesh.html', {'conf_cases': conf_cases, 'act_cases': act_cases, 'rec_cases': rec_cases, 'deaths': deaths, 'fatality': fatality})

# Maharashtra Page Contents


def Maharashtra(requests):
    try:
        # Wikipedia page of COVID-19 for Maharashtra State
        URL = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Maharashtra'
        page = req.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        content = soup.find_all('td')

        conf_cases = int((content[7].get_text().split()[0]).replace(
            ',', ''))   # Confirmed Cases count
        act_cases = content[8].get_text().split()[0]    # Active Cases count
        rec_cases = content[9].get_text().split()[0]    # Recovered Cases count
        deaths = int((content[10].get_text().split()[0]
                      ).replace(',', ''))  # Death count

        # Calculating Fatality rate
        fatality = '{:.2%}'.format(deaths/conf_cases)

        # Adding ',' to the thousands place
        conf_cases = '{:,}'.format(conf_cases)
        deaths = '{:,}'.format(deaths)

    except:
        # If some error occurs just display N/A
        conf_cases = 'N/A'
        act_cases = 'N/A'
        rec_cases = 'N/A'
        deaths = 'N/A'
        fatality = 'N/A'

    # return the rendered page
    return render(requests, 'maharashtra.html', {'conf_cases': conf_cases, 'act_cases': act_cases, 'rec_cases': rec_cases, 'deaths': deaths, 'fatality': fatality})


# Telangana Page Contents
def Telangana(requests):
    try:
        # Wikipedia page of COVID-19 for Telangana State
        URL = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Telangana'
        page = req.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        content = soup.find_all('td')

        conf_cases = int((content[6].get_text().split()[0]).replace(
            ',', ''))   # Confirmed Cases Count
        act_cases = content[7].get_text().split()[0]    # Active Cases count
        rec_cases = content[8].get_text().split()[0]    # Recovered Cases count
        deaths = int(content[9].get_text().split()[0])  # Death Count

        # Calculating Fatality Rate
        fatality = '{:.2%}'.format(deaths/conf_cases)

        # Adding ',' to thousands place
        conf_cases = '{:,}'.format(conf_cases)

    except:
        # If some error occurs just display N/A
        conf_cases = 'N/A'
        act_cases = 'N/A'
        rec_cases = 'N/A'
        deaths = 'N/A'
        fatality = 'N/A'

    # return the rendered page
    return render(requests, 'telangana.html', {'conf_cases': conf_cases, 'act_cases': act_cases, 'rec_cases': rec_cases, 'deaths': deaths, 'fatality': fatality})

# Delhi Page Contents


def Delhi(requests):
    try:
        # Wikipedia page of COVID-19 for Delhi State
        URL = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Delhi'
        page = req.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        content = soup.find_all('td')

        conf_cases = int((content[9].get_text().split()[0]).replace(
            ',', ''))   # Confirmes Cases count
        act_cases = content[10].get_text().split()[0]   # Active Cases count
        rec_cases = content[11].get_text().split()[0]   # Recovered Cases count
        deaths = int((content[12].get_text().split()[0]
                      ).replace(',', ''))  # Death count

        # Calculating fatality rate
        fatality = '{:.2%}'.format(deaths/conf_cases)

        # Adding ',' to the thousands place
        conf_cases = '{:,}'.format(conf_cases)
        deaths = '{:,}'.format(deaths)

    except:
        # If some error occurs just display N/A
        conf_cases = 'N/A'
        act_cases = 'N/A'
        rec_cases = 'N/A'
        deaths = 'N/A'
        fatality = 'N/A'

    # return the rendered page
    return render(requests, 'delhi.html', {'conf_cases': conf_cases, 'act_cases': act_cases, 'rec_cases': rec_cases, 'deaths': deaths, 'fatality': fatality})

# UttarPradesh Page Contents


def Uttarpradesh(requests):
    try:
        # Wikipedia page of COVID-19 for UttarPradesh State
        URL = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Uttar_Pradesh'
        page = req.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        content = soup.find_all('td')

        conf_cases = int((content[8].get_text().split()[0]).replace(
            ',', ''))  # Confirmed Cases count
        act_cases = content[9].get_text().split()[0]    # Active cases count
        rec_cases = content[10].get_text().split()[0]   # Recovered cases count
        deaths = int(content[11].get_text().split()[0])  # Death count

        # Fatality rate Calculation
        fatality = '{:.2%}'.format(deaths/conf_cases)

        # Adding ',' to thousands place
        conf_cases = '{:,}'.format(conf_cases)

    except:
        # If some error occurs just display N/A
        conf_cases = 'N/A'
        act_cases = 'N/A'
        rec_cases = 'N/A'
        deaths = 'N/A'
        fatality = 'N/A'

    # return the rendered page
    return render(requests, 'uttarpradesh.html', {'conf_cases': conf_cases, 'act_cases': act_cases, 'rec_cases': rec_cases, 'deaths': deaths, 'fatality': fatality})


def Punjab(requests):
    try:
        # Wikipedia page of COVID-19 for Punjab State
        URL = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Punjab,_India'
        page = req.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        content = soup.find_all('td')

        conf_cases = int((content[7].get_text().split()[0]).replace(
            ',', ''))    # Confirmed Cases count
        act_cases = content[8].get_text().split()[0]    # Active Cases count
        rec_cases = content[9].get_text().split()[0]   # Recovered Cases count
        deaths = int(content[10].get_text().split()[0])  # Death count

        # Calculating Fatality Rate
        fatality = '{:.2%}'.format(deaths/conf_cases)

    except:
        # If some error occurs just display N/A
        conf_cases = 'N/A'
        act_cases = 'N/A'
        rec_cases = 'N/A'
        deaths = 'N/A'
        fatality = 'N/A'

    # return the rendered page
    return render(requests, 'punjab.html', {'conf_cases': conf_cases, 'act_cases': act_cases, 'rec_cases': rec_cases, 'deaths': deaths, 'fatality': fatality})


def Westbengal(requests):
    try:
        # Wikipedia page of COVID-19 for WestBengal State
        URL = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_West_Bengal'
        page = req.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        content = soup.find_all('td')

        conf_cases = int((content[8].get_text().split()[0]).replace(
            ',', ''))   # Confirmed Cases count
        act_cases = content[9].get_text().split()[0]    # Active Cases count
        rec_cases = content[10].get_text().split()[0]   # Recovered Cases count
        deaths = int(content[11].get_text().split()[0])  # Death Count

        # Calculating Fatality rate
        fatality = '{:.2%}'.format(deaths/conf_cases)

        # Adding ',' to the thousands place
        conf_cases = '{:,}'.format(conf_cases)

    except:
        # If some error occurs just display N/A
        conf_cases = 'N/A'
        act_cases = 'N/A'
        rec_cases = 'N/A'
        deaths = 'N/A'
        fatality = 'N/A'

    # return the rendered page
    return render(requests, 'westbengal.html', {'conf_cases': conf_cases, 'act_cases': act_cases, 'rec_cases': rec_cases, 'deaths': deaths, 'fatality': fatality})
