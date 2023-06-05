# Notes

**The challenge**

The challenge had a login, register and user delete page. it used database to store the information. The page will reflect and store the notes the user give.

**The Exploit**

In this the "/" route gave the flag if there is a user present in the database having the user_id given in the session and also if there is no rows in the select statement.ie, 

```py
    app.get('/', (req, res) => {
    if (!req.session.user_id) {
        return res.redirect('/login?e=login%20to%20make%20notes');
    }

    pool.query(`SELECT * FROM notes WHERE user_id = '${req.session.user_id}';`, (err, results) => {
        pool.query(`SELECT * FROM users WHERE id = '${req.session.user_id}';`, (err, users) => {
            res.render('index', { notes: results, user: users[0] || { username: flag } });
        });
    });
    });
```
But there was a delete route. in the delete route. So it is a race condition challenge. 
We will give many requests to make the user and and delete the user and in that very small time the session is there but there is no user in that user_id. Then we will get the flag.
