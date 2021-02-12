from flask import Flask, render_template,request,jsonify,flash
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key="super secret key"
client=MongoClient('localhost',27017)
db=client.user
collection= db.login
collection1=db.customer
collection2=db.item


@app.route('/')
def root():
    return render_template('layout.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/confirm',methods=['POST','GET'])
def confirm():

        n=request.form.get('username')
        e = request.form.get('email')
        p = request.form.get('password')
        test=collection.find_one({"email":e})
        if test:
            flash("username already registered ")
            return render_template("signup.html")
        else:
            flash("username registered successfully")
            collection.insert({"username":n,"email":e,"password":p})
            return render_template("login.html",username=n,email=e,password=p)


@app.route('/login.html')
def login():
    return render_template('login.html')


@app.route('/mainpage.html')
def mainpage():
    return render_template('mainpage.html')


@app.route('/customer.html')
def customer():
  return render_template('customer.html')


@app.route('/new.html')
def new():
    return render_template('new.html')


@app.route('/submit',methods=['POST','GET'])
def submit():
    fn = request.form.get('fname')
    ln = request.form.get('lname')
    add = request.form.get('adress')
    num = request.form.get('number')
    eml = request.form.get('email')
    ob = request.form.get('Openingbalance')
    collection1.insert_one({"fname":fn,"lname": ln, "adress": add,"email": eml, "number": num, "Openingbalance": ob})
    return render_template('customer.html',fname=fn,lname=ln,adress=add,email=eml,number=num,Openingbalance=ob)


@app.route('/new customer submit',methods=['POST','GET'])
def newcustomersubmit():
    idnum = request.form.get('idnum')
    idname = request.form.get('idname')
    itemdis = request.form.get('itemdis')
    oq = request.form.get('oq')
    unit = request.form.get('unit')
    wl = request.form.get('wl')
    collection2.insert_one({"itemid":idnum,"itemname": idname, "item discription": itemdis,"opening Quality": oq, "unit": unit, "warehouse location": wl})
    return render_template('inventory.html',idnum=idnum,idname=idname,itemdis=itemdis,oq=oq,unit=unit, wl=wl)


@app.route('/inventory.html')
def inventory():
    return render_template('inventory.html')


@app.route('/new item.html')
def newitem():
    return render_template('new item.html')


@app.route('/invoice.html')
def invoice():
    return render_template('invoice.html')


@app.route('/script.js')
def script():
    return render_template('script.js')


@app.route('/expenses.html')
def expenses():
    return render_template('expenses.html')


@app.route('/main.js')
def main():
    return render_template('main.js')


if __name__ == '__main__':
    app.run(debug=True)