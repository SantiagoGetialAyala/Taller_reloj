function updateClock() {
    const now = new Date();
    const seconds = now.getSeconds();
    const minutes = now.getMinutes();
    const hours = now.getHours();

    const secondHand = document.getElementById('second');
    const minuteHand = document.getElementById('minute');
    const hourHand = document.getElementById('hour');

    // Listas circulares 
    const secondDeg = (seconds / 60) * 360;
    const minuteDeg = (minutes / 60) * 360;
    const hourDeg = ((hours % 12) / 12) * 360 + (minutes / 60) * 30;

    secondHand.style.transform = `rotate(${secondDeg}deg)`;
    minuteHand.style.transform = `rotate(${minuteDeg}deg)`;
    hourHand.style.transform = `rotate(${hourDeg}deg)`;
}

setInterval(updateClock, 1000);
