

let b1=document.getElementById("t1bt1")
let b2=document.getElementById("t1bt2")




let jdiv1= document.getElementById("jd1")
let jdiv2= document.getElementById("jd2")


b1.addEventListener('click',s1divf);

// console.log(jdiv1.display)

function s1divf(e)  {
    // console.log(jdiv1.display)
    jdiv1.style.display= "inline-block";
    jdiv2.style.display= "none";
    b1.style.display= "inline-block";
    b2.style.display= "inline-block";

}

b2.addEventListener('click',s1divf2);

function s1divf2(e)  {
    jdiv1.style.display= "none";
    jdiv2.style.display= "inline-block";
    b1.style.display= "inline-block";
    b2.style.display= "inline-block";

}




let jp2d22 =document.getElementById("p2d22")

let jp2d33= document.getElementById("p2d33")






// p2b2=document.getElementById("t1bt5").onclick= function (e){

//     for( let i=0; i<jp2d33.children.length; i++)
//     {
//         setInterval( Mleft() ,16)
//     }

//  }

// p2b1=document.getElementById("t1bt3").onclick= function(e) {
    
//     for( let i=0; i<jp2d33.children.length; i++)
    
//     {
//         jp2d22.children[i].left-= jp2d22.children[i].clientWidth ;
//         console.log(jdiv2)
//         // setInterval( Mleft() ,16)
//     }

// }




let p2b1=document.getElementById("t1bt3")
// p2b1.addEventListener('click', Mleft);

let p2b2=document.getElementById("t1bt5")
// p2b2.addEventListener('click', Mleft);

let jdd1=document.getElementById("jdd1")
let jdd2=document.getElementById("jdd2")
let jdd3=document.getElementById("jdd3")
let jdd4=document.getElementById("jdd4")


let res = 0;


// function Mleft() {
   
//         res += 2;
//         // jp2d22.style.left = res + "px";
//         jdd1.style.left =330+ res + "px";
//         jdd2.style.left =330+ res + "px";
//         jdd3.style.left =330+ res + "px";
//         jdd4.style.left =330+ res + "px";
//         console.log(jdd4.style.left)
        
//         console.log(jdd4.style.left.split("px")[0])
   
//         if (jdd1.style.left.split("px")[0]> 1290)
//         {      
    
//         jdd1.style.left = 345+ "px"
//         // jdd1.style.left = 25+ "%"
//         // jdd1.style.left +=res+"px";
    
//         }
    
//         if (jdd2.style.left.split("px")[0]> 990)
//         {      
    
//         // jdd2.style.left = 86+"px"
//         jdd2.style.left = 5+"%"
//         }
       
//         if (jdd3.style.left.split("px")[0]> 750)
//         {      
    
//         // jdd3.style.left =-171+"px"
//         jdd3.style.left =-15+"%"
       
//         }
    
//         if (jdd4.style.left.split("px")[0]> 500)
//         {      
    
//         // jdd4.style.left = -430+"px"
//         jdd4.style.left = -35+"%"
       
//         }
// }



// let a= setInterval( Mleft ,16)



// // if (jp2d22.style.left== jp2d22.style.maxwidth)
// //         {   
            
            
// //             jp2d22.style.left==innerWidth 
// //         }



var slides = document.getElementById("slides1");
console.log( slides)
var slideImg = slides.children
console.log(slideImg)

let currentIdx = 0;
var slideCount = slideImg.length;
var prev = document.getElementById("prev1");
var next = document.getElementById("next1");
slideWidth = 1000;
slideMargin = 100;

makeClone();
initfunction();

function makeClone(){
  let cloneSlide_first = slideImg[0].cloneNode(true); //slideImg.firstElementChild.cloneNode(true);
  let cloneSlide_last = slides.lastElementChild.cloneNode(true);
  slides.append(cloneSlide_first); 
  slides.insertBefore(cloneSlide_last,slides.firstElementChild);
}

function initfunction(){
  slides.style.width = (slideWidth + slideMargin) * (slideCount+2) + "px";
  slides.style.left = -(slideWidth + slideMargin) + "px";
}

next.addEventListener('click', function () {
  if (currentIdx <= slideCount-1) {
    slides.style.left = -(currentIdx+2) * (slideWidth+slideMargin) + "px";
    slides.style.transition = '0.5s ease-out';  /* + 0.5 */
  }if (currentIdx === slideCount-1){
    setTimeout(function(){
      slides.style.left = -(slideWidth + slideMargin) + "px";
      slides.style.transition = `${0}s ease-out`;
    },500);
    currentIdx = -1;
    } 
    currentIdx+=1;
  }
);

prev.addEventListener('click', function () {
  console.log(currentIdx);
    if (currentIdx >= 0) {
      slides.style.left = -(currentIdx) * (slideWidth + slideMargin) + "px";
      slides.style.transition = '0.5s ease-out';
    }if (currentIdx === 0){
      setTimeout(function(){
        slides.style.left = -(slideCount) * (slideWidth + slideMargin)+ "px";
        slides.style.transition = '0.5s ease-out';
      },500);
      currentIdx=slideCount;
      } 
      currentIdx-=1;
    }
);


