

// @import compass

// @function multiple-box-shadow ($n) 
//   $value: '#{random(2000)}px #{random(20000)}px #FFF'
//   @for $i from 2 through $n
//     $value: '#{$value} , #{random(2000)}px #{random(2000)}px #FFF'

//   @return unquote($value) 

// $shadows-small:  multiple-box-shadow(700)
// $shadows-medium: multiple-box-shadow(200)
// $shadows-big:    multiple-box-shadow(100)

// 별소환 + 별동별







let EsT=null;
let End=null;
let noite;

function init(){

    //estrelas
  
    var style = ["style1", "style2", "style3", "style4"];
    var tam = ["tam1", "tam1", "tam1", "tam2", "tam3"];
    var opacity = ["opacity1", "opacity1", "opacity1", "opacity2", "opacity2", "opacity3"];
  
    function getRandomArbitrary(min, max) {
      return Math.floor(Math.random() * (max - min)) + min;
    }
  
    var estrela = "";
    var qtdeEstrelas = 700;
    // query selector을 쓰면 모든 요소 불러올수 있다.
    noite = document.querySelector(".Constellation");
    var widthWindow = window.innerWidth;
    var heightWindow = window.innerHeight;
  
    for (var i = 0; i < qtdeEstrelas; i++) {
      estrela += "<span class='estrela " + style[getRandomArbitrary(0, 4)] + " " + opacity[getRandomArbitrary(0, 6)] + " "
      + tam[getRandomArbitrary(0, 5)] + "' style='animation-delay: ." +getRandomArbitrary(0, 9)+ "s; left: "
      + getRandomArbitrary(0, widthWindow) + "px; top: " + getRandomArbitrary(0, heightWindow) + "px;'></span>";
    }
  
    noite.innerHTML = estrela;
  
    //meteoros
  
    var numeroAleatorio = 10000;
  
    setTimeout(function(){
      carregarMeteoro();
    }, numeroAleatorio);
  
    function carregarMeteoro(){
      setTimeout(carregarMeteoro, numeroAleatorio);
      numeroAleatorio = getRandomArbitrary(5000, 10000);
      var meteoro = "<div class='meteoro "+ style[getRandomArbitrary(0, 4)] +"'></div>";
      document.getElementsByClassName('chuvaMeteoro')[0].innerHTML = meteoro;
      setTimeout(function(){
        document.getElementsByClassName('chuvaMeteoro')[0].innerHTML = "";
      }, 1000);
    }
  
  }
  
  window.onload = init;



// const canvas = document.getElementById("canvas1");
// const img = new Image();
// const ctx = canvas.getContext("2d");

// ctx.draw

const textArr = [
    // 0
    "print('hello world')",
    "console.log('hello world')",
    // 1
    "for(let i = 0; i < myArr.length; i++)",
    "if (check){ console.log('check') } ",
    // 2
    "while (true) { console.log('newObj' + key); key += 1 }",
    "document.getElementById('LEVEL_3')",
    // 3
    "< GAME > < /GAME >",
    // over
    "< /GAME OVER >"
]

class Text
{
    constructor(x, y, text, speed, font){
        this.x = x;
        this.y = y;
        this.text = text;
        this.speed = speed;
        this.font = font;
    }
    draw()
    {
        ctxBackground.font = this.font;
        if (backgroundMode =="gameOver" )
        {
            ctxBackground.fillStyle="green";
        }
        ctxBackground.fillText(this.text, this.x, this.y);
        this.x += this.speed;
    }
}


const s1= document.getElementById("sd1");
const sinfi1= document.getElementById("ssp1")

// x좌표 y좌표에 랜덤으로 별을 찍는다.  애니매이션이 시작될때마다 
console.log(s1.scrollHeight);


let arayStar =[];   

arayStar.push['star1','star2']

let a= randomNum(0, s1.scrollHeight)


