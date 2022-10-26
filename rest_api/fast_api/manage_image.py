# Import Standard Libraries
from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np

app = FastAPI()


@app.post('/file')
def upload_image(image_file: UploadFile = File(...)):

    # image = cv2.imread(image_file.file.read())

    nparr = np.frombuffer(image_file.file.read(), np.uint8)

    image = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

    return {'image_file_type': image.shape}