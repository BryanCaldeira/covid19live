from django.shortcuts import render
import requests as req
import json

def Main(requests):
    path = (requests.path).strip('/')

    if path == "":
        URL = "https://api-covidlive.herokuapp.com/MN"
        page = 'index.html'

    elif path == "karnataka":
        URL = "https://api-covidlive.herokuapp.com/KA"
        page = 'karnataka.html'

    elif path == "kerala":
        URL = "https://api-covidlive.herokuapp.com/KL"
        page = 'kerala.html'

    elif path == "andhrapradesh":
        URL = "https://api-covidlive.herokuapp.com/AP"
        page = 'andhrapradesh.html'

    elif path == "tamilnadu":
        URL = "https://api-covidlive.herokuapp.com/TN"
        page = 'tamilnadu.html'

    elif path == "maharashtra":
        URL = "https://api-covidlive.herokuapp.com/MH"
        page = 'maharashtra.html'

    elif path == "telangana":
        URL = "https://api-covidlive.herokuapp.com/TS"
        page = 'telangana.html'

    elif path == "delhi":
        URL = "https://api-covidlive.herokuapp.com/DL"
        page = 'delhi.html'

    elif path == "uttarpradesh":
        URL = "https://api-covidlive.herokuapp.com/UP"
        page = 'uttarpradesh.html'

    elif path == "punjab":
        URL = "https://api-covidlive.herokuapp.com/PB"
        page = 'punjab.html'

    elif path == "westbengal":
        URL = "https://api-covidlive.herokuapp.com/WB"
        page = 'westbengal.html'


    response = req.get(URL)
    data = response.text
    data = json.loads(data)

    # return the rendered page
    return render(requests, page, data)
