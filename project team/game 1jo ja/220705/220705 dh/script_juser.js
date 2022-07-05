// 상수 선언 (변하지 않는 객체들)
const canvas = document.getElementById("canvas");
const img = new Image();
const img1 = new Image();
const ctx = canvas.getContext("2d");
const canvasUser = document.getElementById("canvasUser");
const ctxUser = canvasUser.getContext("2d");
const myDiv = document.getElementById("canvasDiv");
const canvasBall = document.getElementById("canvasBall");
const ctxBall = canvasBall.getContext("2d");
const input = document.getElementById('input');
const button = document.getElementById('button');
const startImg = document.getElementById('img');
const endingCredit = document.getElementById('ending-credit');
const screenBlur = document.getElementById('screen-blur');
img.src="background/순수배경.png";
let myGround = new Array(2);

// 변수 선언
let imgCenterX;
let imgCenterY;
let c=0;
let que;
let userFrame;
let score = 0;
let totalTime = 0;
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
					// console.log(userImg[i]);
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
				if (user.y >= 600)
				{
					ctxUser.clearRect(0,0,canvas.width,canvas.height);
					ctxUser.drawImage(userImg[countFrame],canvas.width/2-60,canvas.height-126-65-(user.y-600));
					countFrame+=1;
					if (countFrame==userImg.length)
					{
						countFrame=0;
					}
					userFrame=window.requestAnimationFrame(function(){ animatedUser() })
				}
				else
				{
				ctxUser.clearRect(0,0,canvas.width,canvas.height);
				ctxUser.drawImage(userImg[countFrame],canvas.width/2-60,canvas.height-126-65);
				countFrame+=1;
				if (countFrame==userImg.length)
				{
					countFrame=0;
				}
				userFrame=window.requestAnimationFrame(function(){ animatedUser() })
				}
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
				if (user.y >= 600)
				{
					ctxUser.drawImage(userImg[countFrame],canvas.width/2-60-dis,canvas.height-126-65-(user.y-600));
				}
				else
				{
					ctxUser.drawImage(userImg[countFrame],canvas.width/2-60-dis,canvas.height-126-65);
				}
				countFrame+=1;
				if (countFrame==userImg.length)
				{
					countFrame=0;
				}
				userFrame=window.requestAnimationFrame(function(){ animatedUser() })
			}
		}

		userFrame=window.requestAnimationFrame(function(){ animatedUser() })

	}
	// 점프 함수
	jump(startY)
	{
		let t=0;
		function _jump()
		{
			user.y = startY+user.jumpV*t - 1/2 * 50 * t**2;
			t+=0.15;
			
			if (user.y < 0)
			{
				arrowUp = false;
				user.y = 0;
				myGround[0]=undefined;
				myGround[1]=undefined;
				clearInterval(que);
			}
			// 낙하순간 체크
			else if (user.jumpV < 50 * t)
			{
				// 지형물 객체 검수
				for (let i =0; i< cloudArr.length; i++)
				{
					// x 좌표 필터
					if (user.x >= cloudArr[i].x1 && user.x <= cloudArr[i].x2 )
					{
						// y 좌표 필터. Interval 주기를 고려해서 오차값 범위 내
						if(590 <= Math.floor(user.y) && 610 >= Math.floor(user.y))
						{
							arrowUp = false;
							user.y = 600;
							myGround[0]=cloudArr[i].x1;
							myGround[1]=cloudArr[i].x2;
							clearInterval(que);
						}
					}
				}
				// 지형물 객체 검수
				for (let i =0; i<groundArr.length; i++)
				{
					// x 좌표 필터
					if (user.x >= groundArr[i].x1 && user.x <= groundArr[i].x2 )
					{
						// y 좌표 필터. Interval 주기를 고려해서 오차값 범위 내
						if(285 >= Math.floor(user.y) && 265 <= Math.floor(user.y))
						{
							arrowUp = false;
							user.y = 275;
							myGround[0]=groundArr[i].x1;
							myGround[1]=groundArr[i].x2;
							clearInterval(que);
						}
					}
				}
			}
		}
		que = setInterval(_jump,16)
	}
}


