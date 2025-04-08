from flask import *
from flask_pymongo import PyMongo
import os
app=Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI", "mongodb://localhost:27017/carZ")
mongo=PyMongo(app)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/booking')
def booking():
    return render_template('booking.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/form1')
def form1():
    return render_template('form1.html')
@app.route('/form2')
def form2():
    return render_template('form2.html')
@app.route('/insert2', methods=['POST'])
def signin():
    username = request.form.get('username')
    password = request.form.get('password')
    user = mongo.db.users.find_one({'username': username, 'password': password})
    if user:
        return f"<h2>Welcome back, {username}!</h2><a href='/home'>Go Home</a>"
    else:
        return "<h2>Invalid credentials. Please try again.</h2><a href='/'>Back</a>"
@app.route('/insert3', methods=['POST'])
def signup():
    username = request.form.get('username')
    password = request.form.get('password')
    existing_user = mongo.db.users.find_one({'username': username})
    if existing_user:
        return "<h2>Username already exists. Please choose another.</h2><a href='/'>Back</a>"
    mongo.db.users.insert_one({'username': username, 'password': password})
    return f"<h2>Account created for {username}!</h2><a href='/'>Sign In</a>"
@app.route('/insert', methods=['POST'])
def insert():
    if request.method =='POST':
        name=request.form["name"]
        gender=request.form["gender"]
        contact=request.form["contact"]
        passengers=int(request.form["passengers"])
        plocation=request.form["plocation"]
        dlocation=request.form["dlocation"]
        purpose=request.form["purpose"]
        mongo.db.rides.insert_one({"name":name, "gender":gender, "contact":contact, "passengers":passengers, "plocation":plocation, "dlocation":dlocation, "purpose":purpose})
        return "<h2>Your booking is confirmed.Your cab will arrive quickly.Have a Safe ride...</h2><br><a href='/booking'>Go Back</a>"
@app.route('/insert1', methods=['POST'])
def insert1():
    if request.method =='POST':
        name=request.form["name"]
        gender=request.form["gender"]
        contact=request.form["contact"]
        passengers=int(request.form["passengers"])
        duration=request.form["duration"]
        dlocation=request.form["dlocation"]
        purpose=request.form["purpose"]
        mongo.db.rentals.insert_one({"name":name, "gender":gender, "contact":contact, "passengers":passengers, "duration":duration, "dlocation":dlocation, "purpose":purpose})
        return "<h2>Your booking is confirmed.Your rented car will arrive quickly.Have a Safe drive...</h2><br><a href='/booking'>Go Back</a>"
if __name__=='__main__':
    app.run(debug=True)
