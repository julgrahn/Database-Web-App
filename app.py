from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func 

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres123@localhost/age_collector"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://ekgjuedwnzvfao:579cb99e7e9a8a321524b3c22f1125c13f74220f54741dc5f561b57723bee6f5@ec2-54-234-28-165.compute-1.amazonaws.com:5432/d6p1oai37htosk?sslmode=require"

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
            avg_age = db.session.query(func.avg(Data.age)).scalar()
            avg_age = round(avg_age, 1)
            count = db.session.query(Data.age).count()
            send_email(email, age, avg_age, count)
            return render_template("success.html")
        return render_template("index.html", 
        text = "That email address is already stored!")

if __name__ == '__main__':
    app.debug = True
    app.run()