import sqlite3

dbUsers = sqlite3.connect("users.db")
c = dbUsers.cursor()

def add_user(name, email, password):
    c.execute("SELECT rowid, * FROM User WHERE UserName = (?) and UserPassword = (?)", (name, password))
    items = c.fetchall()
    if not items:
        c.execute("INSERT INTO User VALUES ((?), (?), (?) ) ", (name, email, password))
        return True
    else:
        return False # "Это имя пользователя уже используется."

def check_user(name, email, password):
    c.execute("SELECT rowid, * FROM User WHERE UserName = (?) and UserPassword = (?)", (name, password))
    items = c.fetchall()
    if items:
        return True
    else:
        return False # "Неверный логин или пароль."

c.execute("""CREATE TABLE User (
UserName text,
UserEmail text,
UserPassword
)""")
c.execute("INSERT INTO User VALUES ('Alex', 'sobaka@mail.com', 'qwerty' ) ")
c.execute("SELECT * FROM User")
print(c.fetchall())
name = 'Alex'
email = '12@csd'
password = 'qwerty'
c.execute("SELECT rowid, * FROM User WHERE UserName = (?) and UserPassword = (?)", (name, password))
items = c.fetchall()
if not items:
   c.execute("INSERT INTO User VALUES ((?), (?), (?) ) ", (name, email, password))
dbUsers.commit()

c.execute()

dbUsers.close()