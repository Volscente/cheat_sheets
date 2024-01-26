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
- **Stopword Removal**
- **Normalization**

## Text Representation
It includes several techniques to represent text in a numeric format while retaining its meaning and being able to be passed into an ML model.

Such techniques can be divided in macro areas:
- Basic Vectorization
- Word Embeddings
- Transfer Learning

### Basic Vectorization
Altough such techniques are easy to implement and understand, they do not solve the two major requirements:
- Keep the meaning words and relationship between words &rarr; Lack of relationship between words
- Able to be feed in an ML model &rarr; They produce too sparse matrices

Techniques:
- **One-hot Encoding**
- **Bag-of-words** - A vector is created with the length of the words in the vocabulary. The values in the vector represent the frequency of that word in the text. (e.g., *"A dog is chasing a dog"* - Vocabulary: [dog, chase, person, my, cat, run] - Vector: [2, 1, 0, 1, 0, 0]). That is a technique, but you can use also just 0-1 for the presence of the word instead of its frequency.

### Word Embeddings
It is a technique to encode text into meaningful vectors, which are low dimension and dense. They dimension of each vector can vary from 1 to 4. It fullfils the NLP requirements:
- Keep the meaning words and relationship between words &rarr; Similar words have close vectors
- Able to be feed in an ML model &rarr; Dense Vectors

#### word2vec
It is not a single algorithm, bus a family of model architectures used to learn word embeddings from large datasets. They use the context of the word in order to compute its vector representation.

Two famous algorithms of word2vec are:
- **Continuous bag-of-words (CBOW)** - It predicts the center word given the context.
- **Skip-gram** - It predicts the context given the center word.

The following is an example using TensorFlow:
```python
import tensorflow as tf
from tensorflow.keras.layers import Embedding

# Embed a 1000 word vocabulary into 5 dimensions
embedding_layer = Embedding(1000, 5)

result = embedding_layer(tf.constant([1, 2, 3]))
result.numpy()

result = embedding_layer(tf.constant([[0, 1, 2], [3, 4, 5]]))
```

### Transfer Learning
It is possible to use an laready trained model for computing the embeddings.

# Technologies
## Spacy
It is the *de facto* standard for **Named Entity Recognition** and **Speech Tagging** in Python.

## TensorFlow TextVectorization API
It offers a text processing layer that maps text features to integer sequences.
It includes:
- Proprocessing
- Tokenization
- Vectorization

# Sentence Similarity
## Definition
It defines a metric to measure how similar two sentences are. It's quite useful for many other NLP applications.

## Data Preparation
The very first step is to use a model like BERT to convert the text into a collection of dense vectors. The output of this operation a huge number of vectors with an high dimensionality. Let's say 768 vectors with 512 dimensions each. There's the need to have a more condensed **Sentence Embedding**.

One technique could be to just take the mean of all the dimension, in order to end up with 768 1-D vectors.


# Advanced NLP Models
## Encoder-Decoder Architecture
Taking as example the Language Translation, it consists of two neural networks:
- **Encoder** - It can be an LSTM/GRU that ingestes the input text, one word a time, and encode it
- **Decoder** - It takes the encoded text and map it to the corresponding translation

It does not however scale well with the vocabulary size.

It can be further improved by adding an **Attention Mechanism**:
- It passes more data from the encoder (hidden data)
- It adds an extra step before producing its output

## Transformer
This technology is able to capture the context of a text, which is fundamental in many NLP problems, and adds it to the Encoder-Decoder architecture.

Several Encoders and Decoders are stacked up together. Both Encoder and Decoder have a Self Attention layer and a Feedforward layer. However, the Decoder has in between also a Encoder-Decoder attention.

## BERT
The *Bidirectional Encoder Representations from Transformers* is a trained Transformer model.

It is very powerful since it can handle very long input context and it has been trained on Wikipedia and BookCorpus. 

It is trained on two different tasks, thus is a multi-task objective:
- **Masked Language Modeling (MLM)** - In this task, some words of the sentence are masked and the model tries to predict those masked words
- **Next Sentence Prediction (NPS)** - In this task, the model tries to predict what is the next sentence given two input sentences (Next Sentence & Not Next Sentence)

It works on both sentence-level and token-level tasks.

The input embeddings of BERT includes:
- **Token Embeddings** - The vector representation of the input text (it includes a initial special token called "CLS", that identify the Classificaiton task)
- **Segment Embeddings** - It defined where is the separator between the input sentence A and the input sentence B
- **Position Embeddings** - It incorporates the order of the input sequences