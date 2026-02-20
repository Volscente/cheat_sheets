# JavaScript Overview

## Components

- Runtime Engine: it can be considered as a Python interpreter. It allows the Frameworks and Libraries to run.

- Framework: it provide the blueprints for projects, the structure. A similarity with Python can be FastAPI and Django.

- Library: they are like tools provided to the developers. It is very similar to Python libraries like NumPy and Pandas.

## Node.js

It is a Runtime Engine.

It allows to run JavaScript code on the machine instead of just inside a browser. It builds the code on your machine.

The **npm** is a Package Manager created for Node.js. Since most of the modern JavaScript developments happen on a computer, npm has become the standard way to get any JavaScript code.

The **npm Packages** are specific to the Node.js ecosystem.

The `npx` is used in order to execute packages without installing them.

```bash
# Update npm version
sudo npm install -g npm@11.10.0
```

## Next.js

It is a Full-Stack Framework.

```bash
# Create a new Next.js application using the default template in the folder "frontend"
npx create-next-app@latest frontend

# In case there are reported vulerabilties, run the following command inside the "frontend" folder
npm audit fix
```

## TypeScript

It adds the typing functionality to JavaScript code.

`.ts` (**TypeScript Source**): These are files where you write logic (functions, variables, loops). They get compiled into `.js` files.

`.d.ts` (**Declaration File**): The `d` stands for Declaration.

`.tsx` (**TypeScript with JSX - JavaScript XML**): Used for React Components. It allows you to write HTML-like code directly inside your TypeScript logic.

Think of a `.d.ts` file as a "Table of Contents" or a "Contract."
It contains no logic (no if statements or calculations).
It only tells TypeScript: "Hey, I promise that a function named X exists and it returns a String.
