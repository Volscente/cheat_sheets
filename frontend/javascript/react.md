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

The Lifecycle: Without useEffect, if you put a fetch() call directly in your component, it would run every single time the component renders, causing an infinite loop. useEffect lets you say: "Run this code only once when the page first loads".