function randomNum(min, max){
    var randNum = Math.floor(Math.random()*(max-min+1)) + min;
    return randNum;


}
console.log(randomNum(0,100));




function r1(min, max){
return Math.floor(Math.random() *(max- min)+min);

}
console.log('랜덤', r1(2,5));


let a1= Math.floor(Math.random() *3)
console.log('a1', a1);
let subJectext= ['Skill','portfolio', 'Career','Profile','Project Ex','Pilosophy'];
const tiT1= document.querySelector('.title1');
var subtext="";
let q1=null;
let bb=null;



const platnh1= document.getElementById("Mercury1a");
const platnh2= document.getElementById("Venus1a");
const platnh3= document.getElementById("earth1a");
const platnh4= document.getElementById("Mars1a");
const platnh5= document.getElementById("Jupiter1a");
const platnh6= document.getElementById("Saturn1a");
const rplat= document.getElementById("AllLua");
const lplat= document.getElementById("AllLua1");


const hover1= document.getElementById("hover1");
const hover2= document.getElementById("hover2");
const hover3= document.getElementById("hover3");
const hover4= document.getElementById("hover4");
const hover5= document.getElementById("hover5");
const hover6= document.getElementById("hover6");

platnh1.addEventListener('mouseover', mouOverP );
platnh2.addEventListener('mouseover', mouOverP );
platnh3.addEventListener('mouseover', mouOverP );
platnh4.addEventListener('mouseover', mouOverP );
platnh5.addEventListener('mouseover', mouOverP );
platnh6.addEventListener('mouseover', mouOverP );

platnh1.addEventListener('mouseleave', mouOutP );
platnh2.addEventListener('mouseleave', mouOutP );
platnh3.addEventListener('mouseleave', mouOutP );
platnh4.addEventListener('mouseleave', mouOutP );
platnh5.addEventListener('mouseleave', mouOutP );
platnh6.addEventListener('mouseleave', mouOutP );

platnh1.addEventListener('click', mouClk1)  
platnh1.addEventListener('click', function() {setTimeout(modalOn, 1300)}, {once : true});
platnh2.addEventListener('click', mouClk1 );
platnh3.addEventListener('click', mouClk1 );
platnh4.addEventListener('click', mouClk1 );
platnh5.addEventListener('click', mouClk1 );
platnh6.addEventListener('click', mouClk1 );

// platnh1.addEventListener("keydown", go)  
// platnh2.addEventListener("keydown", go );
// platnh3.addEventListener("keydown", go );
// platnh4.addEventListener("keydown", go );
// platnh5.addEventListener("keydown", go );
// platnh6.addEventListener("keydown", go );




const lua= document.getElementById("lua");
const lua1= document.getElementById("lua1");
const lua2= document.getElementById("lua2");
const lua3= document.getElementById("lua3");
const lua4= document.getElementById("lua4");
const lua5= document.getElementById("lua5");




function mouOverP(){

// for(let i=0 ; i<subJectext.length; i++)
//     {
      

        if (this==platnh1){

            console.log(subJectext[0])
            subtext= "<span>"+subJectext[0]+"</span>";
            tiT1.innerHTML= subtext;
            lua.classList.add("luah");
        }
        else if (this==platnh2){

            console.log(subJectext[1])
            subtext= "<span>"+subJectext[1]+"</span>";
            tiT1.innerHTML= subtext;
            // hover2.style.display="flex";
            lua1.classList.add("luah");
    
        }
        else if (this==platnh3){
            console.log(subJectext[2])
            subtext= "<span>"+subJectext[2]+"</span>";
            tiT1.innerHTML= subtext;
            lua2.classList.add("luah");
        }

        else if (this==platnh4){
            console.log(subJectext[4])
            subtext= "<span>"+subJectext[3]+"</span>";
            tiT1.innerHTML= subtext;
            lua3.classList.add("luah");
        } 

        else if (this==platnh5){
            console.log(subJectext[4])
            subtext= "<span>"+subJectext[4]+"</span>";
            tiT1.innerHTML= subtext;
            lua4.classList.add("luah");
        }

        else if (this==platnh6){
            console.log(subJectext[5])
            subtext= "<span>"+subJectext[5]+"</span>";
            tiT1.innerHTML= subtext;
            lua5.classList.add("luah");
        }
        else
        {
            subtext+= "<span>Universe</span>";
        }
}

