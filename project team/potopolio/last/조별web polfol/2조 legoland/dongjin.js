

var hidden=document.getElementById('section_footer_div3');
var hidden_div=document.getElementById('section_footer_div2_button');
var switch1=true;

hidden_div.addEventListener('click',visivility,true);

function visivility(){
    if (switch1){
        hidden.style.display='inline-block';
        switch1=false;
    }
    else{
        hidden.style.display='none';
        switch1=true;
    }
}



var up_nav=document.getElementById('up-nav');
var nav_links=document.getElementsByClassName("nav-links");
var upper=document.getElementsByClassName('mobile');

window.onresize=function (){
    var innerWidth=window.innerWidth;
    if(innerWidth<=750){0
        up_nav.style.display='none';
        nav_links[0].style.display='none';
        mobile();
    }
    else{
        up_nav.style.display='block';
        nav_links[0].style.display='flex';
        upper[0].style.display="none";
    }
}
function mobile(){
    for (i=0;i<upper.length;i++){
        upper[i].style.display='flex';
    }
}
document.getElementsByClassName("mobile")[0].addEventListener("click",click_upper,false);

var classname_upper=['high','middle','low'];

function click_upper(){
    console.log(upper[0].children.length);
    for(i=0;0<upper[0].children.length;i++){
        upper[0].children[i].className=classname_upper[i]
    }
}

// function create(){
//     var newdiv=document.createElement('div');
//     newdiv.setAttribute("id","mobile_div");
//     var newdiv1=document.createElement('div');
//     newdiv1.setAttribute("id","mobile_div2");
//     var text1;

//     text1="이용권<div class='mobile_div1'>1일 이용권<br>1일 이용권 구매하기<br>연간 이용권<br>연간 이용권 구매하기<br>방문 예약하기<br>공식 채널 구매 티켓 방문 예약하기<br>온라인 티켓 환불 접수</div>";
//     text1+="즐길거리<div class='mobile_div1'>Toggle Navigation<br>테마 파크<br>라이드 & 어트랙션<br>쇼핑<br>다이닝<br>엔터테인먼트</div>";
//     text1+="LEGOLAND® 호텔<div class='mobile_div1'>LEGOLAND® 호텔<br>Thmed room<br>Services & Amenities<br>Dining<br>BEd & Brick</div>";
//     text1+="LEGOLAND®를 200% 즐기는 방법<div class='mobile_div1'>방문 전 확인 사항<br>방문 예약하기<br>운영 시간<br>주차 & 오시는 길<br>COVID - 19 방역지침에 따른 파크 이용 안내<br>보안 관련 안내 사항<br>이용 가이드<br>편의 시설 안내<br>Park Map<br>장애인 편의 제도<br>LEGOLAND Moblie App_KR<br>리조트 분실물 운용 관리<br>자주 묻는 질문 FAQ</div>";
//     text1+="<div>기업 문의<br>학단 문의<br>Jobs</div>";
//     newdiv1.innerHTML=text1;
//     newdiv.appendChild(newdiv1);
//     document.getElementById('header').appendChild(newdiv);
// }

var map=document.getElementById("section_map_img");



function map_open(obj){
    if(obj.value=="Map Open"){
        obj.value="Map Close";
        map.id="section_map_img_open";
    }
    else if (obj.value=="Map Close"){
        obj.value="Map Open";
        map.id="section_map_img";
    }
}

