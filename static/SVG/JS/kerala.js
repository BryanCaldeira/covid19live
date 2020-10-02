var myHeaders = new Headers();

var requestOptions = {
    method: 'GET',
    headers: myHeaders,
    Vary: 'Origin',
};



let proxyurl = "https://cors-anywhere.herokuapp.com/";

var codes = ['AL', 'ER', 'ID', 'KN', 'KS', 'KL', 'KT', 'KZ', 'MA', 'PL', 'PT', 'TV', 'TS', 'WA']
var values = []

let url = "https://api-covidlive.herokuapp.com/KL/dists"
fetch(proxyurl + url, requestOptions)
    .then(response => response.json())
    .then(result => {
        for (let i = 0; i < codes.length; i++)
            values.push(result[codes[i]])
    })
    .catch(error => console.log('error', error));

function Color(id, code) {
    var svg = document.getElementById("kerala-svg")
    var svgDoc = svg.contentDocument
    let index = codes.indexOf(code)
    let B = 140
    let val = values[index]
    val = val.deaths

    if (val > 10 && val <= 20) {
        B = 160
    } else if (val > 20 && val <= 30) {
        B = 180
    } else if (val > 30 && val <= 40) {
        B = 200
    } else if (val > 30 && val <= 100) {
        B = 220
    } else if (val > 100 && val <= 500) {
        B = 255
    }

    svgDoc.getElementById(id).style.fill = 'rgb(' + B + ', 30,60)'
}

setInterval(function () {
    if (values.length != 0) {
        Color('g7933', 'KS')
        Color('g7924', 'KN')
        Color('g7936', 'KZ')
        Color('g7939', 'WA')
        Color('g7944', 'MA')
        Color('g7949', 'TS')
        Color('g7954', 'PL')
        Color('g7976', 'ER')
        Color('g8001', 'ID')
        Color('g7981', 'AL')
        Color('g7986', 'KT')
        Color('g7988', 'PT')
        Color('g7991', 'KL')
        Color('g8006', 'TV')
    }
}, 1000);



var svg = document.getElementById("kerala-svg");
svg.addEventListener("load", function () {
    var svgDoc = svg.contentDocument;


    function Write(dist) {
        svgDoc.getElementById('dist-name').innerHTML = dist
        svgDoc.getElementById('conf').innerHTML = 'Confirmed'
        svgDoc.getElementById('act').innerHTML = 'Active'
        svgDoc.getElementById('rec').innerHTML = 'Recovered'
        svgDoc.getElementById('dec').innerHTML = 'Deceased'
    }

    function WriteNum(code) {
        var ind = codes.indexOf(code)
        var resin = values[ind]
        svgDoc.getElementById('conf-num').innerHTML = resin.confirmed
        svgDoc.getElementById('act-num').innerHTML = resin.active
        svgDoc.getElementById('rec-num').innerHTML = resin.recovered
        svgDoc.getElementById('dec-num').innerHTML = resin.deaths

    }

    svgDoc.getElementById("g7933").onmouseover = function () {
        dist = 'kasaragod'
        WriteNum('KS')
        Write(dist);

    }

    svgDoc.getElementById("g7924").onmouseover = function () {
        dist = 'kannur'
        WriteNum('KN')
        Write(dist);
    }

    svgDoc.getElementById("g7936").onmouseover = function () {
        dist = 'kozhikode'
        WriteNum('KZ')
        Write(dist);
    }


    svgDoc.getElementById("g7939").onmouseover = function () {
        dist = 'wayanad'
        WriteNum('WA')
        Write(dist);
    }

    svgDoc.getElementById("g7944").onmouseover = function () {
        dist = 'malappuram'
        WriteNum('MA')
        Write(dist);
    }

    svgDoc.getElementById("g7949").onmouseover = function () {
        dist = 'thrissur'
        WriteNum('TS')
        Write(dist);
    }

    svgDoc.getElementById("g7954").onmouseover = function () {
        dist = 'palakkad'
        WriteNum('PL')
        Write(dist);
    }

    svgDoc.getElementById("g7976").onmouseover = function () {
        dist = 'ernakulam'
        WriteNum('ER')
        Write(dist);
    }


    svgDoc.getElementById("g8001").onmouseover = function () {
        dist = 'idukki'
        WriteNum('ID')
        Write(dist);
    }

    svgDoc.getElementById("g7981").onmouseover = function () {
        dist = 'alappuzha'
        WriteNum('AL')
        Write(dist);
    }

    svgDoc.getElementById("g7986").onmouseover = function () {
        dist = 'kottayam'
        WriteNum('KT')
        Write(dist);
    }

    svgDoc.getElementById("g7988").onmouseover = function () {
        dist = 'pathanamthitta'
        WriteNum('PT')
        Write(dist);
    }

    svgDoc.getElementById("g7991").onmouseover = function () {
        dist = 'kollam'
        WriteNum('KL')
        Write(dist);
    }

    svgDoc.getElementById("g8006").onmouseover = function () {
        dist = 'thiruvananthapuram'
        WriteNum('TV')
        Write(dist);
    }


    svgDoc.getElementById('svg2').onmouseout = function () {
        svgDoc.getElementById('dist-name').innerHTML = ''
        svgDoc.getElementById('conf').innerHTML = ''
        svgDoc.getElementById('act').innerHTML = ''
        svgDoc.getElementById('rec').innerHTML = ''
        svgDoc.getElementById('dec').innerHTML = ''

        svgDoc.getElementById('conf-num').innerHTML = ''
        svgDoc.getElementById('act-num').innerHTML = ''
        svgDoc.getElementById('rec-num').innerHTML = ''
        svgDoc.getElementById('dec-num').innerHTML = ''

    }

});