document.addEventListener('DOMContentLoaded', function(){

var follow1 = document.getElementById("follow5");
var follow2 = document.getElementById("follow4");
var follow3 = document.getElementById("follow3");
var follow4 = document.getElementById("follow2");
var follow5 = document.getElementById("follow1");

$('input[type=checkbox][name=speechbox]').change(function() {
        if (document.getElementById('speechbox').checked) {
            $('#speech-info').show();
        } else {
            $('#speech-info').hide();
            $('input[name=speech]').val("");
        }
    });


if (window.location.href.split("#")[1] === "L%C3%A4hetetty" ) {
    follow5 = document.getElementById("follow9");
    follow2 = document.getElementById("follow8");
    follow3 = document.getElementById("follow7");
    follow4 = document.getElementById("follow6");
    follow1 = document.getElementById("follow1");
}


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
    mouse.x = e.pageX - 14;
    mouse.y = e.pageY;

    follow1.style.visibility = "visible";
    follow2.style.visibility = "visible";
    follow3.style.visibility = "visible";
    follow4.style.visibility = "visible";
    follow5.style.visibility = "visible";
}

function followMouse(target, beepos, bee) {
    //1. find distance X , distance Y
    var distX = target.x + 42 - beepos.x;
    var distY = target.y - beepos.y;
    //Easing motion
    //Progressive reduction of distance
    beepos.x += distX / (3 );
    beepos.y += distY / (3 );

    bee.style.left = beepos.x + "px";
    bee.style.top = beepos.y - 10 + "px";
}

    // your code goes here
}, false);
