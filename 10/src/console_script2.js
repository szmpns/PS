import { readFile, writeFile } from "fs/promises";
import { readFileSync, writeFileSync } from "fs";
import { exec } from "child_process";

const FILE_PATH = "counter.txt";

async function readCounterAsync() {
  try {
    const data = await readFile(FILE_PATH, "utf-8");
    return parseInt(data) || 0;
  } catch (error) {
    return 0;
  }
}

async function writeCounterAsync(count) {
  await writeFile(FILE_PATH, count.toString());
}

function readCounterSync() {
  try {
    const data = readFileSync(FILE_PATH, "utf-8");
    return parseInt(data) || 0;
  } catch (error) {
    return 0;
  }
}

function writeCounterSync(count) {
  writeFileSync(FILE_PATH, count.toString());
}

async function processSync() {
  const count = readCounterSync();
  console.log(`Liczba uruchomień (SYNC): ${count + 1}`);
  writeCounterSync(count + 1);
}

async function processAsync() {
  try {
    const count = await readCounterAsync();
    console.log(`Liczba uruchomień (ASYNC): ${count + 1}`);
    await writeCounterAsync(count + 1);
  } catch (error) {
    console.error(error);
  }
}

async function processCommands() {
  const commands = [];
  process.stdin.setEncoding("utf-8");

  process.stdin.on("data", (chunk) => {
    commands.push(chunk.trim());
  });

  process.stdin.on("end", async () => {
    for (const cmd of commands) {
      try {
        const { stdout, stderr } = await execPromise(cmd);
        if (stdout) console.log(stdout);
        if (stderr) console.error(stderr);
      } catch (error) {
        console.error(error.message);
      }
    }
  });

  process.stdin.on("error", (error) => {
    console.error("Błąd wejścia standardowego:", error);
  });
}

function execPromise(command) {
  return new Promise((resolve, reject) => {
    exec(command, (error, stdout, stderr) => {
      if (error) {
        reject(error);
      } else {
        resolve({ stdout, stderr });
      }
    });
  });
}

async function main() {
  const [, , option] = process.argv;

  if (option === "--sync") {
    await processSync();
  } else if (option === "--async") {
    await processAsync();
  } else {
    console.log(
      "Wprowadź komendy — naciśnięcie Ctrl+D kończy wprowadzanie danych"
    );
    await processCommands();
  }
}

main().catch((error) => {
  console.error("Wystąpił błąd:", error);
  process.exit(1);
});
