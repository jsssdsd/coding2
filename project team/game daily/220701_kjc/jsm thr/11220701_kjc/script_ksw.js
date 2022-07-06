const canvas = document.getElementById("canvas");
const img = new Image();
const ctx = canvas.getContext("2d");
const canvasMonster = document.getElementById("canvasMonster");
const ctxMonster = canvasMonster.getContext("2d");
img.src="background.png";

img.src="배경.png";
img.onload = function() {
	// (이미지객체, 이미지객체 내 x 좌표, 이미지객체 내 y좌표, 표현되는 너비, 표현되는 높이, 캔버스 x좌표, 캔버스 y좌표)
	ctx.drawImage(img, img.width/2-canvas.width/2, img.height/2, canvas.width, canvas.height, 0, 0, canvas.width, canvas.height)
}

var monsterimgArray1 = ["cat.gif",
"lalala.gif",
"person.gif",
"window.gif"]

var monsterimgArray2 = ["normal.gif",
"Chick.gif"]


class Monster {
constructor (monsterType, monsterHp, monsterX, monsterY, monsterSp, monsterAtk) {
	//프로퍼티
	this.monsterType = monsterType	//몬스터 타입
	this.monsterHp = monsterHp; 	//몬스터 체력
	this.monsterX = monsterX;		//몬스터 x좌표
	this.monsterY = monsterY;		//몬스터 y좌표
	this.monsterSp = monsterSp;	    //몬스터 속도
	this.monsterAtk = monsterAtk;	    //몬스터 공격
/*
	this.normalUrl = "frames/";
	this.walkUrl = "normal.gif";
	this.attackUrl = "attack.gif";
	this.deadUrl = "die.gif";

	this.inquiry = function () {return this.monsterX;}
	this.newX = function() { 
		this.monsterX += 10; 
	}
	this.newX2 = function() { 
		this.monsterX -= 10; 
	}
 
 */
}
 MX() {
	return Number(this.monsterX)
 }
 MY() {
	return Number(this.monsterY)
 }

}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
let count = 0
let count2 = 0
var xArray = [-3300-0,3300-0]
function draw() { //전체함수
function createMonster() { //지상몬스터 생성함수
	// (몬스터이름, 몬스터체력, 몬스터x좌표, 몬스터y좌표, 몬스터스피드, 몬스터공격력)
    makeMonster1 = new Monster('landmonsterN1', '20', xArray[Math.floor(Math.random() * xArray.length)], '0','20', '10'); //HTML
    makeMonster2 = new Monster('landmonsterN2', '20', xArray[Math.floor(Math.random() * xArray.length)], '0','20', '10'); //CSS
    makeMonster3 = new Monster('landmonsterS1', '30', xArray[Math.floor(Math.random() * xArray.length)], '0','10', '30'); //C#
    makeMonster4 = new Monster('landmonsterS2', '30', xArray[Math.floor(Math.random() * xArray.length)], '0','10', '30'); //C	

	imgmon1=new Image();
	imgmon1.src=monsterimgArray1[0]
	// (이미지명, 이미지생성x좌표위치, 이미지생성y좌표위치, 이미지가로길이, 이미지세로길이)
	ctxMonster.drawImage(imgmon1, makeMonster1.monsterX, makeMonster1.monsterY, 100, 100);

	imgmon2=new Image();
	imgmon2.src=monsterimgArray1[1]
	ctxMonster.drawImage(imgmon2, makeMonster2.monsterX, makeMonster2.monsterY, 100, 100);

	imgmon3=new Image();
	imgmon3.src=monsterimgArray1[2]
	ctxMonster.drawImage(imgmon3, makeMonster3.monsterX, makeMonster3.monsterY, 100, 100);

	imgmon4=new Image();
	imgmon4.src=monsterimgArray1[3]
	ctxMonster.drawImage(imgmon4, makeMonster4.monsterX, makeMonster4.monsterY, 100, 100);

	console.log(makeMonster1.monsterX)
	console.log(makeMonster2.monsterX)
	console.log(makeMonster3.monsterX)
	console.log(makeMonster4.monsterX)
}
function createMonster2() { //공중몬스터 생성함수
	// (몬스터이름, 몬스터체력, 몬스터x좌표, 몬스터y좌표, 몬스터스피드, 몬스터공격력)
    makeMonster5 = new Monster('skymonster1', '10', xArray[Math.floor(Math.random() * xArray.length)], Math.floor((Math.random() *(720-(0)))+(0)), '30', '10'); //JS
    makeMonster6 = new Monster('skymonster2', '10', xArray[Math.floor(Math.random() * xArray.length)], Math.floor((Math.random() *(720-(0)))+(0)), '30', '10'); //PY

    imgmon5=new Image();
	imgmon5.src=monsterimgArray2[0]
	// (이미지명, 이미지생성x좌표위치, 이미지생성y좌표위치, 이미지가로길이, 이미지세로길이)
	ctxMonster.drawImage(imgmon5, makeMonster5.monsterX, makeMonster5.monsterY, 100, 100);

	imgmon6=new Image();
	imgmon6.src=monsterimgArray2[1]
	ctxMonster.drawImage(imgmon6, makeMonster6.monsterX, makeMonster6.monsterY, 100, 100);

	console.log(makeMonster5.monsterX)
	console.log(makeMonster5.monsterY)
	console.log(makeMonster6.monsterX)
	console.log(makeMonster6.monsterY)
}
//setInterval 16주기를 5번 실행할때마다 지상몬스터 생성
if(count==0) {
	createMonster()
}
count+=1
if(count==5) {
	createMonster()
	count=0
}
//setInterval 16주기를 50번 실행할때마다 공중몬스터 생성
count2 += 1
if(count2==50) {
	createMonster2()
	count2=0
}




let monsterArray=[makeMonster1.monsterX,makeMonster2.monsterX,makeMonster3.monsterX,makeMonster4.monsterX,makeMonster5.monsterX,makeMonster6.monsterX]
function moveMonster () {
	for(i=0;i<=monsterArray.length;i++) {
		if (monsterArray[i]>0) {
			monsterArray[i]=monsterArray[i]-1
		}
		else if (monsterArray[i]<0) {
			monsterArray[i]=monsterArray[i]+1
		}
	}
	ctxMonster.clearRect(0, 0, canvas.width, canvas.height);
	ctxMonster.drawImage(imgmon1, monsterArray[0], makeMonster1.monsterY, 100, 100);
	ctxMonster.drawImage(imgmon2, monsterArray[1], makeMonster2.monsterY, 100, 100);
	ctxMonster.drawImage(imgmon3, monsterArray[2], makeMonster3.monsterY, 100, 100);
	ctxMonster.drawImage(imgmon4, monsterArray[3], makeMonster4.monsterY, 100, 100);
	ctxMonster.drawImage(imgmon5, monsterArray[4], makeMonster5.monsterY, 100, 100);
	ctxMonster.drawImage(imgmon6, monsterArray[5], makeMonster6.MY(), 100, 100);
	window.requestAnimationFrame(function(){ moveMonster() })
}
window.requestAnimationFrame(function(){ moveMonster() })
setInterval(moveMonster,16)
/*
function draw () {

	for(i=0;i<=newArr.length;i++) {
		if (newArr[i]>0) {
			newX=newArr[i]-100
		}
		else if (newArr[i]<0) {
			newX=newArr[i]+100
		}
		newArr = []
		newArr.push(newX)
	}
}
function drawMonsters() {
	ctxMonster.clearRect(0, 0, canvas.width, canvas.height);
	let imgmon5=new Image();
	imgmon5.onload = function() {
		ctxMonster.drawImage(imgmon5, makeMonster5.MX(), makeMonster5.MY(), 100, 100);
	}	
	imgmon5.src=monsterimgArray2[0]

}
function moveMonster() {
	ctx.drawImage(img, imgCenterX+user.x, imgCenterY+user.y, canvas.width, canvas.height, 0, 0, canvas.width, canvas.height);
}
*/
}
//setInterval(createMonster, 800);
//setTimeout(function() { setInterval(createMonster2, 500) },8000);

setInterval(draw, 16);
