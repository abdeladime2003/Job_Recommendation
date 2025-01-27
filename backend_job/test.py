import json 
import requests
import time
import pandas as pd
url = "https://84d4-105-158-159-180.ngrok-free.app/api/get-job-offers/?limit=10"
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data['data'])
print(df)
df.to_csv('job.csv', index=False)
