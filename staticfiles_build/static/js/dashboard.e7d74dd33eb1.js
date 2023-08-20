let homeBtn = document.querySelector(".nav-item .home");
let dashboardBtn = document.querySelector(".nav-item .dashboard");
homeBtn.classList.remove("active");
dashboardBtn.classList.add("active");

// sidebar
let sidebar = document.querySelector(".sidebar");
let sidebartBtn = document.querySelectorAll(".sidebartBtn");
let navLinks = document.querySelectorAll(".sidebar .nav-pills a");
let section = document.querySelector(".sections");
let sectionForms = document.querySelectorAll(".sections .f");
let navLinks2 = document.querySelectorAll('.dropdown .dropdown-menu a');
sidebartBtn[1].addEventListener("click", function(){
    sidebar.style = "left:-280px";
    section.style.cssText = "width:100%;right:0";
});
sidebartBtn[0].addEventListener("click", ()=>{
    sidebar.style = "left:0;width:280px";
    section.style.cssText = "width:calc(100% - 280px);right:-280px";
});

navLinks.forEach((e)=>{
    e.addEventListener("click", ()=>{
        navLinks.forEach(function(ele){
            ele.classList.remove("active");
        });
        e.classList.add("active");
    });
});
navLinks2.forEach((e)=>{
    e.addEventListener("click", ()=>{
        navLinks2.forEach(function(ele){
            ele.classList.remove("active");
        });
        e.classList.add("active");
    });
});

navLinks[0].onclick = ()=>{
    sectionForms.forEach((e)=>{
        e.style.display = "none";
    });
    sectionForms[0].style.display = "block";
}
navLinks[1].onclick = ()=>{
    sectionForms.forEach((e)=>{
        e.style.display = "none";
    });
    sectionForms[1].style.display = "block";
}
navLinks[2].onclick = ()=>{
    sectionForms.forEach((e)=>{
        e.style.display = "none";
    });
    sectionForms[2].style.display = "block";
}
navLinks[3].onclick = ()=>{
    sectionForms.forEach((e)=>{
        e.style.display = "none";
    });
    sectionForms[3].style.display = "block";
}
navLinks[4].onclick = ()=>{
    sectionForms.forEach((e)=>{
        e.style.display = "none";
    });
    sectionForms[4].style.display = "block";
}
navLinks[5].onclick = ()=>{
    sectionForms.forEach((e)=>{
        e.style.display = "none";
    });
    sectionForms[5].style.display = "block";
}

navLinks2[0].onclick = ()=>{
    sectionForms.forEach((e)=>{
        e.style.display = "none";
    });
    sectionForms[0].style.display = "block";
}
navLinks2[1].onclick = ()=>{
    sectionForms.forEach((e)=>{
        e.style.display = "none";
    });
    sectionForms[1].style.display = "block";
}
navLinks2[2].onclick = ()=>{
    sectionForms.forEach((e)=>{
        e.style.display = "none";
    });
    sectionForms[2].style.display = "block";
}
navLinks2[3].onclick = ()=>{
    sectionForms.forEach((e)=>{
        e.style.display = "none";
    });
    sectionForms[3].style.display = "block";
}
navLinks2[4].onclick = ()=>{
    sectionForms.forEach((e)=>{
        e.style.display = "none";
    });
    sectionForms[4].style.display = "block";
}
navLinks2[5].onclick = ()=>{
    sectionForms.forEach((e)=>{
        e.style.display = "none";
    });
    sectionForms[5].style.display = "block";
}

let globalMsg = document.querySelector('.msg');
globalMsg.style.cssText = "position:absolute;top:0;right:5px;z-index:999";