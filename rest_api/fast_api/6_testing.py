# Import Standard Libraries
import os
import pytest
import json

from fastapi.testclient import FastApi, TestClient, UploadFile, File


# Instance FastApi object
app = FastApi()

# Instance TestClient object
test_client = TestClient(app)


@app.post('/upload_image/')
async def upload_image(image: UploadFile = File(...,
                                                description='Image file from which detect the object')):
    """
    Upload an image and returns the shape

    Args:
        image: UploadFile request body image file

    Returns:

    """


@pytest.mark.parametrize('test_file, expected_output', [
    ('./data/test_images/image_1.jpeg', 'dog'),
    ('./data/test_images/image_2.png', 'cow'),
    ('./data/test_images/image_3.png', 'apple'),
])
def test_detect_object(test_file: str,
                       expected_output: str):

    """
    Test the function packages.rest_api.rest_api.detect_object

    Args:
        test_file: String test file path
        expected_output: String expected detected class

    Returns:
    """

    # Define the File to upload
    files = {"image": open(test_file, "rb")}

    # Retrieve the response
    response = test_client.post("/detect_object/", files=files)

    # Parse the response as JSON
    json_response = json.loads(response.content.decode('utf-8'))

    assert expected_output == json_response['detected_object']