function mouOutP(){

    subtext= "<span>Universe</span>";
    tiT1.innerHTML= subtext;
    hover1.classList.remove("hover11");

    lua.classList.remove("luah");
    lua1.classList.remove("luah");
    lua2.classList.remove("luah");
    lua3.classList.remove("luah");
    lua4.classList.remove("luah");
    lua5.classList.remove("luah");
}



// 모달 click 함수



const modal = document.getElementById("modal")
const modal1 = document.getElementById("modal1")
const modal2 = document.getElementById("modal2")
const modal3 = document.getElementById("modal3")
const modal4 = document.getElementById("modal4")
const modal5 = document.getElementById("modal5")
let aa=null;

// 행성클릭시 이벤트 추가 슈퍼문효과ㄱ
let pRleng =0;
let pg1= document.getElementById('pg1');
let pg2= document.getElementById('pg2');
let pg3= document.getElementById('pg3');

let plengB=0;
let cct=1;
let plengSWM =0;
let plengSw=0;
let pgB=0;

let winsz= document.getElementById("pg1");
let winsz1= getComputedStyle(winsz);
let winsz1w= parseInt(winsz1.width.split("p")[0]);
console.log("winsz1w",winsz1w)



// let pleng=document.getElementById('widthL');
let pleng1=0;
let pleng2=0;
let pleng3=0;
let pleng4=0;
let pleng5=0;

pg1.style.width= plengSw-23+"px";
pg2.style.width= plengSw-23+"px";
pg3.style.width= plengSw-23+"px";
let pgw1=0;
let pg1width1=0;
let pg1width=0;


function mouClk1d1(){
    modalOn();
}


function go(e){

    if (e.keyCode == 39){
        chgNxSi();
    }

    else if (e.keyCode == 37){
        chgBfSi();

    }

    else if (e.keyCode == 27){
        closeEsc();

    }
    }

let inw=null;
let in1=null;
let AllModal= document.querySelector(".Allmodal");



