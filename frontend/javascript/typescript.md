# TypeScript

## Types vs. Interfaces
An interfaces is always used to defining the shape of an **Object**.

A type is more flexible: it can be used to defining objects, strings, numbers and complex combinations of those.


## Static Typing and Runtime Validation

There is a main difference between the usage of **TypeScript Interfaces** and **Zod Objects**

TypeScript interface is for "Compile-Time". TypeScript Interfaces disappear once the code is converted to JavaScript.
These types are used for static typing and are stored in `frontend/src/types`.

```ts
export interface Word {
  id: number;
  word: string;
  gender?: string;
  translation: string;
  category?: string;
  created_at: string;
}
```

Zod is for "Runtime" validation. Zod exists while the user is actually using the app. It acts as a "bouncer" for your forms. It takes the raw input from the user, checks it against your rules (e.g., "Must be a string," "Must not be empty"), and provides the error messages that `react-hook-form` needs to show the user.

```ts
// Runtime Validation
import { z } from "zod";

export const wordSchema = z.object({
  word: z.string().min(1, "German word is required"),
  translation: z.string().min(1, "Translation is required"),
  gender: z.enum(["der", "die", "das", "none"]),
  category: z.enum(["noun", "verb", "adjective", "adverb", "preposition", "other"]),
  word_plural: z.string().optional(),
  example_sentences: z.string().optional(),
});

// Generate a TypeScript Type
export type WordFormValues = z.infer<typeof wordSchema>;
```

By using `export type WordFormValues = z.infer<typeof wordSchema>;`, you actually generate a TypeScript type from the Zod schema. It is a bridge between Zod and TypeScript. The `typeof` looks at the object `WordSchema` and retrieves the attributes. The `infer<...>` is a function provided by Zod and creates the TypeScript Interface from the Zod object. 
