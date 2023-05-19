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
## Spread Information
### Variance
``` python
# ddof = 1 is for sample variance
# Without ddof, the population variance is computed
np.var(data['column'], ddof=1)
```
### Standard Deviation
``` python
# ddof = 1 is for sample std
# Without ddof, the population std is computed
np.std(data['column'], ddof=1)
```
### Compute Variance and Standard Deviation
``` python
data.groupby('category_column')['column'].agg([np.var, np.std])
```
### Quantiles
``` python
# Return the 0.5 quantile
np.quantile(data['column'], 0.5)
```
### Quartiles
``` python
# Return the quartiles (Two options)
np.quantile(data['column'], [0, 0.25, 0.5, 0.75, 1])
np.quantile(data['column'], np.linspace(0, 1.0, 5)))

# Compute the sixth quantile to divide the data in 5 quintiles
np.quantile(data['column'], np.linspace(0, 1.0, 6)))
```
### Interquanrtile Range (IQR)
``` python
from scipy.stats import iqr
iqr(data['column'])
```
# Probability
## Sample
``` python
# P(x) = Number of possible outcomes for x / Number of total possible outcomes
sales.sample() # Sample one row
sales.sample(2) # Sample two rows - Sample without Replacemet (No name can appear twice)
sales.sample(5, replace=True) #Sample 5 rows - Sample with Replacement (Names can appear more than twice)
```
## Set the Seed
``` python
np.random.seed(10)
```