const states = [{
        name: 'Andhra Pradesh',
        elem: 'andhrapradesh'
    },
    {
        name: 'Arunachal Pradesh',
        elem: 'arunachalpradesh'
    },
    {
        name: 'Assam',
        elem: 'assam'

    },
    {
        name: 'Bihar',
        elem: 'bihar'
    },
    {
        name: 'Chattisgarh',
        elem: 'chattisgarh'
    },
    {
        name: 'Delhi',
        elem: 'delhi'
    },
    {
        name: 'Goa',
        elem: 'goa'
    },
    {
        name: 'Gujarat',
        elem: 'gujarat'
    },
    {
        name: 'Haryana',
        elem: 'haryana'
    },
    {
        name: 'Himachal Pradesh',
        elem: 'himachalpradesh'
    },
    {
        name: 'Jammu & Kashmir',
        elem: 'jammu&kashmir'
    },
    {
        name: 'Jharkhand',
        elem: 'jharkhand'
    },
    {
        name: 'Karnataka',
        elem: 'karnataka'
    },
    {
        name: 'Kerala',
        elem: 'kerala'
    },
    {
        name: 'Madhya Pradesh',
        elem: 'madhyapradesh'
    },
    {
        name: 'Maharashtra',
        elem: 'maharashtra'
    },
    {
        name: 'Manipur',
        elem: 'manipur'
    },
    {
        name: 'Meghalaya',
        elem: 'meghalaya'
    },
    {
        name: 'Mizoram',
        elem: 'mizoram'
    },
    {
        name: 'Nagaland',
        elem: 'nagaland'
    },
    {
        name: 'Orissa',
        elem: 'orissa'
    },
    {
        name: 'Punjab',
        elem: 'punjab'
    },
    {
        name: 'Rajasthan',
        elem: 'rajasthan'
    },
    {
        name: 'Sikkim',
        elem: 'sikkim'
    },
    {
        name: 'Tamil Nadu',
        elem: 'tamilnadu'
    },
    {
        name: 'Telangana',
        elem: 'telangana'
    },
    {
        name: 'Tripura',
        elem: 'tripura'
    },
    {
        name: 'Uttarakhand',
        elem: 'uttarakhand'
    },
    {
        name: 'Uttar Pradesh',
        elem: 'uttarpradesh'
    },
    {
        name: 'West Bengal',
        elem: 'westbengal'
    },
];


const list = document.getElementById('list')


function setList(group) {
    clearList();
    for (const state of group) {
        const item = document.createElement('li');
        const atag = document.createElement('a');
        item.classList.add('list-group-item');
        if (localStorage.getItem('Mode') === "enable")
            item.classList.add('ls_dark');
        atag.href = state.elem;
        atag.innerText = state.name;
        item.appendChild(atag);
        list.appendChild(item);
    }
    if (group.length === 0) {
        setNoResults();
    }

}

function clearList() {
    while (list.firstChild) {
        list.removeChild(list.firstChild);
    }

}

function setNoResults() {
    const item = document.createElement('li');
    item.classList.add('list-group-item');
    if (localStorage.getItem('Mode') === "enable")
        item.classList.add('ls_dark');
    const text = document.createTextNode('No results');
    item.appendChild(text);
    list.appendChild(item);

}

function getRelevancy(value, searchTerm) {
    if (value === searchTerm)
        return 2;
    else if (value.startsWith(searchTerm))
        return 1;
    else
        return 0;

}

const searchInput = document.getElementById('search_input');

searchInput.addEventListener("input", (event) => {
    let val = event.target.value;
    if (val && val.trim().length > 0) {
        val = val.trim().toLowerCase();
        setList(states.filter(state => {
            return state.elem.includes(val);
        }).sort((elem1, elem2) => {
            return getRelevancy(elem2.elem, val) - getRelevancy(elem1.elem, val);
        }));
    } else {
        clearList();
    }
});