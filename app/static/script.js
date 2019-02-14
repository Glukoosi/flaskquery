document.addEventListener('DOMContentLoaded', function(){
var follow1 = document.getElementById("beer4");
var follow2 = document.getElementById("beer3");
var follow3 = document.getElementById("beer2");
var follow4 = document.getElementById("beer1");
var follow5 = document.getElementById("bus");
var mouse = {x: 0, y: 0}; //mouse.x, mouse.y

document.addEventListener("mousemove", getMouse);

follow1.style.position = "absolute"; //css
follow2.style.position = "absolute"; //css
follow3.style.position = "absolute"; //css
follow4.style.position = "absolute"; //css
follow5.style.position = "absolute"; //css

var follow1pos = {x: 0, y: 0};
var follow2pos = {x: 0, y: 0};
var follow3pos = {x: 0, y: 0};
var follow4pos = {x: 0, y: 0};
var follow5pos = {x: 0, y: 0};

setInterval(followMouse, 50, follow2pos, follow1pos, follow1);
setInterval(followMouse, 50, follow3pos, follow2pos, follow2);
setInterval(followMouse, 50, follow4pos, follow3pos, follow3);
setInterval(followMouse, 50, follow5pos, follow4pos, follow4);
setInterval(followMouse, 50, mouse, follow5pos, follow5);


function getMouse(e) {
    mouse.x = e.pageX - 11;
    mouse.y = e.pageY;
}

function followMouse(target, beepos, bee) {
    //1. find distance X , distance Y
    var distX = target.x + 22 - beepos.x;
    var distY = target.y - beepos.y;
    //Easing motion
    //Progressive reduction of distance
    beepos.x += distX / (3 );
    beepos.y += distY / (3 );

    bee.style.left = beepos.x + "px";
    bee.style.top = beepos.y + "px";


}

    // your code goes here
}, false);
