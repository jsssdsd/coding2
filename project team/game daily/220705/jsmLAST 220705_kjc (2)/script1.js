




Lid_N0= [];  //로그인 정보기록.
let Lid_N1 = document.getElementById("name").value;
let Lbt_0 =document.getElementById("Lbutton");

Lbt_0.addEventListener('click',loginR);
function loginR()
{

	Lid_N0 = Lid_N1;
	console.log(Lid_N0);
}

