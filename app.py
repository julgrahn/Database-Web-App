from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres123@localhost/age_collector"
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
        if db.session.query(Data).filter(Data.email == email).count() == 0:
            data = Data(email, age)
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")
        return render_template("index.html", 
        text = "That email address is already stored!")

if __name__ == '__main__':
    app.debug = True
    app.run()