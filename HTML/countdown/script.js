let timerStart = false;
let secondsRemaining;
secondsRemaining = parseInt(document.querySelector('#seconds').value);        
const button = document.querySelector('button');
console.log("Script running")
button.addEventListener('click', updateTimer);

function start() {
    const timerElement = document.querySelector('.timer');
    secondsRemaining = document.querySelector('#seconds').value;
    const hours = Math.floor(secondsRemaining / 3600);
    const minutes = Math.floor((secondsRemaining / 60) % 60);
    const seconds = secondsRemaining % 60;
    timerElement.textContent = `${hours.toString().padStart(2, 0)}:${minutes.toString().padStart(2, 0)}:${seconds.toString().padStart(2, 0)}`;
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
            // add any additional logic for timer completion here
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
    secondsRemaining = document.querySelector('#seconds').value;
    const hours = Math.floor(secondsRemaining / 3600);
    const minutes = Math.floor((secondsRemaining / 60) % 60);
    const seconds = secondsRemaining % 60;
    timerElement.textContent = `${hours.toString().padStart(2, 0)}:${minutes.toString().padStart(2, 0)}:${seconds.toString().padStart(2, 0)}`;
    timerStart = false;
}