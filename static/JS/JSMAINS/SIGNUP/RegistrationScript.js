const v = document.getElementById("mId");

v.style.visibility = `hidden`;

function validation() {
    let mail = document.getElementById("rEmail").value;
    const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (mail.match(pattern)) {
        v.classList.add("valid");
        v.classList.remove("invalid");
        v.style.visibility = 'hidden';
    } else {
        v.classList.add("invalid");
        v.classList.remove("valid");
        v.style.visibility = 'visible';
    }
}

/*const pwl = document.getElementById("pwchecklabel");

  pwl.style.visibility = 'hidden';
  function pwcheck(){
  let pw1 = document.getElementById("pw");
  let pw2 = document.getElementById("cpw");
  if(pw1.value !== pw2.value){
    pwl.style.visibility = 'visible';
    pwl.removeAttribute("name")
  }
  else{
    pwl.style.visibility = 'hidden';
    pwl.className += "valid"
  }

}*/