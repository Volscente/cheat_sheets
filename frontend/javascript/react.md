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
