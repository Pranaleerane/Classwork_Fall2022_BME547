#%%
import requests


r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/pmr15")
print(r.status_code)
print(r.text)


r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F7")
print(r.status_code)
print(r.text)


r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F4")
print(r.status_code)
print(r.text)


out_data = {"Name": "pmr15", "Match": "No"}
r = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check",
                  json = out_data)
print(r.status_code)
print(r.text)
