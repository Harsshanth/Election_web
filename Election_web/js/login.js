var loginno;
var password;

function validate() 
{
    loginno = document.getElementById("loginno").value;
    password = document.getElementById("password").value;
   
    if(loginno=="EC123"&& password=="password")
    {
        window.location.href="user";
       
       console.log("heloo");
        return false;
    }

    else if (loginno==" " || password==" " ){
        alert("Aadhaar or Voter Id are empty");
    }
    else{
        alert("login Failed");
    }
    
}













