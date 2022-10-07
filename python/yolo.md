# Utils Functions

## Draw Bounding Boxes
```python
def draw_bounding_bow(image: np.ndarray, 
                      class_id: int, 
                      point_1: Tuple[float, float], 
                      point_2: Tuple[float, float]) -> None:
    """
    Draw a bounding box over the passed image from the points 1 and 2
    
    Parameters:
        image: numpy.ndarray of image shape (n, m, 3)
        class_id: Integer of class color
        point_1: Tuple of floats for x and y coordinates
        point_2: Tuple of floats for x and y coordinates
    
    Returns:
        Draw bounding box over the image
    """
    
    # Retrieve the label
    label = classes[class_id]
    
    # Retrieve the color
    color = class_colors[class_id]
    
    # Draw the bounding box
    cv2.rectangle(image, 
                  point_1, 
                  point_2, 
                  color, 
                  2)
    
    # Put the text over the bounding box
    cv2.putText(image, 
                label, 
                (point_1[0]-10, point_1[1]-10), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.5, 
                color, 
                2)
```
