var loader = document.querySelector('.loader');
var body = document.body;
var src_div = document.querySelector('.search');
var src_in = document.querySelector('#search_input');
var src_clsico = document.querySelectorAll('i');
var th = document.querySelectorAll('th');
var td = document.querySelectorAll('td');
var li = document.querySelectorAll('li');
var tot = document.querySelector('#tot');
var sun = document.getElementById('sun_icon');
var moon = document.getElementById('moon_icon');
var li_src = document.querySelectorAll('.list-group-item');


var Mode = localStorage.getItem('Mode');

const enableNight = () => {

    loader.classList.add('loader_night');
    body.classList.add('body_night');
    src_div.classList.add('search_input_night');
    src_in.classList.add('search_input_night');
    sun.style.display = "block";
    moon.style.display = "none";
    for (let i = 0; i < src_clsico.length; i++)
        src_clsico[i].classList.add('tot_night');

    for (let i = 0; i < th.length; i++)
        th[i].classList.add('tdthli_night');

    for (let i = 0; i < td.length; i++)
        td[i].classList.add('tdthli_night');

    for (let i = 0; i < li.length; i++)
        li[i].classList.add('tdthli_night');

    tot.classList.add('tot_night');
    localStorage.setItem('Mode', 'enable');

}


const disableNight = () => {

    loader.classList.remove('loader_night');
    body.classList.remove('body_night');
    src_div.classList.remove('search_input_night');
    src_in.classList.remove('search_input_night');
    sun.style.display = "none";
    moon.style.display = "block";
    for (let i = 0; i < src_clsico.length; i++)
        src_clsico[i].classList.remove('tot_night');

    for (let i = 0; i < th.length; i++)
        th[i].classList.remove('tdthli_night');

    for (let i = 0; i < td.length; i++)
        td[i].classList.remove('tdthli_night');

    for (let i = 0; i < li.length; i++)
        li[i].classList.remove('tdthli_night');

    tot.classList.remove('tot_night');

    for (let i = 0; i < li_src.length; i++)
        li_src[i].classList.remove('ls_dark');
    localStorage.setItem('Mode', null);

}

if (Mode === "enable") {
    enableNight();
}


function SetDayNight() {
    Mode = localStorage.getItem('Mode');
    if (Mode !== 'enable')
        enableNight();
    else
        disableNight();
}