// deno.ts

const { run, args } = Deno;

const tasks = JSON.parse(Deno.readTextFileSync("deno_tasks.json"));

const taskName = args[1];

if (!taskName || !tasks.tasks[taskName]) {
  console.error(`Task not found: ${taskName}`);
  Deno.exit(1);
}

const taskCommand = tasks.tasks[taskName];

run({
  cmd: taskCommand.split(" "),
  stdout: "inherit",
  stderr: "inherit",
});
