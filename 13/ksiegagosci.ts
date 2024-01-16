import express, { Request, Response } from "express";
import mongoose, { Document, Schema, Model } from "mongoose";

// Model dla wpisu w księdze gości
interface IGuestBookEntry extends Document {
  name: string;
  message: string;
}

const GuestBookEntrySchema: Schema = new Schema({
  name: { type: String, required: true },
  message: { type: String, required: true },
});

const GuestBookModel: Model<IGuestBookEntry> = mongoose.model(
  "GuestBookEntry",
  GuestBookEntrySchema
);

// Połączenie z bazą danych MongoDB
mongoose.connect("mongodb+srv://szmpns:test123@guestbook.ebjhnn9.mongodb.net/", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Aplikacja Express
const app = express();
app.use(express.urlencoded({ extended: true }));

// Trasy
app.get("/", async (req: Request, res: Response) => {
  try {
    const entries: IGuestBookEntry[] = await GuestBookModel.find();
    res.status(200).send(`
      <head><meta charset="utf-8"><title>Księga gości</title></head>
      <body>
        <h1>Poprzednie wpisy</h1>
        ${entries
          .map((entry) => `<p>${entry.name}: ${entry.message}</p>`)
          .join("")}
        <h2>Nowy wpis:</h2>
        <form action="/" method="post">
          <label>Twoje imię i nazwisko:</label><br>
          <input type="text" name="name"><br>
          <label>Treść wpisu:</label><br>
          <textarea name="message" rows="4" cols="50"></textarea><br>
          <input type="submit" value="Dodaj wpis">
        </form>
      </body>
    `);
  } catch (error) {
    res.status(500).send("Błąd odczytu księgi gości");
  }
});

app.post("/", async (req: Request, res: Response) => {
  try {
    const {
      name = "Anonymous",
      message = "",
    }: { name?: string; message?: string } = req.body;
    const newEntry: IGuestBookEntry = new GuestBookModel({ name, message });
    await newEntry.save();
    res.redirect("/");
  } catch (error) {
    res.status(500).send("Błąd dodawania wpisu");
  }
});

// Nasłuchiwanie na porcie 8000
const PORT: number = 8000;
app.listen(PORT, () => {
  console.log(`Serwer uruchomiony na porcie ${PORT}`);
});
