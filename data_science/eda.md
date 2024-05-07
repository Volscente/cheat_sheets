# General
## Shapes Information & Null Values Information
``` python
from colorama import Style, Fore

# Define Colors
black = Style.BRIGHT + Fore.BLACK
magenta = Style.BRIGHT + Fore.MAGENTA
red = Style.BRIGHT + Fore.RED
blue = Style.BRIGHT + Fore.BLUE
reset_colors = Style.RESET_ALL

# Print shapes information
print(f'{blue}Data Shapes:'
      f'{blue}\n- Train Data     -> {red}{train_data.shape}'
      f'{blue}\n- Original Data  -> {red}{original_data.shape}'
      f'{blue}\n- Test Data      -> {red}{test_data.shape}\n')
      
# Print null values information
print(f'{blue}Data Columns with Null Values:'
      f'{blue}\n- Train Data     -> {red}{train_data.isnull().any().sum()}'
      f'{blue}\n- Original Data  -> {red}{original_data.isnull().any().sum()}'
      f'{blue}\n- Test Data      -> {red}{test_data.isnull().any().sum()}\n')
```

# Correlation
## Feature-Target Correlations
It is quite important to show the correlation between each feature and the target variable.
- **Avoiding Data Leakage** - It there a correlation of 1.0 between a feature and the label, that might be *leaking* 
information about the target. Thi would mislead the model.
- **Ensuring Meaningful Relationships** - If a feature has a correlation close to 0, that might have a weak linear relationship
with the target. It is not necessarily useless, but it does introduce challenges:
  - Model might struggle to make accurate prediction
  - Overfitting risk of the model to the noise introduced by such low-meaningful features
  - It is complex to demonstrate non-linear relationships.
