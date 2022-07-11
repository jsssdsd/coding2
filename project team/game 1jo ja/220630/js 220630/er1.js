drawLPrjt(){
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
		ctx_projtil.arc(canvas.width/2+this.fx1-user.x, canvas.height-126+(this.fy+user.y+10), 20, 0, Math.PI*2);
		}
		else
		{
		if (user.x > 3200-640)
		{
			ctx_projtil.arc(canvas.width/2+this.fx1-3200+640, canvas.height-126-(this.fy+user.y+10), 20, 0, Math.PI*2);
		}
		else if (user.x < -3200+640)
		{
			ctx_projtil.arc(canvas.width/2+this.fx1+3200-640, canvas.height-126-(this.fy+user.y+10), 20, 0, Math.PI*2);
		
		}
		// projtil_array.push(canvas.width/2+this.fx1-user.x);
		// projtil_array_x.push(canvas.width/2+this.fx1-user.x);
		// projtil_array.push(canvas.height-126-(this.fy+user.y+10));

		}
		ctx_projtil.fillStyle = "#0095DD";
		ctx_projtil.fill();
		ctx_projtil.closePath();
	}
		// projtil_array.push(this.fx1-user.x);
		
		// cx += dx;
		// cy += dy;
	

	}