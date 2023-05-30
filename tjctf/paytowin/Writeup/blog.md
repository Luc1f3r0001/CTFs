# Pay To Win

**The Challenge**
This challenge had a login page. When we put a username into it it will laod a web page saying that you're not a premium user.

**The Exploit**
Here the page had two cookies, data and hash in which data was base64 encoded and had basically
```py
    data = {
        "username":username,
        "user_type":"basic"
    }
```
and hash was 
```py
    users[username] = hex(random.getrandbits(24))[2:]

    data_hash = hash(b64data.decode() + users[username])
```
Here the user[username] is getrandbits(24) which is can be easily bruteforced.*crack() in solv.py*

After getting this value we can make our own data and hash which contains user_type as premium and give it as cookies.

Now we have the premium page but the page shows "Due to supply chain issues, we cannot provide you with a flag... Sorry, and thanks for supporting this site". Here in the page it shows
```py
    theme_name = request.args.get('theme') or 'static/premium.css'
    return render_template('premium.jinja',theme_to_use=open(theme_name).read())
```
Here it takes a value as theme parameter which will be openned by the site So there you can give the flag file and get the flag as the template in the site.
The file = /secret-flag-dir/flag.txt

**Flag**
Flag = tjctf{not_random_enough_64831eff}