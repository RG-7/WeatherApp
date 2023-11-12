# Project Weather App

import urllib.request
import json
import os

city = input("Enter the city name : ")
api_key = "YOUR_API_KEY"

url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

with urllib.request.urlopen(url) as response:
   data = response.read()
   json_data = json.loads(data)

temperature = json_data["current"]["temp_c"]  
text = f"Temperature at {city} is {temperature} degree Celcius"
print(text)
os.system(f'PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\');"')

