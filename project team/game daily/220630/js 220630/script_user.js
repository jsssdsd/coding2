// 상수 선언 (변하지 않는 객체들)
const canvas = document.getElementById("canvas");
const img = new Image();
const ctx = canvas.getContext("2d");

const canvasUser = document.getElementById("canvasUser");
const ctxUser = canvasUser.getContext("2d");

const canvas_projtil = document.getElementById("canvas_projtil");
const ctx_projtil = canvas_projtil.getContext("2d");

const myDiv = document.getElementById("canvasDiv");
img.src="background/순수배경.png";

// 변수 선언
let imgCenterX;
let imgCenterY;
let projtil_array=[];
let projtil_array_x =[];
let projtil_array_y =[];
// 유저 클래스 객체 정의
class User
{
	// 객체 속성 설정
	constructor(life, X, Y)
	{
		this.life = life; // 10
		this.x = X; // 0
		this.y = Y; // 0
		this.normalUrl = "Chick/Chick/";
		this.walkUrl = "Chick/Chick-walk/";
		this.attackUrl = "Chick/Chick-attack/";
		this.deadUrl = "Chick/Chick-dead/";
		this.arrow = "left";
		this.speed = 6;
		this.jumpV = 190;
		this.damage = 1;
	}
	// 공격 받음 함수
	attacked()
	{
		this.life -= 1 ;
	}
	// 움직임 함수
	draw(action)
	{
		let userImg = new Array();
		let url;
		let countFrame=0;
		if (action == "normal")
		{
			url = this.normalUrl;
			if (user.arrow == "right")
			{
				url = url.substring(0,url.length-1);
				url += "R/"
				
				for (let i=0; i<27; i++)
				{
					userImg[i] = new Image();
					userImg[i].src=url+i+".gif";
				}
			}
			else
			{
				for (let i=0; i<27; i++)
				{
					userImg[i] = new Image();
					userImg[i].src=url+i+".gif";
				}
			}
		}
		else if (action == "walk")
		{
			url = this.walkUrl;
			if (user.arrow == "right")
			{
				url = url.substring(0,url.length-1);
				url += "R/"
				for (let i=0; i<20; i++)
				{
					userImg[i] = new Image();
					userImg[i].src=url+i+".gif";
				}
			}
			else
			{
				for (let i=0; i<19; i++)
				{
					userImg[i] = new Image();
					userImg[i].src=url+i+".gif";
				}
			}
		}
		else if (action == "dead")
		{
			url = this.deadUrl;
			for (let i=0; i<16; i++)
			{
				userImg[i] = new Image();
				userImg[i].src=url+i+".gif";
			}
		}
		// 공격모션 보류
		// 키 입력할때마다 모션 초기화 시 버벅임 문제 발생가능성
		else if (action == "attack")
		{
			url = this.attackUrl;
			if (user.arrow == "right")
			{
				url = url.substring(0,url.length-1);
				url += "R/"
				
				for (let i=0; i<27; i++)
				{
					userImg[i] = new Image();
					userImg[i].src=url+i+".gif";
				}
			}
			else
			{
				for (let i=0; i<16; i++)
				{
					userImg[i] = new Image();
					userImg[i].src=url+i+".gif";
				}
			}
		}
		function animatedUser() {
			if (user.x <= 3200-640 && user.x >= -3200+640)
			{
				ctxUser.clearRect(0,0,canvas.width,canvas.height);
				ctxUser.drawImage(userImg[countFrame],canvas.width/2-60,canvas.height-126-65);
				countFrame+=1;
				if (countFrame==userImg.length)
				{
					countFrame=0;
				}
				window.requestAnimationFrame(function(){ animatedUser() })
			}
			else
			{
				let dis;
				if (user.x <= -3200+640)
				{
					dis = -3200+640 - user.x
				}
				else
				{
					dis = 3200-640 - user.x
				}
				ctxUser.clearRect(0,0,canvas.width,canvas.height);
				ctxUser.drawImage(userImg[countFrame],canvas.width/2-60-dis,canvas.height-126-65);
				countFrame+=1;
				if (countFrame==userImg.length)
				{
					countFrame=0;
				}
				window.requestAnimationFrame(function(){ animatedUser() })
			}
		}

		window.requestAnimationFrame(function(){ animatedUser() })

	}
	// 점프 함수
	jump()
	{
		let t=0;
		function _jump()
		{
			user.y = user.jumpV*t - 1/2 * 50 * t**2;
			t+=0.15;
			if (user.y < 0)
			{
				arrowUp = false;
				user.y = 0;
				clearInterval(que);
			}
		}
		let que = setInterval(_jump,16)
	}

	
	shoot()
	{
		let sht=0;
		function _shoot()
		{
			projectil_1.x = user.x
			projectil_1.y= user.y 
			clearInterval(que);
			
		}
		let que = setInterval(_shoot,16)
	}
}