function mouClk1(){

    console.log('클릭')
    inw= window.addEventListener("keydown", (e) => console.log((e)));
    AllModal.style.display="flex";
    AllModal.classList.remove("ModalClose")

    if (this==platnh1){

        pg11s=0
        plengSWM=0;
        plengB =modal.querySelector("#inline");
        plengB1= getComputedStyle(plengB);
        plengSw= parseInt(plengB1.width.split("p")[0]);
        console.log("plengSw",plengSw);

        pgw1 =modal.querySelector("#pg1");
        pg1width=getComputedStyle(pgw1);
        pg1width1= parseInt(pg1width.width.split("p")[0]);
        console.log("pg1width1",pg1width1);

        pleng1= modal.querySelector("#widthL");
        pRleng =pleng1.children.length
        console.log("pRleng",pRleng);
          
        plengSWM= parseInt(plengB1.width.split("p")[0])* pRleng -20;
        console.log("plengSWM",plengSWM);
        pleng1.style.width=plengSWM+"px";
        
        //p1,p2,p3  의값도 나눠줘서 지정해준다. 
    
        modal.classList.remove("ModalClose");

        platnh1.classList.add("big_P");
        lua .classList.add("zind");
        lua1.classList.remove("zind");
        lua2.classList.remove("zind");
        lua3.classList.remove("zind");
        lua4.classList.remove("zind");
        lua5.classList.remove("zind");
        

        End= setTimeout(modalOn, 1300); 
        in1= window.addEventListener("keydown", go);
        rplat.classList.remove("remov")
     }
     
    else if (this==platnh2){
        pg11s=0
        plengSWM=0;
        plengB =modal1.querySelector("#inline");
        console.log(plengB)
        plengB1= getComputedStyle(plengB);
        plengSw= parseInt(plengB1.width.split("p")[0]);
        console.log("plengSw",plengSw);
        pleng1= modal1.querySelector("#widthL");
        pRleng =pleng1.children.length
        console.log("pRleng",pRleng);
          
        plengSWM= parseInt(plengB1.width.split("p")[0])* pRleng -20;;
        pleng1.style.width=plengSWM+"px";

        modal1.classList.remove("ModalClose");

    

        platnh2.classList.add("big_P");
        lua1 .classList.add("zind");
        lua2.classList.remove("zind");
        lua3.classList.remove("zind");
        lua4.classList.remove("zind");
        lua5.classList.remove("zind");

        let q2= setInterval( modalOn1,1300); 
        clearTimeout(End);
        in1= window.addEventListener("keydown", go);
        rplat.classList.remove("remov")
        
    }
  
    else if (this==platnh3){
        pg11s=0
        plengSWM=0;
        plengB =modal2.querySelector("#inline");
        console.log(plengB)
        plengB1= getComputedStyle(plengB);
        plengSw= parseInt(plengB1.width.split("p")[0]);
        console.log("plengSw",plengSw);
        pleng1= modal2.querySelector("#widthL");
        pRleng =pleng1.children.length
        console.log("pRleng",pRleng);
          
        plengSWM= parseInt(plengB1.width.split("p")[0])* pRleng -20;;
        pleng1.style.width=plengSWM+"px";


         modal2.classList.remove("ModalClose");

        //  modal.style.display="none";
        //  modal1.style.display="none";
        //  modal3.style.display="none";
        //  modal4.style.display="none";
        //  modal5.style.display="none";
         
         platnh3.classList.add("big_P");
         lua2 .classList.add("zind");
         lua3.classList.remove("zind");
         lua4.classList.remove("zind");
         lua5.classList.remove("zind");
         lua.classList.remove("zind");
         lua1.classList.remove("zind");
        
         let q3= setInterval( modalOn2,1300); 
        //  aa =setTimeout( modalOn, 1000);
         console.log('aa값',aa);
         in1= window.addEventListener("keydown", go);
         rplat.classList.remove("remov")
         
        }

    else if (this==platnh4){
        pg11s=0
        plengSWM=0;
        plengB =modal3.querySelector("#inline");
        console.log(plengB)
        plengB1= getComputedStyle(plengB);
        plengSw= parseInt(plengB1.width.split("p")[0]);
        console.log("plengSw",plengSw);
        pleng1= modal3.querySelector("#widthL");
        pRleng =pleng1.children.length
        console.log("pRleng",pRleng);
          
        plengSWM= parseInt(plengB1.width.split("p")[0])* pRleng -20;
        pleng1.style.width=plengSWM+"px";


        modal3.classList.remove("ModalClose");

        // modal.style.display="none";
        // modal2.style.display="none";
        // modal1.style.display="none";
        // modal4.style.display="none";
        // modal5.style.display="none";
        

        platnh4.classList.add("big_P");
        lua3 .classList.add("zind");
        lua4.classList.remove("zind");
        lua5.classList.remove("zind");
        lua1.classList.remove("zind");
        lua2.classList.remove("zind");
        // Allmodal.classList.add("zind");

        let q4= setInterval( modalOn3,1300); 
        in1= window.addEventListener("keydown", go);
        rplat.classList.add("remov")
  
    } 

    else if (this==platnh5){
        pg11s=0
        plengSWM=0;
        plengB =modal4.querySelector("#inline");
        console.log(plengB)
        plengB1= getComputedStyle(plengB);
        plengSw= parseInt(plengB1.width.split("p")[0]);
        console.log("plengSw",plengSw);
        pleng1= modal4.querySelector("#widthL");
        pRleng =pleng1.children.length
        console.log("pRleng",pRleng);
          
        plengSWM= parseInt(plengB1.width.split("p")[0])* pRleng -20;
        pleng1.style.width=plengSWM+"px";


        modal4.classList.remove("ModalClose");

        // modal.style.display="none";
        // modal2.style.display="none";
        // modal3.style.display="none";
        // modal1.style.display="none";
        // modal5.style.display="none";
        
        platnh5.classList.add("big_P");
        lua4.classList.add("zind");
        lua5.classList.remove("zind");  
        

        let q5= setInterval(modalOn4, 1300); 
        in1= window.addEventListener("keydown", go);
        rplat.classList.add("remov")
     
       
    }

    else if (this==platnh6){
        plengSWM=0;
        plengB =modal5.querySelector("#inline");
        console.log(plengB)
        plengB1= getComputedStyle(plengB);
        plengSw= parseInt(plengB1.width.split("p")[0]);
        console.log("plengSw",plengSw);
        pleng1= modal5.querySelector("#widthL");
        pRleng =pleng1.children.length
        console.log("pRleng",pRleng);
          
        plengSWM= parseInt(plengB1.width.split("p")[0])* pRleng -20;;
        pleng1.style.width=plengSWM+"px";

        modal5.classList.remove("ModalClose");

        // modal.style.display="none";
        // modal2.style.display="none";
        // modal3.style.display="none";
        // modal4.style.display="none";
        // modal1.style.display="none";
        
        platnh6.classList.add("big_P");
        lua5.classList.add("zind");
        

        let q6= setInterval( modalOn5,1300);
        in1= window.addEventListener("keydown", go);
        rplat.classList.add("remov")
   
    }
  
}
function modalOn() {
    modal.style.display = "flex"
    // EsT= setTimeout(modalOn,1300, Event);

}
function modalOn1() {
    modal1.style.display = "flex"

}

