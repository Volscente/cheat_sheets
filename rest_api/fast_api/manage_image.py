# Import Standard Libraries
from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np

# Instance FastAPI object
app = FastAPI()


@app.post('/file')
def upload_image(image_file: UploadFile = File(...)):

    # Read the 'SpooledTemporaryFile' in image_file.file.read() as Numpy Array
    numpy_array = np.frombuffer(image_file.file.read(), np.uint8)

    # Read OpenCV Image
    image = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

    return {'image_file_type': image.shape}
