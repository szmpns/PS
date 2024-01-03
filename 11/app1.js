import express from "express";
import morgan from "morgan";
import { fileURLToPath } from "url";
import path from "path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();

app.use(morgan("dev"));
app.use("/static", express.static(path.join(__dirname, "static")));
/* ******** */
/* "Routes" */
/* ******** */

/* ------------- */
/* Route 'GET /' */
/* ------------- */
app.get("/", (request, response) => {
  // Generating the form if the relative URL is '/', and the GET method was used to send data to the server'
  response.send(`
    <!DOCTYPE html>
    <html lang="en">
       <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>First Express application</title>
       </head>
       <body>
          <main>
             <h1>First Express application</h1>
             <form method="GET" action="/submit">
                <label for="name">Give your name</label>
                <input name="name">
                <br>
                <input type="submit">
                <input type="reset">
             </form>
             <img src="/static/images/dog.jpg" alt="Image" style="max-width: 100%; height: auto;">
          </main>
       </body>
    </html>    
           `); // Send the response to the browser
});

/* ------------------- */
/* Route 'GET /submit' */
/* ------------------- */
app.get("/submit", (request, response) => {
  // Processing the form content, if the relative URL is '/submit', and the GET method was used to send data to the server'
  /* ************************************************** */
  // Setting an answer header — we inform the browser that the returned data is plain text
  response.set("Content-Type", "text/plain");
  /* ************************************************** */
  // Place given data (here: 'Hello <name>') in the body of the answer
  response.send(`Hello ${request.query.name}`); // Send a response to the browser
});

/* ************************************************ */
// The application is to listen on port number 8000
app.listen(8000, () => {
  console.log("The server was started on port 8000");
  console.log('To stop the server, press "CTRL + C"');
});
