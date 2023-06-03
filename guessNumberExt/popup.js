let up = document.getElementById("up");
let down = document.getElementById("down");
let guessing = document.getElementById("guess");
let demo = document.getElementById("demo");
let target = Math.floor((Math.random() * 100) + 1);
let guess = 50; let count = 0; let max = 100; let min =0;

guessing.innerHTML = guess;

up.addEventListener("click",()=>{
    guess += 1;
    guessing.innerHTML = guess;
})
down.addEventListener("click",()=>{
    guess -= 1;
    guessing.innerHTML = guess;
})
guessing.addEventListener("click",guessTheNumber)

function guessTheNumber(){
    if (target == -1){
        target = Math.floor((Math.random() * 100) + 1);
        guess = 50; max = 100; min = 0;
        guessing.innerHTML = guess;
        guessing.style.backgroundColor = "#efefef"
        count = 0;
        demo.innerHTML = "Guess!!" + range(max,min)
        }
    else {
        if (guess == target){
            demo.innerHTML = "you got it in "+count+" trials!!!"
            guessing.style.backgroundColor = "#00ff00"
            target = -1;
        }
        else {
            count++
            if (guess > target){
                max = guess
                demo.innerHTML = "it's smaller" + range(max,min)
            }
            if (guess < target){
                min = guess 
                demo.innerHTML = "it's bigger" + range(max,min)
            }
        }
    }
}

function range(max,min){
    return " ("+min+" < target < "+max+")";
}