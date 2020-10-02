from django.shortcuts import render
import requests as req
import json


def Main(requests):
    path = (requests.path).strip('/')
    page = 'index2.html'
    img = allData = SVG = ''

    if path == "":
        URL = "https://api-covidlive.herokuapp.com/SS"
        URL2 = "https://api-covidlive.herokuapp.com/all-data"
        response2 = req.get(URL2)
        allData = response2.text
        allData = json.loads(allData)

        page = 'index.html'

    elif path == "andhrapradesh":
        URL = "https://api-covidlive.herokuapp.com/AP"
        img = '<img alt="India Andhra Pradesh COVID-19 map.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/41/India_Andhra_Pradesh_COVID-19_map.svg/220px-India_Andhra_Pradesh_COVID-19_map.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/41/India_Andhra_Pradesh_COVID-19_map.svg/330px-India_Andhra_Pradesh_COVID-19_map.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/41/India_Andhra_Pradesh_COVID-19_map.svg/440px-India_Andhra_Pradesh_COVID-19_map.svg.png 2x" data-file-width="2749" data-file-height="2363" width="220" height="189">'

    elif path == "arunachalpradesh":
        URL = "https://api-covidlive.herokuapp.com/AR"
        img = '<img src="http://www.onefivenine.com/images/StateMaps/Arunachal%20Pradesh.jpg" width = "280" height = "189">'

    elif path == "assam":
        URL = "https://api-covidlive.herokuapp.com/AS"
        img = '<img alt="India Assam COVID-19 map.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e9/India_Assam_COVID-19_map.svg/400px-India_Assam_COVID-19_map.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/e9/India_Assam_COVID-19_map.svg/600px-India_Assam_COVID-19_map.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/e9/India_Assam_COVID-19_map.svg/800px-India_Assam_COVID-19_map.svg.png 2x" data-file-width="765" data-file-height="633" width="400" height="331">'

    elif path == "bihar":
        URL = "https://api-covidlive.herokuapp.com/BR"
        img = '<img alt="Bihar Corona Map.png" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/05/Bihar_Corona_Map.png/220px-Bihar_Corona_Map.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/05/Bihar_Corona_Map.png/330px-Bihar_Corona_Map.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/05/Bihar_Corona_Map.png/440px-Bihar_Corona_Map.png 2x" data-file-width="565" data-file-height="533" width="220" height="208">'

    elif path == "chattisgarh":
        URL = "https://api-covidlive.herokuapp.com/CG"
        img = '<img src="https://i.pinimg.com/564x/85/8c/4d/858c4d67f1b21cafe2027488ef8bbc88.jpg" width="400" height="400">'

    elif path == "delhi":
        URL = "https://api-covidlive.herokuapp.com/DL"
        img = '<img alt="Location map India Delhi EN.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Location_map_India_Delhi_EN.svg/220px-Location_map_India_Delhi_EN.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Location_map_India_Delhi_EN.svg/330px-Location_map_India_Delhi_EN.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Location_map_India_Delhi_EN.svg/440px-Location_map_India_Delhi_EN.svg.png 2x" data-file-width="768" data-file-height="764" width="220" height="219">'

    elif path == "goa":
        URL = "https://api-covidlive.herokuapp.com/GA"
        img = '<img src="https://i.pinimg.com/originals/66/a7/84/66a784c992b1da5722de5bca3db20b29.png" width="320" height="419">'

    elif path == "gujarat":
        URL = "https://api-covidlive.herokuapp.com/GJ"
        img = '<img alt="India Gujarat COVID-19 map.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/3/33/India_Gujarat_COVID-19_map.svg/370px-India_Gujarat_COVID-19_map.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/3/33/India_Gujarat_COVID-19_map.svg/555px-India_Gujarat_COVID-19_map.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/3/33/India_Gujarat_COVID-19_map.svg/740px-India_Gujarat_COVID-19_map.svg.png 2x" data-file-width="2170" data-file-height="1722" width="370" height="294">'

    elif path == "haryana":
        URL = "https://api-covidlive.herokuapp.com/HR"
        img = '<img alt="India Haryana COVID-19 map.svg" src="//upload.wikimedia.org/wikipedia/en/thumb/d/d6/India_Haryana_COVID-19_map.svg/220px-India_Haryana_COVID-19_map.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/en/thumb/d/d6/India_Haryana_COVID-19_map.svg/330px-India_Haryana_COVID-19_map.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/d/d6/India_Haryana_COVID-19_map.svg/440px-India_Haryana_COVID-19_map.svg.png 2x" data-file-width="769" data-file-height="943" width="220" height="270">'

    elif path == "himachalpradesh":
        URL = "https://api-covidlive.herokuapp.com/HP"
        img = '<img src="https://www.onefivenine.com/images/StateMaps/Himachal%20Pradesh.jpg" width="270" height="270">'

    elif path == "jammu&kashmir":
        URL = "https://api-covidlive.herokuapp.com/JK"
        img = '<img src="https://static.toiimg.com/photo/msid-71870888/71870888.jpg?resizemode=4&width=400" width="350" height="270">'

    elif path == "jharkhand":
        URL = "https://api-covidlive.herokuapp.com/JS"
        img = '<img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Jharkhand.png/800px-Jharkhand.png" width = "350" height = "270" >'

    elif path == "karnataka":
        URL = "https://api-covidlive.herokuapp.com/KA"
        img = '<img alt="India Karnataka COVID-19 map.svg" src="http://upload.wikimedia.org/wikipedia/commons/thumb/2/28/India_Karnataka_COVID-19_map.svg/220px-India_Karnataka_COVID-19_map.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/28/India_Karnataka_COVID-19_map.svg/330px-India_Karnataka_COVID-19_map.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/28/India_Karnataka_COVID-19_map.svg/440px-India_Karnataka_COVID-19_map.svg.png 2x" data-file-width="1630" data-file-height="2356" width="220" height="318">'

    elif path == "kerala":
        URL = "https://api-covidlive.herokuapp.com/KL"
        SVG = "KL"

    elif path == "madhyapradesh":
        URL = "https://api-covidlive.herokuapp.com/MP"
        img = '<img alt="India Madhya Pradesh COVID-19 map.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/1a/India_Madhya_Pradesh_COVID-19_map.svg/330px-India_Madhya_Pradesh_COVID-19_map.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/1a/India_Madhya_Pradesh_COVID-19_map.svg/495px-India_Madhya_Pradesh_COVID-19_map.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/1a/India_Madhya_Pradesh_COVID-19_map.svg/660px-India_Madhya_Pradesh_COVID-19_map.svg.png 2x" data-file-width="950" data-file-height="650" width="330" height="226">'

    elif path == "maharashtra":
        URL = "https://api-covidlive.herokuapp.com/MH"
        img = '<img alt="India Maharashtra COVID-19 map.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/3/30/India_Maharashtra_COVID-19_map.svg/220px-India_Maharashtra_COVID-19_map.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/3/30/India_Maharashtra_COVID-19_map.svg/330px-India_Maharashtra_COVID-19_map.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/3/30/India_Maharashtra_COVID-19_map.svg/440px-India_Maharashtra_COVID-19_map.svg.png 2x" data-file-width="2168" data-file-height="1671" width="220" height="170">'

    elif path == "manipur":
        URL = "https://api-covidlive.herokuapp.com/MN"
        img = '<img src="https://www.onefivenine.com/images/StateMaps/Manipur.jpg" width="220" height="170">'

    elif path == "meghalaya":
        URL = "https://api-covidlive.herokuapp.com/ML"
        img = '<img src="https://www.onefivenine.com/images/StateMaps/Meghalaya.jpg" width="370" height="300">'

    elif path == "mizoram":
        URL = "https://api-covidlive.herokuapp.com/MZ"
        img = '<img src="https://www.onefivenine.com/images/StateMaps/Mizoram.jpg" width="300" height="400">'

    elif path == "nagaland":
        URL = "https://api-covidlive.herokuapp.com/NL"
        page = 'nagaland.html'

    elif path == "orissa":
        URL = "https://api-covidlive.herokuapp.com/OR"
        img = '<img src="//upload.wikimedia.org/wikipedia/commons/thumb/d/d4/India_Odisha_COVID-19_cases.svg/440px-India_Odisha_COVID-19_cases.svg.png" width="300" height="300">'

    elif path == "punjab":
        URL = "https://api-covidlive.herokuapp.com/PB"
        img = '<img alt="India Punjab COVID-19 map.png" src="//upload.wikimedia.org/wikipedia/commons/d/d9/India_Punjab_COVID-19_map.png" decoding="async" data-file-width="1084" data-file-height="1200" width="300" height="300">'

    elif path == "rajasthan":
        URL = "https://api-covidlive.herokuapp.com/RJ"
        img = '<img src="//upload.wikimedia.org/wikipedia/commons/thumb/5/54/India_Rajasthan_COVID-19_map.svg/330px-India_Rajasthan_COVID-19_map.svg.png" width="300" height="300">'

    elif path == "sikkim":
        URL = "https://api-covidlive.herokuapp.com/SK"
        img = '<img src="https://diligentias.com/wp-content/uploads/2019/06/sikkim.jpg" width="300" height="300">'

    elif path == "tamilnadu":
        URL = "https://api-covidlive.herokuapp.com/TN"
        img = '<img src="//upload.wikimedia.org/wikipedia/commons/thumb/a/aa/India_Tamil_Nadu_COVID-19_map.svg/220px-India_Tamil_Nadu_COVID-19_map.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/aa/India_Tamil_Nadu_COVID-19_map.svg/330px-India_Tamil_Nadu_COVID-19_map.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/aa/India_Tamil_Nadu_COVID-19_map.svg/440px-India_Tamil_Nadu_COVID-19_map.svg.png 2x" data-file-width="512" data-file-height="636" width="220" height="273">'

    elif path == "telangana":
        URL = "https://api-covidlive.herokuapp.com/TS"
        img = '<img src="https://www.telangana.gov.in/PublishingImages/Pages/Home/Telangana-New-Map-33-Districts.png" width="250" height="270">'

    elif path == "tripura":
        URL = "https://api-covidlive.herokuapp.com/TR"
        img = '<img src="https://lh3.googleusercontent.com/proxy/YSsfwDfu8KFJtDbUZ0Yy8GmRaDdCHQDLSAr2sh14JBfp4t6ltmPrDWxK8UlsPhrxxtJyQr2Bp1aZMElWittRH8YSGVpMK5jY1UP_O_COKmMuqWm1RiglTZmb52k" width="270" height="270">'

    elif path == "uttarakhand":
        URL = "https://api-covidlive.herokuapp.com/UK"
        img = '<img src="https://slusi.dacnet.nic.in/dmwai/UTTARAKHAND/UTTARAKHAND.png" width="300" height="270">'

    elif path == "uttarpradesh":
        URL = "https://api-covidlive.herokuapp.com/UP"
        img = '<img src="//upload.wikimedia.org/wikipedia/commons/thumb/8/8a/India_Uttar_Pradesh_COVID-19_map.svg/220px-India_Uttar_Pradesh_COVID-19_map.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/8a/India_Uttar_Pradesh_COVID-19_map.svg/330px-India_Uttar_Pradesh_COVID-19_map.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/8a/India_Uttar_Pradesh_COVID-19_map.svg/440px-India_Uttar_Pradesh_COVID-19_map.svg.png 2x" data-file-width="2253" data-file-height="2338" width="220" height="228">'

    elif path == "westbengal":
        URL = "https://api-covidlive.herokuapp.com/WB"
        img = '<img src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9f/India_West_Bengal_COVID-19_map.svg/220px-India_West_Bengal_COVID-19_map.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9f/India_West_Bengal_COVID-19_map.svg/330px-India_West_Bengal_COVID-19_map.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9f/India_West_Bengal_COVID-19_map.svg/440px-India_West_Bengal_COVID-19_map.svg.png 2x" data-file-width="768" data-file-height="1159" width="220" height="332">'

    response = req.get(URL)
    data = response.text
    data = json.loads(data)
    data.update({"img": img})
    data.update({"SVG": SVG})

    if path == "":
        stateCodes = ['AP', 'AR', 'AS', 'BR', 'CG', 'DL', 'GA', 'GJ', 'HR', 'HP', 'JK', 'JS', 'KA',
                      'KL', 'MP', 'MH', 'MN', 'ML', 'MZ', 'NL', 'OR', 'PB', 'RJ', 'SK', 'TN', 'TS', 'TR', 'UK', 'UP', 'WB']

        data.update({"codes": stateCodes})
        for elem in stateCodes:
            lst = [allData[elem]["confirmed"], allData[elem]["active"], allData[elem]
                   ["recovered"], allData[elem]["deaths"], allData[elem]["fatality_rate"]]
            print(lst)
            data.update({elem: lst})

    # return the rendered page
    return render(requests, page, data)
