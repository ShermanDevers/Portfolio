let timerStart = false;
let hours;
let minutes;
let seconds;
let secondsRemaining;

function readInput() {
    hours = parseInt(document.querySelector('#hours').value);
    minutes = parseInt(document.querySelector('#minutes').value);
    seconds = parseInt(document.querySelector('#seconds').value);
    secondsRemaining = (hours * 3600) + (minutes * 60) + seconds;
    start();
}


const button = document.querySelector('button');
console.log("Script running")
button.addEventListener('click', updateTimer);

function start() {
    const timerElement = document.querySelector('.timer');
    console.log("Hours", hours);
    console.log("Minutes", minutes);
    console.log("Seconds", seconds);
    timerElement.textContent = `${hours.toString().padStart(2, 0)}:${minutes.toString().padStart(2, 0)}:${seconds.toString().padStart(2, 0)}`;
    console.log(timerElement.textContent);
    timerStart = true;
}

function updateTimer() {
    if (timerStart == true) {
        if (secondsRemaining < 0) {
            timerElement.textContent = "00:00:00";
        }
        const timerElement = document.querySelector('.timer');
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