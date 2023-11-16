# Data Preparation
## Definition
The goal of the data preparation process in a NLP project is to manipulate the text data so that they can be used and read from the machine during the model training and inference.

The steps to prepare data are:
1. Raw Text
2. Tokenization - Split the text into single tokens (e.g., words)
3. Preprocessing - Apply standard preprocessing operations, such as punctation removal
4. Text Representation - Convert the texts into vectors

## Tokenization
It divides the text into smaller pieces, called *Tokens*. Different tokenization strategies might not be suited for all language. For example, using whitespaces do not work with Chinese.

Every tokenization strategy has its pros and cons.

## Preprocessing
This step might involve different transformations:
- **Lowercasing**
- **Stemming (keep root of the word)**
- Stopword Removal
- Normalization

## Text Representation
It includes several techniques to represent text in a numeric format while retaining its meaning and being able to be passed into an ML model.

Such techniques include:
- **One-hot Encoding**
- **Bag-of-words** - A vector is created with the length of the words in the vocabulary. The values in the vector represent the frequency of that word in the text. (e.g., *"A dog is chasing a dog"* - Vocabulary: [dog, chase, person, my, cat, run] - Vector: [2, 1, 0, 1, 0, 0])

# Technologies
## TensorFlow TextVectorization API
It offers a text processing layer that maps text features to integer sequences.
It includes:
- Proprocessing
- Tokenization
- Vectorization