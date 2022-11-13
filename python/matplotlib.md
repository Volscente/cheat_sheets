# Setup Parameters

## Adjust figure size
``` python
# Set matplotlib figure size
plt.rcParams["figure.figsize"] = (20,9)
```

# Image

## Show Image
``` python
# Show Image
image = mpimg.imread(image_path)
plt.axis('off')
plt.imshow(image)
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

# Matrix

## Plot Matrix with Colorbar
``` python
plt.matshow(matrix, 
            cmap='gray')
plt.colorbar()
```
