import sqlite3

def verifyExams(listofUsersAnswer,listofExpectAnswer):
    assert len(listofUsersAnswer)==len(listofExpectAnswer)

    resultList=[]

    for index in range(0,len(listofUsersAnswer)):
        if listofUsersAnswer[index].upper()==listofExpectAnswer[index].upper() :
            resultList.append("true")
        else :
            resultList.append("false")
    
    return resultList

def question_for_exams_voc():
    card = sqlite3.connect('./backend/bd/question.db',check_same_thread=False)
    card_curs = card.cursor()
    list_question_for_exams = list(card_curs.execute("SELECT question,answer FROM card WHERE id_field=1 ORDER BY RANDOM() LIMIT 10"))
    print(clean_list(list_question_for_exams))
    return clean_list(list_question_for_exams)

def clean_list(liste):
    liste_clean=[(tup[0].strip().upper(), tup[1].strip().upper()) for tup in liste]
    return liste_clean
