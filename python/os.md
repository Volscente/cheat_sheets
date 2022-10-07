# Environment Variables

## List Environment Variables

``` python
print(os.environ)
```

# Directories

## Change Current Working Directory

``` python
# Set root path
os.chdir(os.environ['<environment_variable'])
```

# Files

## Check if File Exists
``` python
# Check whatever the '<filename>' file is not present and download it
if not os.path.isfile(<file_path>):
    
    # Download '<filename>'
    urlretrieve(<file_url>, <file_path>)
```
