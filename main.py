from flask import Flask, render_template, url_for, request
from flask import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:*******@localhost/age_collector"
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), unique = True)
    age = db.Column(db.Integer)

    def __init__(self, email, age):
        self.email = email
        self.age = age
        

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods = ["POST", "GET"])
def success():
    if request.method == "POST":
        email = request.form["email_name"]
        age = request.form["age_name"]
        return render_template("success.html")

if __name__ == '__main__':
    app.debug = True
    app.run()