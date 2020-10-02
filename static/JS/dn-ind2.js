try {
    var mapTag = document.getElementById('map-tag');
} catch (err) {}
var stateName = document.querySelector('.state-name');
var val = document.querySelectorAll('.val');
var lab = document.querySelectorAll('.lab')
var stateBody = document.body;

if (localStorage.getItem('Mode') === "enable") {
    stateBody.style.backgroundColor = "rgb(38, 38, 47)"
    try {
        mapTag.style.color = "white";
    } catch (err) {}
    stateName.style.color = "white";

    for (let i = 0; i < val.length; i++)
        val[i].style.color = "white";
    for (let i = 0; i < lab.length; i++)
        lab[i].style.color = "white";
} else {
    stateBody.style.backgroundColor = "white"
    try {
        mapTag.style.color = "black";
    } catch (err) {}
    stateName.style.color = "black";

    for (let i = 0; i < val.length; i++)
        val[i].style.color = "black";
    for (let i = 0; i < lab.length; i++)
        lab[i].style.color = "black";
}