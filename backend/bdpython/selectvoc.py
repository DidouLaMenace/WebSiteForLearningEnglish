import sqlite3

card = sqlite3.connect('./backend/bd/question.db',check_same_thread=False)

card_curs = card.cursor()

def theme_selected_voc(theme):
    list_card_question = list(card_curs.execute("SELECT question FROM card WHERE sujet='"+theme+"' "))
    list_card_answer = list(card_curs.execute("SELECT answer FROM card WHERE sujet='"+theme+"' "))
    return (clean_list(list_card_question),clean_list(list_card_answer))

def clean_list(liste):
    liste_clean = [x[0].strip().upper() for x in liste]
    return liste_clean