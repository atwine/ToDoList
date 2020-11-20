from flask import Flask, render_template, redirect, url_for, request, redirect, g,session

#these are the models from before.
import model

app = Flask(__name__)

#we need a secret KEY
app.secret_key = 'atwine-gwerU78h'

#this is the login page
@app.route('/',methods = ['GET','POST']) #this is like how you see : www.google.com
def home():
        return render_template('login.html')
#home
@app.route('/homepage',methods = ['GET']) #this is like how you see : www.google.com
def homepage():
        return render_template('home.html')

        #we need a link to the dashboard in this html page.

#aboutus page
@app.route('/aboutus', methods = ['GET'])
def aboutus():
    return   render_template('aboutus.html')

#dashboard page
@app.route('/dashboard',methods = ['GET'])
def dashboard():
    return render_template('dashboard.html')

#privacy page
@app.route('/privacy', methods = ['GET'])
def privacy():
    return render_template('privacy.html')
#signup page
@app.route('/signup', methods = ['GET'])
def signup():
    return render_template('signup.html')

#termsofuse page
@app.route('/termsofuse', methods = ['GET'])
def termsofuse():
    return render_template('termsofuse.html')

if __name__ == '__main__': #this helps you run the app
    app.run(port = 7000, debug = True)
    #when you declare debug = True when you make changes you don't have to keep terminating the server.
