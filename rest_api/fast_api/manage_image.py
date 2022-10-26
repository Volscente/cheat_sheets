# Import Standard Libraries
from fastapi import FastAPI, UploadFile, File
import cv2

app = FastAPI()


@app.post('/file')
def upload_image(image_file: UploadFile = File(...)):

    image = cv2.imread(image_file.filename)

    return {'image_shape': image.shape}