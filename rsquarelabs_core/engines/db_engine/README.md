# db_engine 

db_engine is a class that gives does the database operations across the tool. Its a wrapper for database [sqlite](https://www.sqlite.org/). 
Read http://www.tutorialspoint.com/sqlite/sqlite_overview.htm for more info on sqlite and its implementations. 

Here is the tutorial for using sqlite with python https://docs.python.org/2/library/sqlite3.html

## How to use 

### Create a new table 

If you want to create a new table, just create the table structure in tables.sqlite file, do the below
```
In DBEngine.do_connect() method 

# execute sql command 
self.conn.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
              
```

To access the methods inside DBEngine create an `db_object = DBEngine('/<path>/database.db')`


### Inserting data

```
db_object = DBEngine('/<path>/database.db')
cur = db_object.do_insert("INSERT INTO projects (title)\
                VALUES('%s')" %(project_data["title"]))
```



### Selecting an item 

```
db_object = DBEngine('/<path>/database.db')
t = ('RHAT',)
data = db_object.do_select('SELECT * FROM stocks WHERE symbol=?', t)

[ WARNING: never do c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol), its INSECURE ]

# if you want to get the first one object
print data.fetchone()

# if you want to access all the objects
for datum in data:
    print datum[0], datum[1]
    
```

### Updating an item

added soon


### deleting an item

added soon



