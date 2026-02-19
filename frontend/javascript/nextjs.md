# NextJS Framework

## Folder .next

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
