class ObjectManager {
    constructor() {
        this.objectArray = [];    // 오브젝트 저장할 배열
    }

    addObject(obj) { // 새로운 오브젝트 등록
        this.objectArray.push(obj);
    }

    removeObject(obj) {  // 오브젝트 삭제
        obj.container.removeChild(obj.div);
        this.objectArray.splice(this.objectArray.indexOf(obj), 1);
    }

    tick() { // tick() 처리
        for (var i = 0; i < this.objectArray.length; i++) {
            this.objectArray[i].tick();
        }
    }

    render() {  // render() 처리
        for (var i = 0; i < this.objectArray.length; i++){
            this.objectArray[i].render();
        }
    }

}