// 투사체 클래스 객체 정의
let x = 10;
let ballImg = new Array();
let url;
let countFrame=0;


class Ball
{
	constructor(x,y,arrow,action,attacked) {
		this.x = x;
		this.y = y;
		this.arrow = arrow;
		this.speed = 16;
		this.normalUrl = "atk/thr/";
		this.attackedUrl = "atk/attacked/";
		this.action=action;
		this.attacked=attacked;
		// this.action="normal1";
		// this.action1="normal1";
		// this.attacked="attacked";
		// this.attacked1="attacked1";
		//for  문으로 세팅한다.

	
		// this.attackUrl = "Chick/Chick-attack/";
		// this.deadUrl = "Chick/Chick-dead/";
	// 	ani(action)
	// {
		// let ballImg = new Array();
		// let url;
		// let countFrame=0;
		if (this.action == "normal")
		{
			url = this.normalUrl;
			if (user.arrow == "right")
			{
				url = url.substring(0,url.length);
				
				for (let i=0; i<4; i++)
				{
					ballImg[i] = new Image();
					ballImg[i].src=url+i+".gif";
					// console.log('ballImg는',ballImg[i]);
				}
			}
			else
			{
				url = url.substring(0,url.length);
				for (let i=0; i<4; i++)
				{
					ballImg[i] = new Image();
					ballImg[i].src=url+i+".gif";
					// console.log('ballImg는',ballImg);
				}
			}
		}

		else if (this.action == "normal1")
		{
			url = this.attackedUrl;
			if (user.arrow == "right")
			{
				url = url.substring(0,url.length+1);
				// url += "R/"
				for (let i=0; i<8; i++)
				{
					ballImg[i] = new Image();
					ballImg[i].src=url+i+".gif";
					// console.log('ballImg는',ballImg[i]);
				}
			}
			else
			{
				for (let i=0; i<8; i++)
				{
					ballImg[i] = new Image();
					ballImg[i].src=url+i+".gif";
					// console.log('ballImg는',ballImg);	
				}

			}
		}

		//맞았을때 투사체 이미지 설정 

		if (this.attacked == "normal")
		{
			url = this.normalUrl;
			if (user.arrow == "right")
			{
				url = url.substring(0,url.length);
				
				for (let i=0; i<4; i++)
				{
					ballImg[i] = new Image();
					ballImg[i].src=url+i+".gif";
					// console.log('ballImg는',ballImg[i]);
				}
			}
			else
			{
				url = url.substring(0,url.length);
				for (let i=0; i<4; i++)
				{
					ballImg[i] = new Image();
					ballImg[i].src=url+i+".gif";
					// console.log('ballImg는',ballImg);
				}
			}
		}

		else if (this.attacked == "normal1")
		{
			url = this.attackedUrl;
			if (user.arrow == "right")
			{
				url = url.substring(0,url.length+1);
				// url += "R/"
				for (let i=0; i<8; i++)
				{
					ballImg[i] = new Image();
					ballImg[i].src=url+i+".gif";
					// console.log('ballImg는',ballImg[i]);
				}
			}
			else
			{
				for (let i=0; i<8; i++)
				{
					ballImg[i] = new Image();
					ballImg[i].src=url+i+".gif";
					// console.log('ballImg는',ballImg);	
				}

			}
		}






	}
	
	

