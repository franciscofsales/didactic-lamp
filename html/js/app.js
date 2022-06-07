const Http = new XMLHttpRequest();
const url='http://localhost:8080';
const button = document.getElementById('btn-datetime');
const span = document.getElementById('datetime');

button.addEventListener('click', (e) => {
    e.preventDefault();

    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
        response = JSON.parse(Http.responseText);
        span.textContent = response.message;
    }
});
