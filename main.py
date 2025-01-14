from flask import Flask,render_template, request
from algo import Movie_rec

app = Flask(__name__)
MR = Movie_rec

@app.route("/")
def home():
    matlis = MR.all_movies()
    return render_template("Home.html",matlis = matlis)

@app.route("/Home", methods=['POST','GET'])
def result():
    if request.method == 'POST':
        req_name = request.form.get('Movie_Name')
        top_num = request.form.get('Top_num')
        Lom = request.form.get("Lom")
        tsl = MR.all_movies()
        matlis = MR.all_movies()
        
        if Lom:
            tsl,matlis,K = MR.Knn(Lom,req_name,k=int(top_num))
            # print(" THIS IS tsl :",tsl)
            # print(" THIS IS matlis :",matlis)

            return render_template("Home.html",
                                   Lom = Lom,
                                   tsl=tsl,
                                   matlis=matlis,
                                   req_name=req_name,
                                   top_num = K
                                   
                                   )
        
        else:
            return render_template("Home.html",matlis = matlis)
    return render_template("Home.html",matlis = matlis)

if __name__ == '__main__':
    app.run(debug=True)