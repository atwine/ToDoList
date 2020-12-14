from flask import Flask, render_template, redirect, url_for, request, redirect, g,session

#these are the models from before.
import model

app = Flask(__name__)

#we need a secret KEY
app.secret_key = 'atwine-gwerU78h'

username = ''
user = model.check_users()#this checks the user


#what happens before before_request
@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username'] #this calls an empty session as per username which is empty


# 1|Gordon|Ramsy
# 2|Ironman|Tonny
# 3|Atwine|12345

#this is the login page
@app.route('/',methods = ['GET','POST']) #this is like how you see : www.google.com
def home():
        if request.method == 'POST':
            session.pop('username', None) #first you clear the session that there could be before loggin in.
            areyouuser = request.form.get('username') #pick the username from the form.
            pwd = model.checkpwd(areyouuser) #check the password of the username
            if request.form.get('password') == pwd:
                session['username'] = request.form.get('username')
                return redirect(url_for('dashboard')) #if the password is correct then take them home.
        return render_template('login.html', message ="Please Try Again: There is A mistake")#if not then take them to the index.html page.

#home
@app.route('/homepage',methods = ['GET']) #this is like how you see : www.google.com
def homepage():
        return render_template('home.html')

#aboutus page
@app.route('/aboutus', methods = ['GET','POST'])
def aboutus():
    return   render_template('aboutus.html')

#dashboard page
@app.route('/dashboard',methods = ['GET','POST'])
def dashboard():

    if request.method == 'POST':
        itemname = request.form.get(itemname)
        itemdescription = request.form.get(itemdescription)
        new_task = model.Todo(itemname,itemdescription)
    else:
        tasks = model.fetch()
        return render_template('dashboard.html', tasks = tasks)

#admindashboard page
@app.route('/admindashboard',methods = ['GET','POST'])
def admindashboard():
    return render_template('admindashboard.html')



#privacy page
@app.route('/privacy', methods = ['GET'])
def privacy():
    return render_template('privacy.html')
#signup page
@app.route('/signup', methods = ['GET','POST'])
def signup():
    if request.method == 'GET':
        message = 'Please Sign Up!'
        return   render_template('signup.html', message = message)
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        return render_template('signup.html', message = model.signup(username, password))

#termsofuse page
@app.route('/termsofuse', methods = ['GET'])
def termsofuse():
    return render_template('termsofuse.html')

#this takes you to the already logged in session of the application.
@app.route('/getsession')
def getsession():
    if 'username' in session:
        return session['username']
    return redirect(url_for('login'))

#logout of the application.
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('home'))





#we need a page for the admin to log in.
@app.route('/admin', methods = ['GET','POST'])
def admin():
    if request.method == 'POST':
        session.pop('username', None) #first you clear the session that there could be before loggin in.
        areyouuser = request.form.get('username') #pick the username from the form.
        pwd = model.checkpwd_admin(areyouuser) #check the password of the username
        if request.form.get('password') == pwd:
            session['username'] = request.form.get('username')
            return redirect(url_for('admindashboard')) #if the password is correct then take them home.
    return render_template('admin.html', message ="Please Try Again: There is A mistake")#if not then take them to the index.html page.


if __name__ == '__main__': #this helps you run the app
    app.run(port = 7000, debug = True)
    #when you declare debug = True when you make changes you don't have to keep terminating the server.