		adraw() {
			
			if (user.x <= 3200-640 && user.x >= -3200+640)

			{
				//draw("normal") 이렇게 실행함
				if (user.y >= 600)
				{

					// context.clearRect(0, 0, canvas.width, canvas.height);
					// console.log(user.x,user.y);
					// ctxBall.beginPath();
					// ctxBall.arc(650+x, 150, 1220, 0, Math.PI * 2, false);
					// ctxBall.closePath();
					// ctxBall.fill();
					// x += 2;
					

					ctxBall.drawImage(ballImg[countFrame],canvas.width/2 +this.x-(user.x),
					canvas.height - this.y + 600 - 120);
					countFrame+=1;
					if (countFrame==ballImg.length)
						{
							countFrame=0;
						}
						// window.requestAnimationFrame(function(){ adraw })
						// window.requestAnimationFrame(function(){ adraw() })
				}
				else
	
				{
					
				
					ctxBall.drawImage(ballImg[countFrame],canvas.width/2 + this.x-(user.x) ,
					canvas.height - this.y + user.y - 130);
					countFrame+=1;
					if (countFrame==ballImg.length)
						{
							countFrame=0;
						}
						// window.requestAnimationFrame(function(){ adraw() })
						// window.requestAnimationFrame(function(){ adraw })
				}
	
			}
			else if (user.x > 3200-640)
			{
				if (user.y >= 600)
				{
					// ctxBall.clearRect(0,0,canvas.width,canvas.height);	
					ctxBall.drawImage(ballImg[countFrame],canvas.width/2 + this.x -3200+640 ,
					canvas.height - this.y + 600 - 130);
					countFrame+=1;
					if (countFrame==ballImg.length)
						{
							countFrame=0;
						}
						// window.requestAnimationFrame(function(){ adraw() })
						
				}
				else
				{
					// ctxBall.clearRect(0,0,canvas.width,canvas.height);
					ctxBall.drawImage( ballImg[countFrame],canvas.width/2 + this.x -3200+640 ,
					canvas.height - this.y + user.y - 130);
					countFrame+=1;
					if (countFrame==ballImg.length)
						{
							countFrame=0;
						}
						// window.requestAnimationFrame(function(){ adraw() })
				}
			
			}
			else if (user.x > 3200-640)
			{
				if (user.y >= 600)
				{
					// ctxBall.clearRect(0,0,canvas.width,canvas.height);
					ctxBall.drawImage( ballArr[countFrame],canvas.width/2 + this.x +3200-640 ,
					canvas.height - this.y + 600 - 130);
					countFrame+=1;
					if (countFrame==ballImg.length)
						{
							countFrame=0;
						}
						// window.requestAnimationFrame(function(){ adraw() })
				}
				else
				{
					// ctxBall.clearRect(0,0,canvas.width,canvas.height);
					ctxBall.drawImage(ballArr[countFrame],canvas.width/2 + this.x +3200-640 ,
					canvas.height - this.y + user.y - 130);
					countFrame+=1;
					if (countFrame==ballImg.length)
						{
							countFrame=0;
						}
						// window.requestAnimationFrame(function(){ adraw() })
				}
				
			}
			// window.requestAnimationFrame(function(){ adraw })
			if (this.arrow == "right")
			{
			this.x += this.speed;
		}
		else
		{
			this.x -= this.speed;
		}
		// window.requestAnimationFrame(function(){ adraw() })
		
	

		}
		// console.log('ballImg는',ballImg[i]);
		 
	}

// 유저 객체 생성
const user= new User(10,  0 , 0);
const ball1  =new Ball(10,2);



// 맵 세팅 시 설정되는 것들.
function setting() {
	makeGround();
	user.draw("normal");
	button.visibility = 'visible';
	// ball1.action="normal";
	// ballArr[i].action("normal");
	// ballArr[c].ani("normal");
	}

// div 이벤트 추가
myDiv.addEventListener("keydown", moveUserKeyDown );
myDiv.addEventListener("keyup", moveUserKeyUp );

// 키 다운 변수 선언
let arrowLeft = false;
let arrowRight = false;
let arrowUp = false;
let arrowDown = false;
let toggleDown = false;
let modX;
let spaceDown = false;
let ballCnt = 0;
let ballArr = new Array();

