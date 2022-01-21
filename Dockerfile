# Dockerfile, Image, Container
FROM python:3.9.7

WORKDIR /fastapi-app

COPY readReceipt_requirements.txt .

RUN pip install -r readReceipt_requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python
RUN apt-get update
RUN apt install -y libgl1-mesa-glx
RUN apt install -y tesseract-ocr-jpn


COPY ./app ./app

CMD ["python", "./app/main.py"]
