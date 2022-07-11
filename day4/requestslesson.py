import requests
response=requests.get('http://www.python.org/dowloads/')
text=response.text
print(text)
