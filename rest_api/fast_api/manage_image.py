# Import Standard Libraries
from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.post('/file')
def upload_image(image_file: UploadFile = File(...)):

    return {'file_name': image_file.filename}