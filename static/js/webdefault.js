/*
    Name: Bryant Hanks
    Assignment: CS336 Assignment #5b
    Created: 11/13/2022
    Description: javascript file
 */

/**
 * Confirms form input is correct with no conflicting sessions. Calls for error if an error is found
 */
function registrationValidation() {
    if (document.getElementById('b1').checked == true) {
        if(document.querySelector('input[name="day2"]:checked')) {
            //alert("something in Day 2 is selected");
            errorWindow("<p>If you take Difficult Conversations, you cannot take any workshops in Session 2</p>");
        }
        else{
            if(document.getElementById('b3').checked == true) {
                //alert("You cannot take b3 because it required c2. You cannot take c2 because b1 doesn't allow any day2");
                errorWindow("<p>Life Management requires a prerequisite from Session 2.<br>Difficult Conversations conflicts with all workshops in Session 2</p>");
            }
            else {
                //passes validation
                approved();
            }
        }
    }
    else if(document.getElementById('c2').checked == true) {
        if(document.getElementById('b3').checked == true) {
            //This is valid
            approved();
        }
        else{
            //alert("If you take c2, you need to take b3");
            errorWindow("<p>If you take Value of Project Management, you need to take Techniques to Balance Life</p>");
        }
    }
    else if(document.getElementById('b3').checked == true) {
        //alert("You cannot take b3 without c2");
        errorWindow("<p>You cannot take Techniques to Balance Life without Value of Project Management </p>");
    }
    else{
        approved();
    }

}

/**
 * makes a pop up with custom error that is in the middle of the window
 * @param err string that outputs the error to display
 */
function errorWindow(err) {
    const sheet = new CSSStyleSheet();

    let leftBrowserEdge = screenLeft;
    let topBrowserEdge = screenTop;

    let width = 500;
    let height = 400;

    let browserWidth = window.innerWidth;
    let browserHeight = window.innerHeight;

    var left = leftBrowserEdge + ((browserWidth - width) / 2);
    var top = topBrowserEdge + ((browserHeight - height) / 2);

    var windowOptions = ("height=" + height + ",width=" + width + ",top=" + top + ",left=" + left);
    var myWindow = window.open("", "errWindow", windowOptions);

    myWindow.document.writeln("<body bgcolor='#b22222'>" + err + "</body>");
}

/**
 * opens the thankyou.html document with valid submission and creates string value for cookie creation
 */
function approved() {
    const form = document.getElementById('reg');
    let id = "123456";
    //let id = Array.from(form.elements).at(1).value;
    let cookieContents = "|";

    Array.from(form.elements).forEach(element => {
        cookieContents = cookieContents + element.name;
        cookieContents = cookieContents + ":";
        cookieContents = cookieContents + element.value;
        cookieContents = cookieContents + "|";
    });
    cookieContents = cookieContents.substring(33);

    setCookie(id,cookieContents);
    //document.getElementById('reg').action="{{ url_for('thankyou') }}"
}

/**
 * create cookie
 */
function setCookie(name, value){
    document.cookie= name + "=" + value + "; path=/";
}

/**
 * Fills in form if an acceptable cookie is found
 */
function fillIn(){
    let form = document.getElementById('reg');

    let cookieTray = document.cookie.split('; ').map(function(x){
        return x.split("=")
    });

    for(var i = 0; i < cookieTray.length; i++) {
        let theID = Array.from(form.elements).at(1).value;
        if (cookieTray[i][0] == theID) {
            console.log("I found the cookie " + theID);
            let cookieOven = cookieTray[i][1].split("|").map(function (x) {
                return x.split(":")
            })

            for (var j = 0; j < 12; j++) {
                Array.from(form.elements).at(j + 3).value = cookieOven[j][1];
            }
        }

        else {
            console.log("I didn't find the cookie " + theID);
        }
    }
}

/**
 * Load from local storage current votes for the poll
 */
function voteLoad(){
    if(localStorage.getItem('p1') == null){
        setLocal('p1',0);
    }
    if(localStorage.getItem('p2') == null){
        setLocal('p2',0);
    }
    if(localStorage.getItem('p3') == null){
        setLocal('p3',0);
    }
    var spans = document.getElementsByTagName("span");

    spans[0].textContent=" Total Count: " + getLocal('p1');
    spans[1].textContent=" Total Count: " + getLocal('p2');
    spans[2].textContent=" Total Count: " + getLocal('p3');
}

/**
 * sets local storage value
 * @param name - name/id
 * @param value - number of votes
 */
function setLocal (name, value){
    localStorage.setItem(name, value);
}

/**
 * gets local storage value
 * @param name - name/id to look up
 * @returns {number} - this is the numerical value
 */
function getLocal (name){
    let val = +localStorage.getItem(name);
    return val;
}

/**
 * Creates a pop up to state what option was chosen
 */
function poll() {
    var value= document.getElementsByName("award");
    var selectValue=Array.from(value).find(radio => radio.checked);
    var curVal;


    if(selectValue.value == "Pen #1"){
        curVal = getLocal('p1');
        curVal += 1;
        setLocal('p1',curVal);
    }
    if(selectValue.value == "Pen #2"){
        curVal = getLocal('p2');
        curVal += 1;
        setLocal('p2',curVal);
    }
    if(selectValue.value == "Pen #3"){
        curVal = getLocal('p3');
        curVal += 1;
        setLocal('p3',curVal);
    }

    //alert("Thank you for voting for: " + selectValue.value);
}

