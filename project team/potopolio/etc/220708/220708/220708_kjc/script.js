// 준철JS
// 네비바에서 메뉴화면으로 전환하기


// 960px ~ 1440px 모바일 -> 모니터
window.onresize = function() {
    if (matchMedia("screen and (min-width:960px) and (max-width:1440px)").matches)
    {
        if (switchScreen == 1)
        {
            moveToMain();
        }
    }
}

switchScreen=0;
function moveToNav(){
    let menuIcons = document.getElementById("myInfo");
    let dis = document.getElementById("screen1");
    let app = document.getElementById("mobile1");
    if (switchScreen == 0)
    {
        switchScreen += 1;
        dis.classList.add("none");
        app.classList.remove("none");
        app.classList.remove("mobile_icon2");
        menuIcons.children[0].classList.add("none");
        menuIcons.children[1].classList.add("none");
        menuIcons.children[2].classList.add("none");
        menuIcons.children[3].classList.remove("mobile_icon1");
        menuIcons.children[3].classList.add("none");
        menuIcons.children[4].classList.remove("none");
    }
}
function moveToMain() {
    let menuIcons = document.getElementById("myInfo");
    let dis = document.getElementById("screen1");
    let app = document.getElementById("mobile1");
    if (switchScreen == 1)
    {
        switchScreen = 0;
        dis.classList.remove("none");
        app.classList.add("none");
        app.classList.add("mobile_icon2");
        menuIcons.children[0].classList.remove("none");
        menuIcons.children[1].classList.remove("none");
        menuIcons.children[2].classList.remove("none");
        menuIcons.children[3].classList.remove("none");
        menuIcons.children[3].classList.add("mobile_icon1");
        menuIcons.children[4].classList.add("none");
    }
}

let plusMinusT = false;

function openMobileNav(obj) {
    if (plusMinusT == false)
    {
        let plus1 = obj.children[0];
        let plus2 = obj.children[1];
        
        plus1.style.transform = 'rotate(-180deg)';
        plus2.style.transform = 'rotate(180deg)';
        plusMinusT=true;
    }
    else
    {
        closeMobileNav(obj);
        openMobileNav(obj);
    }
}
function closeMobileNav(obj) {
    let mySiblings = obj.parentNode.children
    for (let i=0; i < mySiblings.length; i++)
    {
        let babies = mySiblings[i].children;
        babies[0].style.transform = 'rotate(0deg)';
        babies[1].style.transform = 'rotate(90deg)';
    }
    plusMinusT = false;
}