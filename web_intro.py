import requests


# r = requests.get("https://api.github.com/repos/dward2/BME547/branches")
# print(r)
# print(type(r))
# print(r.text)
# if r.status_code:
#     answer = r.json()
#     print(type(answer))
#     for branch in answer:
#         print(branch["name"])
# else:
#     print("bad request: {}".format(r.text))


# output_info = {"name" : "David Ward",
#                 "net_id" : "daw74",
#                 "e-mail" : "david.a.ward@duke.edu"}


# r = requests.post("http://vcm-21170.vm.duke.edu:5000/student",
#                    json = output_info)


# print(r)
# print(r.text)

# r = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
# print(r.text)


output_info = {"user" : "seij001",
               "message" : "hi my name is pranal"}


r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
                    json = output_info)


print(r)
print(r.text)

r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/Pranaleerane")
print(r.text)