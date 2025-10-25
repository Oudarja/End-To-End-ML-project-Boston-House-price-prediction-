# here the dockerized API is being tested
# Here dockerized api will be consumed
import requests
import json

url = "http://localhost:8000/predict"

sample_data = {
        "CRIM": 0.1,
        "ZN": 18.0,
        "INDUS": 2.31,
        "CHAS": 0,
        "NOX": 0.538,
        "RM": 6.575,
        "AGE": 65.2,
        "DIS": 4.09,
        "RAD": 1,
        "TAX": 296.0,
        "PTRATIO": 15.3,
        "B": 396.9,
        "LSTAT": 4.98
    }


json_data = json.dumps(sample_data)

response = requests.post(url, data=json_data)

prediction = response.json().get("predicted_price")

print(f"Predicted house price: {prediction}")

# Predicted house price: 29.942805298376744