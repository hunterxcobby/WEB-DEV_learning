from django.test import TestCase
import requests

# Create your tests here.
requests = requests.get('http://127.0.0.1:8000')

print(requests.json())