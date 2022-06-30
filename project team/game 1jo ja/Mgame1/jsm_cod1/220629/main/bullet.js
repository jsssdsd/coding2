


class Bullet extends GameObject {
    constructor(type, container, x, y, velX, velY, initData) {
        super(type, container, x, y, velX, velY, initData);
        this.accel = this.initData.accel;    // 탄 속도 증가 값
        this.delay = this.initData.delay;    // 탄 생성 후 대기값
        this.speed = this.initData.speed;
        this.damage = this.initData.damage;
    }
}



class PlayerChar extends GameObject {
    constructor(container, initData) {
        super("PLAYER", container, initData.x, initData.y, 0, 0, initData);
        this.skillCoolDown = this.initData.bullet.skill.interval;
    }

normalBullet() {
    if (this.tickCount % this.initData.bullet.normal.interval == 0) {
        var bullet = new NormalBullet(this.container, this.x + 70, this.y + 40, this.initData.bullet.normal.speed, 0, this.initData.bullet.normal);
        objectManager.addObject(bullet);
    }
}
}