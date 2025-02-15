# Definition
Recommendation system is an umbrella term that collects every piece of the system that produces recommendations. Including the model, the data pipeline, the data collection and the data streaming ingestion.

Sometimes, we think about recommendation only in the sense of items recommended to a user. However, especially in marketing, the other way around is also true: recommending potential interested users to a product.

# Goal
The main goal of any recommendation system is to reduce the overload of information that the user is subjected to while, for example, looking at a product catalog. Given the amount of items, it is not feasible for the user to look through them all. A recommendation system is able to filtering that huge amount of information for just what the user might be interested to. This ultimately leads to improving the user decision-making process.

# Types     
## Content-based Filtering
This recommender uses the information about the product in order to recommend it to the user. For example, recommending a film to a user that is very similar to another film the user has "highly" rated. It is possible to use explicit and implicit feedbacks from the user in order to understand the rating of a movie (when not explicitly given).

This approach does not take into account the information coming from other users. This heavily relies on how you construct the features representing that item.

### User & Item Embeddings
A crucial aspect of Content-based filtering is the capacity of measure the similarity between two items. In this case, embeddings come really helpful, because they can represent an item through a numeric feature vector.

Once the embeddings are in place, a simple dot product between two items can give a similarity score. This requires that both the User and Item embeddings have the same dimensions. Each dimension of the embedding represents a feature.

Dot products is a greast tool, but it does not scale well with huge data.

The best way to build User & Item Embeddings to overcome the scale problem is to learn them from the data and compress them to find the best generalities to rely on (**Latent Factors**). In this way, the total amount of space required would be `latent_factors * (number_users + number_items)`.

The number of latent factors should alwas be less than `(U * V)/(2(U+V))` where `U` is the number of users and `V` is the number of items.

#### Example
```python
# 2-D Dimensional Embedding
# 1. Children - Adult
# 2. Artfilm - Blockbuster
items = [
    (-1, 1), # Shrek is for children (-1) and is a blockbuster (1)
    (1, 1) # Batman the Dark Knight
]

# The user embedding represents how much they like Children/Adult and Artfilm/Blockbuster movies
users = [
    (0.1, 1) # It does not like Children, but likes Blockbuster movies
    (0.7, 0.5) # It quite likes Children and Blockbuster movies
]
# Perform the dot product to obtain the user preference
user_1_preference_film_1 = np.dot(items[0], users[0]) # -0.9
```

## Collaborative Filtering
### User Interaction Tables
It learns about similarity between items and users, in order to recommend the most appropriate element. It practice, it recommends an item to a user that other similar users liked. That's why it is *"Collaborative"*, because it uses information from other similar users in order to construct the recommendation. It is thus based on *"Interactions"* of the users through the so called **User Interaction Table**.

This approach is independent from the features used to represent an item, leading to less engineering effort in such a direction. It involves heavy matric factorization, which does not rely on any previously constructed features.

### Factorization
#### Definition
However, the User Interaction Table is very sparse. So it is important to use a Matrix Factorization approach to shrink it into two smaller matrices:
- **User Factors**
- **Item Factors**

Through the above two matrices, it is possible to take a User ID, multiply it by the Item Factors and obtain the ratings of that user for all the items. Also the other way around it is possible: all the ratings for all the users for a single item.

#### Computation
These two matrices are an approximation and are computed by minimize a cost function, for example the Squared Error between the original User Interaction Table and the Dot Product between the User Factors and the Item Factors. This can be achieved through:
- **SGD** - Flexible and parallelizable, but slow. It does not capture unobserved interactions pairs
- **ALS** - It works only for Least Squares, it is parallelizable and it is faster. It does capture unobserved interactions pairs. It first computes the User Factors while keeping the Item Factors constant. That's why it is called "Alternating".

In order to handle unobserved interaction pairs, some of the techniques are:
- **WALS** - It uses weights
- **ALS** - Ingores missing interactions
- **SVD** - It sets them to zero

##### WALS (Weighted Alternating Least Squares)
It is based on ALS, an algorithm that does not need labels, but only the ratings matrix organized into rows and columns. The weights in this WALS algorithm can be used to encode features like the revenue of an item, so that most profitable items would be recommended more.

It iteratives fix U and computes V, then does the other way around, until convergence.

## Knowledge-based
They are based about the knowledge about the users, items and recommendation criteria. It is used in situation when there are not much previous interaction with certain items. For example, while selling high value houses: you would not have much previous or similar data about that. That's why the user is asked for specific preferences, before making recommendations.

## Deep Neural Network
They are very flexible, since they can be used to predict the rating, the interactions or even the next item. Using for example the user features, predict the rating of a movie like a standard regression problem. Or it is possible to predict the next movie, like a classification problem.

## Context-Aware Recommendation Systems (CARS)
A user is not just a user and an item is not just an item. The context of why a user choose an item, when and how, is very important too. Such contenxt can be expressed as additional feauteres, like `Where: [Home, Theater, Event]`.

There are three types of CARS algorithms:
- **Contextual Prefiltering** - It filters data before computing the *User Interaction Matrix*. For example, it might filter every interaction happened on the weekend.
- **Contextual Postfiltering** - It works the other way around: first compute the *User Interaction Matrix* and then filters by the context.
- **Contextual Modeling** - It is a classic ML model.

# Pitfalls
- Especially in Collaborative Filtering, the matrix factorization might lead to a very sparse and skewed matrix.
- The **Cold Start** problem arises, when there are not enough information about the user or the interactions. It affects both new users in the system and new items added to the catalog.

