const http = require("http");
const fs = require("fs");
const url = require("url");
const querystring = require("querystring");

const guestBookFile = "guestbook.txt";

/**
 * Odczytuje zawartość księgi gości z pliku.
 * @param {function} callback - Funkcja zwrotna wywoływana po odczytaniu danych.
 */
function readGuestBook(callback) {
  fs.readFile(guestBookFile, "utf8", (err, data) => {
    if (err) {
      callback(err, null);
    } else {
      const entries = data.split("\n").filter((entry) => entry.trim() !== "");
      callback(null, entries);
    }
  });
}

/**
 * Dodaje nowy wpis do księgi gości.
 * @param {string} newEntry - Nowy wpis do dodania.
 * @param {function} callback - Funkcja zwrotna wywoływana po dodaniu wpisu.
 */
function appendToGuestBook(newEntry, callback) {
  fs.appendFile(guestBookFile, newEntry, (err) => {
    if (err) {
      callback(err);
    } else {
      callback(null);
    }
  });
}

/**
 * Obsługuje żądania HTTP.
 * @param {http.IncomingMessage} req - Obiekt reprezentujący przychodzące żądanie.
 * @param {http.ServerResponse} res - Obiekt reprezentujący odpowiedź serwera.
 */
function handleRequest(req, res) {
  const parsedUrl = url.parse(req.url);
  const pathName = parsedUrl.pathname;

  if (req.method === "GET" && pathName === "/") {
    readGuestBook((err, entries) => {
      if (err) {
        res.writeHead(500, { "Content-Type": "text/html; charset=utf-8" });
        res.end("Błąd odczytu księgi gości");
      } else {
        let guestBookContent =
          '<head><meta charset="utf-8"><title>Księga gości</title></head><body><h1>Poprzednie wpisy</h1>';
        entries.forEach((entry) => {
          guestBookContent += `<p>${entry}</p>`;
        });
        guestBookContent += `
          <h2>Nowy wpis:</h2>
          <form action="/" method="post">
              <label>Twoje imię i nazwisko:</label><br>
              <input type="text" name="name"><br>
              <label>Treść wpisu:</label><br>
              <textarea name="message" rows="4" cols="50"></textarea><br>
              <input type="submit" value="Dodaj wpis">
          </form>
        `;
        res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
        res.end(guestBookContent);
      }
    });
  } else if (req.method === "POST" && pathName === "/") {
    let body = "";
    req.on("data", (chunk) => {
      body += chunk.toString();
    });
    req.on("end", () => {
      const parsedBody = querystring.parse(body);
      const name = parsedBody.name || "Anonymous";
      const message = parsedBody.message || "";
      const newEntry = `${name}\n${message}\n`;

      appendToGuestBook(newEntry, (err) => {
        if (err) {
          res.writeHead(500, { "Content-Type": "text/html; charset=utf-8" });
          res.end("Błąd dodawania wpisu");
        } else {
          res.writeHead(302, { Location: "/" });
          res.end();
        }
      });
    });
  } else {
    res.writeHead(404, { "Content-Type": "text/html; charset=utf-8" });
    res.end("Strona nie istnieje");
  }
}

const server = http.createServer(handleRequest);

const PORT = 8000;
server.listen(PORT, () => {
  console.log(`Serwer uruchomiony na porcie ${PORT}`);
});
