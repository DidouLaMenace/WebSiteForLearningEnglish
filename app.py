from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def page_accueil():
    return render_template("accueil/english.html")

@app.route("/culture&history")
def edit2021():
    return render_template("cult/culture.html")

@app.route("/grammar")
def edit2022():
    return render_template("gram/grammar.html")

@app.route("/vocabulary")
def editsuivante():
    return render_template("voc/vocabulary.html")

@app.route("/card-voc-theme")
def card_voc_theme():
    return render_template("voc/stack-voc.html")

@app.route("/card-gram-theme")
def card_gram_theme():
    return render_template("gram/stack-gram.html")

@app.route("/card-culture-theme")
def card_cult_theme():
    return render_template("cult/stack-cult.html")

@app.route("/exams")
def exams():
    return render_template("exams/exams.html")

if __name__=="__main__":
    app.debug=True
    app.run()