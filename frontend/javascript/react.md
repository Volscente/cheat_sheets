# ReacJS

## useState

The `useState` hook is similar to a Python function.

In standard Python, if you change a variable, the console doesn't automatically re-print the value. In React, **State** is a special variable that React "watches." When the state changes, React immediately re-renders (refreshes) the UI to reflect that change.

It allows your application to remember things (like a list of words fetched from a DB) between renders.

```javascript
const [words, setWords] = useState<Word[]>([]);
```

The `Word[]` is a TypeScrit generic and it tells the compiler: "This state will specifically hold a list (array) of objects that follow the `Word` interface".

The `([])` initialises the state with an empy list.

## useEffect

This function handles Side Effects. In a pure function, you input $A$ and get $B$. A "Side Effect" is anything that happens outside the function, like fetching data from an external API (your FastAPI backend).

```javascript
export default function Home() {
  // 1. State Management: 'words' stores the data, 'loading' handles the UI spinner while the words are loaded from DB
  const [words, setWords] = useState<Word[]>([]);
  const [loading, setLoading] = useState(true);

  // 2. Data Fetching: Request words from the FastAPI backend service
  const fetchWords = async () => {
    try {
      const response = await fetch("http://localhost:8000/words/");
      const data = await response.json();
      setWords(data);
    } catch (error) {
      console.error("Error fetching words:", error);
    } finally {
      setLoading(false); // Set to false after loading words or an error occured
    }
  };

  // 3. Effect Hook: This runs fetchWords() once as soon as the page loads
  useEffect(() => {
    fetchWords();
  }, []);

  return()
```

In the above code, the function `Home()` is called from ReactJS everytime the UI needs to be updated. If we don't use `useEffect`, as soon as the data are fetched from the database, the `Home()` would be triggered again, creating an infinite loop.

## React Props

React components use props to communicate with each other. Every parent component can pass some information to its child components by giving them props.

```js
import { getImageUrl } from "./utils.js";

function Avatar({ person, size }) {
  return (
    <img
      className="avatar"
      src={getImageUrl(person)}
      alt={person.name}
      width={size}
      height={size}
    />
  );
}

export default function Profile() {
  return (
    <div>
      <Avatar
        size={100}
        person={{
          name: "Katsuko Saruhashi",
          imageId: "YfeOqp2",
        }}
      />
      <Avatar
        size={80}
        person={{
          name: "Aklilu Lemma",
          imageId: "OKS67lh",
        }}
      />
      <Avatar
        size={50}
        person={{
          name: "Lin Lanying",
          imageId: "1bX5QH6",
        }}
      />
    </div>
  );
}
```

The parent component `Profile` is passing props to its child component `Avatar`, which are `size` and `person`.

## React Hook Form

### Introduction

The React Hook Form allows us to create simple UI form React components that can be integrated in any website.

Let's now look at an example of the a React Hook Form `frontend/src/components/AddWordModal.tsx`.

