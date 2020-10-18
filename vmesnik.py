import bottle
from model import *

@bottle.get('/')
def osnovna_stran():
    primer = Bisekcija_linearna_funkcija([5,1],[-10,1],6)
    return bottle.template('osnovna_stran.html', primer=primer)



@bottle.post('/izracun/')
def izracun(): 
    funkcija = pretvorba(bottle.request.forms['funkcija'])
    interval = pretvorba(bottle.request.forms['interval'])
    natancnost = int(bottle.request.forms['natancnost'])
    a =  Bisekcija_linearna_funkcija(funkcija, interval, natancnost)
    if a.obstaja_nicla_v_intervalu() is False:
        return bottle.template('jejhata.html')
    else:
        return bottle.template('izracun.html', a=a, interval=interval, natancnost=natancnost)

bottle.run(debug=True, reloader=True)


