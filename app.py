from flask import Flask,render_template,request

app=Flask(__name__)

##### TOURNOI #####
@app.route("/")
def page_accueil():
    return render_template("tournoi.html")

### Exercice ###
@app.route("/culture")
def edit2021():
    return render_template("culture.html")

@app.route("/grammar")
def edit2022():
    return render_template("grammar.html")

@app.route("/vocabulary")
def editsuivante():
    return render_template("vocabulary.html")

@app.route("/card-voc-theme")
def card_voc_theme():
    return render_template("stack-voc.html")

@app.route("/card-gram-theme")
def card_gram_theme():
    return render_template("stack-gram.html")

@app.route("/card-culture-theme")
def card_cult_theme():
    return render_template("stack-cult.html")

if __name__=="__main__":
    app.debug=True
    app.run()