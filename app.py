from flask import Flask, render_template, session
# from flaskext.mysql import MySQL
# import pymysql

# mysql =MySQL()
app = Flask(__name__, template_folder='templates')

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'pytestcrud'
app.config['MYSQL_DATABASE_PASSWORD'] = '12345'
app.config['MYSQL_DATABASE_HOST'] = '3306'

# mysql.init_app(app)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
