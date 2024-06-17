import requests

r = requests.get('http://www.uwu.ac.lk/')

print(r.status_code)
print(r.text)
print(r.url)
