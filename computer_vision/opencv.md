# Read Image

# Read Image from URL
``` python
import cv2
import numpy as np

# Retrieve string of the image from the url
image_string = requests.get(dish_images.iloc[0]['url']).content

# Convert the string to bytes
image_bytes = np.frombuffer(image_string, np.uint8)

# Read the image through OpenCV
image_cv2 = cv2.imdecode(image_bytes, cv2.IMREAD_UNCHANGED)
```

# Show Image

## Show Single Image
``` python
import cv2

# Read image
image_cv2 = cv2.imread(<image_path>)

# Show image
cv2.imshow('image', image_cv2)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.waitKey(1)
```
