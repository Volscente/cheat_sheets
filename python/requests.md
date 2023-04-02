# Download
## Download file if does not exist
``` python
from pathlib import Path
from urllib.request import urlretrieve

# Retrieve model file path
model_file_path = Path(os.path.abspath('')).parents[1] / \
                  configuration['text_detection_model_file_path'][0] / \
                  configuration['text_detection_model_file_path'][1]
                  
# Check if the model file is present
if not model_file_path.exists():
    
    # Download the model file
    urlretrieve(configuration['text_detection_model_url'], model_file_path)
```
