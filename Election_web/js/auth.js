var aadhaar;
var migrate;
var voterId;
var Party1;
var Party2;
var Party3;


function validate_user() 
{
    aadhaar = document.getElementById("aadhaar").value;
    localStorage.setItem("aadhaar",aadhaar);
    voterId = document.getElementById("voterId").value;
    localStorage.setItem("voterid",voterId);
    voterCode = document.getElementById("voterCode").value;
    if(aadhaar=="832244541320" && voterId=="WJB3457470" && voterCode=="9000" )
    {
        window.location.href="vote";
        return false;
    }
    else if (aadhaar==""||voterId==""|| voterCode==""){
        alert("Aadhaar or Voter Id are empty");
    }
    else{
        alert("login Failed");
    }
    
}















