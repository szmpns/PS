import { fileURLToPath } from "url";
import { dirname } from "path";
import express from "express";
import morgan from "morgan";
import path from "path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const app = express();

app.locals.pretty = app.get("env") === "development"; // The resulting HTML code will be indented in the development environment

app.use(morgan("dev"));
app.use("/static", express.static(path.join(__dirname, "static")));

// Set the 'views' directory for your templates
app.set("views", path.join(__dirname, "views"));

// Set Pug as the view engine
app.set("view engine", "pug");

// Middleware to parse incoming request data
app.use(express.urlencoded({ extended: true }));

/* ******** */
/* "Routes" */
/* ******** */

/* ------------- */
/* Route 'GET /' */
/* ------------- */
app.get("/", (request, response) => {
  let students = [
    {
      fname: "Jan",
      lname: "Kowalski",
    },
    {
      fname: "Anna",
      lname: "Nowak",
    },
  ];

  response.render("index", { title: "Hey", message: "Hello there!", students }); // Przekazanie tablicy students do widoku
});

/* ------------------- */
/* Route 'GET /submit' */
/* ------------------- */
app.get("/submit", (request, response) => {
  response.set("Content-Type", "text/plain");
  response.send(`Hello ${request.query.name}`);
});

/* ---------------- */
/* Route 'POST /' */
/* ---------------- */
app.post("/", (request, response) => {
  const name = request.body.name;
  response.send(`Hello ${name}`);
});

/* ************************************************ */
// The application is to listen on port number 8000
app.listen(8000, () => {
  console.log("The server was started on port 8000");
  console.log('To stop the server, press "CTRL + C"');
});

export default app; // Export the app for testing purposes
