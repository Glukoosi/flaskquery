from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import Form
from app.models import Model
from datetime import datetime
from flask_basicauth import BasicAuth
import os

app.config['BASIC_AUTH_USERNAME'] = os.environ.get("ADMIN_USER") or 'admin'
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get("ADMIN_PASSWORD") or 'helevetinhyvasalasana' # TODO: this could be somewhere else
appurl = os.environ.get("URL")
basic_auth = BasicAuth(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()

    starttime = datetime(2018, 2, 18, 13, 37, 00)
    endtime = datetime(2020, 3, 15, 00, 00, 00)
    nowtime = datetime.now()


    entries = Model.query.all()

    if form.validate_on_submit():
        flash('Kiitos ilmoittautumisesta!')
        sub = Model(

            name=form.name.data,
            mail=form.mail.data,
            year=form.year.data,
            nonalcoholic=form.nonalcoholic.data,
            food=form.food.data,
            speech=form.speech.data,
            other=form.other.data,
            public=form.public.data,
            datetime=nowtime
        )

        db.session.add(sub)
        db.session.commit()
        return redirect(appurl+"#Lähetetty")
    return render_template('index.html', title='Grand OTiT',
                           entries=entries,
                           starttime=starttime,
                           endtime=endtime,
                           nowtime=nowtime,
                           appurl=appurl,
                           form=form)

@app.route('/admin', methods=['GET'])
@basic_auth.required
def admin():
    entries = Model.query.all()
    return render_template('admin.html', title='Grand OTiT', appurl=appurl,
                           entries=entries)