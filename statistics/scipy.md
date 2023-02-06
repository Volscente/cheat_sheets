# Z-Score
## Compute the Z-Score of several feature across the 'quality' categorical variable classes
``` python
# Import Standard Libraries
from scipy.stats import zscore

# Compute the Z-Score of the features across different 'quality' values
# NOTE: .iloc[:, 1:-1] excludes the first column 'ID' and the last one 'quality'
z_scores = train_data.iloc[:, 1:-1].groupby(train_data['quality'], 
                                            group_keys=True).apply(zscore)
```
