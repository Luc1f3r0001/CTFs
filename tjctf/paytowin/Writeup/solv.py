import requests
from base64 import b64encode, b64decode
import json
import hashlib


url = "https://pay-to-win.tjc.tf/"
og_data = "eyJ1c2VybmFtZSI6ICJoYWkiLCAidXNlcl90eXBlIjogImJhc2ljIn0="
og_hash = "e99f12b369f466cece7d887f4239f5c25a141da52bf72f05c396ad4282c629fd"
def hash(data):
    return hashlib.sha256(bytes(data, 'utf-8')).hexdigest()

c=0
""" def crack():
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
                print(i) """

def cook(a):
    data = {
        "username":"hai",
        "user_type":"premium"
    }
    b64data = b64encode(json.dumps(data).encode())
    data_hash = hash(b64data.decode() + a)
    print("data = ",b64data,"hash = ",data_hash)
cook("c37925")
