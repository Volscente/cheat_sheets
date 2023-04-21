# General
## Shapes Information
``` python
# Define Colors
black = Style.BRIGHT + Fore.BLACK
magenta = Style.BRIGHT + Fore.MAGENTA
red = Style.BRIGHT + Fore.RED
blue = Style.BRIGHT + Fore.BLUE
reset_colors = Style.RESET_ALL

# Print shapes information
print(f'{blue} Data Shapes:'
      f'{blue}\n- Train Data           -> {red}{train_data.shape}'
      f'{blue}\n- Test Data            -> {red}{test_data.shape}'
      f'{blue}\n- Train Original Data  -> {red}{train_original_data.shape}'
      f'{blue}\n- Test Original Data   -> {red}{test_original_data.shape}\n')
```
