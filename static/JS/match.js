function scrollWin() 
{
	document.getElementById("tag_war").innerHTML = ""
	document.getElementById("line_ap").style.borderColor="#E8E8E8";
	document.getElementById("line_del").style.borderColor="#E8E8E8";
	document.getElementById("line_kar").style.borderColor="#E8E8E8";
	document.getElementById("line_ker").style.borderColor="#E8E8E8";
	document.getElementById("line_mah").style.borderColor="#E8E8E8";
	document.getElementById("line_pb").style.borderColor="#E8E8E8";
	document.getElementById("line_tn").style.borderColor="#E8E8E8";
	document.getElementById("line_tel").style.borderColor="#E8E8E8";
	document.getElementById("line_up").style.borderColor="#E8E8E8";
	document.getElementById("line_wb").style.borderColor="#E8E8E8";


    var x = document.getElementById("search_input").value;
    if(x === ""){
    	window.scrollTo(0,0);
    	console.log("here")
    }
    else{
    	x = x.toLowerCase()
    	console.log(x)
    	
    	if("andhra pradesh andhrapradesh ap".includes(x))
    	{
    		document.getElementById("ap").scrollIntoView(true);
    		document.getElementById("line_ap").style.borderColor="#A7D883";
    	}
    	else if("delhi".includes(x)){
    		document.getElementById("del").scrollIntoView(true);
    		document.getElementById("line_del").style.borderColor="#A7D883";
    	}
    	else if("karnataka".includes(x)){
    		document.getElementById("kar").scrollIntoView(true);
    		document.getElementById("line_kar").style.borderColor="#A7D883";
    	}
    	else if("kerala".includes(x)){
    		document.getElementById("ker").scrollIntoView(true);
    		document.getElementById("line_ker").style.borderColor="#A7D883";
    	}
    	else if("maharashtra".includes(x)){
    		document.getElementById("mah").scrollIntoView(true);
    		document.getElementById("line_mah").style.borderColor="#A7D883";
    	}
    	else if("punjab".includes(x)){
    		document.getElementById("pb").scrollIntoView(true);
    		document.getElementById("line_pb").style.borderColor="#A7D883";
    	}
    	else if("tamilnadu tamil nadu tn".includes(x)){
    		document.getElementById("tn").scrollIntoView(true);
    		document.getElementById("line_tn").style.borderColor="#A7D883";
    	}
    	else if("telangana".includes(x)){
    		document.getElementById("tel").scrollIntoView(true);
    		document.getElementById("line_tel").style.borderColor="#A7D883";
    	}
    	else if("uttar pradesh uttarpradesh up".includes(x)){
    		document.getElementById("up").scrollIntoView(true);
    		document.getElementById("line_up").style.borderColor="#A7D883";
    	}
    	else if("west bengal westbengal wb".includes(x)){
    		document.getElementById("wb").scrollIntoView(true);
    		document.getElementById("line_wb").style.borderColor="#A7D883";
    	}
    	else{
    		document.getElementById("tag_war").innerHTML = x.concat(" not found!")
    	}
    	window.scrollBy(0, -40);
    	var x = document.getElementById("search_input").value="";

    }

}
