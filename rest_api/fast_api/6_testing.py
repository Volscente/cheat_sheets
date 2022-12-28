# Import Standard Libraries
import os
import pytest
import json
import numpy as np
import cv2

from typing import List

from fastapi import FastAPI, UploadFile, File
from fastapi.testclient import TestClient

# Instance FastApi object
app = FastAPI()

# Instance TestClient object
test_client = TestClient(app)


@app.post('/upload_image/')
async def upload_image(image_file: UploadFile = File(...,
                                                description='Image file from which detect the object')):
    """
    Upload an image and returns the Blob shape

    Args:
        image_file: UploadFile request body image file

    Returns:
        blob_shape: Tuple[int] Blob shape
    """

    # Read the 'SpooledTemporaryFile' in image_file.file.read() as Numpy Array
    numpy_array = np.frombuffer(image_file.file.read(), np.uint8)

    # Read OpenCV Image
    image = cv2.imdecode(numpy_array, cv2.IMREAD_UNCHANGED)

    # Read blob from image
    blob = cv2.dnn.blobFromImage(image=image,
                                 size=(416, 416),
                                 scalefactor=1 / 255.,
                                 swapRB=True,
                                 crop=False)

    return {'blob_shape': blob.shape}


@pytest.mark.parametrize('test_file, expected_output', [
    ('./../../computer_vision/yolo/images/dog_image_1.jpeg', [1, 3, 416, 416]),
])
def test_detect_object(test_file: str,
                       expected_output: List[int]):

    """
    Test the function packages.rest_api.rest_api.detect_object

    Args:
        test_file: String test file path
        expected_output: Tuple[int] expected detected class

    Returns:
    """

    # Define the File to upload
    files = {"image_file": open(test_file, "rb")}

    # Retrieve the response
    response = test_client.post("/upload_image/", files=files)

    # Parse the response as JSON
    json_response = json.loads(response.content.decode('utf-8'))

    assert json_response['blob_shape'] == expected_output
