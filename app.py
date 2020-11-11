from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

#this is the home page
@app.route('/',methods = ['GET']) #this is like how you see : www.google.com
def home():
        return render_template('home.html')
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