```tsx
import { WordFormValues, wordSchema } from "@/lib/wordSchema";
import { zodResolver } from "@hookform/resolvers/zod";
import { PlusCircle } from "lucide-react";
import { useState } from "react";
import { useForm } from "react-hook-form";

// Properties how page.tsx talks to AddWordModal
interface AddWordModalProps {
  onWordAdded: () => void; // Callback to refresh the table
}

export default function AddWordModal({ onWordAdded }: AddWordModalProps) {
  // Controls whether to show AddWord UI form (initially set to False -> Not show)
  const [isOpen, setIsOpen] = useState(false);

  // Reach Hook Form
  const {
    register, // Register input data and apply validation
    handleSubmit, // Receive form data after validation
    reset, // Clear form
    formState: { errors },
  } = useForm<WordFormValues>({
    resolver: zodResolver(wordSchema), // Schema validation
    defaultValues: { gender: "none", category: "noun" },
  });

  const onSubmit = async (data: WordFormValues) => {
    try {
      const response = await fetch("http://localhost:8000/words/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        reset(); // Clear form
        setIsOpen(false); // Close the UI form upon submitting new word to be added
        onWordAdded(); // Trigger table refresh
      }
    } catch (error) {
      console.error("Failed to add word:", error);
    }
  };

  return (
    <>
      <button
        onClick={() => setIsOpen(true)}
        className="flex items-center gap-2 bg-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-700 transition-colors"
      >
        <PlusCircle className="w-5 h-5" /> Add New Word
      </button>

      {isOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50">
          <div className="bg-white p-6 rounded-xl shadow-xl w-full max-w-md">
            <h2 className="text-xl font-bold mb-4">Add German Word</h2>
            <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
              <div>
                <label className="block text-sm font-medium">German Word</label>
                <input
                  {...register("word")}
                  className="w-full border p-2 rounded"
                />
                {errors.word && (
                  <p className="text-red-500 text-xs">{errors.word.message}</p>
                )}
              </div>

              <div>
                <label className="block text-sm font-medium">Translation</label>
                <input
                  {...register("translation")}
                  className="w-full border p-2 rounded"
                />
                {errors.translation && (
                  <p className="text-red-500 text-xs">
                    {errors.translation.message}
                  </p>
                )}
              </div>

              <div className="flex justify-end gap-3 mt-6">
                <button
                  type="button"
                  onClick={() => setIsOpen(false)}
                  className="text-gray-500"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="bg-indigo-600 text-white px-4 py-2 rounded"
                >
                  Save Word
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </>
  );
}
```

### AddWordModalProps (React Props)

```js
interface AddWordModalProps {
  onWordAdded: () => void; // Callback to refresh the table
}
```

It is declaring an interface that acts as a React Props.
It has a single property that as the prefix `on` which is a common convertion for event handlers. The property is of type **function** and this function takes **no arguments**. The return type is `void`.

It essentially says _"this component expects to receive a function called onWordAdded, which takes no input and returns nothing."_.

It defines a contract saying that whoever uses the `AddWordModal` component must pass it a function `(onWordAdded)` to call after a word is successfully added.

In the `page.tsx`, it used to immediately call the function `fetchWords` after using the `AddWordModel` component. It creates an immediate event handler that calls the second function:

```js
{
  /* Pass fetchWords so the modal can refresh the table after adding a new word */
}
<AddWordModal onWordAdded={fetchWords} />;
```

### AddWordModal (Function)

Export a function `AddWordModal` which has only one parameter. The specific property being extracted from the incoming object (the props). Instead of writing `props.onWordAdded` inside the function body, destructuring lets you use `onWordAdded` directly.

### isOpen (useState)

The `useState` defined `const [isOpen, setIsOpen] = useState(false);` is used in order to set the visibility of the form (a.k.a., open and close it when needed).

### Reach Hook Form Core (useForm)

The function `useForm` use the destructuring in order to retrieve 4 different elements needed in the Hook Form:

- `register` - It retrieves the input data and apply the validation. This is a function you apply to your HTML `<input>` tags. It "connects" the input to the form logic so the library can track what the user types.
- `handleSubmit` - Receive form data after the validation. This is a "wrapper" function. It first runs the Zod validation we created. If the data is valid, it then executes your onSubmit function. If invalid, it stops the submission and shows errors.
- `reset` - It clears the form.
- `formState: { errors }` - This is an object that React Hook Form updates in real-time. If Zod says "Translation is required," the errors object will suddenly contain a message for the translation field.

```js
const {
  register, // Register input data and apply validation
  handleSubmit, // Receive form data after validation
  reset, // Clear form
  formState: { errors },
} = useForm <
WordFormValues >
{
  resolver: zodResolver(wordSchema), // Schema validation
  defaultValues: { gender: "none", category: "noun" },
};
```

The `resolver` tells what Zod object to use for the validation.
