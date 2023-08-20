window.onload = ()=>{
    let links = document.querySelectorAll(".navbar .navbar-nav li a");
let navbar_btn_open = document.querySelector(".navbar .open");
let navbar_btn_close = document.querySelector(".navbar .close");

navbar_btn_open.onclick = ()=>{
    navbar_btn_close.style = "display:block";
    navbar_btn_open.style = "display:none";
}
navbar_btn_close.onclick = ()=>{
    navbar_btn_close.style = "display:none";
    navbar_btn_open.style = "display:block";
}
links.forEach(
    (ele) => {
        ele.onclick = ()=>{
            // delete active
            links.forEach(
                (ele)=>{
                     ele.classList.remove("active");
                }
            );
            // active new link
           ele.classList.add("active");
        }
    }
);1


// scrolling

let section = document.querySelector(".sec1");
let navbar = document.querySelector(".navbar");
let navDropDown = document.querySelector(".drop-profile ul");
let navDropLink = document.querySelectorAll(".drop-profile ul li a");

// go up btn and other when scroll
let btnUp = document.createElement("button");
let btnTxt = document.createTextNode("UP");
btnUp.appendChild(btnTxt);
btnUp.className = "btnUp";
document.body.appendChild(btnUp);
btnUp.style.cssText = "display:none;background-color: black;position: fixed;bottom: 20px;right: 20px;padding: 5px 10px;color: #fff;border: 0;cursor: pointer;border-radius:10px;font-size:1.3em";
btnUp.innerHTML = '<i class="fa-solid fa-circle-arrow-up"></i>'

window.onscroll = function(){
    if(window.scrollY >= section.offsetTop+70){
        navbar.style = "box-shadow: 0 0 20px #181f2b;position: fixed;width:100%;z-index:999;background-color:rgba(34, 34, 34, 0.85)";
        btnUp.style.cssText = "display:block;background-color: black;position: fixed;bottom: 20px;right: 20px;padding: 5px 10px;color: #fff;border: 0;cursor: pointer;border-radius:10px;font-size:1.3em";
        if(navDropDown){
                  navDropDown.style = "background-color:rgba(34, 34, 34, 0.85);";
            for(let i =0; i < navDropLink.length; i++){
                navDropLink[i].style = 'color:#fff';
            }  
        }

    }
    if(window.scrollY < section.offsetTop+70){
        navbar.style = "box-shadow: 0";
        btnUp.style.cssText = "display:block";
        if(navDropDown){
            navDropDown.style = "background-color:#fff;";
            for(let i =0; i < navDropLink.length; i++){
                navDropLink[i].style = 'color:#000';
            }
        }
    }
}
btnUp.onclick = ()=>{
    window.scrollTo({
        top:0,
        behavior: 'smooth'
    });
}


var typed = new Typed('#text', {
    strings: ['> Web Developer', '> Full Stack', '> Django Developer'],
    typeSpeed: 50,
    backSpeed:100,
    backDelay:1000,
    loop:true
});


// Aos

const observer = new IntersectionObserver(
    (entries)=>{
        entries.forEach(
            (entry)=>{
                if(entry.isIntersecting){
                    entry.target.classList.add('show');
                }/*else{
                    entry.target.classList.remove('show');
                }*/
            }
        );
    }
);

const hiddenElement = document.querySelectorAll('.hidden');
hiddenElement.forEach(
    (el)=>{
        observer.observe(el)
    }
);

}



// comment more
let moreBtn = document.querySelectorAll(".user-comment .more-comment");
let moreCommentDiv = document.querySelectorAll(".more-content");
moreBtn.forEach((e)=>{
    e.addEventListener("click", (ele)=>{
        moreCommentDiv.forEach((e)=>{
            e.classList.remove("active");
        });
        e.nextElementSibling.classList.add("active");
    });
    
});

document.addEventListener("click",(ele)=>{
    if(ele.target.id == "more-i" || ele.target.id == "more-btn"){
    }else{
        moreCommentDiv.forEach((e)=>{
            e.classList.remove("active");
        });
    }
});


// project imgs
let sectionView = document.querySelector(".section-view");
let sectionDivImg = document.querySelectorAll(".section-view .imgs-div .img");
let nextBtn = document.querySelector(".section-view .next");
let prevBtn = document.querySelector(".section-view .prev");
if(sectionView){
    // view project action
    let viewBtns = document.querySelectorAll(".data-pro .view-project");
    let exitProjectView = document.querySelector(".section-view .exit-project");
    viewBtns.forEach((e)=>{
        e.onclick = ()=>{
            sectionView.style = "display:flex;opacity:1;";
            sectionView.style.transform = "translateX(0%)";
        }
    });
        exitProjectView.onclick = function(){
            sectionView.style = "display:flex;opacity:0;";
            sectionView.style.transform = "translateX(-100%)";
        };
    
    let counter = 1;
    setInterval(()=>{
        document.querySelector(".img-counter h3").innerHTML = `${counter}/${sectionDivImg.length}`;
    },1);
    nextBtn.addEventListener("click",()=>{
        let activeNow = document.querySelector(".section-view .imgs-div .img.active");
        sectionDivImg.forEach((e)=>{
            e.classList.remove("active");
        });
        if(counter < sectionDivImg.length){
            counter++;
            activeNow.nextElementSibling.classList.add("active");
        }else{
            sectionDivImg[0].classList.add("active");
            counter = 1;
        }
    });
    prevBtn.onclick = ()=>{
        let activeNow = document.querySelector(".section-view .imgs-div .img.active");
        sectionDivImg.forEach((e)=>{
            e.classList.remove("active");
        });
        if(counter > 1){
            counter--;
            activeNow.previousElementSibling.classList.add("active");
        }else{
            sectionDivImg[sectionDivImg.length-1].classList.add("active");
            counter = sectionDivImg.length;
        }
    }
}

// search
// let searchOpen = document.querySelector('.search');
// let searchForm = document.querySelector('.search-form');
// let searchClose = document.querySelector('.search-form .close');
// let openSearchMobile = document.querySelector(".open-search-mobile");
// searchOpen.onclick = ()=>{
//     searchForm.style.transform = "translateY(0%)";
// }
// openSearchMobile.onclick = ()=>{
//     searchForm.style.transform = "translateY(0%)";
// }
// searchClose.onclick = ()=>{
//     searchForm.style.transform = "translateY(-100%)";
// }
projectImgs = [];
let viewProject = document.querySelectorAll(".view-project");

viewProject.forEach((e)=>{
    e.addEventListener("click",(ele)=>{
        var projectId = ele.target.dataset.id;
        projectData(projectId);
    });
});

function projectData(projectId){
    var url = '/view_project/';

    fetch(url, {
        method: "POST",
        headers: {
            'content-type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body: JSON.stringify({'projectId':projectId})
    })

    .then((Response)=>{
        return Response.json()
    })

    .then((data)=>{
        dataCome = data.split(',');
        let proImgs = document.querySelectorAll('.section-view img');
        for(let i=0 ;i <proImgs.length; i++){
            proImgs[i].src = `/images/${dataCome[i]}`;
        }
    })
}

function getToken(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  const csrftoken = getToken('csrftoken');

