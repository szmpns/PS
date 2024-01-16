// app_guestbook.ts
import { Application, Router, Context } from "https://deno.land/x/oak/mod.ts";
import {
  dejsEngine,
  oakAdapter,
  viewEngine,
} from "https://deno.land/x/view_engine/mod.ts";
import { MongoClient } from "https://deno.land/x/deno_mongo/mod.ts";

const app = new Application();
const router = new Router();

// View engine setup
app.use(viewEngine(oakAdapter, dejsEngine, { viewRoot: "./views" }));

// MongoDB connection setup
const client = new MongoClient();
const uri = "mongodb+srv://mietek:siema@guestbook.ebjhnn9.mongodb.net/";
await client.connect(uri);
const db = client.database("Guestbook");
const entries = db.collection("test.guestbookentries");

// Model dla wpisu w księdze gości
interface IGuestBookEntry {
  name: string;
  message: string;
}

// Routes
router.get("/", async (ctx: Context) => {
  const guestbookEntries = await entries.find();
  const entriesArray: IGuestBookEntry[] = await guestbookEntries.toArray();
  await ctx.render("index.ejs", { entries: entriesArray });
});

router.post("/add-entry", async (ctx: Context) => {
  const requestBody = await ctx.request.body().value;
  const name = requestBody.get("name");
  const message = requestBody.get("message");

  await entries.insertOne({ name, message });

  ctx.response.redirect("/");
});

// Use the router
app.use(router.routes());
app.use(router.allowedMethods());

// Start the app
console.log("App is listening on port: 8000");
await app.listen({ port: 8000 });
