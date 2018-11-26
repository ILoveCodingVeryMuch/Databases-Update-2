from flask import Flask, render_template, redirect, url_for, request
import pymysql
import pymysql.cursors

conn= pymysql.connect(host='localhost', user='root', password='Rainbow.86', db='ProjectTestDBA')
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello,World!'


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/AdminWelcome')
def AdminWelcome():
    return 'You are an admin!'

@app.route('/Search', methods =['GET', 'POST'])
def ManagerHome():
    a = conn.cursor()
    a.execute("CREATE TABLE PurchaseOrder (ItemNa VARCHAR(50), Pri VARCHAR(25), ItemCount INT(50))")
    error = None
    if request.method == 'POST':
        item = request.form['search']
        sql = 'SELECT * FROM ItemTable WHERE ItemName = %s'
        data = a.execute(sql, (item))
        results = data.fetchall()
        return render_template('results.html', table=table)
    else:
        flash('No results found!')
        return redirect(url_for('ManagerHome'))
    return render_template('Search.html', error = error)

@app.route('/results')

@app.route('/VendorHome')
def CustomerHome():
    return 'You are a vendor!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        usern = request.form['username']
        passw = request.form['password']
        a = conn.cursor()
        sql = 'SELECT * FROM UserTable WHERE UserName = %s AND PasswordInf = %s'
        data = a.execute(sql, (usern, passw))
        data2 = a.fetchone()
        if data2[2] == "Admin":
            return redirect(url_for('AdminWelcome'))
        elif data2[2] == "Manager":
            return redirect(url_for('ManagerHome'))
        elif data2[2] == "Vendor":
            return redirect(url_for('VendorHome'))
        #....
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('fancylogin.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)