function modalOn2() {
    modal2.style.display = "flex"

}
function modalOn3() {
    modal3.style.display = "flex"

}
function modalOn4() {
    modal4.style.display = "flex"

}
function modalOn5() {
    modal5.style.display = "flex"

}

function isModalOn() {
     modal.style.display = "flex"
}




// 모달 창 끄기 func

const closeBtn = modal.querySelector(".closearea");
const closeBtn1 =modal1.querySelector(".closearea");
const closeBtn2 = modal2.querySelector(".closearea");
const closeBtn3 = modal3.querySelector(".closearea");
const closeBtn4 = modal4.querySelector(".closearea");
const closeBtn5 = modal5.querySelector(".closearea");


closeBtn.addEventListener('click', closeMod);
closeBtn1.addEventListener('click', closeMod);
closeBtn2.addEventListener("click", closeMod);
closeBtn3.addEventListener("click", closeMod);
closeBtn4.addEventListener("click", closeMod);
closeBtn5.addEventListener("click", closeMod);

// platnh1.addEventListener("keydown", go)  
// platnh2.addEventListener("keydown", go );
// platnh3.addEventListener("keydown", go );
// platnh4.addEventListener("keydown", go );
// platnh5.addEventListener("keydown", go );
// platnh6.addEventListener("keydown", go );


function closeEsc()
{

    cct=1
    plengSWM =0;
    pgB=0;
    pleng=0;
    pRleng=0;
    lengSWM=0;
    AllModal.style.display="none";
    modal.classList.add("ModalClose");
    modal1.classList.add("ModalClose");
    modal2.classList.add("ModalClose");
    modal3.classList.add("ModalClose");
    modal4.classList.add("ModalClose");
    modal5.classList.add("ModalClose");

    platnh1.classList.remove("big_P");
    platnh2.classList.remove("big_P");
    platnh3.classList.remove("big_P");
    platnh4.classList.remove("big_P");
    platnh5.classList.remove("big_P");
    platnh6.classList.remove("big_P");
    

}


