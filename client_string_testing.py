# %%
import requests


r = requests.get("http://127.0.0.1:5000/until_next_meal/breakfast")
print(r.status_code)
print(r.text)


r = requests.get("http://127.0.0.1:5000/until_next_meal/lunch")
print(r.status_code)
print(r.text)


r = requests.get("http://127.0.0.1:5000/until_next_meal/dinner")
print(r.status_code)
print(r.text)
