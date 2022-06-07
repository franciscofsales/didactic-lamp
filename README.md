# didactic-lamp

This repository exemplifies how to execute a simple FastAPI HTTP API alongside NGINX, serving a static website with JavaScript that consumes the API.

# How to use

To build the Docker image, simply execute:

```bash
docker build -t didactic_lamp -f docker/Dockerfile .
```

Afterwards, you can execute it using:

```bash
docker run --rm -it -p 80:80 -p 8080:8080 didactic_lamp
```
# Examples

```bash
▶ curl localhost:80
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Didactic Lamp</title>
        <link rel="stylesheet" href="css/style.css">
    </head>
    <body>
        <button id="btn-datetime" class="button-56">Get current date and time</button>
        <div class="datetime-container">
            <span id="datetime"></span>
        </div>
        <script src="js/app.js"></script>
    </body>
</html>
```

```bash
▶ curl localhost:8080
{"message":"Hello, World! It's currently 2022-06-07T21:40:27.450565 (UTC)."}
```
