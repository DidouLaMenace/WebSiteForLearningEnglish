from flask import Flask,render_template,request
from backend.content.selectvoc import theme_selected_voc
from backend.content.exams import question_for_exams_voc

app=Flask(__name__)

theme_voc=["Animals","Gardening","Astronomy","Physical description","Family and Friends","Fruits and vegetables","Computer science","In the house", "Weather", "The human body","Hobbies","Nationality","Science","TOEIC"]
theme_voc_img=["animaux.png","jardinage.png","astronomie.png","descriptionphysique.png","famille.png","legumes.png","informatique.png","maison.png","meteo.png","corpshumain.png","loisirs.png","nationalite.png","la-science.png","toeic.png"]

theme_gram=["Present Simple","Present Continuous","Preterit","Past continuous","Present Perfect","Present Perfect Continuous","Past Perfect","Future Simple","Future Continuous","Modals","Comparative","Superlative"]

theme_culture = ["Monarchy","Industrial Revolution","Commonwealth","World Wars","Religious History","Sports and Leisure"]


@app.route("/")
def page_accueil():
    return render_template("accueil/english.html")

@app.route("/culture&history")
def edit2021():
    nb_of_culture_theme = len(theme_culture)
    return render_template("cult/culture.html",theme_culture=theme_culture,nb_of_culture_theme=nb_of_culture_theme)

@app.route("/grammar")
def edit2022():
    nb_of_grammar_theme=len(theme_gram)
    return render_template("gram/grammar.html",theme_gram=theme_gram,nb_of_grammar_theme=nb_of_grammar_theme)

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

@app.route("/train-grammar")
def card_gram_theme():
    theme_selected = request.args.get("selected_theme")
    all_card_theme = theme_selected_voc(theme_selected)
    question = all_card_theme[0]
    answer = all_card_theme[1]
    return render_template("gram/stack-gram.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)

@app.route("/train-culture&history")
def card_cult_theme():
    theme_selected = request.args.get("selected_theme")
    all_card_theme = theme_selected_voc(theme_selected)
    question = all_card_theme[0]
    answer = all_card_theme[1]
    return render_template("cult/stack-cult.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)

@app.route("/exams",methods=["GET","POST"])
def exams():
    listforexams=question_for_exams_voc()
    vocfrenchexams=[]
    vocenglishexams=[]
    for i in range(len(listforexams)):
        vocfrenchexams.append(listforexams[i][0])
        vocenglishexams.append(listforexams[i][1])
    return render_template("exams/exams.html",lenlistforexams=len(listforexams),vocfrenchexams=vocfrenchexams,vocenglishexams=vocenglishexams)

if __name__=="__main__":
    app.debug=True
    app.run()