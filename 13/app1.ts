// app1.ts

/**
 * @author Stanisław Polak <polak@agh.edu.pl>
 */

// @deno-types="npm:@types/express@^4"
import express, { Express, Request, Response } from "npm:express@^4";
import morgan from "npm:morgan@^1";
import "npm:pug@^3";

const app: Express = express();
const deno_logo =
  "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Deno_2021.svg/120px-Deno_2021.svg.png";

app.set("view engine", "pug");
app.locals.pretty = app.get("env") === "development";

app.use(morgan("dev"));
app.use(express.urlencoded({ extended: false }));

app.get("/", function (_req: Request, res: Response) {
  res.render("index", { deno_logo });
});

app.post("/", function (req: Request, res: Response) {
  res.send(`Hello '${(req as any).body.name}'`);
});

const port = 8000;

app.listen(port, function () {
  console.log(`The application is available on port ${port}`);
});

// Dodaj obsługę restartu na zmiany w kodzie źródłowym
if (import.meta.main) {
  const watcher = Deno.watchFs(".");

  for await (const event of watcher) {
    if (event.kind === "modify" || event.kind === "create") {
      console.log("Restarting the application...");
      Deno.run({
        cmd: [
          "deno",
          "run",
          "--unstable",
          "--allow-run",
          "--allow-read",
          "--allow-write",
          "--allow-net",
          "--no-check",
          "app1.ts",
        ],
        stdout: "inherit",
        stderr: "inherit",
      }).status();
      break;
    }
  }
}