let Imodal=  document.getElementById("modal")
let Imodal1=  document.getElementById("modal1")
let Imodal2=  document.getElementById("modal2")
let Imodal3=  document.getElementById("modal3")
let Imodal4=  document.getElementById("modal4")
let Imodal5=  document.getElementById("modal5")


function closeMod(){
    cct=1
    plengSWM =0;
    pgB=0;
    pleng=0;
    pRleng=0;
    lengSWM=0;
    
    // AllModal.classList.remove("Allmodal")
    AllModal.style.display="none";

    Imodal.style.display="none";
    Imodal1.style.display="none";
    Imodal2.style.display="none";
    Imodal3.style.display="none";
    Imodal4.style.display="none";
    Imodal5.style.display="none";

    if(this== closeBtn){
        
        modal.classList.add("ModalClose");
        platnh1.classList.remove("big_P");
        // AllModal.style.display="none";
        clearTimeout(End);
        console.log('q0는',End);
        // platnh1.removeEventListener('click', function(){q1=setTimeout(modalOn, 1300)} );
        // 새로고침 함수 location .reload, .시간 ms
        // setTimeout('location.reload()',650); 
    }
    else if(this==closeBtn1){
        modal1.classList.add("ModalClose");
        platnh2.classList.remove("big_P");
        // AllModal.style.display="none";
    }
    else if(this==closeBtn2){

        modal2.classList.add("ModalClose");
        platnh3.classList.remove("big_P");
        
        // bb = window.setTimeout(modal1,1300)
        // clearTimeout(aa);
        // console.log('aa값',aa);    
    }
    else if(this==closeBtn3){

        modal3.classList.add("ModalClose");
        platnh4.classList.remove("big_P");
        
        
    }
    else if(this==closeBtn4){
        modal4.classList.add("ModalClose");
        platnh5.classList.remove("big_P");
        
    
    }
    else if(this==closeBtn5){
        modal5.classList.add("ModalClose");
        platnh6.classList.remove("big_P");
        
    
    }
}






// 다음 이전 슬라이드 


const nextb = modal.querySelector(".next-area");
const nextb1 =modal1.querySelector(".next-area");
const nextb2 = modal2.querySelector(".next-area");
const nextb3 = modal3.querySelector(".next-area");
const nextb4 = modal4.querySelector(".next-area");
const nextb5 = modal5.querySelector(".next-area");

const bfb = modal.querySelector(".before-area");
const bfb1 =modal1.querySelector(".before-area");
const bfb2 = modal2.querySelector(".before-area");
const bfb3 = modal3.querySelector(".before-area");
const bfb4 = modal4.querySelector(".before-area");
const bfb5 = modal5.querySelector(".before-area");

const abB= document.getElementById("mod_before1");
const anB= document.getElementById("mod_next1");

nextb.addEventListener('click', chgNxSi);
nextb1.addEventListener('click', chgNxSi);
nextb2.addEventListener('click', chgNxSi);
nextb3.addEventListener('click', chgNxSi);
nextb4.addEventListener('click', chgNxSi);
nextb5.addEventListener('click', chgNxSi);

bfb.addEventListener('click', chgBfSi);
bfb1.addEventListener('click', chgBfSi);
bfb2.addEventListener('click', chgBfSi);
bfb3.addEventListener('click', chgBfSi);
bfb4.addEventListener('click', chgBfSi);
bfb5.addEventListener('click', chgBfSi);

nextb.addEventListener("keydown", go)  
nextb1.addEventListener("keydown", go );
nextb2.addEventListener("keydown", go );
nextb3.addEventListener("keydown", go );
nextb4.addEventListener("keydown", go );
nextb5.addEventListener("keydown", go );

bfb.addEventListener("keydown", go)  
bfb1.addEventListener("keydown", go );
bfb2.addEventListener("keydown", go );
bfb3.addEventListener("keydown", go );
bfb4.addEventListener("keydown", go );
bfb5.addEventListener("keydown", go );


