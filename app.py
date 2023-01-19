from flask import Flask,render_template,request

app=Flask(__name__)

##### TOURNOI #####
@app.route("/")
def page_accueil():
    return render_template("tournoi.html")

### Edition ###
@app.route("/2021")
def edit2021():
    return render_template("edition2021.html")

@app.route("/2022")
def edit2022():
    return render_template("edition2022.html")

@app.route("/edition-suivante")
def editsuivante():
    return render_template("edition-suivante.html")

### Présentation Général ###
@app.route("/Tdl")
def presentation():
    return render_template("presentation.html")

if __name__=="__main__":
    app.debug=True
    app.run()