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
### Quantiles
``` python
# Return the 0.5 quantile
np.quantile(data['column'], 0.5)
```
### Quartiles
``` python
# Return the quartiles
np.quantile(data['column'], [0, 0.25, 0.5, 0.75, 1])
```
### Interquanrtile Range (IQR)
``` python
from scipy.stats import iqr
iqr(data['column'])
```