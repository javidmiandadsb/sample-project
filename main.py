from flask import Flask, render_template , request,redirect,url_for,jsonify,flash
from pymongo import MongoClient
import pymongo
from flask_jwt_extended import JWTManager,jwt_required,create_access_token
import json
from bson import ObjectId


app = Flask(__name__)
app.secret_key="super secret key"
jwt=JWTManager(app)
app.config["JWT_SECRET_KEY"]="this-is-secret_key"
client=MongoClient('localhost',27017)
db=client.users
collection=db.login

@app.route('/signup')
def home():
    return render_template('signup.html')

@app.route('/confirm',methods=['POST','GET'])
def confirm():

        n=request.form.get('username')
        e=request.form.get('email')
        p=request.form.get('password')
        test=collection.find_one({"email":e})
        if test:
            flash("Username already registered")
            return render_template('signup.html')
        else:
            flash("user name registered Succesfully")
            collection.insert_one({"username":n,"email":e,"password":p})
            return render_template('signup.html', username=n, email=e, password=p)



if __name__ == '__main__':

    app.run(debug=True,port=4919)