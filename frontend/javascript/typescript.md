# TypeScript

## Types vs. Interfaces
An interfaces is always used to defining the shape of an **Object**.

A type is more flexible: it can be used to defining objects, strings, numbers and complex combinations of those.


## Static Typing and Runtime Validation

### Introduction

There is a main difference between the usage of **TypeScript Interfaces** and **Zod Objects**


### Interface Example

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
### Zod Example

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

### Infer

By using `export type WordFormValues = z.infer<typeof wordSchema>;`, you actually generate a TypeScript type from the Zod schema. It is a bridge between Zod and TypeScript. The `typeof` looks at the object `WordSchema` and retrieves the attributes. The `infer<...>` is a function provided by Zod and creates the TypeScript Interface from the Zod object. 

### Usage

1. The Source of Truth (`wordSchema.ts`): You define your rules once in Zod (e.g., word must be a string). This acts as your Runtime bouncer.

2. The Automatic Type Generation: Instead of manually writing a second TypeScript interface (which you might forget to update later), `z.infer` automatically creates `WordFormValues`. Now, TypeScript knows exactly what the form data looks like.

3. The Form Handshake (`AddWordModal.tsx` the ReactJS compoent): When you initialize your form with `useForm<WordFormValues>`, you are telling React Hook Form: "This form must strictly follow the shape of our WordFormValues."

4. Developer Experience: Because of this "handshake," if you try to access a field in your code that doesn't exist in the schema (like errors.translation_typo), VS Code will highlight it in red and warn you immediately.

5. Submission: When `handleSubmit(onSubmit)` is called, the data variable is guaranteed to be of type `WordFormValues`. You can safely send it to your FastAPI backend knowing it has already passed the "bouncer" check.
