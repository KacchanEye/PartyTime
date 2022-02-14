from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
import datetime
from . import db
from .models import Party
from datetime import timedelta

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", user=current_user)


mindate = datetime.datetime.today().date() + timedelta(days=3)


@views.route('/comunione', methods=['GET', 'POST'])
@login_required
def comunione():
    if request.method == 'POST':
        
        #fetch data
        partyDetails = request.form
        
        nbambini = partyDetails['nbambini']
        via = partyDetails['via']
        civico = partyDetails['civico']
        citta = partyDetails['citta']
        cap = partyDetails['cap']
        dataf = datetime.datetime.strptime(partyDetails['dataf'],'%Y-%m-%d').date()
        oini = datetime.datetime.strptime(partyDetails['oini'],'%H:%M').time()
        durata = partyDetails['durata']
        tipo = 'Comunione'
        qualita = partyDetails['qualita']
        
        if qualita == 'Silver':
            tariffa = 5
        elif qualita == 'Gold':
            tariffa = 6
        else:
            tariffa = 7

        prezzo = (float(tariffa)*int(nbambini))*int(durata) #((tariffa*nbambini)*durata))
        
        id1 = current_user.get_id()

        if not via:
            flash("Inserire la Via", category='error')
        elif not civico:
            flash("Inserire il Civico", category='error')
        elif not citta:
            flash("Inserire la Citta'", category='error')
        else:
            new_party = Party(nbambini=nbambini,via=via,civico=civico,citta=citta,cap=cap,dataf=dataf,oini=oini,durata=durata,tipo=tipo,qualita=qualita,prezzo=prezzo,id1=id1)
            db.session.add(new_party)
            db.session.commit()
            flash("Preparati alla festa! Totale " + str(prezzo) + "euro.", category='succes')
            return redirect(url_for('views.ordini'))
        
    
    return render_template("comunione.html", user=current_user, mindate=mindate)

@views.route('/compleanno', methods=['GET','POST'])
@login_required
def compleanno():
    if request.method == 'POST':
        
        #fetch data
        partyDetails = request.form
        
        nbambini = partyDetails['nbambini']
        via = partyDetails['via']
        civico = partyDetails['civico']
        citta = partyDetails['citta']
        cap = partyDetails['cap']
        dataf = datetime.datetime.strptime(partyDetails['dataf'],'%Y-%m-%d').date()
        oini = datetime.datetime.strptime(partyDetails['oini'],'%H:%M').time()
        durata = partyDetails['durata']
        tipo = 'Compleanno'
        qualita = partyDetails['qualita']
        
        if qualita == 'Silver':
            tariffa = 4
        elif qualita == 'Gold':
            tariffa = 5
        else:
            tariffa = 6

        prezzo = (float(tariffa)*int(nbambini))*int(durata) #((tariffa*nbambini)*durata))
        
        id1 = current_user.get_id()

        if not via:
            flash("Inserire la Via", category='error')
        elif not civico:
            flash("Inserire il Civico", category='error')
        elif not citta:
            flash("Inserire la Citta'", category='error')
        else:
            new_party = Party(nbambini=nbambini,via=via,civico=civico,citta=citta,cap=cap,dataf=dataf,oini=oini,durata=durata,tipo=tipo,qualita=qualita,prezzo=prezzo,id1=id1)
            db.session.add(new_party)
            db.session.commit()
            flash("Preparati alla festa! Totale " + str(prezzo) + "euro.", category='succes')
            return redirect(url_for('views.ordini'))
        
    
    return render_template("compleanno.html", user=current_user, mindate=mindate)

@views.route('/matrimonio', methods=['GET','POST'])
@login_required
def matrimonio():
    if request.method == 'POST':
        
        #fetch data
        partyDetails = request.form
        
        nbambini = partyDetails['nbambini']
        via = partyDetails['via']
        civico = partyDetails['civico']
        citta = partyDetails['citta']
        cap = partyDetails['cap']
        dataf = datetime.datetime.strptime(partyDetails['dataf'],'%Y-%m-%d').date()
        oini = datetime.datetime.strptime(partyDetails['oini'],'%H:%M').time()
        durata = partyDetails['durata']
        tipo = 'Matrimonio'
        qualita = partyDetails['qualita']
        
        if qualita == 'Silver':
            tariffa = 7
        elif qualita == 'Gold':
            tariffa = 8
        else:
            tariffa = 9

        prezzo = (float(tariffa)*int(nbambini))*int(durata) #((tariffa*nbambini)*durata))
        
        id1 = current_user.get_id()

        if not via:
            flash("Inserire la Via", category='error')
        elif not civico:
            flash("Inserire il Civico", category='error')
        elif not citta:
            flash("Inserire la Citta'", category='error')
        else:
            new_party = Party(nbambini=nbambini,via=via,civico=civico,citta=citta,cap=cap,dataf=dataf,oini=oini,durata=durata,tipo=tipo,qualita=qualita,prezzo=prezzo,id1=id1)
            db.session.add(new_party)
            db.session.commit()
            flash("Preparati alla festa! Totale " + str(prezzo) + "euro.", category='succes')
            return redirect(url_for('views.ordini'))
        
    
    return render_template("matrimonio.html", user=current_user, mindate=mindate)

@views.route('/misc', methods=['GET','POST'])
@login_required
def misc():
    if request.method == 'POST':
        
        #fetch data
        partyDetails = request.form
        
        nbambini = partyDetails['nbambini']
        via = partyDetails['via']
        civico = partyDetails['civico']
        citta = partyDetails['citta']
        cap = partyDetails['cap']
        dataf = datetime.datetime.strptime(partyDetails['dataf'],'%Y-%m-%d').date()
        oini = datetime.datetime.strptime(partyDetails['oini'],'%H:%M').time()
        durata = partyDetails['durata']
        tipo = 'Misc'
        qualita = partyDetails['qualita']
        
        if qualita == 'Silver':
            tariffa = 6
        elif qualita == 'Gold':
            tariffa = 7
        else:
            tariffa = 8

        prezzo = (float(tariffa)*int(nbambini))*int(durata) #((tariffa*nbambini)*durata))
        
        id1 = current_user.get_id()

        if not via:
            flash("Inserire la Via", category='error')
        elif not civico:
            flash("Inserire il Civico", category='error')
        elif not citta:
            flash("Inserire la Citta'", category='error')
        else:
            new_party = Party(nbambini=nbambini,via=via,civico=civico,citta=citta,cap=cap,dataf=dataf,oini=oini,durata=durata,tipo=tipo,qualita=qualita,prezzo=prezzo,id1=id1)
            db.session.add(new_party)
            db.session.commit()
            flash("Preparati alla festa! Totale " + str(prezzo) + "euro.", category='succes')
            return redirect(url_for('views.ordini'))
        
    
    return render_template("misc.html", user=current_user, mindate=mindate)

@views.route('/ordini', methods=['GET','POST'])
@login_required
def ordini():
    #Party.query.filter_by(idfesta=1).delete()
    #db.session.commit()
    return render_template("ordini.html", user=current_user)

