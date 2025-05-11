import json
from django.db import models
import requests

from mysite import settings

def make_post_request(url, data, headers):
    try:
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()  # Assuming the response is in JSON format
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

class Avenger(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=36, primary_key=True)