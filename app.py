from flask import Flask,render_template,request
from backend.bdpython.selectvoc import theme_selected_voc

app=Flask(__name__)

theme_voc=["Animals","Gardening","Astronomy","Physical description","Family and Friends","Fruits and vegetables","Computer science","In the house", "Weather", "The human body","Hobbies","Nationality","Science","TOEIC"]
theme_voc_img=["animaux.png","jardinage.png","astronomie.png","descriptionphysique.png","famille.png","legumes.png","informatique.png","maison.png","meteo.png","corpshumain.png","loisirs.png","nationalite.png","la-science.png","toeic.png"]
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
    max_number_of_theme=len(theme_voc)
    return render_template("voc/vocabulary.html",theme_voc=theme_voc,theme_voc_img=theme_voc_img,max_number_of_theme=max_number_of_theme)

@app.route("/card-voc-theme",methods=["GET","POST"])
def card_voc_theme():
    theme_selected=request.form.get("selected_theme")
    print("theme" + theme_selected)
    all_card_theme = theme_selected_voc(theme_selected)
    question = all_card_theme[0]
    answer = all_card_theme[1]
    return render_template("voc/stack-voc.html",number_of_cards=len(question),question=question,answer=answer)

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