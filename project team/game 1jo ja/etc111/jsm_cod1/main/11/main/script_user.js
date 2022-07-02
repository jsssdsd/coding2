const canvas = document.getElementById("canvas");
const img = new Image();
const ctx = canvas.getContext("2d");

img.src="background.png";

img.onload = function() {
	// (이미지객체, 이미지객체 내 x 좌표, 이미지객체 내 y좌표, 표현되는 너비, 표현되는 높이, 캔버스 x좌표, 캔버스 y좌표)
	ctx.drawImage(img, img.width/2-canvas.width/2, img.height/2, canvas.width, canvas.height, 0, 0, canvas.width, canvas.height
	 )
}
