// 준철JS
// 네비바에서 메뉴화면으로 전환하기

// 960px ~ 1440px 모바일 -> 모니터
window.onresize = function() {
    if (matchMedia("screen and (min-width:960px) and (max-width:1440px)").matches)
    {
        // 화면을 늘리면 메인 스크린모니터 화면으로 바꾼다.
        if (switchScreen == 1)
        {
            moveToMain();
        }
    }
    program_bg.style.height = innerHeight + "px";
    program_bg.style.width = innerWidth + "px";
    program_bg.style.backgroundPosition = "70% 0px";
}
// 배경 이미지 설정하기
let program_bg = document.getElementById("program_bg");
program_bg.style.height = innerHeight + "px";
program_bg.style.width = innerWidth + "px";
program_bg.style.backgroundImage = "url(img_src/program-bg-1-tune-up.jpg)"
program_bg.style.backgroundPosition = "70% 0px";
// 클릭하면 섹션이 네비게이션 div로 바뀐다
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
// 클릭하면 섹션이 본문으로 바뀐다.
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


// 토글 애니메이션
let plusMinusT = false;
let sumH;
function openMobileNav(oo) {
    let obj = oo.parentNode;
    let plus1 = obj.children[1];
    let plus2 = obj.children[2];
    let baby = obj.children[3];
    // "-" 된 카테고리 클릭해서 "+"로 만든다
    if(plus1.style.transform == 'rotate(-180deg)')
    {

        plus1.style.transform = 'rotate(0deg)';
        plus2.style.transform = 'rotate(90deg)';
        baby.style.height = "0px";
        plusMinusT=false;

    }
    // "+" 카테고리 클릭해서 "-"로 만든다
    else if (plusMinusT == false)
    {
        plus1.style.transform = 'rotate(-180deg)';
        plus2.style.transform = 'rotate(180deg)';

        sumH = 81*baby.children.length;
        baby.style.height = sumH+"px";
 
        plusMinusT=true;
    }
    // 이미 "-" 된 카테고리를 "+" 로 바꾸고 클릭한 카테고리를 "-"로 바꿈
    else
    {
        if (plusMinusT2==true)
        {
            let closeK = document.getElementsByClassName("m_level2")[1];
            closeMobileNav2(closeK.children[0]);
        }
        closeMobileNav(obj);
        openMobileNav(oo);
    }
}

//  모든 카테고리를 + 로 만들어주는 함수
function closeMobileNav(obj) {
    let mySiblings = obj.parentNode.children
    for (let i=0; i < mySiblings.length; i++)
    {
        let babies = mySiblings[i].children;
        babies[1].style.transform = 'rotate(0deg)';
        babies[2].style.transform = 'rotate(90deg)';
        babies[3].style.height = "0px";
    }
    plusMinusT = false;
}

// 2단 클릭시 함수
let plusMinusT2 = false;
let sumH2;
function openMobileNav2(oo) {
    let obj = oo.parentNode;
    let plus1 = obj.children[1];
    let plus2 = obj.children[2];
    let baby = obj.children[3];
    // "-" 된 카테고리 클릭해서 "+"로 만든다
    if(plus1.style.transform == 'rotate(-180deg)')
    {

        plus1.style.transform = 'rotate(0deg)';
        plus2.style.transform = 'rotate(90deg)';
        baby.style.height = "0px";
        obj.parentNode.style.height = sumH + "px";
        plusMinusT2=false;
    }
    // "+" 카테고리 클릭해서 "-"로 만든다
    else if (plusMinusT2 == false)
    {
        plus1.style.transform = 'rotate(-180deg)';
        plus2.style.transform = 'rotate(180deg)';

        sumH2 = 81*baby.children.length;
        baby.style.height = sumH2+"px";
        obj.parentNode.style.height = sumH + sumH2 + "px";
        console.log(obj.parentNode)
        plusMinusT2=true;
    }
    // 이미 "-" 된 카테고리를 "+" 로 바꾸고 클릭한 카테고리를 "-"로 바꿈
    else
    {
        closeMobileNav2(obj);
        openMobileNav2(oo);
    }
}
function closeMobileNav2(obj) {
    let mySiblings = obj.parentNode.children
    for (let i=0; i < mySiblings.length; i++)
    {
        let babies = mySiblings[i].children;
        babies[1].style.transform = 'rotate(0deg)';
        babies[2].style.transform = 'rotate(90deg)';
        babies[3].style.height = "0px";
    }
    plusMinusT2 = false;
}