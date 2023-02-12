from flask import Flask, render_template

#Kreiranje flask aplikacije
app = Flask(__name__)

#kreiraj rutu
@app.route('/')
def hello():
    moje_ime = "Uroš"
    naredba_safe = "ovo je <strong>Boldiran</strong> tekst"
    omiljena_pica = ["papričice", "kečap", "suvo meso", "rukola", 34]
    return render_template("index.html", moje_ime=moje_ime, naredba_safe=naredba_safe, omiljena_pica=omiljena_pica)
    #return "<h1>Zdravo svete</h1>"

# localhost:5000/user/Marko
@app.route('/user/<ime>')
def user(ime):    
    #return "<h1>Zdravo {} !!!</h1>".format(name)
    return render_template("user.html", ime=ime)

#kreiraj Error stranicu

#Nepostojeći URL
@app.errorhandler(404)
def stranica_nije_nadjena(e):
    return render_template("404.html"), 404

#greška na serveru
@app.errorhandler(500)
def greska_servera(e):
    return render_template("500.html"), 500
