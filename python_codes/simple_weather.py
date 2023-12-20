import requests

r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=ad379e648427e15fd5eb9aff68fd854e')

print(r)
print("\n")
d = r.json()
for entry in d.items():
    print(entry)