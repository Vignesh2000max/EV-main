var area = document.getElementById('area')

var mys_areas = ['Kuvempu Nagara', 'Srirampura, Alanahalli', 'Bannimantap', 'Bogadi Road',
                    'Boochahalli', 'Chamrajpura', 'Gokulam', 'Hulikere', 'J P Nagar', 'Jantagalli', 'Jayalakshmipuram']
var blore_areas = ['Around Railway Station', 'Begur Kopa Road', 'Doddaballapur Road', 'Electronic City', 'Hebbal',
                    'Hesaraghatta', 'Hoskote', 'Hosur', 'Hosur Road', 'Indiranagar', 'International Airport', 'Jayanagar', 'JP Nagar']
const addOptions = (list) => {
    var select_node = document.createElement('SELECT')
    select_node.setAttribute('name', 'area')
    for(var i=0; i<list.length;i++){
        var node = document.createElement('OPTION')
        node.setAttribute('value', list[i])
        var textchild = document.createTextNode(list[i])
        node.appendChild(textchild)
        select_node.appendChild(node)
        area.appendChild(select_node)
    }
}
const check_city = (val) => {
    area.classList.remove('d-none')
    area.removeChild(area.childNodes[0]);
    if(val == 'mysore'){
        addOptions(mys_areas)
    }
    else if(val == 'bangalore'){
        addOptions(blore_areas)
    }
    else{
        area.classList.add('d-none')
    }
}

