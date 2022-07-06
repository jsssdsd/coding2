
let canvas_projtil = document.getElementById("canvas_projtil");
// const img = new Image();
ctx_projtil = canvas_projtil.getContext("2d");

// M_array=[];
let Chr_array=[];
let projtil_array=[];
let m1_array=[];

class GM_Monster{

    constructor(Gm_Mon_where,Gm_Mon_size,Gm_Mon_speed,Gm_Mon_N,M_array){
        this.Gm_Mon_where= Gm_Mon_where;
        this.Gm_Mon_size= Gm_Mon_size;
        this.Gm_Mon_speed= Gm_Mon_speed;
        this.Gm_Mon_N=Gm_Mon_N;
        this.M_array= M_array=[];



    }
}




let GM_Monster1 = new GM_Monster(false,false,false,5,false);
mq=[];
function GM_Monster_makingR(x)
{

    ctx.beginPath();


    for(let i= 0; i<=x.Gm_Mon_N; i++){
       
        ctx.rect(800+60*i,600,50,50);
        // m1_array= ctx.rect(800+60*i,600,50,50);
        m2= 800+60*i;
        m3 =50;
        m1_array.push(m2);
        m1_array.push(m3);
        mq.push(m1_array);
    
        console.log('몬스터 배열',m1_array);

    }

    ctx.strokeStyle = "magenta" ;
    // ctx.strokeStyle.zIndex = 6;
    ctx.stroke();

}




// GM_Monster1.GM_Monster_makingR();
console.log(GM_Monster1);   

setTimeout(GM_Monster_makingR(GM_Monster1),500);

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
// let fx =0;
// let fy =0; 
let fx=cx+25;
let fy=cy+25; 

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
let projecti_speed = 3;

let projecti1 = new GM_US_projectile(projecti_x,projecti_y,projecti_angle,projecti_speed);

console.log(projecti1);


// canvas.addEventListener("mousedown", function (e) { Tclk(e) }, false);

let c = 0;

class projectil_Sh{
constructor(fx,fy,prot_Lmoving,prot_Rmoving,prot_upmoving,isFired,isHitted,missilePower,PSinterval){
this.isFired=isFired;
this.isHitted=isHitted;
this.missilePower=missilePower;
this.PSinterval= PSinterval;
this.fx=fx;
this.fy=fy;
this.prot_Lmoving=prot_Lmoving;
this.prot_Rmoving=prot_Rmoving;
this.prot_upmoving=prot_upmoving;

}

Leftmoving() {
    return prot_Lmoving= false;
}

Rightmoving() {
    return prot_Rmoving= false;
}

prot_upmoving() {
    return prot_upmoving= false;
}




    // drawBall(fx,fy) {
    // fx=cx+25;
    // fy=cy+25;   
    // ctx_projtil.beginPath();
    // ctx_projtil.arc(fx, fy, 20, 0, Math.PI*2);
    // ctx_projtil.fillStyle = "#0095DD";
    // ctx_projtil.fill();
    // ctx_projtil.closePath();
    
//    var img1 = new Image (); //이미지 객체 생성
// img1.src = "1.png" ;
//     img1.onload = function () //이미지 로딩 완료시 실행되는 함수
// {
// //(20,20)을 중심으로 100*100의 사이즈로 이미지를 그림 context. drawImage (img,20,20,100,100)
// context. drawImage (img1,fx,fy,100,100)
// }


    draw(fx,fy) {
        //for (let i=0; i<1;i+=i) {
        c=0;
        projtil_array=null;
        ctx_projtil.clearRect(0, 0, canvas.width, canvas.height);
        fx=cx+25;
        fy=cy+25;   
        ctx_projtil.beginPath();
        ctx_projtil.arc(fx, fy, 20, 0, Math.PI*2);
        ctx_projtil.fillStyle = "#0095DD";
        ctx_projtil.fill();
        ctx_projtil.closePath();
      
        cx += dx;
        cy += dy;
        
        for(let i=0; i< M_array ; i++)
        if (this.fx== M_array.x  && this.fy== M_array.y) 
        {
            console.log(Monster)
        }
        
    }

    // projtil_array=null;
   
   
    // // window.addEventListener("keydown", function (e){drawBall(e)}, false);
        // projectil_Sh.drawBall(fx,fy);
 
       // }   
        
       
}






let arrLpt= [];
let arrLpt1= [];

while (projtil_array.length >5) {
    console.log(projtil_array);


}


// for(let i=0; i<= c ; i++){

// projtil_array = new projectil_Sh();

// arrLpt = projtil_array[i].xi
// arrLpt1 = projtil_array[i].yi

// }

let prt_a1 = new projectil_Sh();


prt_a1.Ldraw = function()
{
    console.log("prt_a1값",prt_a1)
    c= c+1;
    for (i=0;i<c; i++){


    function draw(fx,fy,dx,dy) {
        //for (let i=0; i<1;i+=i) {
        c=0;
        projtil_array=null;
        ctx_projtil.clearRect(0, 0, canvas.width, canvas.height);
        fx=cx+25;
        fy=cy+25;   
        ctx_projtil.beginPath();
        ctx_projtil.arc(fx, fy, 20, 0, Math.PI*2);
        ctx_projtil.fillStyle = "#0095DD";
        ctx_projtil.fill();
        ctx_projtil.closePath();
      
        cx += dx;
        cy += dy;
    }

    }
    // if (c=1){
    // projtil_array = new projectil_Sh()
    // }
    //    projtil_array= setInterval(draw,50)
    // return setInterval(prt_a1.draw,100);

    return setInterval( prt_a1.draw,15);

}




window.onkeydown = (e) => console.log(e, e.keyCode);
window.addEventListener("keydown", function (e){GM_US_projectile_shoot(e)}, false);

function GM_US_projectile_shoot(e) {
        
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
            }
            else if(e.keyCode == 40) {  //아래
                dx=0;
                dy+=projecti_speed;
               
            }
            else if(e.keyCode == 32) {  //스페이스바 
                //projtil_array= setInterval(window.addEventListener("keydown", function (e){draw(e)}, false),100);
            //    projtil_array= setInterval(draw,50)  //  여기에 그냥 메서드를 넣는다. 클래스로 만들어서.
            // projtil_array=  

                prt_a1.isFired=true;
                prt_a1.Ldraw();
                let projtsvx= new ObjectManager();
                projtsvx.addObject;

                
                
            }

            // function playerAttack() {
            //     if (keyMap[90]) { // 노멀
            //         userChar.normalBullet();\
            //     }
            // }


}



// normalBullet() {
//     if (this.tickCount % this.initData.bullet.normal.interval == 0) {
//         var bullet = new NormalBullet(this.container, this.x + 70, this.y + 40, this.initData.bullet.normal.speed, 0, this.initData.bullet.normal);
//         objectManager.addObject(bullet);
//     }
// }

 // projectil 투사체 발사=================================================== 
