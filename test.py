import uvicorn
from fastapi import FastAPI, File, UploadFile
from starlette.responses import RedirectResponse
from serve.serve_model import *



image = Image.open(r"D:\id-card\extract-information-from-identity-card\samples\lucquangtri.jpg")
prediction = predict(image)
print(prediction)
