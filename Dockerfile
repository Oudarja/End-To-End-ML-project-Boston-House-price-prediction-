# This file is used to build a docker image for the ML project
# take python slim image as base image from 
# docker hub
FROM python:3.9-slim


# set working directory to /app
# inside the container
WORKDIR /app


# set working directory in the container
# copy all the files from current directory 
# to /app in the container
COPY . /app

RUN pip install -r requirements.txt
# expose port 8000 for the app

EXPOSE 8000
# command to run the app using uvicorn  
# This runs the FastAPI app located in app/main.py
# 0.0.0.0 means it will be accessible from outside the container
# “Allow incoming connections from anywhere” — including Docker port mapping like:
# docker run -p 8000:8000 your_image
# Then you can access it from your local machine at:
# http://localhost:8000
# run app instance from app module
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]