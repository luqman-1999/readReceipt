from typing import Optional

from fastapi import FastAPI
import uvicorn


app = FastAPI()

import pytesseract
from PIL import Image
import cv2
 
 
img = cv2.imread("./app/receipt.png",cv2.IMREAD_COLOR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
gray = cv2.bilateralFilter(gray, 11, 17, 17) 
 
text = pytesseract.image_to_string(gray, 'jpn')


@app.get("/")
def read_root():
    return {"MUHAMAD LUQMAN HASIF BIN MUHAMAD JASNI A18MJ0074": text}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
    
if __name__ == '__main__':
	uvicorn.run(app, port=8000, host="0.0.0.0")
