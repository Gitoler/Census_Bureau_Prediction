"""
Unit test of client deploy api
author: Ung Van Tuan
Date: June 20th 2023
"""

import requests
import json

# Url of the deployed app on render
#url = "https://salary-pred-api.onrender.com/predict/"
url = "https://webpredictsalary.azurewebsites.net/predict/"


# explicit the sample to perform inference on
sample =  {
    "age": 50,
    "workclass": "Private",
    "fnlgt": 234721,
    "education": "Doctorate",
    "marital_status": "Separated",
    "occupation": "Exec-managerial",
    "relationship": "Not-in-family",
    "race": "Black",
    "sex": "Female",
    "capital_gain": 0,
    "capital_loss": 0,
    "hours_per_week": 50,
    "native_country": "United-States"
}

data = json.dumps(sample)
print(data)

# post to API and collect response
response = requests.post(url, data=data )

# display output - response will show sample details + model prediction added
print("response status code", response.status_code)
print("response content:")
print(response.json())