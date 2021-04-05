/**
 * TODO:
 * Be able to render a grid to the screen
 * Be able to create a grid based on a bias value
 * Be able to do a "generation" and the rerender the grid
 * Add in the ability to change a variety of parameters
 */

// Canvas element
let c;
let g;
let w;
let h;




function drawLine() {
    c = document.getElementById("mainCanvas");

    const ctx = c.getContext("2d");

    ctx.moveTo(0,0);
    ctx.lineTo(200, 100);
    ctx.stroke();
    console.log("hello world");
    console.log(c);
}

function generateGrid(bias) {
    g = [];
    

}

