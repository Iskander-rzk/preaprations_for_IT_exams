from django import forms
import sqlite3

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


dbUsers = sqlite3.connect("users.db")
c = dbUsers.cursor()

class User(forms.Form):
    def __init__(self, username, password, email=None):
        self.username = forms.CharField()
        self.password = forms.CharField(widget=forms.PasswordInput)
        self.email = forms.CharField(widget=forms.EmailInput)
    def add_user(self):
        c.execute("SELECT rowid, * FROM User WHERE UserName = (?) and UserPassword = (?)", (self.username, self.password))
        items = c.fetchall()
        if not items:
            c.execute("INSERT INTO User VALUES ((?), (?), (?) ) ", (self.username, self.email, self.password))
            return True
        else:
            return False # "Это имя пользователя уже используется."

    def check_user(self):
        c.execute("SELECT rowid, * FROM User WHERE UserName = (?) and UserPassword = (?)", (self.username, self.password))
        items = c.fetchall()
        if items:
            return True
        else:
            return False # "Неверный логин или пароль."


dbUsers.close()