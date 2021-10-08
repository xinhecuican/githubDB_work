// HTML element
var h1 = document.querySelector("h1");
var resetButton = document.querySelector("#resetGame");
var modeButtons = document.querySelectorAll(".mode")

// Square properties
var numSquares = 9;
var colors = [];
var pickedColor;
var squares = document.querySelectorAll(".square");
var colorDisplay = document.getElementById("colorDisplay");
var messageDisplay = document.querySelector("#message");

// Initialize: 
// S1 set up mode btn liseteners
// S2 set up square
// S3 reset (form random color list, randomly pick color, fill certain squares)
initGame();


function initGame() {
    // S1 set up mode btn liseteners
    setUpModeButtons();
    // S2 set up squares and realize game logic
    setUpSquares();
    // S3 reset (form random color list, randomly pick color, fill certain squares)
    reset();
}

// Mode btn logic: switch difficulty and update colors
function setUpModeButtons() {
    for (var i = 0; i < modeButtons.length; ++i) {
        modeButtons[i].addEventListener("click", function() {
            for (var j = 0; j < modeButtons.length; ++j) {
                modeButtons[j].classList.remove("buttonSelected");
            }
            this.classList.add("buttonSelected");
            // Figure out how many squares to show
            if (this.textContent === "Easy") {
                numSquares = 3;
            } else if (this.textContent === "Medium") {
                numSquares = 6;
            } else {
                numSquares = 9;
            }
            reset();
        })
    }
}

// Square logic, and game logic
function setUpSquares() {
    for (var i = 0; i < squares.length; ++i) {
        // add click listeners to all squares
        squares[i].addEventListener("click", function() {
            // get color of clicked square
            var clickedColor = this.style.backgroundColor;
            // compare color to pickedColor
            if (clickedColor === pickedColor) {
                messageDisplay.textContent = "Correct!";
                resetButton.textContent = "Play Again?";
                changeColors(clickedColor);
                h1.style.backgroundColor = clickedColor;
            }
            else {
                this.style.backgroundColor = "#232323";
                messageDisplay.textContent = "Try Again";
            }
        });
    }
}

// reset (form random color list, randomly pick color, fill certain squares)
function reset() {
    // S1 generate all new colors
    colors = generateRandomColors(numSquares);
    // S2 pick a new random color from array
    pickedColor = pickColor();
    // S3 change colorDisplay in header to match picked color
    colorDisplay.textContent = pickedColor;
    // S4 change colors of squares
    for (var i = 0; i < squares.length; ++i) {
        if (colors[i]) {
            squares[i].style.backgroundColor = colors[i];
            squares[i].style.display = "block";
        } else {
            squares[i].style.display = "none";
        }
    }
    // S5 reset h1 backgroundColor
    h1.style.backgroundColor = "steelblue";
    // S6 reset msg
    messageDisplay.textContent = "";
    // S7 reset play again btn
    resetButton.textContent = "New Colors";
}

// Reset logic on reset btn
resetButton.addEventListener("click", function() {
    reset();
})

// When select correctly, change all rest squares to target color
function changeColors(color) {
    // loop through all squares
    for (var i = 0; i < squares.length; ++i) {
        // change each color to match given color
        squares[i].style.backgroundColor = color;
    }
}

// Randomly generate color list
function generateRandomColors(numOfColor) {
    // make an array
    var colorArr = [];
    // repeat numOfColor times
    for (var i = 0; i < numOfColor; ++i) {
        // get random color in rgb-string form and push into array
        colorArr.push(randomRgb());
    }
    // return result array
    return colorArr;
}

// Generate a random rgb value
function randomRgb() {
    // pick r value from 0 - 255
    var rValue = Math.floor(Math.random() * 256);
    // pick g value from 0 - 255
    var gValue = Math.floor(Math.random() * 256);
    // pick b value from 0 - 255
    var bValue = Math.floor(Math.random() * 256);
    // build a rgb() string
    return "rgb(" + rValue + ", " + gValue + ", " + bValue + ")";
}

// Randomly pick target color from color list
function pickColor() {
    var randomNum = Math.floor(Math.random() * colors.length);
    return colors[randomNum];
}

