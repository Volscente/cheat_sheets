# Definition
Recommendation system is an umbrella term that collects every piece of the system that produces recommendations. Including the model, the data pipeline, the data collection and the data streaming ingestion.

Sometimes, we think about recommendation only in the sense of items recommended to a user. However, especially in marketing, the other way around is also true: recommending potential interested users to a product.

# Goal
The main goal of any recommendation system is to reduce the overload of information that the user is subjected to while, for example, looking at a product catalog. Given the amount of items, it is not feasible for the user to look through them all. A recommendation system is able to filtering that huge amount of information for just what the user might be interested to. This ultimately leads to improving the user decision-making process.

# Types
## Content-based Filtering
This recommender uses the information about the product in order to recommend it to the user. For example, recommending a film to a user that is very similar to another film the user has "highly" rated. It is possible to use explicit and implicit feedbacks from the user in order to understand the rating of a movie (when not explicitly given).

This approach does not take into account the information coming from other users. This heavily relies on how you construct the features representing that item.

### Similarity Measurement
A crucial aspect of Content-based filtering is the capacity of measure the similarity between two items. In this case, embeddings come really helpful, because they can represent an item through a numeric feature vector.

Once the embeddings are in place, a simple dot product between two items can give a similarity score.

## Collaborative Filtering
It learns about similarity between items and users, in order to recommend the most appropriate element. It practice, it recommends an item to a user that other similar users liked. That's why it is *"Collaborative"*, because it uses information from other similar users in order to construct the recommendation. It is thus based on *"Interactions"* of the users.

This approach is independent from the features used to represent an item, leading to less engineering effort in such a direction. It involves heavy matric factorization, which does not rely on any previously constructed features.

## Knowledge-based
They are based about the knowledge about the users, items and recommendation criteria. It is used in situation when there are not much previous interaction with certain items. For example, while selling high value houses: you would not have much previous or similar data about that. That's why the user is asked for specific preferences, before making recommendations.

## Deep Neural Network
They are very flexible, since they can be used to predict the rating, the interactions or even the next item.

# Pitfalls
- Especially in Collaborative Filtering, the matrix factorization might lead to a very sparse and skewed matrix.
- The **Cold Start** problem arises, when there are not enough information about the user or the interactions. It affects both new users in the system and new items added to the catalog.