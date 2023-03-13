import sqlite3

dico = open("/home/didoulamenace/Documents/Telecom/Anglais/anglais/backend/bd/sports.txt",'r')

con = sqlite3.connect("/home/didoulamenace/Documents/Telecom/Anglais/anglais/backend/bd/question.db")
cur = con.cursor()

liste = dico.readlines()

a=1502

id_field = 3
sujet = "Sports and Leisure"

for i in range(0,len(liste),2):
    question=liste[i]
    answer=liste[i+1]
    query = "INSERT INTO card (sujet,question,answer,id_field) VALUES (?,?,?,?);"
    ajout=(sujet,question,answer,id_field)
    cur.execute(query,ajout)
    a+=1

con.commit()
dico.close()
con.close()