let c=1;
let pt1=0;

class projectil_Sh{
	// constructor(fx,fy,project_n,prot_Rmoving,prot_upmoving,isFired,isHitted,missilePower,prot_Lmoving){
	constructor(fx,fy){		
	this.fx=fx;
	this.fy=fy;
	// this.isFired=isFired;
	this.fx1= fx;
	this.fy1= fy+50;
	// this.isHitted=isHitted;
	// this.missilePower=missilePower;
	// // this.PSinterval= PSinterval;
	
	// this.prot_Lmoving=prot_Lmoving;
	// this.prot_Rmoving=prot_Rmoving;
	// this.prot_upmoving=prot_upmoving;
	// this.project_n=project_n;
	
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
	
	projtil_shting(){
	
		for (let i=0;i<c; i++){
				//for (let i=0; i<1;i+=i) {
				// c=0;	
				// projtil_array=;
				// fx1=user.x;
				console.log(user.x);
				// fy1=user.y;
				// ctxUser.clearRect(0, 0, canvas.width, canvas.height);
				ctx_projtil.beginPath();
				// ctx_projtil.arc(user.x+500, -user.y+600, 20, 0, Math.PI*2);
				if(user.x <= 3200-640 && user.x >= -3200+640)
				{
				ctx_projtil.arc(canvas.width/2+this.fx1-user.x, canvas.height-126-(this.fy1+user.y+10), 20, 0, Math.PI*2);
			
				}	

				else
				{
				if (user.x > 3200-640)
				{
					ctx_projtil.arc(canvas.width/2+this.fx1-32200+640+user.x , canvas.height-126-(this.fy1+user.y+10), 20, 0, Math.PI*2);
				
				}
				else if (user.x < -3200+640)
				{
					ctx_projtil.arc(canvas.width/2+this.fx1+3200-640+32200+640+user.x, canvas.height-126-(this.fy1+user.y+10), 20, 0, Math.PI*2);
				
					
				}

				}
				projtil_array.push(canvas.width/2+this.fx1-user.x);
				projtil_array_x.push(canvas.width/2+this.fx1-user.x);
				projtil_array_y.push(canvas.height-126-(this.fy1+user.y+10));

				
				ctx_projtil.fillStyle = "#0095DD";
				ctx_projtil.fill();
				ctx_projtil.closePath();

				// projtil_array.push(this.fx1-user.x);
				
				// cx += dx;
				// cy += dy;
			
		
			}
			
				// console.log('projtil_array값'+projtil_array);
				console.log('projtil_arrayx값'+projtil_array_x);
				console.log('projtil_arrayy값'+projtil_array_y);
	
	}

	projtil_shting1(){
	

				pt1+= 1;
				console.log(user.x);
				// fy1=user.y;
				// ctxUser.clearRect(0, 0, canvas.width, canvas.height);
				ctx_projtil.beginPath();
				// ctx_projtil.arc(user.x+500, -user.y+600, 20, 0, Math.PI*2);
				if(user.x <= 3200-640 && user.x >= -3200+640)
				{
					ctx_projtil.arc(canvas.width/2-this.fx1+650-user.x , canvas.height+126+(+this.fy1-user.y-900), 20, 0, Math.PI*2);
					
				// ctx_projtil.arc(canvas.width/2+this.fx1-user.x, canvas.height-126-(this.fy+user.y+10), 20, 0, Math.PI*2);
				}	
																			
				
				else
				{
				if (user.x > 3200-640)
				{
					ctx_projtil.arc(canvas.width/2+this.fx1-3200+640, canvas.height-126-(this.fy1+user.y+10), 20, 0, Math.PI*2);
					// ctx_projtil.arc(canvas.width/2+this.fx1-3200+640, canvas.height-126-(this.fy+user.y+10), 20, 0, Math.PI*2);
				
				}
				else if (user.x < -3200+640)
				{
					ctx_projtil.arc(canvas.width/2+this.fx1+3200-640, canvas.height-126-(this.fy1+user.y+10), 20, 0, Math.PI*2);
					// ctx_projtil.arc(canvas.width/2+this.fx1+3200-640, canvas.height-126-(this.fy+user.y+10), 20, 0, Math.PI*2);
			
				}
				}
				ctx_projtil.fillStyle = "#0095DD";
				ctx_projtil.fill();
				ctx_projtil.closePath();
				

				pt1= 0;
				// console.log('pt1값'+pt1);
	
	}

	

}

// function drawcirc(fx,fy,dx,dy) {
// 	//for (let i=0; i<1;i+=i) {
// 	c=0;
// 	projtil_array=null;
// 	ctx_projtil.clearRect(0, 0, canvas.width, canvas.height);
// 	ctx_projtil.beginPath();
// 	ctx_projtil.arc(fx, fy, 20, 0, Math.PI*2);
// 	ctx_projtil.fillStyle = "#0095DD";
// 	ctx_projtil.fill();
// 	ctx_projtil.closePath();

// 	cx += dx;
// 	cy += dy;
// }	



// eval("ground"+i+"= new Ground("+xArr[i]+",320,'"+cat+"')");  이걸로 for문안에서 클래스 객체 생성 가능.
//선택대표 피사체 객체 생성
let fx1=0;
let fy1=0;
let projectil_1 =new projectil_Sh(fx1,fy1);

console.log('projectil_1의값',projectil_1);

// 유저 객체 생성=============================
const user= new User(10,  0 , 0);

// 이미지 로드 시 캔버스 배경 설정
img.onload = function() {
	// (이미지객체, 이미지객체 내 x 좌표, 이미지객체 내 y좌표, 표현되는 너비, 표현되는 높이, 캔버스 x좌표, 캔버스 y좌표)
	imgCenterX =  img.width/2 - canvas.width/2;	
	imgCenterY = img.height/2;
	ctx.drawImage(img, imgCenterX, imgCenterY, canvas.width, canvas.height, 0, 0, canvas.width, canvas.height);
	setting();
}

// 맵 세팅 시 설정되는 것들.
function setting() {
	makeGround();
	makeProjecTT();
	
	user.draw("normal");
}

// div 이벤트 추가
myDiv.addEventListener("keydown", function(e) { moveUserKeyDown(e) } );
myDiv.addEventListener("keyup", function(e) { moveUserKeyUp(e) } );

// 키 다운 변수 선언
let arrowLeft = false;
let arrowRight = false;
let arrowUp = false;
let arrowDown = false;
let toggleDown = false;
let space = false;
let modX;
let cp1 =0;

// 키 다운 함수 호출
function moveUserKeyDown(e) {
	console.log(user.x);
	// 왼쪽 방향키
	if ( arrowRight==false && e.code== "ArrowLeft" )
	{
		arrowLeft = true;
		user.arrow="left";
		if (toggleDown == false)
		{
			user.draw("walk");
			toggleDown = true;
			modX = setInterval(function() { user.x-=user.speed;
				if ( user.x <= -3200 )
				{
					clearInterval(modX);
				} },16);
			
		}
	}
	// 오른쪽 방향키
	else if ( arrowLeft==false && e.code== "ArrowRight" )
	{
		arrowRight = true;
		user.arrow="right";
		if (toggleDown == false)
		{
			user.draw("walk");
			toggleDown = true;
			modX = setInterval(function() { user.x+=user.speed;
				if ( user.x >= 3200 )
				{
					clearInterval(modX);
				} },16);

		}
	}
	// 점프 (위 방향키)
	if( arrowUp==false && e.code=="ArrowUp" )
	{
		arrowUp = true;
		user.jump();
	}

	// space (투사체 )
	if( space==false && e.code=="Space" )
	{ 
	
		space = true;
		user.shoot();
		projectil_1.projtil_shting();
		

		for ( let i = 0; i< projtil_array_x.length; i++ ){

		eval("prjA"+i+"= new projectil_Sh("+projtil_array_x[i]+","+projtil_array_y[i]+")");
		// prjA = eval("prjA"+i);
		
		console.log("prjA0값=" ,prjA0);
		prjA.push(prjA0);

		}


		for (let m=0; m< prjA.length; m++){
		eval("prjB"+m+"= new projectil_Sh("+prjA[m].fx1+","+prjA[m].fy1+")");
		prjB[m] = eval("prjB"+m);
		// console.log("prjB[m]값=" ,prjB[m]);
	
		}

		console.log("prjB값=" ,prjB);
		console.log("prjA길이값="+prjA.length);
		projtil_array_x= [];
		projtil_array_y= [];

		cp1+=1;

		// for (let i = 0; i<projtil_array_x.length; i++)
		// {
		// 	//let cat;
			
		// 	eval("prjA"+i+"= new projectil_Sh("+projtil_array_x[i]+", "+projtil_array_y[i]+")")
		// 	prjA1[i] = eval("prjA"+i);
		// 	console.log("prjA1값="+prjA1[i])
		// 	}
	


		space = false;
	
	}

}

// 키 업 토글 제어 (중복 클릭 방지 기능)
function moveUserKeyUp(e) {

	if ( e.code== "ArrowLeft" )
	{
		arrowLeft = false;
		if (arrowRight==false)
		{
			toggleDown=false;
			user.draw("normal");
			clearInterval(modX);
		}

	}
	else if ( e.code== "ArrowRight" )
	{
		arrowRight = false;
		if (arrowLeft==false)
		{
			toggleDown=false;
			user.draw("normal");
			clearInterval(modX);
		}
	}

}
// 배경 움직임 함수
function moveCanvas() {
	ctx.clearRect(0,0,canvas.width,canvas.height);
	if(user.x <= 3200-640 && user.x >= -3200+640)
	{
		ctx.drawImage(img, imgCenterX+user.x, imgCenterY-user.y, canvas.width, canvas.height, 0, 0, canvas.width, canvas.height);
	}
	// 맵 경계선 제어
	else
	{
		if (user.x > 3200-640)
			ctx.drawImage(img, imgCenterX+3200-640, imgCenterY-user.y, canvas.width, canvas.height, 0, 0, canvas.width, canvas.height);
		else if (user.x < -3200+640)
			ctx.drawImage(img, imgCenterX-3200+640, imgCenterY-user.y, canvas.width, canvas.height, 0, 0, canvas.width, canvas.height);
	}
	
}

// 이미지 url 배열
const imgGroundArr = ["background/눈기둥(지형).png","background/사막기둥(지형).png","background/풀기둥(지형).png"];
// 지형 클래스



class Ground
{
	constructor(X,url)
	{
		this.x1=X;
		this.x2=X+400;
		this.y=275;
		this.url=url;
		
		// 이미지 객체 생성을 반복하면 로딩이 길어지며 깜빡임이 생긴다.
		// 가능한 이미지 객체 생성 및 할당을 반복함수 안에서 호출하면 안된다.
		this.groundImg = new Image();
		this.groundImg.src=this.url;
	}

