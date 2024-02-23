import flask

app = flask.Flask(__name__)


# Renders: 

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():

    def valid_login(name, password):
        if name == "admin" and password == "12345":
            return True
        else:
            return False

    def log_user(name):
        return flask.render_template("login.html", login=name)
    

    myError = ""
    if flask.request.method == "POST":
        if valid_login(flask.request.form['name'], flask.request.form['password']):
            return log_user(flask.request.form['name'])
        else:
            myError = "Invalid name/password"

    return flask.render_template("login.html", error=myError)
