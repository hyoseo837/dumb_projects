const PI2 = Math.PI * 2;
var objectdata = [];
lera = ['left', 'right'];
dirlist = [
    [0, 1],
    [1, 0],
    [-1, 0],
    [0, -1]
]

function turn(pair, LR) {
    k = pair;
    d = 0;
    theta = 0;

    if (k[0] == 0) {
        if (k[1] == 1) { theta = 0; } else if (k[1] == -1) { theta = 2; }
    } else if (k[0] == 1) { theta = 1; } else if (k[0] == -1) { theta = 3; }

    if (LR == 'right') { d = 1; } else if (LR == 'left') { d = 3; }

    theta = (theta + d) % 4;

    if (theta == 0) { result = [0, 1]; } else if (theta == 1) { result = [1, 0]; } else if (theta == 2) { result = [0, -1]; } else if (theta == 3) { result = [-1, 0]; }
    // console.log(result)
    return result
}

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
        window.requestAnimationFrame(this.animate.bind(this));
        this.ctx.clearRect(0, 0, this.stageWidth, this.stageHeight);

        for (let i = 0; i < objectdata.length; i++) {

            const item = objectdata[i];
            this.stage = [this.stageWidth, this.stageHeight]
            item.update(this.stage);
            item.draw(this.ctx, this.stageWidth, this.stageHeight);
        }

    }
}


class ant {
    constructor(x, y, dir) {
        this.x = x;
        this.y = y;
        this.dir = dir;
        this.speed = 3;
        this.color = 'black'
    }

    update(stage) {
        this.x += this.speed * this.dir[0];
        this.y -= this.speed * this.dir[1];

        if (this.y < 10 || this.y > stage[1] - 10) {
            this.dir = turn(this.dir, 'right');
        }
        if (this.x < 10 || this.x > stage[0] - 10) {
            this.dir = turn(this.dir, 'right');
        }
    }

    draw(ctx) {

        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.arc(this.x, this.y, 3, 0, PI2, false);
        ctx.fill();
        ctx.beginPath();
        ctx.arc(this.x - this.dir[0] * 4, this.y + this.dir[1] * 4, 2, 0, PI2, false);
        ctx.fill();
        ctx.beginPath();
        ctx.arc(this.x - this.dir[0] * 9, this.y + this.dir[1] * 9, 4, 0, PI2, false);
        ctx.fill();
    }

}

for (i = 0; i < 100; i++) {
    objectdata.push(new ant(Math.random() * 1200 + 10, Math.random() * 650 + 10, dirlist[Math.floor(Math.random() * 4)]))
}
window.onload = () => {
    new App()
}