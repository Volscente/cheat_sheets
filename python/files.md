# Read File

## Read Single Column File as List

Sample File:
``` txt
dog
cat
human
```

``` python
# Open the file and read each line into a list
with open(file_path, 'r') as file:
    list = [line.strip() for line in file.readlines()]
```