// 키 다운 함수 호출
function moveUserKeyDown(e) {
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
		startY=user.y;
		user.jump(startY);
	}
	// 스페이스바
	if (spaceDown==false && e.code=="Space")

	// ballq= new Ball(2,3,3,"fdfd","fdfd");
	// console.log(ballq);
	
	{	
		// eval("Ball"+ballCnt+"= new Ball("+user.x+","+user.y+",'"+user.arrow+"');");
		eval("Ball"+ballCnt+"= new Ball("+user.x+","+user.y+",'"+user.arrow+"','normal1','normal');");
		//위에서 바꾸면 된다 충알 객체를 개꿀!!!
		// console.log(Ball0);
		ballArr[ballCnt] = eval("Ball"+ballCnt);
		// ballArr[ballCnt].ani("normal");
		ballCnt+=1;
	
		spaceDown=true;
		setTimeout(function(){
			spaceDown=false;
		},16);
		console.log(ballArr)
		

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
		if (user.y >= 600)
		{
			ctx.drawImage(img, imgCenterX+user.x, imgCenterY-600, canvas.width, canvas.height, 0, 0, canvas.width, canvas.height);
		}
		else
		{
			ctx.drawImage(img, imgCenterX+user.x, imgCenterY-user.y, canvas.width, canvas.height, 0, 0, canvas.width, canvas.height);
		}

	}
	// 맵 경계선 제어
	else
	{
		if (user.x > 3200-640)
		{
			if (user.y >= 600)
			{
				ctx.drawImage(img, imgCenterX+3200-640, imgCenterY-600, canvas.width, canvas.height, 0, 0, canvas.width, canvas.height);
			}
			else
			{
				ctx.drawImage(img, imgCenterX+3200-640, imgCenterY-user.y, canvas.width, canvas.height, 0, 0, canvas.width, canvas.height);
			}
		}
		else if (user.x < -3200+640)
		{
			if (user.y >= 600)
			{
				ctx.drawImage(img, imgCenterX-3200+640, imgCenterY-600, canvas.width, canvas.height, 0, 0, canvas.width, canvas.height);
			}
			else
			{
				ctx.drawImage(img, imgCenterX-3200+640, imgCenterY-user.y, canvas.width, canvas.height, 0, 0, canvas.width, canvas.height);
			}
		}
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
			if (user.y >= 600)
			{
				ctxGround.drawImage(this.groundImg, canvas.width/2+this.x1-user.x , canvas.height-126-(this.y-600));
			}
			else
			{
				ctxGround.drawImage(this.groundImg, canvas.width/2+this.x1-user.x , canvas.height-126-(this.y-user.y));
			}
		}
		else
		{
			if (user.x > 3200-640)
			{
				if (user.y >= 600)
				{
					ctxGround.drawImage(this.groundImg, canvas.width/2+this.x1-3200+640 , canvas.height-126-(this.y-600));
				}
				else
				{
					ctxGround.drawImage(this.groundImg, canvas.width/2+this.x1-3200+640, canvas.height-126-(this.y-user.y));
				}
			}
			else if (user.x < -3200+640)
			{
				if (user.y >= 600)
				{
					ctxGround.drawImage(this.groundImg, canvas.width/2+this.x1+3200-640 , canvas.height-126-(this.y-600));
				}
				else
				{
					ctxGround.drawImage(this.groundImg, canvas.width/2+this.x1+3200-640, canvas.height-126-(this.y-user.y));
				}
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

// 지형 클래스 객체를 요소로 가지는 배열을 이용해 그려준다.
function moveGround(){
	ctxGround.clearRect(0,0,canvas.width,canvas.height);
	for (let i=0; i<groundArr.length;i++)
	{
		groundArr[i].draw();
	}
	for (let i=0; i<cloudArr.length;i++)
	{
		cloudArr[i].draw();
	}
}

// y값 고정 풀기 및 고정
function modY() {
	if (myGround[0]==undefined)
	{
	}
	else
	{
		// 2단에서 밖으로 나가면
		if (user.y == 275)
		{
			if (user.x < myGround[0] || user.x > myGround[1])
			{
				arrowUp=true;
				let t=0;
				function a()
				{
					user.y -= 1/2 * 50 * t**2;
					t+=0.02;
					if (user.y < 0)
					{
						user.y=0;
						arrowUp=false;
						clearInterval(que);
					}
				}
				let que = setInterval(a,16);
			}
		}
		// 3단에서 밖으로 나가면
		else if (user.y == 600)
		{
			if (user.x < myGround[0] || user.x > myGround[1])
			{
				arrowUp=true;
				let t=0;
				function a()
				{
					user.y -= 1/2 * 50 * t**2;
					t+=0.02;
					if (user.y < 0)
					{
						user.y=0;
						arrowUp=false;
						clearInterval(que)
					}
					else
					{
						// 지형물 객체 검수
						for (let i =0; i<groundArr.length; i++)
						{
							// x 좌표 필터
							if (user.x >= groundArr[i].x1 && user.x <= groundArr[i].x2 )
							{
								// y 좌표 필터. Interval 주기를 고려해서 오차값 범위 내
								if(280 >= Math.floor(user.y) && 260 <= Math.floor(user.y))
								{
									arrowUp = false;
									user.y = 275;
									myGround[0]=groundArr[i].x1;
									myGround[1]=groundArr[i].x2;
									clearInterval(que);
								}
							}
						}
					}
				}
				let que = setInterval(a,16);
			}
		}
	}
}

// 공 그려주기
function moveBall() {
	ctxBall.clearRect(0,0,canvas.width,canvas.height);	for (let i = 0 ; i < ballArr.length; i++)
	{
		c+=1;
	//draw("normal") 이렇게 실행함
		ballArr[i].adraw();
		
	}
}






// 동휘님 코드->

const pythonhelloworld = "print('hello world')";
const pythonHelloWorld = 'print("hello world")';
const javascripthelloworld = "console.log('hello world')";
const javascriptHelloWorld =  'console.log("hello world")';

function checkInput (e) {
	const value = e.target.value;
	const keyCode = e.keyCode;
	if(keyCode === 13){
		if(value === pythonhelloworld || value === javascripthelloworld){
			moveToGameScreen();
		}
		else if(value === pythonHelloWorld || value === javascriptHelloWorld){
			moveToGameScreen();
		}		
		else{
			alert("잘못된 입력입니다. \n 1. console.log('hello world') \n 2. print('hello world') \n 중 하나를 입력해주세요!");
			input.value = '';
		}
	}

}

defaultText = ' < GAME START > '.repeat(20); 
textList = [];

for(let i = 0; i < 50; i++){
	const rand = Math.random() * defaultText.length;
	const modifiedText = defaultText.slice(rand, defaultText.length) + defaultText.slice(0, rand);
	textList.push(modifiedText);
}

function drawInitialScreenText() {

	ctx.beginPath();
	ctx.fillRect(0, 0,1280, 720);
	ctx.fillstyle = "black";
	ctx.fill();

	ctx.font = 'bold 36px Arial';

	for(let i = 0; i < textList.length; i++){
		//i가 textlist의 길이인 13보다 작다면?
		ctx.save();
		ctx.translate(100 * i, 0);
		ctx.rotate((Math.PI / 180) * 90);
		ctx.fillStyle = "green";
		ctx.fillText(textList[i], 0, 0);
		ctx.restore();
	}
}

// textList에 있는 모든 텍스트 각각 회전시키는 함수
function rotateInitailScreenText() {
	for(let i = 0; i < textList.length; i++){
		const currentText = textList[i];
		const rotatedText = currentText.slice(-1,currentText.length) + currentText.slice(0, -1);
		textList[i] = rotatedText;
	}
}

// 현재 살아남은 시간을 텍스트로 그리기 위한 함수
// 현재 16ms 마다 draw() 함수가 실행되므로, 함수 호출시마다 16ms씩 더함.
// 현재 구름이 타임텍스트 위로 올라오는 이슈 있음. 구름 그리는 함수가 타임텍스트 그리는 함수 다음으로 실행되야함.

const canvasTimeScore = document.getElementById('canvasTimeScore');
const ctxTimeScore = canvasTimeScore.getContext('2d'); 
ctxTimeScore.font = '36px Helvetica, Arial, sans-serif';

let timeText;
let min;
let sec;

function drawTimeText() { 

	ctxTimeScore.clearRect(0, 0, canvasTimeScore.width, canvasTimeScore.height);

	totalTime += 16;

	min = Math.floor(totalTime / (1000*60))
	sec = Math.floor((totalTime / (1000))%60)

	timeText =  min + ':' + sec;

	ctxTimeScore.fillText(timeText, 600, 50);
}

// 현재 스코어를 텍스트로 그리기 위한 함수
const scoreText = '점수: ' + score;
function drawScoreText() {

	ctxTimeScore.fillText(scoreText, 1100, 50);
 }

// 엔딩크레딧으로 이동 -> 조건 설정 후 이 함수 호출해주면 됨.
function moveToEndingCredit(){

	myDiv.style.display = 'none';
	button.style.display = 'none';
	endingCredit.style.display = 'block';
}

// 전체 인터벌
function draw() {
	// 10점 이상, 10초(10000ms) 이상 시 엔딩크레딧으로 이동
	if(score >= 10 && totalTime >= 10000){
		moveToEndingCredit();
	}

	moveCanvas();
	moveGround();
	modY();
	moveBall();
	drawTimeText();
	drawScoreText();
}

input.addEventListener('keypress', checkInput);

let interval = setInterval(function (){
	drawInitialScreenText();
	rotateInitailScreenText();
}, 150);

// 게임 스크린으로 이동
function moveToGameScreen(){
	// (이미지객체, 이미지객체 내 x 좌표, 이미지객체 내 y좌표, 표현되는 너비, 표현되는 높이, 캔버스 x좌표, 캔버스 y좌표)
	imgCenterX =  img.width/2 - canvas.width/2;	
	imgCenterY = img.height/2;
	ctx.drawImage(img, imgCenterX, imgCenterY, canvas.width, canvas.height, 0, 0, canvas.width, canvas.height);
	setting();

	input.style.display='none'; // 입력 input 제거
	startImg.style.display= 'none'; // 시작 이미지 제거
	button.style.display='block'; // 버튼 표시

	myDiv.focus(); // 게임에 바로 포커스가 가도록

	clearInterval(interval); // 시작화면 interval 제거

	interval = setInterval(draw, 16); // 게임 화면 interval 시작
}

let isGameOver = false;

// 개임 중지/재개
// 현재 점프 중 중지 시 오류
function pauseAndResume() {
	if(interval){
		clearInterval(interval);
		clearInterval(modX);
		clearInterval(que);
		interval = null;
		modX = null;
		que = null;
		window.cancelAnimationFrame(userFrame);
		screenBlur.style.display = 'block';
		button.innerText = '재개';
		myDiv.removeEventListener("keydown", moveUserKeyDown );
		myDiv.removeEventListener("keyup", moveUserKeyUp );
	}else{
		interval = setInterval(draw, 16);
		myDiv.focus();
		myDiv.addEventListener("keydown", moveUserKeyDown );
		myDiv.addEventListener("keyup", moveUserKeyUp );
		button.innerText = '중지';
		screenBlur.style.display = 'none';
	}
}

button.addEventListener('click', pauseAndResume);


// <-