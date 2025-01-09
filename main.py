from flask import Flask,render_template
from algo import Movie_rec

app = Flask(__name__)
MR = Movie_rec()

@app.route("/")
def home():
    # a = MR.Knn(input("Enter the input:"))
    return render_template("Home.html")


if __name__ == '__main__':
    app.run(debug=True)