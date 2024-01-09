let timerStart = false;
let hours;
let minutes;
let seconds;
let secondsRemaining;
let alerted = false;
const timerElement = document.querySelector('.timer');

function readInput() {
    hours = parseInt(document.querySelector('#hours').value);
    if (isNaN(hours)) {
        alert("Please enter a numerical value for all inputs");
        alerted = true;
    }
    minutes = parseInt(document.querySelector('#minutes').value);
    if (isNaN(minutes) && alerted == false) { 
        alert("Please enter a numerical value for all inputs");
    }

    seconds = parseInt(document.querySelector('#seconds').value);
    if (isNaN(seconds) && alerted == false) {
        alert("Please enter a numerical value for all inputs");
    }

    secondsRemaining = (hours * 3600) + (minutes * 60) + seconds;
    if (alerted == false) {
        start();
    }
}


const button = document.querySelector('button');
console.log("Script running")
button.addEventListener('click', updateTimer);

function start() {
    const timerElement = document.querySelector('.timer');
    timerElement.textContent = `${hours.toString().padStart(2, 0)}:${minutes.toString().padStart(2, 0)}:${seconds.toString().padStart(2, 0)}`;
    timerStart = true;
}

function updateTimer() {
    if (timerStart == true) {
        if (secondsRemaining < 0) {
            timerElement.textContent = "00:00:00";
        }
        console.log(secondsRemaining);
        if (secondsRemaining === 0) {
            timerElement.textContent = "Time's up!";
            return;
        }
        const hours = Math.floor(secondsRemaining / 3600);
        const minutes = Math.floor((secondsRemaining / 60) % 60);
        const seconds = secondsRemaining % 60;
        timerElement.textContent = `${hours.toString().padStart(2, 0)}:${minutes.toString().padStart(2, 0)}:${seconds.toString().padStart(2, 0)}`;
        secondsRemaining--;
        setTimeout(updateTimer, 1000);
    }
}

updateTimer();

function resetTimer() {
    const timerElement = document.querySelector('.timer');
    timerElement.textContent = `${hours.toString().padStart(2, 0)}:${minutes.toString().padStart(2, 0)}:${seconds.toString().padStart(2, 0)}`;
    timerStart = false;
}