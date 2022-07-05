




let Lid_N0= [];  //로그인 정보기록.
function printName() {
	Lid_N1 = document.getElementById("name").value;
}
const Lbt_0 =document.getElementById("Lbutton");

Lbt_0.addEventListener('click',loginR);
function loginR()
{
	console.log(Lid_N1)
	Lid_N0.push(Lid_N1);
	console.log(Lid_N0);
}

