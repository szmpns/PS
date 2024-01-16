import express from "express";
import morgan from "morgan";
import { encodeXML } from "entities";
import fetch from "node-fetch"; // Dodajemy import node-fetch

const app1 = express();
const app2 = express();

app1.set("view engine", "pug");
app1.locals.pretty = app1.get("env") === "development";
app2.use(morgan("dev"));
app2.use(express.urlencoded({ extended: false }));

app1.get("/", function (request, response) {
  response.render("index");
});

// Obsługa zapytania od klienta
app1.get("/fetch-data", function (req, res) {
  const { name } = req.query;

  // Wykonujemy zapytanie do serwera app2
  fetch(`http://localhost:8000/submit?name=${name}`)
    .then((response) => {
      // Odebranie odpowiedzi z serwera app2
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then((data) => {
      // Po otrzymaniu odpowiedzi, umieść dane w elemencie div
      const displayElement = `<div>${data}</div>`;
      res.send(displayElement); // Odpowiedź na żądanie /fetch-data
    })
    .catch((error) => {
      console.error("Error:", error);
      res.status(500).send("Internal Server Error");
    });
});

app2.all("/submit", function (req, res) {
  let name = req.query.name ?? req.body.name;

  switch (req.accepts(["html", "text", "json", "xml"])) {
    case "json":
      res.type("application/json");
      res.json({ welcome: `Hello '${name}'` });
      console.log(
        `\x1B[32mThe server sent a JSON document to the browser using the '${req.method}' method\x1B[0m`
      );
      break;

    case "xml":
      name = name !== undefined ? encodeXML(name) : "";
      res.type("application/xml");
      res.send(`<welcome>Hello '${name}'</welcome>`);
      console.log(
        `\x1B[32mThe server sent an XML document to the browser using the '${req.method}' method\x1B[0m`
      );
      break;

    default:
      res.type("text/plain");
      res.send(`Hello '${name}'`);
      console.log(
        `\x1B[32mThe server sent a plain text to the browser using the '${req.method}' method\x1B[0m`
      );
  }
});

app2.listen(8000, function () {
  console.log("The server was started on port 8000");
  app1.listen(8001, function () {
    console.log("The server was started on port 8001");
    console.log('To stop the servers, press "CTRL + C"');
  });
});
