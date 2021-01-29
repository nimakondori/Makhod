var tz = Intl.DateTimeFormat().resolvedOptions().timeZone

function Countdown() {
    const request = new XMLHttpRequest();
    request.open("GET", `/time?tz=${tz}`);
    request.send();
    request.onreadystatechange = (e) => {
        data = JSON.parse(request.responseText)
        document.getElementById('days').innerHTML = data.day;
        document.getElementById('hours').innerHTML = data.hour;
        document.getElementById('minutes').innerHTML = data.min;
        document.getElementById('secs').innerHTML = data.sec;
        if (data.day == 0 && data.hour == 0 && data.min == 0 && data.sec==0){
            document.getElementById('days').innerHTML = ""
            document.getElementById('hours').innerHTML = ""
            document.getElementById('minutes').innerHTML = ""
            document.getElementById('secs').innerHTML = ""
            document.getElementById("button").style.display = "inline-block"
        }

    };
};
window.onload = function() {
    setInterval(Countdown, 100);
};
