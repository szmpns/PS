import { fileURLToPath } from "url";
import { dirname } from "path";
import express from "express";
import morgan from "morgan";
import path from "path";
import { MongoClient } from "mongodb";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const app = express();

app.locals.pretty = app.get("env") === "development";

app.use(morgan("dev"));
app.use("/static", express.static(path.join(__dirname, "static")));
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "pug");
app.use(express.urlencoded({ extended: true }));

app.get("/:department", async (request, response) => {
  const department = request.params.department;
  const client = new MongoClient("mongodb://localhost:8000");

  try {
    await client.connect();
    const db = client.db("AGH");
    const collection = db.collection("students");

    let students;
    if (department) {
      students = await collection.find({ department: department }).toArray();
    } else {
      students = await collection.find({}).toArray();
    }

    response.render("index", {
      title: "Hey",
      message: "Hello there!",
      students,
    });
  } catch (error) {
    console.error(error);
    response.status(500).send("Something went wrong!");
  } finally {
    await client.close();
  }
});

app.listen(8000, () => {
  console.log("The server was started on port 8000");
  console.log('To stop the server, press "CTRL + C"');
});

export default app;
