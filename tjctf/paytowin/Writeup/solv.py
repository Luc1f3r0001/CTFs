import requests
from base64 import b64encode, b64decode
import json
import hashlib


url = "https://pay-to-win.tjc.tf/"
og_data = "eyJ1c2VybmFtZSI6ICJoYWkiLCAidXNlcl90eXBlIjogImJhc2ljIn0="
og_hash = "70ea705483abf5e899932de256904154a30c9d95a17800ed1b0dda17af41d633"
def hash(data):
    return hashlib.sha256(bytes(data, 'utf-8')).hexdigest()

c=0
def crack():
    for i in range(0xFFFFFF):
        r = hex(i)[2:]
        data = {
            "username": "hai",
            "user_type": "basic"
        }
        b64data = b64encode(json.dumps(data).encode())
        data_hash = hash(b64data.decode() + r)
        if og_data == b64data.decode() and og_hash == data_hash:
            print(r)
            return r
        else:
            i=i+1
            if i%1000000==0:
                print(i)

def cook(a):
    data = {
        "username":"hai",
        "user_type":"premium"
    }
    b64data = b64encode(json.dumps(data).encode())
    data_hash = hash(b64data.decode() + a)
    print("data = ",b64data,"hash = ",data_hash)

cook(crack())
