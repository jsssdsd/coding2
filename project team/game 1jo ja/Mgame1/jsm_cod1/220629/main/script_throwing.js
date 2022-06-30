
const canvas_projtil = document.getElementById("canvas_projtil");
// const img = new Image();
const ctx_projtil = canvas_projtil.getContext("2d");

let M_array=[];
let Chr_array=[];
let projtil_array=[];


class GM_Monster{

    constructor(Gm_Mon_where,Gm_Mon_size,Gm_Mon_speed){
        this.Gm_Mon_where= Gm_Mon_where;
        this.Gm_Mon_size= Gm_Mon_size;
        this.Gm_Mon_speed= Gm_Mon_speed;

}

}
function GM_Monster_makingR()
{

    ctx.beginPath();
    for( let i= 0; i<5; i++){
       
        M_array= ctx.rect(800+60*i,600,50,50);
       
    }
    ctx.strokeStyle = "magenta" ;
    // ctx.strokeStyle.zIndex = 6;
    ctx.stroke();



}


let GM_Monster1_where= 5;
let GM_Monster1__size =10;
let GM_Monster1_speed = 10; 


let GM_Monster1 = new GM_Monster(GM_Monster1_where,GM_Monster1__size,GM_Monster1_speed);
// GM_Monster1.GM_Monster_makingR();
console.log(GM_Monster1);
setTimeout(GM_Monster_makingR,500);
//Monster=================================================== 



class GM_US_chr {
    
    constructor(GM_US_chr_distance,GM_US_chr_size,GM_US_chr_speed){
 this.GM_US_chr_distance= GM_US_chr_distance;
 this.GM_US_chr_size= GM_US_chr_size;
 this.GM_US_chr_speed= GM_US_chr_speed;
    }

   

}

function GM_Chr_makingR()
{

    ctx.beginPath();
    for(let i= 0; i<1; i++){
       
        Chr_array= ctx.rect(cx+20*i,cy,50,50);
       
    }
  
    ctx.strokeStyle = "magenta" ;
    // ctx.strokeStyle.zIndex = 6;
    ctx.stroke();
    const img = new Image();
    // ctx.img.src="chr_n1.gif";

}

let GM_US_chr_distance1= 5;
let GM_US_chr_size1 =10;
let GM_US_chr_speed1 = 10; 
let cx= 500;
let cy= 600;
let GM_US_chr1= new GM_US_chr(GM_US_chr_distance1,GM_US_chr_size1,GM_US_chr_speed1)

   setTimeout(GM_Chr_makingR,500);



//user=================================================== 
let missileRadius = 5;
let missileX;
let missileY;
let isCharging = false;
let isFired = false;
let isHitted = false;
let gauge = Math.PI;
const gaugeDIF = Math.PI / 60;
const gaugeBarRadius = 30;
let missilePower;
let missileDx;
let missileDy;
const GRAVITY_ACCELERATION = 0.098;


let user_key1 =0;
let dx = 0;
let dy = 0;
let fx =0;
let fy =0; 

window.onkeydown = (e) => console.log(e, e.keyCode);
window.addEventListener("keydown", function (e){GM_US_projectile_shoot(e)}, false);    

function drawBall(){
    ctx_projtil.beginPath();
    ctx_projtil.arc(fx, fy, 20, 0, Math.PI*2);
    ctx_projtil.fillStyle = "#0095DD";
    
    }
function draw() {
    ctx_projtil.clearRect(0, 0, canvas.width, canvas.height);
    fx=cx+25;
    fy=cy+25;
    drawBall();
    ctx_projtil.fill();
    ctx_projtil.closePath();
    cx += dx; //dx x축 이속
    cy += dy; //dx y축 이속
    } 



class projectil_Sh{
constructor(isFired , isHitted,isCharging,gauge,missilePower){
this.isFired=isFired;
this.isHitted=isHitted;
this.isCharging=isCharging;
this.gauge=gauge;
this.missilePower=missilePower;
}

 drawBall(){
    
    ctx_projtil.beginPath();
    ctx_projtil.arc(fx, fy, 20, 0, Math.PI*2);
    ctx_projtil.fillStyle = "#0095DD";
    
    }
 draw() {
    ctx_projtil.clearRect(0, 0, canvas.width, canvas.height);
    fx=cx+25;
    fy=cy+25;
    drawBall();
    ctx_projtil.fill();
    ctx_projtil.closePath();
    cx += dx; //dx x축 이속
    cy += dy; //dx y축 이속
    } 
}

function  GM_US_projectile_shoot(e)
    {
       
            if(e.keyCode == 39)  {//오른쪽

               
                dx+=projecti_speed;
                dy= 0;
              
            }
            else if(e.keyCode == 37) {  //왼쪽
               
             
                dx-=projecti_speed;
                dy= 0;
              
              
            }
            else if(e.keyCode == 38) {  //위쪽
                
                dx= 0;
                dy-= projecti_speed;
                // setInterval(draw,10)
            }
            else if(e.keyCode == 40) {  //아래
               
                dx=0;
                dy+=projecti_speed;
               
            }
            else if(e.keyCode == 32) {  //스페이스바 
                projtil_array= setInterval(draw,10)
                isFired=true;
                
            }


        }



class GM_US_projectile {
    
     constructor(Gm_US_projt_x,Gm_US_projt_y,Gm_US_projt_angle,Gm_US_projt_speed){
     this.Gm_US_projt_x= Gm_US_projt_x;
     this.Gm_US_projt_y= Gm_US_projt_y;
     this.Gm_US_projt_angle= Gm_US_projt_angle;
     this.Gm_US_projt_speed= Gm_US_projt_speed
        }
        
    
     
        }
    
    
    




let projecti_x= cx;
let projecti_y =cy;
let projecti_angle = 5; 
let projecti_speed = 1; 

let projecti1 = new GM_US_projectile(projecti_x,projecti_y,projecti_angle,projecti_speed);

console.log(projecti1);

//projecti1.GM_US_projectile_shoot();

// setInterval(draw, 10);

// function draw() {
    
//     //drawBricks();
//     //drawBall();
//     //drawPaddle();
//     //drawScore();
//     //collisionDetection();
// }

