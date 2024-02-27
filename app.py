import flask
import mysql.connector

app = flask.Flask(__name__)


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
    database="db"
)
cursor = db.cursor()
table = "table"



# Renders: 

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():

    def valid_login(name, password):
        if name in cursor.execute(f"Select name in {table}"):
            if password == cursor.execute(f"Select password in table where name = {name}"):
                return True
            else:
                return False
        else:
            return False

    myError = ""
    if flask.request.method == "POST":
        
        if valid_login(flask.request.form['name'], flask.request.form['password']):
            return flask.render_template("index.html", login=True, username=flask.request.form['name'])
        else:
            myError = "Invalid name/password"


    return flask.render_template("login.html", error=myError)



@app.route("/register", methods=["GET", "POST"])
def register():

    def createAccount(name, email, password):
        cursor.execute(f"insert into {table} (name, email, password) values (\'{name}\', \'{email}\', \'{password}\')")
        db.commit()

        return flask.render_template("index.html", login=True)


    myError=""
    if flask.request.method == "POST":
        receives = {"name": flask.request.form['name'], "email": flask.request.form['email'], "password": flask.request.form['password']}
        cursor.execute(f"Select email from {table}")
        if ( receives["email"] ) not in cursor.fetchall():
            createAccount(receives["name"], receives["email"], receives["password"])
        else:
            myError = "Email already taken"


    return flask.render_template("register.html", error=myError)
