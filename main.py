from flask import Flask,render_template, request
from algo import Movie_rec

app = Flask(__name__)
MR = Movie_rec

@app.route("/")
def home():
    # a = MR.Knn(input("Enter the input:"))
    return render_template("Home.html")

@app.route("/Home", methods=['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
        tsl = MR.Knn()
        # print(tsl)
        return render_template("Home.html",result = result,tsl=tsl)

if __name__ == '__main__':
    app.run(debug=True)