function scrollWin() {
	// Make all Border Line Colour to #E8E8E8
	document.getElementById("tag_war").innerHTML = ""
	codes = ['ap', 'ar', 'as', 'br', 'cg', 'dl', 'ga', 'gj', 'hr', 'hp', 'jk', 'js', 'ka', 'kl', 'mp', 'mh', 'mn', 'ml', 'mz', 'nl', 'or', 'pb', 'rj', 'sk', 'tn', 'ts', 'tr', 'uk', 'up', 'wb']

	for (let i = 0; i < codes.length; i++) {
		document.getElementById("line_" + codes[i]).style.borderColor = "#E8E8E8";
	}

	var x = document.getElementById("search_input").value;
	if (x === "") {
		// If Search State is NULL Scroll to top
		window.scrollTo(0, 0);
	} else {
		// Convert the Searched State to lowercase to match
		x = x.toLowerCase()
		console.log(x)

		if ("andhra pradesh andhrapradesh ap".includes(x)) {
			document.getElementById("ap").scrollIntoView(true);
			document.getElementById("line_ap").style.borderColor = "#A7D883";
		} else if ("arunachal pradesh arunachalpradesh ar".includes(x)) {
			document.getElementById("ar").scrollIntoView(true);
			document.getElementById("line_ar").style.borderColor = "#A7D883";
		} else if ("assam as".includes(x)) {
			document.getElementById("as").scrollIntoView(true);
			document.getElementById("line_as").style.borderColor = "#A7D883";
		} else if ("bihar br".includes(x)) {
			document.getElementById("br").scrollIntoView(true);
			document.getElementById("line_br").style.borderColor = "#A7D883";
		} else if ("chattisgarh cg".includes(x)) {
			document.getElementById("cg").scrollIntoView(true);
			document.getElementById("line_cg").style.borderColor = "#A7D883";
		} else if ("delhi dl".includes(x)) {
			document.getElementById("dl").scrollIntoView(true);
			document.getElementById("line_dl").style.borderColor = "#A7D883";
		} else if ("goa ga".includes(x)) {
			document.getElementById("ga").scrollIntoView(true);
			document.getElementById("line_ga").style.borderColor = "#A7D883";
		} else if ("gujarat gj".includes(x)) {
			document.getElementById("gj").scrollIntoView(true);
			document.getElementById("line_gj").style.borderColor = "#A7D883";
		} else if ("haryana hr".includes(x)) {
			document.getElementById("hr").scrollIntoView(true);
			document.getElementById("line_hr").style.borderColor = "#A7D883";
		} else if ("himachal pradesh himachalpradesh hp".includes(x)) {
			document.getElementById("hp").scrollIntoView(true);
			document.getElementById("line_hp").style.borderColor = "#A7D883";
		} else if ("jammu and kashmir jk j&k".includes(x)) {
			document.getElementById("jk").scrollIntoView(true);
			document.getElementById("line_jk").style.borderColor = "#A7D883";
		} else if ("jharkhand js".includes(x)) {
			document.getElementById("js").scrollIntoView(true);
			document.getElementById("line_js").style.borderColor = "#A7D883";
		} else if ("karnataka ka".includes(x)) {
			document.getElementById("ka").scrollIntoView(true);
			document.getElementById("line_ka").style.borderColor = "#A7D883";
		} else if ("kerala kl".includes(x)) {
			document.getElementById("kl").scrollIntoView(true);
			document.getElementById("line_kl").style.borderColor = "#A7D883";
		} else if ("madhya pradesh madhyapradesh mp".includes(x)) {
			document.getElementById("mp").scrollIntoView(true);
			document.getElementById("line_mp").style.borderColor = "#A7D883";
		} else if ("maharashtra mh".includes(x)) {
			document.getElementById("mh").scrollIntoView(true);
			document.getElementById("line_mh").style.borderColor = "#A7D883";
		} else if ("manipur mn".includes(x)) {
			document.getElementById("mn").scrollIntoView(true);
			document.getElementById("line_mn").style.borderColor = "#A7D883";
		} else if ("meghalaya ml".includes(x)) {
			document.getElementById("ml").scrollIntoView(true);
			document.getElementById("line_ml").style.borderColor = "#A7D883";
		} else if ("mizoam mz".includes(x)) {
			document.getElementById("mz").scrollIntoView(true);
			document.getElementById("line_mz").style.borderColor = "#A7D883";
		} else if ("nagaland nl".includes(x)) {
			document.getElementById("nl").scrollIntoView(true);
			document.getElementById("line_nl").style.borderColor = "#A7D883";
		} else if ("orissa or".includes(x)) {
			document.getElementById("or").scrollIntoView(true);
			document.getElementById("line_or").style.borderColor = "#A7D883";
		} else if ("punjab pb".includes(x)) {
			document.getElementById("pb").scrollIntoView(true);
			document.getElementById("line_pb").style.borderColor = "#A7D883";
		} else if ("rajasthan rj".includes(x)) {
			document.getElementById("rj").scrollIntoView(true);
			document.getElementById("line_rj").style.borderColor = "#A7D883";
		} else if ("sikkim sk".includes(x)) {
			document.getElementById("sk").scrollIntoView(true);
			document.getElementById("line_sk").style.borderColor = "#A7D883";
		} else if ("tamilnadu tamil nadu tn".includes(x)) {
			document.getElementById("tn").scrollIntoView(true);
			document.getElementById("line_tn").style.borderColor = "#A7D883";
		} else if ("telangana ts".includes(x)) {
			document.getElementById("ts").scrollIntoView(true);
			document.getElementById("line_ts").style.borderColor = "#A7D883";
		} else if ("tripura tr".includes(x)) {
			document.getElementById("tr").scrollIntoView(true);
			document.getElementById("line_tr").style.borderColor = "#A7D883";
		} else if ("uttarakhand uk".includes(x)) {
			document.getElementById("uk").scrollIntoView(true);
			document.getElementById("line_uk").style.borderColor = "#A7D883";
		} else if ("uttarpradesh uttar pradesh up".includes(x)) {
			document.getElementById("up").scrollIntoView(true);
			document.getElementById("line_up").style.borderColor = "#A7D883";
		} else if ("west bengal westbengal wb".includes(x)) {
			document.getElementById("wb").scrollIntoView(true);
			document.getElementById("line_wb").style.borderColor = "#A7D883";
		} else {
			document.getElementById("tag_war").innerHTML = x.concat(" not found!")
		}
		window.scrollBy(0, -100);
		var x = document.getElementById("search_input").value = "";

	}

}

document.addEventListener("keypress", function (event) {
	if (event.keyCode == 13) {
		scrollWin();
	}
});