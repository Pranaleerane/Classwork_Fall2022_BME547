from tkinter import filedialog
import base64
from flask import Flask, request, jsonify
import requests


def upload_image():
    filename = get_image_filename()
    b64_string = convert_file_to_b64(filename)
    print(b64_string)
    result = upload_b64_to_server(b64_string)
    return result


def get_image_filename():
    filename = filedialog.askopenfilename()
    #filename = "1.jpg"
    return filename


def convert_file_to_b64(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string

def upload_b64_to_server(b64_string):
    out_data = {"image": b64_string, "net_id": "pmr15", "id_no": 99}
    r = requests.post("http://vcm-21170.vm.duke.edu/add_image", json =out_data)
    print(r.status_code)
    print(r.text)


def b64_string_to_file(b64_string, filename):
    image_bytes = base64.b64decode(b64_string)
    with open(filename, "wb") as out_file:
        out_file.write(image_bytes)
    return None



if __name__ == '__main__':
    upload_image()