	draw()
	{
		if(user.x <= 3200-640 && user.x >= -3200+640)
		{
			ctxGround.drawImage(this.groundImg, canvas.width/2+this.x1-user.x , canvas.height-126-(this.y-user.y));
			//,canvas.width/2-60,canvas.height-126-65
		}
		else
		{
			if (user.x > 3200-640)
			{
				ctxGround.drawImage(this.groundImg, canvas.width/2+this.x1-3200+640, canvas.height-126-(this.y-user.y));
			}
			else if (user.x < -3200+640)
			{
				ctxGround.drawImage(this.groundImg, canvas.width/2+this.x1+3200-640, canvas.height-126-(this.y-user.y));
			}
		}
	}
}
// 구름 객체 생성
class Cloud
{
	constructor(X)
	{
		this.x1=X;
		this.x2=X+360;
		this.y=550;
		this.url="background/구름(지형).png";
		
		// 이미지 객체 생성을 반복하면 로딩이 길어지며 깜빡임이 생긴다.
		// 가능한 이미지 객체 생성 및 할당을 반복함수 안에서 호출하면 안된다.
		this.groundImg = new Image();
		this.groundImg.src=this.url;
	}
	draw()
	{
		if(user.x <= 3200-640 && user.x >= -3200+640)
		{
			ctxGround.drawImage(this.groundImg, canvas.width/2+this.x1-user.x , canvas.height-126-(this.y-user.y));
		}
		else
		{
			if (user.x > 3200-640)
			{
				ctxGround.drawImage(this.groundImg, canvas.width/2+this.x1-3200+640, canvas.height-126-(this.y-user.y));
			}
			else if (user.x < -3200+640)
			{
				ctxGround.drawImage(this.groundImg, canvas.width/2+this.x1+3200-640, canvas.height-126-(this.y-user.y));
			}
		}
	}
}
// 지형 랜덤생성 (랜덤 x 값 부여)
// 세팅 함수에 포함시킬것.
const canvasGround = document.getElementById("canvasGround");
const ctxGround = canvasGround.getContext("2d");
// 지형 클래스 객체 배열
let groundArr = [];
let cloudArr = [];


// 지형 클래스 객체 생성 및 최초 출력
function makeGround() {
	// 지형 몇 개 생성 // 4개로 지정
	let randCnt1 = 4;
	let xArr = [];
	
	while(true)
	{
		let t=true;
		for(let i=0; i<randCnt1; i++)
		{
			xArr[i] = Math.floor(Math.random()*(6400-800)-2600);
		}
		for(let i=0; i<xArr.length; i++)
		{
			for(let m=0; m<xArr.length-i; m++)
			{
				if (i == (xArr.length - m - 1))
				{
				}
				else if((xArr[i] - xArr[xArr.length-m-1]) < 400+410 && (xArr[i] - xArr[xArr.length-m-1]) > -400-410 )
				{
					t=false;
				}
				else
				{
				}
			}
		}
		if (t==true)
		{
			break;
		}
	}
	xArr.sort(function(a,b) {
		return a - b;
	});
	for ( let i = 0; i < xArr.length; i++ )
	{
		let cat;
		if (xArr[i]<-1450)
			cat = imgGroundArr[1];
		else if (xArr[i]<1250 && xArr[i]>=-1450)
			cat = imgGroundArr[2];
		else
			cat = imgGroundArr[0];
		eval("ground"+i+"= new Ground("+xArr[i]+",'"+cat+"')");
		groundArr[i] = eval("ground"+i);
		
	}
	console.log(ground1);

	console.log(xArr)
// 구름 지형 만들기
	for (let i=0; i<groundArr.length-1;i++)
	{
		let key = Math.floor(Math.random()*2);
		if (key == 0)
		{
			eval("cloud"+i+"= new Cloud("+groundArr[i].x2+")");
		}
		else
		{
			let key2 = groundArr[i+1].x1-(groundArr[i+1].x2-groundArr[i+1].x1);
			eval("cloud"+i+"= new Cloud("+key2+")");
		}
		cloudArr[i] = eval("cloud"+i);
	}
}
//============================================피사체 어레이 생성및 같이 움직임





// 투척물 클래스 객체 생성 및 최초 출력
// 투척물 몇 개 생성 // 4개로 지정
	// let randCnt1 = 4;
	// let pojtxArr = [];
	// let prjA1 = [];

let prjA = [];
let prjB = [];


function makeProjecTT() {
	while(true)
	{
	let t=true;
	// for(let i=0; i<randCnt1; i++)
	// {
	// 	pojtxArr[i] = Math.floor(Math.random()*(6400-800)-2600);
	// }  생성이니까 난이미 쏠때 생성할꺼라 저장함.
	// let projtil_array

	for(let i=0; i<prjB.length; i++)  //projtil_array_x
	{
		for(let m=0; m<prjB.length-i; m++)
		{
			if (i == (prjB.length - m - 1))
			{ 
			}
			// else if((projtil_array_x[i] - projtil_array_x[prjA.length-m-1]) < 400+410 && (prjA[i] - prjA[prjA.length-m-1]) > -400-410 ) 원본
			else if((prjB[i] - prjB[prjB.length-m-1]) < prjB.fx1+prjB.fx1+10 && (prjB[i] - prjB[prjB.length-m-1]) > -prjB.fx1-prjB.fx1+200 )
			{
				t=false;
			}
			else
			{
			}
		}
	}
	if (t==true)
	
		{
		break;
		}

	}
// projtil_array_x.sort(function(a,b) {
// 	return a - b;
// });


// 	for (let i = 0; i<projtil_array_x.length; i++)
// 	{
// 		//let cat;
		
// 		eval("prjA"+i+"= new projectil_Sh("+projtil_array_x[i]+", "+projtil_array_y[i]+")")
// 		prjA1[i] = eval("prjA"+i);
		
		
// 		console.log("prjA1값="+prjA1)
// 		// eval("prjR"+i+"= new projectil_Sh("+projtil_array_x[i]+", "+projtil_array_y[i]+")")
// 		// prjA1[i] = eval("prjR"+i);
// 		// console.log("prjA1값="+prjA1)
// }
	
	
// prjA0.projtil_shting1();



	

// 지형 클래스 객체를 요소로 가지는 배열을 이용해 그려준다.
function moveGround(){
	ctxGround.clearRect(0,0,canvas.width,canvas.height);
	for (let i=0; i<groundArr.length;i++)
	{
		groundArr[i].draw();
		// console.log(groundArr[i]);
	}
	for (let i=0; i<cloudArr.length;i++)
	{
		cloudArr[i].draw();
	}
}

// function move_projtil(){

// 	// ctx_projtil.clearRect(0,0,canvas.width,canvas.height);
// 	for (let i=0; i<prjA.length;i++)
// 	{
// 		console.log('prjA값=' ,prjA);

// 		prjA[i].projtil_shting1();
// 		// projectil_1.projtil_shting();
// 	}
	
// }

function move_projtil(){

	 ctx_projtil.clearRect(0,0,canvas.width,canvas.height);	
	for (let i=0; i<prjB.length;i++)
	{
		console.log('prjB값=' ,prjB);

		prjB[i].projtil_shting1();
		// projectil_1.projtil_shting();
		
	}

}

function gravity() {
// 	for (let i=0; i<groundArr.length;i++)
// 	{
// 		if (user.x >= groundArr[i].x1 && user.x <= groundArr[i].x2)
// 		{
// 			console.log(1);
// 			arrowUp = false;
// 			user.y = groundArr[i].y;
// 		}
// }
}

// 전체 인터벌
function draw() {
	moveCanvas();
	moveGround();
	move_projtil();
	gravity();
}

setInterval(draw,16);
}