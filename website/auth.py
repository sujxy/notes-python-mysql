from flask import Blueprint 

auth = Blueprint('auth' , __name__) 

@auth.route('/login') 
def login() : 
    return "<h1>Login page</h1> "

@auth.route('/logout') 
def logout() :
    return "<h1>logout</h1> "

@auth.route('/register') 
def register() : 
    return '<h1>Register page</h1> ' 
  