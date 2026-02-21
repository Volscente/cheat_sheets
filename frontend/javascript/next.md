# NextJS Framework

## Folders

### .next

The folder is automatically created upon running one of the following commands:

```bash
npx create-next-app@latest frontend
npm run dev
npm build
```

It contains the optimized, compiled version of your code that the browser actually understands.

Never edit anything inside `.next` manually. If you delete this folder, Next.js will simply recreate it the next time you start the app. It is usually excluded from Git because it changes every time you save a file.

Files included:

- `routes.d.ts`: It scans your `src/app` folder and makes a list of every valid link.
- `cache-life.d.ts`: It defines the "shape" of how your app handles data caching.
- `validator.ts`: It validates that your "Server Components" and "Client Components" aren't breaking the rules (e.g., trying to use a database secret in a file that runs in the browser).

### app

In Next.js, this folder uses a file-system based router, meaning the way you organize your folders and files here directly dictates how your website looks and functions.

Basic files:

- `favicon.ico`: It’s the icon that appears in the browser tab, next to your page title
- `globals.css`: This is where Tailwind CSS is initialized. It contains instructions that apply to every single page of your app. A global stylesheet.
- `layout.tsx`: This file defines the permanent structure of your website. If you want a Navigation Bar or a Footer to stay on the screen while you switch between pages, you put it here. It contains the `<html>` and `<body>` tags. Every "Page" you create is injected into this layout as a "child."
- `page.tsx`: This file maps to your root URL (`<http://localhost:3000/>`). Whatever code you write here is what the user sees first.

When a user visits your site, Next.js does this:

1. Loads the `layout.tsx` (The wrapper).
2. Imports the `globals.css` (The styling rules).
3. Injects the content of `page.tsx` into the middle of the layout.
4. Displays the `favicon.ico` in the tab.

### node_modules

It stores all project dependencies.

The `.bin` contains executable scripts. When you run `npm run dev`, it actually goes into `node_modules/.bin/next` to start the engine.

## Files

### Overview

- `package.json`: It is the Main Manifest. It lists the name of the app, the scripts (like `dev`),
  and the list of libraries required.
- `package-lock.json`: It records the exact version of every single sub-dependency.
- `tsconfig.json`: It includes TypeScript rules and when to apply them.
- `next.config.ts`: Specific configurations for Next.js framework and how it should behave (e.g., adding an image domain).
- `postcss.config.mjs`and `tailwind.config.ts`: Tailwind specific configurations for CSS generation.

### tsconfig.json

It includes for example the repository root path reference:

```json
"paths": {
      "@/*": ["./src/*"]
    }
```

## page.tsx

As the user opens the Browser, the AppRouter from Next.js automatically searches in the `app` or `src/app` for the file `page.tsx`.

In this file there is a `export default` that defines what should be called in that occsaion.
