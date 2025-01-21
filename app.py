import Projet
from flask import Flask, render_template               #Importation du fichier python principal
app = Flask(__name__)                                  #Importation des bibliothèques

@app.route('/')
def fonction():
    return render_template('Projet.html')              #Connection du fichier python avec flask

@app.route('/heure.html')
def fonction2():                                       #Connection du fonction 'heure' avec Flask
    return render_template("heure.html")               #La fonction est lancé avec l'action de l'utilisateur au page web
                                                       
@app.route('/minuteur.html')
def fonction3():
    if request.method == "POST":
        minute = request.form.get("minute")            #Connection du fonction 'minuteur' avec Flask
        return Projet.countdown(minute)                #La variable 'minute' prend la réponse saisie par l'utilisateur
    return render_template("minuteur.html")            #au site web et lance la fonction python.
 
@app.route('/', methods =["GET", "POST"])

@app.route('/alarme.html')
def fonction4():
    if request.method == "POST":
        heure = request.form.get("heure")              #Connection du fonction 'alarme' avec Flask
        minute = request.form.get("minute")            #Les variables 'heure' et 'minute' prennent la réponse saisie
        return Projet.alarme(heure, minute)            #par l'utilisateur au site web et lance la fonction python.
    return render_template("alarme2.html")
    
@app.route('/chronometre.html')
def fonction5():
    if request.method == "POST":                       #Connection du fonction chronomètre avec Flask
        return Projet.c()                              #La fonction est lancé avec l'action de l'utilisateur
    return render_template("chronometre.html")         #au page web.

@app.route('/temperature.html')
def fonction6():
    if request.method == "POST":                       #Connection du fonction température avec Flask
        return Projet.temp()                           #La fonction est lancé avec l'action de l'utilisateur
    return render_template("temperature.html")         #au page web.

def main(): 
    if __name__ == '__main__':                         #La fonction principale qui fait tourner tout le fichier python 
        app.run(debug=True)                            #quand l'application web est ouverte.