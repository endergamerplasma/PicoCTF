import requests

r = requests.head("http://mercury.picoctf.net:28916/")
print(r.headers)
