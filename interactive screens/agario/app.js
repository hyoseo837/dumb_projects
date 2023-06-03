const PI2 = Math.PI * 2;
var objectdata = [];
var colors = ['red', 'darkblue', 'green', 'purple'];
var maxbab = 100;


class App {
    constructor() {

        this.canvas = document.createElement('canvas');
        document.body.appendChild(this.canvas);
        this.ctx = this.canvas.getContext('2d');

        this.pixelRatio = (window.devicePixelRatio > 1) ? 2 : 1;

        window.addEventListener('resize', this.resize.bind(this), false);
        this.resize();

        window.requestAnimationFrame(this.animate.bind(this));

    }


    resize() {
        this.stageWidth = window.innerWidth - 20;
        this.stageHeight = window.innerHeight - 20;

        this.canvas.width = this.stageWidth * this.pixelRatio;
        this.canvas.height = this.stageHeight * this.pixelRatio;
        this.ctx.scale(this.pixelRatio, this.pixelRatio);
    }


    animate() {
        maxbab = this.stageHeight * this.stageWidth / 3000;
        if (objectdata.length < maxbab) {
            objectdata[objectdata.length] = new bab();
        }
        window.requestAnimationFrame(this.animate.bind(this));
        this.ctx.clearRect(0, 0, this.stageWidth, this.stageHeight);

        objectdata[0].move();
        for (let i = 0; i < objectdata.length; i++) {

            const item = objectdata[i];
            this.stage = [this.stageWidth, this.stageHeight]
            if (item.update(this.stage, objectdata[0].posx, objectdata[0].posy, objectdata[0].size)) {
                console.log('eaten!')
                objectdata[i] = new bab();
                objectdata[0].xp += item.size
            }
            item.draw(this.ctx, this.stageWidth, this.stageHeight);
        }

    }
}


class bab {
    constructor() {
        this.x = Math.random();
        this.y = Math.random();
        this.color = colors[Math.floor(Math.random() * 4)]
        this.size = 3;
    }

    update(stage, posx, posy, size) {
        var a = posx - this.posx;
        var b = posy - this.posy;

        this.distance = Math.sqrt(a * a + b * b);

        if (this.distance < size) {
            return true;
        } else {
            return false;
        }
    }

    draw(ctx, stageWidth, stageHeight) {
        this.posx = 20 + Math.round(this.x * stageWidth - 40);
        this.posy = 20 + Math.round(this.y * stageHeight - 40);

        ctx.beginPath();
        ctx.fillStyle = this.color;
        ctx.arc(this.posx, this.posy, this.size, 0, PI2, false);
        ctx.fill();
    }

}

class player {
    constructor() {
        this.posx = 300;
        this.posy = 300;
        this.size = 10;
        this.color = 'gray';
        this.xp = 0;
        this.level = 1;
        this.speed = 0;
        this.rate = 0;
    }

    update(stage) {
        this.stageWidth = stage[0];
        this.stageHeight = stage[1];


        if (this.posy > this.stageHeight) {
            this.posy -= this.stageHeight;
        }
        if (this.posy < 0) {
            this.posy += this.stageHeight;
        }
        if (this.posx > this.stageWidth) {
            this.posx -= this.stageWidth;
        }
        if (this.posx < 0) {
            this.posx += this.stageWidth;
        }



        if (this.xp >= this.level * 3) {
            this.xp -= this.level * 3;
            this.level++;
        }
        this.size = this.level * 3 + 10
        this.speed = 0.2 * Math.pow(0.85, this.level)
        this.rate = Math.floor(this.xp / this.level * 100 / 3)
        return false
    }

    draw(ctx) {
        ctx.beginPath();
        ctx.fillStyle = this.color;
        ctx.arc(this.posx, this.posy, this.size, 0, PI2, false);
        ctx.fill();
        // ctx.drawImage('popcat.png', this.posx - this.size, this.posy - this.size, this.size * 2, this.size * 2)
        ctx.fillStyle = 'white';
        ctx.fillText(this.level, this.posx - 5, this.posy);
        ctx.fillText(this.rate + ' %', this.posx - 5, this.posy + 10);
    }

    move() {
        document.addEventListener('keydown', (event) => {
            if (event.key == 'ArrowUp') {
                this.posy -= this.speed;
            }
            if (event.key == 'ArrowDown') {
                this.posy += this.speed;
            }
            if (event.key == 'ArrowRight') {
                this.posx += this.speed;
            }
            if (event.key == 'ArrowLeft') {
                this.posx -= this.speed;
            }
        })
    }
}

objectdata[0] = new player();
// for (let i = 1; i < 100; i++) {
//     objectdata[i] = new bab();
// }

window.onload = () => {
    new App()
}