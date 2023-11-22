# Introduction
## Definition
Recommendation system is an umbrella term that collects every piece of the system that produces recommendations. Including the model, the data pipeline, the data collection and the data streaming ingestion.

Sometimes, we think about recommendation only in the sense of items recommended to a user. However, especially in marketing, the other way around is also true: recommending potential interested users to a product.

## Goal
The main goal of any recommendation system is to reduce the overload of information that the user is subjected to while, for example, looking at a product catalog. Given the amount of items, it is not feasible for the user to look through them all. A recommendation system is able to filtering that huge amount of information for just what the user might be interested to.

## Types
### Content-based Filtering
This recommender uses the information about the product in order to recommend it to the user. For example, recommending the most rated film among a category that a specific user likes. This recommendation is based on the product information (most rated) and then it is personalised on the specific user preferences (category that they like).

### Collaborative Filtering
It learns about similarity between items and users, in order to recommend the most appropriate element. It practice, it recommends an item to a user that other similar users liked. That's why it is *"Collaborative"*, because it uses information from other similar users in order to construct the recommendation. It is thus based on *"Interactions"* of the users.