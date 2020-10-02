from django.shortcuts import render
import requests as req
import json


def Main(requests):
    path = (requests.path).strip('/')
    page = 'index2.html'
    img = SVG = CODE = NAME = ''

    dis = {}
    if path == "":
        response = req.get("https://api-covidlive.herokuapp.com/SS")
        allData = response.text
        allData = json.loads(allData)
        dis.update(
            {"confirmed": allData['confirmed'], "active": allData['active'], "recovered": allData['recovered'], "deaths": allData['deaths'], "fatality_rate": allData['fatality_rate']})

        page = 'index.html'

    elif path == "andhrapradesh":
        NAME = "Andhra Pradesh"
        CODE = 'AP'
        img = '<img alt="India Andhra Pradesh COVID-19 map.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/41/India_Andhra_Pradesh_COVID-19_map.svg/220px-India_Andhra_Pradesh_COVID-19_map.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/41/India_Andhra_Pradesh_COVID-19_map.svg/330px-India_Andhra_Pradesh_COVID-19_map.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/41/India_Andhra_Pradesh_COVID-19_map.svg/440px-India_Andhra_Pradesh_COVID-19_map.svg.png 2x" data-file-width="2749" data-file-height="2363" width="220" height="189">'

    elif path == "arunachalpradesh":
        NAME = "Arunachal Pradesh"
        CODE = 'AR'
        img = '<img src="http://www.onefivenine.com/images/StateMaps/Arunachal%20Pradesh.jpg" width = "280" height = "189">'

    elif path == "assam":
        NAME = "Assam"
        CODE = 'AS'
        img = '<img alt="India Assam COVID-19 map.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e9/India_Assam_COVID-19_map.svg/400px-India_Assam_COVID-19_map.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/e9/India_Assam_COVID-19_map.svg/600px-India_Assam_COVID-19_map.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/e9/India_Assam_COVID-19_map.svg/800px-India_Assam_COVID-19_map.svg.png 2x" data-file-width="765" data-file-height="633" width="400" height="331">'

    elif path == "bihar":
        NAME = "Bihar"
        CODE = 'BR'
        img = '<img alt="Bihar Corona Map.png" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/05/Bihar_Corona_Map.png/220px-Bihar_Corona_Map.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/05/Bihar_Corona_Map.png/330px-Bihar_Corona_Map.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/05/Bihar_Corona_Map.png/440px-Bihar_Corona_Map.png 2x" data-file-width="565" data-file-height="533" width="220" height="208">'

    elif path == "chattisgarh":
        NAME = "Chattisgarh"
        CODE = 'CH'
        img = '<img src="https://i.pinimg.com/564x/85/8c/4d/858c4d67f1b21cafe2027488ef8bbc88.jpg" width="400" height="400">'

    elif path == "delhi":
        NAME = "Delhi"
        CODE = 'DL'
        img = '<img alt="Location map India Delhi EN.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Location_map_India_Delhi_EN.svg/220px-Location_map_India_Delhi_EN.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Location_map_India_Delhi_EN.svg/330px-Location_map_India_Delhi_EN.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Location_map_India_Delhi_EN.svg/440px-Location_map_India_Delhi_EN.svg.png 2x" data-file-width="768" data-file-height="764" width="220" height="219">'

    elif path == "goa":
        NAME = "Goa"
        CODE = 'GA'
        img = '<img src="https://i.pinimg.com/originals/66/a7/84/66a784c992b1da5722de5bca3db20b29.png" width="320" height="419">'

    elif path == "gujarat":
        NAME = "Gujarat"
        CODE = 'GJ'
        img = '<img alt="India Gujarat COVID-19 map.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/3/33/India_Gujarat_COVID-19_map.svg/370px-India_Gujarat_COVID-19_map.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/3/33/India_Gujarat_COVID-19_map.svg/555px-India_Gujarat_COVID-19_map.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/3/33/India_Gujarat_COVID-19_map.svg/740px-India_Gujarat_COVID-19_map.svg.png 2x" data-file-width="2170" data-file-height="1722" width="370" height="294">'

    elif path == "haryana":
        NAME = "Haryana"
        CODE = 'HR'
        img = '<img alt="India Haryana COVID-19 map.svg" src="//upload.wikimedia.org/wikipedia/en/thumb/d/d6/India_Haryana_COVID-19_map.svg/220px-India_Haryana_COVID-19_map.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/en/thumb/d/d6/India_Haryana_COVID-19_map.svg/330px-India_Haryana_COVID-19_map.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/d/d6/India_Haryana_COVID-19_map.svg/440px-India_Haryana_COVID-19_map.svg.png 2x" data-file-width="769" data-file-height="943" width="220" height="270">'

    elif path == "himachalpradesh":
        NAME = "Himachal Pradesh"
        CODE = 'HP'
        img = '<img src="https://www.onefivenine.com/images/StateMaps/Himachal%20Pradesh.jpg" width="270" height="270">'

    elif path == "jammu&kashmir":
        NAME = "Jammu & Kashmir"
        CODE = 'JK'
        img = '<img src="https://static.toiimg.com/photo/msid-71870888/71870888.jpg?resizemode=4&width=400" width="350" height="270">'

    elif path == "jharkhand":
        NAME = "Jharkhand"
        CODE = 'JH'
        img = '<img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Jharkhand.png/800px-Jharkhand.png" width = "350" height = "270" >'

    elif path == "karnataka":
        NAME = "Karnataka"
        CODE = 'KA'
        img = '<img alt="India Karnataka COVID-19 map.svg" src="http://upload.wikimedia.org/wikipedia/commons/thumb/2/28/India_Karnataka_COVID-19_map.svg/220px-India_Karnataka_COVID-19_map.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/28/India_Karnataka_COVID-19_map.svg/330px-India_Karnataka_COVID-19_map.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/28/India_Karnataka_COVID-19_map.svg/440px-India_Karnataka_COVID-19_map.svg.png 2x" data-file-width="1630" data-file-height="2356" width="220" height="318">'

    elif path == "kerala":
        NAME = "Kerala"
        CODE = 'KL'
        SVG = "KL"

    elif path == "madhyapradesh":
        NAME = "Madhya Pradesh"
        CODE = 'MP'
        img = '<img alt="India Madhya Pradesh COVID-19 map.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/1a/India_Madhya_Pradesh_COVID-19_map.svg/330px-India_Madhya_Pradesh_COVID-19_map.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/1a/India_Madhya_Pradesh_COVID-19_map.svg/495px-India_Madhya_Pradesh_COVID-19_map.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/1a/India_Madhya_Pradesh_COVID-19_map.svg/660px-India_Madhya_Pradesh_COVID-19_map.svg.png 2x" data-file-width="950" data-file-height="650" width="330" height="226">'

    elif path == "maharashtra":
        NAME = "Maharashtra"
        CODE = 'MH'
        img = '<img alt="India Maharashtra COVID-19 map.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/3/30/India_Maharashtra_COVID-19_map.svg/220px-India_Maharashtra_COVID-19_map.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/3/30/India_Maharashtra_COVID-19_map.svg/330px-India_Maharashtra_COVID-19_map.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/3/30/India_Maharashtra_COVID-19_map.svg/440px-India_Maharashtra_COVID-19_map.svg.png 2x" data-file-width="2168" data-file-height="1671" width="220" height="170">'

    elif path == "manipur":
        NAME = "Manipur"
        CODE = 'MN'
        img = '<img src="https://www.onefivenine.com/images/StateMaps/Manipur.jpg" width="220" height="170">'

    elif path == "meghalaya":
        NAME = "Meghalaya"
        CODE = 'ML'
        img = '<img src="https://www.onefivenine.com/images/StateMaps/Meghalaya.jpg" width="370" height="300">'

    elif path == "mizoram":
        NAME = "Mizoram"
        CODE = 'MZ'
        img = '<img src="https://www.onefivenine.com/images/StateMaps/Mizoram.jpg" width="300" height="400">'

    elif path == "nagaland":
        NAME = "Nagaland"
        CODE = 'NL'
        page = 'nagaland.html'

    elif path == "odisha":
        NAME = "Odisha"
        CODE = 'OR'
        img = '<img src="//upload.wikimedia.org/wikipedia/commons/thumb/d/d4/India_Odisha_COVID-19_cases.svg/440px-India_Odisha_COVID-19_cases.svg.png" width="300" height="300">'

    elif path == "punjab":
        NAME = "Punjab"
        CODE = 'PB'
        img = '<img alt="India Punjab COVID-19 map.png" src="//upload.wikimedia.org/wikipedia/commons/d/d9/India_Punjab_COVID-19_map.png" decoding="async" data-file-width="1084" data-file-height="1200" width="300" height="300">'

    elif path == "rajasthan":
        NAME = "Rajasthan"
        CODE = 'RJ'
        img = '<img src="//upload.wikimedia.org/wikipedia/commons/thumb/5/54/India_Rajasthan_COVID-19_map.svg/330px-India_Rajasthan_COVID-19_map.svg.png" width="300" height="300">'

    elif path == "sikkim":
        NAME = "Sikkim"
        CODE = 'SK'
        img = '<img src="https://diligentias.com/wp-content/uploads/2019/06/sikkim.jpg" width="300" height="300">'

    elif path == "tamilnadu":
        NAME = "Tamil Nadu"
        CODE = 'TN'
        img = '<img src="//upload.wikimedia.org/wikipedia/commons/thumb/a/aa/India_Tamil_Nadu_COVID-19_map.svg/220px-India_Tamil_Nadu_COVID-19_map.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/aa/India_Tamil_Nadu_COVID-19_map.svg/330px-India_Tamil_Nadu_COVID-19_map.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/aa/India_Tamil_Nadu_COVID-19_map.svg/440px-India_Tamil_Nadu_COVID-19_map.svg.png 2x" data-file-width="512" data-file-height="636" width="220" height="273">'

    elif path == "telangana":
        NAME = "Telengana"
        CODE = 'TG'
        img = '<img src="https://www.telangana.gov.in/PublishingImages/Pages/Home/Telangana-New-Map-33-Districts.png" width="250" height="270">'

    elif path == "tripura":
        NAME = "Tripura"
        CODE = 'TR'
        img = '<img src="https://lh3.googleusercontent.com/proxy/YSsfwDfu8KFJtDbUZ0Yy8GmRaDdCHQDLSAr2sh14JBfp4t6ltmPrDWxK8UlsPhrxxtJyQr2Bp1aZMElWittRH8YSGVpMK5jY1UP_O_COKmMuqWm1RiglTZmb52k" width="270" height="270">'

    elif path == "uttarakhand":
        NAME = "Uttarakhand"
        CODE = 'UT'
        img = '<img src="https://slusi.dacnet.nic.in/dmwai/UTTARAKHAND/UTTARAKHAND.png" width="300" height="270">'

    elif path == "uttarpradesh":
        NAME = "Uttarpradesh"
        CODE = 'UP'
        img = '<img src="//upload.wikimedia.org/wikipedia/commons/thumb/8/8a/India_Uttar_Pradesh_COVID-19_map.svg/220px-India_Uttar_Pradesh_COVID-19_map.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/8a/India_Uttar_Pradesh_COVID-19_map.svg/330px-India_Uttar_Pradesh_COVID-19_map.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/8a/India_Uttar_Pradesh_COVID-19_map.svg/440px-India_Uttar_Pradesh_COVID-19_map.svg.png 2x" data-file-width="2253" data-file-height="2338" width="220" height="228">'

    elif path == "westbengal":
        NAME = "West Bengal"
        CODE = 'WB'
        img = '<img src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9f/India_West_Bengal_COVID-19_map.svg/220px-India_West_Bengal_COVID-19_map.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9f/India_West_Bengal_COVID-19_map.svg/330px-India_West_Bengal_COVID-19_map.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9f/India_West_Bengal_COVID-19_map.svg/440px-India_West_Bengal_COVID-19_map.svg.png 2x" data-file-width="768" data-file-height="1159" width="220" height="332">'

    response = req.get('https://api.covid19india.org/v4/data.json')
    data = response.text
    data = json.loads(data)

    if path == "":
        stateCodes = ['AP', 'AR', 'AS', 'BR', 'CH', 'DL', 'GA', 'GJ', 'HR', 'HP', 'JK', 'JH', 'KA',
                      'KL', 'MP', 'MH', 'MN', 'ML', 'MZ', 'NL', 'OR', 'PB', 'RJ', 'SK', 'TN', 'TG', 'TR', 'UT', 'UP', 'WB']

        for elem in stateCodes:
            allData = data[elem]['total']
            lst = ['{:,}'.format(int(allData.get("confirmed", 'N/A'))), '{:,}'.format(int(allData.get("recovered", 'N/A'))),
                   '{:,}'.format(int(allData.get("deceased", '00'))), '{:,}'.format(int(allData.get("tested", 'N/A'))), '{:.2%}'.format(int(allData.get("deceased", "00"))/int(allData.get("confirmed", "00")))]
            dis.update({elem: lst})
    else:
        dis.update({"state": NAME})
        allData = data[CODE]['total']
        dis.update({"confirmed": '{:,}'.format(
            int(allData.get("confirmed", "00"))), "recovered": '{:,}'.format(int(allData.get("recovered", "00"))), "deceased": '{:,}'.format(int(allData.get("deceased", "00"))), "tested": '{:,}'.format(int(allData.get("tested", "00"))), "rate": '{:.2%}'.format(int(allData.get("deceased", "00"))/int(allData.get("confirmed", "00")))})

    dis.update({"img": img})
    dis.update({"SVG": SVG})

    # return the rendered page
    return render(requests, page, dis)
