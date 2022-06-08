const url='http://localhost:8080';
const button = document.getElementById('btn-datetime');
const span = document.getElementById('datetime');

button.addEventListener('click', (e) => {
    e.preventDefault();

    fetch(url)
    .then((resp) => resp.json())
    .then(function(data) {
        span.innerHTML = data.message;
    })
    .catch(function(error) {
        span.textContent = 'There has been a problem with your fetch operation: ' + error.message;
    });
});
