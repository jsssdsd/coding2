let myDiv = document.getElementById("full");
let myAsks = document.getElementsByClassName("myAsk")
let correct = new Array(1,1,2,0,1,1,2,1,0,1);
let myArr = new Array();
let chart = document.getElementById("piechart");
let sum = 0;

let key = 0;

window.onload = function() {

	for (let i=0; i<myAsks.length; i++)
	{
		if (i==0)
		{
		}
		else
		{
		myAsks[i].style.display = "none";
		}
	}

	chart.style.display = "none";
}


function getNext() {
	let found = null;
	let kA = document.getElementsByName("no"+key);
	for (let i=0; i<kA.length; i++)
	{
		if (kA[i].checked==true)
			found=i;
	}
	if (found != null)
	{
		myArr+=found;
		myAsks[key].style.display="none";
		key +=1;
		myAsks[key].style.display="block";
	}
}

function getResult() {
	let found = null;
	let kA = document.getElementsByName("no"+key);
	for (let i=0; i<kA.length; i++)
	{
		if (kA[i].checked==true)
			found=i;
	}
	if (found != null)
	{
		myArr+=found;
		for (let i=0; i<myArr.length; i++)
		{
			if (myArr[i] == correct[i])
				sum+=1
		}
		console.log(sum+"개 맞췄다.");
		chart.style.display = "block";
		google.charts.load('current', {'packages':['corechart']});
		google.charts.setOnLoadCallback(drawChart);

		function drawChart()
		{
			var data = google.visualization.arrayToDataTable([
			['Task', 'Hours per Day'],
			['정답', sum],
			['오답', 10-sum]]);

			let options = {'title':'퀴즈 결과', 'width':550, 'height':400};

			let chart = new google.visualization.PieChart(document.getElementById('piechart'));
			chart.draw(data, options);
		}
	}
}