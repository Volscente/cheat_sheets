# TypeScript

## Static Typing and Runtime Validation

TypeScript is for "Compile-Time". TypeScript Interfaces disappear once the code is converted to JavaScript.
These types are used for static typing and are stored in `frontend/src/types`.

Zod is for "Runtime" validation. Zod exists while the user is actually using the app. It acts as a "bouncer" for your forms. It takes the raw input from the user, checks it against your rules (e.g., "Must be a string," "Must not be empty"), and provides the error messages that `react-hook-form` needs to show the user.

By using `z.infer<typeof wordSchema>`, you actually generate a TypeScript type from the Zod schema. This ensures your validation rules and your TypeScript types are always perfectly synchronized, so you never have to define them twice.
