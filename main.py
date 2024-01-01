from model import model_pipeline
from question import answer
from fastapi import FastAPI, UploadFile
from PIL import Image
import io
app = FastAPI()

@app.get('/')
def root():
    return {"hello":"world"}

@app.post('/ask')
def ask(text:str,image:UploadFile):
    content = image.file.read()
    image = Image.open(io.BytesIO(content))
    # image = Image(image.file)
    result = model_pipeline(text,image)
    return {"result":result}

@app.get('/hello')
def qanda():
    result = answer()
    return result