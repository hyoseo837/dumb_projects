let board = ["","","","","","","","",""];
let turn = 0;
let sign = ["o","x"]
let colors = ["tomato","skyblue"]
let done = false;
let score = [0,0];


let para = document.getElementById("demo")
let btns = []
btns.push(document.getElementById('0'))
btns.push(document.getElementById('1'))
btns.push(document.getElementById('2'))
btns.push(document.getElementById('3'))
btns.push(document.getElementById('4'))
btns.push(document.getElementById('5'))
btns.push(document.getElementById('6'))
btns.push(document.getElementById('7'))
btns.push(document.getElementById('8'))
let game = document.getElementById("game")
let scoreboard = document.getElementById("scoreboard")


for(let i=0; i<9;i++){
    btns[i].addEventListener("click",()=>{
        if (board[i] == "" && done == false){
            board[i] = sign[turn];
            btns[i].style.backgroundColor = colors[turn];
            turn = Number(!turn);
            checkwin();
        }
    })
}

game.addEventListener("click",()=>{
    board = ["","","","","","","","",""];
    turn = 0;
    done = false;
    for(let i=0; i<9;i++){
        btns[i].style.backgroundColor = "#cdcdcd";
    }
    para.innerHTML = "TicTacToe";
})

function checksame(a,b,c){
    if (board[a] == board[b] && board[b]==board[c] && board[a] != ""){
        done = true;
        if (board[a] == "o"){
            para.innerHTML = "player 1 win";
            score[0] += 1;
        }
        if (board[a] == "x"){
            para.innerHTML = "player 2 win";
            score[1] += 1;
        }
        scoreboard.innerHTML = score[0]+" : "+score[1]
    }
}

function checkwin(){
    checksame(0,1,2);
    checksame(3,4,5);
    checksame(6,7,8);
    checksame(0,3,6);
    checksame(1,4,7);
    checksame(2,5,8);
    checksame(0,4,8);
    checksame(2,4,6);
}