function article_site1 () {
  window.open('https://www.legoland.kr/legoland-%EB%A5%BC-200-%EC%A6%90%EA%B8%B0%EB%8A%94-%EB%B0%A9%EB%B2%95/%EC%9D%B4%EC%9A%A9-%EA%B0%80%EC%9D%B4%EB%93%9C/%ED%8E%B8%EC%9D%98-%EC%8B%9C%EC%84%A4-%EC%95%88%EB%82%B4/', '_blank'); 
}
function article_site2 () {
window.open("https://www.legoland.kr/legoland-%ED%98%B8%ED%85%94/legoland-%ED%98%B8%ED%85%94/","_blank");
}
function article_site3 () {
  window.open("https://www.google.com/maps/search/%EB%A0%88%EA%B3%A0%EB%9E%9C%EB%93%9C/data=!3m1!4b1","_blank");
}
var aaa=true;
window.onload=function(){
  if(window.innerWidth>750)
  aaa=true;
  else if(window.innerWidth<=750)
  aaa=false;
}
window.onscroll = function() {
  if(aaa){
  scroll12(); scroll2(); scroll3();}
  else if (!aaa){
    scroll4();}
  };
window.onresize=function(){
  if(window.innerWidth>750)
  aaa=true;
  else if (window.innerWidth<=750)
  aaa=false;
}
let k=0;
function scroll12 () {
if (400<=document.documentElement.scrollTop && document.getElementById("article_first_img")) {
  document.getElementById("article_first_img").id = "article_first_img2";
  document.getElementById("article_first_text").id = "article_first_text2";
  k++;
}
else if (document.documentElement.scrollTop <400 && document.getElementById("article_first_img2") ) {
  document.getElementById("article_first_img2").id = "article_first_img"; 
  document.getElementById("article_first_text2").id = "article_first_text";
  k--;
}
};

let p=0;
function scroll2 () {
if (1200<=document.documentElement.scrollTop && document.getElementById("article_second_img")) {
  document.getElementById("article_second_img").id = "article_second_img2";
  document.getElementById("article_second_text").id = "article_second_text2";
  p++;
}
else if (document.documentElement.scrollTop <1200 && document.getElementById("article_second_img2") ) {
  document.getElementById("article_second_img2").id = "article_second_img"; 
  document.getElementById("article_second_text2").id = "article_second_text";
  p--;
}
};

let q=0;
function scroll3 () {
  if (1300<=window.scrollY && document.getElementById("article_third_img")) {
    document.getElementById("article_third_img").id = "article_third_img2";
    document.getElementById("article_third_text").id = "article_third_text2";
    q++;
  }
  else if (document.documentElement.scrollTop <1300 && document.getElementById("article_third_img2")) {
    document.getElementById("article_third_img2").id = "article_third_img"; 
    document.getElementById("article_third_text2").id = "article_third_text";
    q--;
  }
};

function scroll4 (){
  var WM=window.matchMedia("screen and (max-width:750px)");
  //var IH=window.innerHeight;
  var HI=window.scrollY;
  if (WM.matches) {
    if (400<=HI && document.getElementById("article_first_img")) {
      document.getElementById("article_first_img").id = "article_first_img2";
      document.getElementById("article_first_text").id = "article_first_text2";
    }
    else if(700 <=HI && document.getElementById("article_second_img")){
      document.getElementById("article_second_img").id = "article_second_img2";
      document.getElementById("article_second_text").id = "article_second_text2";
    }
    else if(900<=HI && document.getElementById("article_third_img")){
      document.getElementById("article_third_img").id = "article_third_img2";
      document.getElementById("article_third_text").id = "article_third_text2";
    }
  }
}


function navigo (){

document.addEventListener('scroll', onScroll, { passive: true });
function onScroll () {
   const scrollposition = pageYOffset;
 const nav = document.querySelector('nav');
 if (1<=scrollposition){
   nav.classList.add('fix')
 }
 else {
   nav.classList.remove('fix');
 }
} 

}
navigo()


const saTriggerMargin = 100;
const saElementList = document.querySelectorAll('.sa');

const saFunc = function() {
for (const element of saElementList) {
  if (!element.classList.contains('show')) {
    if (window.innerHeight > element.getBoundingClientRect().top + saTriggerMargin) {
      element.classList.add('show');
    }
  }
}
}

window.addEventListener('load', saFunc);
window.addEventListener('scroll', saFunc);

window.addEventListener('scroll',function(){scroll1()})

function scroll1(){
  if ((window.scrollY>=145 && document.getElementById('section_footer_div1')) || (window.scrollY>=145 && document.getElementById('section_footer_div1'))){
      document.getElementById('section_footer_div1').id='section_footer_div1_visible';
  }
  else if (window.scrollY<145 && document.getElementById('section_footer_div1_visible')){
      document.getElementById('section_footer_div1_visible').id="section_footer_div1"
  }
}


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






