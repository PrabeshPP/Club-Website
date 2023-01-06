// Working on Custom Authentication

function changeBG(){
    var navBar=document.getElementById("navBar")
    var scrollValue=window.scrollY;
    if(scrollValue>0){
        navBar.classList.add("navBarBgColor")
    }else{
        navBar.classList.remove("navBarBgColor")
    }
}

window.addEventListener('scroll',changeBG);