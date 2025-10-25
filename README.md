# End-To-End-ML-project-Boston-House-price-prediction-
An end-to-end ML project covering dataset understanding, preprocessing, model training, and serving predictions via a FastAPI application. It includes model serialization with pickle, Git/GitHub version control, CI/CD automation using GitHub Actions, Docker containerization, and final deployment using Docker.

## Features

-  FastAPI backend for real-time prediction  
-  Dockerized API (portable & platform-independent)  
-  ML model served via REST API (`/predict`)  
-  Tested using Python `requests` client  

---

##  Tech Stack

| Component | Technology |
|-----------|------------|
| Backend API | FastAPI (Python) |
| Model | Trained ML Regression Model |
| Containerization | Docker |

---

## How to Run the API (Docker)

Make sure **Docker Desktop is running**, then:

```bash
docker pull oudarjateamalpha/house-prediction:latest
docker run -it --rm -p 8000:8000 oudarjateamalpha/house-prediction:latest
```
