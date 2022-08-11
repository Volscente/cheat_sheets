---
title: "Data Cleaning"
tags: ""
---

# Interquartile Range (IQR)

``` python
# Define the list of columns for which compute the IQR
iqr_columns = ['Year_Birth', 
               'Income', 
               'MntWines', 
               'MntFruits', 
               'MntMeatProducts', 
               'MntFishProducts', 
               'MntSweetProducts', 
               'MntGoldProds', 
               'NumDealsPurchases', 
               'NumWebPurchases',
               'NumCatalogPurchases', 
               'NumWebVisitsMonth']

# Compute Q1 and Q3
q1 = data[iqr_columns].quantile(0.25)
q3 = data[iqr_columns].quantile(0.75)

# Compute the IQR
iqr = q3 - q1

# Compute the lower and upper filtering bounds
lower_filtering_bound = q1 - 1.5*iqr
upper_filtering_bound = q3 + 1.5*iqr

# Filter outliers
data_cleaned_outliers = data[~((data[iqr_columns] < lower_filtering_bound) |(data[iqr_columns] > upper_filtering_bound)).any(axis=1)].reset_index(drop=True)
```
