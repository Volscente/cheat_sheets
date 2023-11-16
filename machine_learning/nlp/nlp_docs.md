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
- Lowercasing
- Stemming (keep root of the word)
- Stopword Removal
- Normalization

# Technologies
## TensorFlow TextVectorization API
It offers a text processing layer that maps text features to integer sequences.
It includes:
- Proprocessing
- Tokenization
- Vectorization