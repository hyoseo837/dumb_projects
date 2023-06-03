let para = document.getElementById("demo");
let but = document.getElementById("btn");
let colors = ["#4285F4","#DB4437","#F4B400","#0F9D58"];
let color = 0;

but.addEventListener("click",fun1)

function fun1(){
    para.innerHTML = "hello world" + color;
    color += 1;
    if (color == 4){
        color -= 4;
    }
    but.style.backgroundColor = colors[color];
}