#%%
import requests

def upload_patient_info(patient_name, patient_id, patient_blood_type):

    out_data = {"name": "ann ables","id": 1,"blood_type": "A+"}
    r = requests.post("http://127.0.0.1:5000/new_patient", json =out_data)
    return r.text, r.status_code


test_data = {"id": 1, "test_name": "HDL","test_result": 60}
r = requests.post("http://127.0.0.1:5000/add_test", json = test_data)
print(r.status_code)
print(r.text)
#%%