document.addEventListener('DOMContentLoaded',function(){
    var u_type = document.getElementById('u_type')
    var fname = document.getElementById('fname')
    var lname = document.getElementById('lname')
    var stname = document.getElementById('station_name')
    var npoints = document.getElementById('num_points') 
    var uname = document.getElementById('uname')
    var email = document.getElementById('email')
    var address = document.getElementById('address')
    var city = document.getElementById('city')
    var state = document.getElementById('state')
    var pin = document.getElementById('pin')
    var contact = document.getElementById('contact')
    var password = document.getElementById('password')
    var con_password = document.getElementById('con_password')
    var btn = document.getElementById('signup-btn')
    var fname_error='First name can not be less han 3 letters',
        lname_error='Last name can not be empty',
        email_error='Invalid Email',
        uname_error='Invalid Username (should contain 5 or more characters)',
        password_error='Password should contain 1 uppercase, 1 number and 1 special character, length between 7 and 15',
        address_error= 'Address Cannot be empty',
        city_error = 'Please choose a city',
        state_error = 'Please choose a state',
        pin_error = 'Please enter proper pin',
        contact_error = 'Invalid Contact',
        cPass_error = 'Password does not match',
        stname_error = 'Invalid station name',
        npoints_error = 'Charge points can not be 0';
    var fname_val, lname_val, stname_val, npoints_val, uname_val, email_val, address_val, city_val, state_val, pin_val, contact_val, password_val, cPass_val;

    const U_NAME_REGEX = /^[A-Za-z0-9_-]*$/;
    const PASS_REGEX = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{7,15}$/;
    const EMAIL_REGEX = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;

    var alertbox = document.getElementById('alert')
    var errors = []
    var hasError = true

    if(hasError){
        btn.setAttribute('disabled','true')
    }

    const textValidation = (input,req) => {
        var req_length = 0
        if(req == 'fname'){
            req_length = 3
        }
        else if(req == 'lname'){
            req_length = 1
        }
        else if(req == 'address' || req == 'stname'){
            req_length = 5
        }
        else if(req == 'notEmpty'){
            req_length = 1
        }

        if(input.length >= req_length){
            return true
        }
        else{
            return false
        }
    }

    const numberValidation = (input,req) => {
        var req_length = 0
        if(req == 'pin' && Number(input)){
            req_length = 6
        }
        else if(req == 'contact' && Number(input)){
            req_length = 10
        }

        else if(req == 'npoints' && Number(input)){
            req_length = 1
        }

        if(input.length == req_length){
            return true
        }
        else{
            return false
        }
    }

    const textPatternValidation = (input,req) =>{
        if(req == 'emailVal'){
            if(EMAIL_REGEX.test(input)){
                return true
            }
            else{
                return false
            }
        }
        else if(req == 'unameVal'){
            if(U_NAME_REGEX.test(input) && input.length >= 5){
                return true
            }
            else{
                return false
            }
        }
        else if(req == "passVal"){
            if(PASS_REGEX.test(input) && input.length >= 7 && input.length <=15){
                return true
            }
            else{
                return false
            }
        }
        else if(req == "con_password"){
            var pass = password.value
            if(input == pass){
                return true
            }
            else{
                return false
            }
        }
    }

    const displayError  =() => {
        alertbox.classList.remove('d-none')
        var error = ''
        for(var i=0; i<errors.length; i++){
            error = error+'<div class="alert alert-danger">'+errors[i]+'</div>'
        }
        alertbox.innerHTML=error

        if(errors.length == 0 && uname_val && email_val && password_val && cPass_val && pin_val && address_val && contact_val && city_val && state_val){
            if(u_type.value == 'manager' && stname_val && npoints_val){
                hasError = false
            }
            else if(u_type.value != 'manager' && fname_val && lname_val){
                hasError = false
            }
        }
        else{
            hasError = true
        }

        if(hasError == false){
            btn.removeAttribute('disabled')
        }
        else{
            btn.setAttribute('disabled','true')
        }
    }

    const removeOutline = (error_type, element) => {
        element.classList.remove('outline')
        var i = errors.indexOf(error_type)
        if(errors[i] == error_type){
            errors.splice(i, 1)
            displayError()
        }
    }

    const setValue = (element) => {
        var val = element.value
        return val
    }
    
    if(u_type.value != 'manager'){
        fname.onkeyup= function (e) {
            fname_val = setValue(fname)
            var val = textValidation(fname_val, "fname")
            if(val == true){
                removeOutline(fname_error, fname)
            }
            else{
                fname.classList.add('outline')
                if(!errors.includes(fname_error)){
                    errors.push(fname_error)
                    displayError()
                }
            }
        };
    
        lname.onkeyup= function (e) {
            lname_val = setValue(lname)
            var val = textValidation(lname_val, "notEmpty")
            if(val == true){
                removeOutline(lname_error, lname)
            }
            else{
                lname.classList.add('outline')
                if(!errors.includes(lname_error)){
                    errors.push(lname_error)
                    displayError()
                }
            }
        };
    }
    else{
        stname.onkeyup= function (e) {
            stname_val = setValue(stname)
            var val = textValidation(stname_val, "stname")
            if(val == true){
                removeOutline(stname_error, stname)
            }
            else{
                stname.classList.add('outline')
                if(!errors.includes(stname_error)){
                    errors.push(stname_error)
                    displayError()
                }
            }
        };

        npoints.onblur= function (e) {
            npoints_val = setValue(npoints)
            var val = numberValidation(npoints_val, "npoints")
            if(val == true){
                removeOutline(npoints_error, npoints)
            }
            else{
                npoints.classList.add('outline')
                if(!errors.includes(npoints_error)){
                    errors.push(npoints_error)
                    displayError()
                }
            }
        };
    }

    uname.onkeyup= function (e) {
        uname_val = setValue(uname)
        var val = textPatternValidation(uname_val, "unameVal")
        if(val == true){
            removeOutline(uname_error, uname)
        }
        else{
            uname.classList.add('outline')
            if(!errors.includes(uname_error)){
                errors.push(uname_error)
                displayError()
            }
        }
    };

    email.onkeyup= function (e) {
        email_val = setValue(email)
        var val = textPatternValidation(email_val.toLowerCase(), "emailVal")
        if(val == true){
            removeOutline(email_error, email)
        }
        else{
            email.classList.add('outline')
            if(!errors.includes(email_error)){
                errors.push(email_error)
                displayError()
            }
        }
    };

    password.onkeyup= function (e) {
        password_val = setValue(password)
        var val = textPatternValidation(password_val, "passVal")
        if(val == true){
            removeOutline(password_error, password)
        }
        else{
            password.classList.add('outline')
            if(!errors.includes(password_error)){
                errors.push(password_error)
                displayError()
            }
        }
    };

    address.onkeyup= function (e) {
        address_val = setValue(address)
        var val = textValidation(address_val, "address")
        if(val == true){
            removeOutline(address_error, address)
        }
        else{
            address.classList.add('outline')
            if(!errors.includes(address_error)){
                errors.push(address_error)
                displayError()
            }
        }
    };

    city.onblur= function (e) {
        city_val = setValue(city)
        var val = textValidation(city_val, "notEmpty")
        if(val == true){
            removeOutline(city_error, city)
            check_city(city_val)
        }
        else{
            city.classList.add('outline')
            if(!errors.includes(city_error)){
                errors.push(city_error)
                displayError()
            }
        }
    };

    state.onblur= function (e) {
        state_val = setValue(state)
        var val = textValidation(state_val, "notEmpty")
        if(val == true){
            removeOutline(state_error, state)
        }
        else{
            state.classList.add('outline')
            if(!errors.includes(state_error)){
                errors.push(state_error)
                displayError()
            }
        }
    };

    pin.onkeyup= function (e) {
        pin_val = setValue(pin)
        var val = numberValidation(pin_val, "pin")
        if(val == true){
            removeOutline(pin_error, pin)
        }
        else{
            pin.classList.add('outline')
            if(!errors.includes(pin_error)){
                errors.push(pin_error)
                displayError()
            }
        }
    };
    
    contact.onkeyup= function (e) {
        contact_val = setValue(contact)
        var val = numberValidation(contact_val, "contact")
        if(val == true){
            removeOutline(contact_error, contact)
        }
        else{
            contact.classList.add('outline')
            if(!errors.includes(contact_error)){
                errors.push(contact_error)
                displayError()
            }
        }
    };

    con_password.onkeyup = function (e) {
        cPass_val = setValue(con_password)
        var val = textPatternValidation(cPass_val, "con_password")
        if(val == true){
            removeOutline(cPass_error, con_password)
        }
        else{
            con_password.classList.add('outline')
            if(!errors.includes(cPass_error)){
                errors.push(cPass_error)
                displayError()
            }
        }
    };

    // TOGGLE SIGNUP & SIGNIN
    var signup = document.getElementById('signup')
    var signin = document.getElementById('signin')
    var toggleBtn_signup = document.getElementById('toggle-signup')
    var toggleBtn_signin = document.getElementById('toggle-signin')
    var signupForm = true
    var signinForm = false

    toggleBtn_signup.onclick = function(e) {
        signupForm = !signupForm
        signinForm = !signinForm
        signup.classList.remove('d-none')
        signin.classList.add('d-none')
        toggleBtn_signup.classList.add('active')
        toggleBtn_signin.classList.remove('active')
    }

    toggleBtn_signin.onclick = function(e) {
        signupForm = !signupForm
        signinForm = !signinForm
        signup.classList.add('d-none')
        signin.classList.remove('d-none')
        toggleBtn_signup.classList.remove('active')
        toggleBtn_signin.classList.add('active')
    }
})

document.getElementById('search_city').onblur = function(e) {
    console.log("on blur")
    check_city(document.getElementById('search_city').value) 
}