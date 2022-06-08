from io import BytesIO
import numpy as np
from PIL import Image
from src.merged_model import CompletedModel
#import easyocr;

model = None


def load_model():
    model = CompletedModel()
    return model


def predict(image: Image.Image):
    global model
    if model is None:
        model = load_model()

    img = np.asarray(image)
    print("test: ", img)
    result = model.predict(img)
    # reader = easyocr.Reader(["vi","en"])
    # result = reader.readtext(image)
    return result


def read_image_file(file) -> Image.Image:
    image = Image.open(BytesIO(file))

    return image