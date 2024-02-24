import flask
import mysql.connector

app = flask.Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=""
)
cursor = db.cursor()


# Renders: 

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():

    def valid_login(name, password):
        if name in cursor.execute("Select name in table"):
            if password == cursor.execute(f"Select password in table where name = {name}"):
                return True
            else:
                return False
        else:
            return False

    def log_user(name):
        return flask.render_template("index.html", login=True, username=name)
    
    def existAccount(username, email):
        account = cursor.execute(f"Select username, email where username={username}")
            


    def createAccount(username, email, password):
        pass

    myError = ""
    if flask.request.method == "POST":
        
        if valid_login(flask.request.form['name'], flask.request.form['password']):
            return log_user(flask.request.form['name'])
        else:
            myError = "Invalid name/password"

        if existAccount(flask.request.form['username_register'], flask.request.form['email_register']):
            createAccount(flask.request.form['username_register'], flask.request.form['email_register'], flask.request.form['password_register'])
            log_user(flask.request.form['username_register'])
        else:
            myError = "name already taken/ email already exists"


    return flask.render_template("login.html", error=myError)
