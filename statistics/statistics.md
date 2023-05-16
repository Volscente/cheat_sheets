# Descriptive Statistics
## Summarise Data
### Mean
``` python
np.mean(data['column'])
```
### Median
``` python
np.median(data['column'])
```
### Mode
``` python
import statistics
statistics.mode(data['column'])
```
### Mean and Median over GroupBy
``` python
data.groupby('category_column')['numeric_column'].agg([np.mean, np.median])
```
### Mean and Median over Single Column
``` python
data.['numeric_column'].agg([np.mean, np.median])
```