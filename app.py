from flask import Flask,render_template,request
from backend.content.selectvoc import theme_selected_voc
from backend.content.exams import question_for_exams_voc,verifyExams

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

@app.route("/train-vocabulary",methods=["GET","POST"])
def card_voc_theme():
    theme_selected = request.args.get("selected_theme")
    all_card_theme = theme_selected_voc(theme_selected)
    question = all_card_theme[0]
    answer = all_card_theme[1]
    return render_template("voc/stack-voc.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)

@app.route("/card-gram-theme")
def card_gram_theme():
    return render_template("gram/stack-gram.html")

@app.route("/card-culture-theme")
def card_cult_theme():
    return render_template("cult/stack-cult.html")

@app.route("/exams",methods=["GET","POST"])
def exams():
    listeforexams=question_for_exams_voc()
    vocfrenchexams=[]
    vocenglishexams=[]
    for i in range(len(listeforexams)):
        vocfrenchexams.append(listeforexams[i][0])
        vocenglishexams.append(listeforexams[i][1])
    return render_template("exams/exams.html",lenlisteforexams=len(listeforexams),vocfrenchexams=vocfrenchexams,vocenglishexams=vocenglishexams)

@app.route("/exams-result",methods=["GET","POST"])
def exams_result():
    listofUserAnswer=[]
    for i in range(10):
        listofUserAnswer.append(request.form.get("Answer"+str(i)))
    return render_template("exams/exams-result.html")

if __name__=="__main__":
    app.debug=True
    app.run()