ml=modal.children.length;
ml1=modal1.children.length;
ml2=modal2.children.length;
ml3=modal3.children.length;
ml4=modal4.children.length;
ml5=modal5.children.length; 

let c=0;

// 여기서 버트인 디펄트2개빼면 contants수 가된다. 

const xP50= document.getElementById("Jupiter1a");
const xM0= document.getElementById("Saturn1a");
// dragup.addEventListener('drag', mouClk1 );
// dragdown.addEventListener('drag', mouClk1 );


function moudragup(){


}


function moudragdown(){


}





// let pg11= plengS.left;

let pg11s=0;

function chgNxSi(obj){

    pg11s=plengSw-3;
    if(cct<pRleng){
        
       
        console.log('pg11s',pg11s);
        // plus크기의 div의 길이, 위치  click 이벤트때마다 변경
        
        // pleng.style.left=-plengSw+ "px";
        pgB-=pg11s;
        pleng1.style.left=pgB+"px";
 
        cct+=1;
        this.classList.remove("blur");
        anB.classList.remove("blur");
        console.log('cct',cct);
         if (cct==pRleng){
        
            this.classList.add("blur");
            anB.classList.add("blur");
            abB.classList.remove("blur");
            console.log('cct',cct);
        }
     }

    else if (cct==pRleng){
        
        this.classList.add("blur");
         anB.classList.add("blur");
         abB.classList.remove("blur");
        console.log('cct',cct);
    }
    // for(let i=0; i<pRleng;i++ ){

    // }
}


function set1(){

    setTimeout(function() {pleng.style.left=-plengSw+ "px"; },{once:true} ,1300) 
}


function chgBfSi(obj){

    pg11s=plengSw-2;
    // 우선 긴 obj의 길이를 정해준다. 
        
        // pg11s=plengSw;
        if(cct>1){
            
            // plus크기의 div의 길이, 위치  click 이벤트때마다 변경
            pgB+=pg11s;
            console.log('pg11s',pg11s);
            
            pleng1.style.left= (pgB+"px");
            // console.log(pleng.style.left);
            cct-=1;

            this.classList.remove("blur");
            bfb.classList.remove("blur");
            
            
            console.log(cct);
            if(cct==1){
                this.classList.add("blur");
                bfb.classList.add("blur");
                nextb.classList.remove("blur");
                console.log('cct',cct);
    
            }
            
        }
        else if(cct==1){
            this.classList.add("blur");
            bfb.classList.add("blur");
            nextb.classList.remove("blur");
            console.log('cct',cct);

        }
        // for(let i=0; i<pRleng;i++ ){
    
    
    
        // }
    }





class drawing
{
    constructor(x, y, text, speed, font){
        this.x = x;
        this.y = y;
        this.text = text;
        this.speed = speed;
        this.font = font;
    }
    draw()
    {
        ctxBackground.font = this.font;
        if (backgroundMode =="gameOver" )
        {
            ctxBackground.fillStyle="green";
        }
        ctxBackground.fillText(this.text, this.x, this.y);
        this.x += this.speed;
    }
}



let cx=0;
let cy=0;
let mpoint = document.getElementById("sd1")
mpoint.addEventListener('click', firefly);


let s1W= document.getElementById("s1");

function firefly() {
    console.log("pageX: ",event.pageX, 
    "pageY: ", event.pageY, 
    "clientX: ", event.clientX, 
    "clientY:", event.clientY)
    // mpoint.classList.add("redF1");

    cx =event.clientX;
    cy =event.clientY;
    


//    Math.floor(Math.random() * (max - min)) + min;

    Math.floor(Math.random() * 100);
    // clientX.draw

   
}



let s1S = getComputedStyle(s1);

let s1SW= parseInt(s1S.width.split("p")[0]);
console.log("s1SW",s1SW)


