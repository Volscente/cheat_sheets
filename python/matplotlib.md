# Setup Parameters

## Adjust figure size
``` python
# Set matplotlib figure size
plt.rcParams["figure.figsize"] = (20,9)
```

# Image

## Show Image
``` python
# Show image
plt.imshow(image)
plt.title('<title>')
plt.axis('off')
plt.show()
```

## Show Blob Image
``` python
# Show Blob
plt.imshow(blob_image[0, 0, :, :])
plt.title('Blob')
plt.axis('off')
plt.show()
```
