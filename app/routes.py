from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import RegForm, RegSwagForm
from .models import Reg
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegForm()

    starttime = datetime(2018, 1, 19, 12, 00, 00)
    endtime = datetime(2018, 2, 2, 23, 59, 00)
    nowtime = datetime.now()

    limit = 64
    maxlimit = 100

    partisipants = Reg.query.all()
    count = Reg.query.count()

    if form.validate_on_submit() and count <= maxlimit:
        flash('Kiitos ilmoitautumisestasi')
        sub = Reg(
            name=form.name.data,
            email=form.email.data,
            representative=form.representative.data,
            greeting=form.greeting.data,
            food=form.food.data,
            alcohol=form.alcohol.data,
            gambina=form.gambina.data,
            avec=form.avec.data,
            free=form.free.data,
        )
        db.session.add(sub)
        db.session.commit()
        return redirect(url_for('index'))
    elif form.is_submitted() and count > maxlimit:
        flash('Ilmoittautuminen on täynnä')
    return render_template('swag.html', title='#swag vujuilmo', partisipants=partisipants, count=count, starttime=starttime, endtime=endtime, nowtime=nowtime, limit=limit, form=form)


@app.route('/jasenistonilmo', methods=['GET', 'POST'])
def jasenisto():
    form = RegSwagForm()

    starttime = datetime(2017, 1, 19, 12, 00, 00)
    endtime = datetime(2018, 2, 2, 23, 59, 00)
    nowtime = datetime.now()

    limit = 64
    maxlimit = 100

    partisipants = Reg.query.all()
    count = Reg.query.count()

    if form.validate_on_submit() and count <= maxlimit:
        flash('Kiitos ilmoitautumisestasi')
        sub = Reg(
            name=form.name.data,
            email=form.email.data,
            representative='#swag',
            greeting=form.greeting.data,
            food=form.food.data,
            alcohol=form.alcohol.data,
            gambina=form.gambina.data,
            avec=form.avec.data,
            free=form.free.data,
        )
        db.session.add(sub)
        db.session.commit()
        return redirect(url_for('jasenisto'))
    elif form.is_submitted() and count > maxlimit:
        flash('Ilmoittautuminen on täynnä')
    return render_template('swagjasenisto.html', title='#swag vujuilmo (jäsenistö)', partisipants=partisipants, count=count, starttime=starttime, endtime=endtime, nowtime=nowtime, limit=limit, form=form)
