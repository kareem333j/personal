// input required 
let wantedInput = document.querySelectorAll('.wanted');

// django
let usernameRegisterOnly = document.querySelector(".registerUser input");
let numOfusers = document.querySelectorAll(".userNames p").length;
let users = [];
for(let i=0; i<numOfusers;i++){
    users.push(document.querySelectorAll(".userNames p")[i].innerHTML)
}
if(document.querySelector(".userNames")){
    document.querySelector(".userNames").remove();
}
// end django

let formValid = false;
let emailRe = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,9}$/igm;
let usernameRe = /^[A-Za-z][A-Za-z0-9_-]{5,29}$/ig;
let passwordRe = /[\w+\W+\s\S]{8,}/ig;
let emaill = false;
let username = false;
let password = false;

// check for register
wantedInput.forEach((e)=>{
    e.addEventListener("blur",(ele)=>{
        setInterval(function(){
        if(e.value === ""){
            InputError(e);
            e.nextElementSibling.textContent = "this field required";
        }else{
            RemoveInputError(e);
            RemoveInputHelp(e);
        }
        // email check
        if(e.value !== "" && e.id === "emailField"){
            if(emailRe.test(e.value) === true){
                emailRe.test(e.value);
                emaill = true;
            }else{
                e.nextElementSibling.textContent = "email is incorrect";
                InputError(e);
                emaill = false;
            }
        }
        // username check
        if(e.value !== "" && e.id === "username" || e.value !== "" && e.id === "username-login"){
            if(usernameRe.test(e.value) === true){
                usernameRe.test(e.value);
                username = true;
                // django
                for(let i=0; i<users.length;i++){
                    if(users[i] === e.value && e.id === "username"){
                        e.nextElementSibling.textContent = `username already used`;
                        username =false;
                        break;
                    }else{
                        username = true;
                    }

                    
                }
                if(username === false){
                    InputError(e);
                }else{
                    RemoveInputError;
                }
                // end django
            }else{
                if(e.value.length <= 5){
                    e.nextElementSibling.textContent = `Username must be at least 6 characters`;
                }else{
                    let usernameSymbol = /[^\w_-]/ig;
                    e.nextElementSibling.textContent = `"${e.value.match(usernameSymbol)}" Not allowed symbol`;
                }
                InputError(e);
                username = false;
            }
        }
        // password check
        let pass1 = document.getElementById("pass1");
        let pass2 = document.getElementById("pass2");
        if(e.value !== "" && e.id === "pass1" || e.value !== "" && e.id === "pass2"){
            if(passwordRe.test(e.value) === true){
                passwordRe.test(e.value);
                if(pass1.value !== pass2.value){
                    if(pass1.value.length >= 8){
                        pass1.nextElementSibling.textContent = "Password fields not matched";
                    }
                    InputError(pass1);
                    InputError(pass2);
                    password = false;
                }else{
                    password = true;
                    RemoveInputError(pass1);
                    RemoveInputError(pass2);
                    RemoveInputHelp(pass1);
                    RemoveInputHelp(pass2);
                }
            }else{
                e.nextElementSibling.textContent = "Password must be at least 8 characters";
                InputError(e);
                password = false;
            }
        }
        },10);
    });
});

if(document.getElementById('register-form')){
setInterval(function(){
    if(username === true && password === true && emaill === true){
        submitActive(document.getElementById("register-btn"));
    }else{
        submitDisactive(document.getElementById("register-btn"));
    }
}, 10);

    document.getElementById('register-form').onsubmit = ()=>{
    if(username === true && password === true && emaill === true){
        return true;
    }else{
        return false;
    }
    }
}


// action methods

function submitDisactive(e){
    e.style.cssText = "opacity:0.4;cursor: no-drop;";
}
function submitActive(e){
    e.style.cssText = "opacity:1;cursor: pointer;";
}
function InputError(e){
    e.style.cssText = "border: 1px solid red";
    e.nextElementSibling.style.cssText = "color:red";
}

function RemoveInputHelp(e){
    e.nextElementSibling.textContent = "";
    e.nextElementSibling.style.display = "none";
}

function RemoveInputError(e){
    e.style.cssText = "border:1px #dee2e solid;";
}


// msgs
if(document.querySelector("msg")){
    if(document.querySelector("msg").innerHTML === '<i class="fa-regular fa-circle-xmark me-2"></i>{{msg}}'){
        document.querySelector("msg").remove("alert-danger");
        document.querySelector("msg").add("alert-success");
        document.querySelector("msg").innerHTML === '<i class="fa-solid fa-circle-check"></i>Account created successfully';
    }
}