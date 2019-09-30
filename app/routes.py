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

    starttime = datetime(2019, 9, 24, 13, 37, 00)
    endtime = datetime(2019, 10, 10, 23, 59, 59)
    nowtime = datetime.now()


    entries = Model.query.all()

    fuksit = []
    prot = []
    hallitus = []
    koops = []
    teekkarit = []

    for entry in entries:
        if entry.status == "fuksi":
            if entry.public:
                name = entry.name
            else:
                name = "Fuksinorsu"
            if len(fuksit) >= 30:
                name += " Varasijalla"
            fuksit.append(name)
        elif entry.status == "pro":
            if entry.public:
                name = entry.name
            else:
                name = "Pronorsu"
            if len(prot) >= 6:
                name += " Varasijalla"
            prot.append(name)
        elif entry.status == "hallituslainen":
            if entry.public:
                name = entry.name
            else:
                name = "varmaa sandalf"
            if len(fuksit) >= 9:
                name += " Varasijalla"
            hallitus.append(name)
        elif entry.status == "koops":
            if entry.public:
                name = entry.name
            else:
                name = "koopsnorsu"
            if len(fuksit) >= 1:
                name += " Varasijalla"
            koops.append(name)
        elif entry.status == "teekkari":
            if entry.public:
                name = entry.name
            else:
                name = "Remminorsu"
            if len(fuksit) >= 1:
                name += " Varasijalla"
            teekkarit.append(name)


    if form.validate_on_submit():
        flash('Kiitos ilmoittautumisesta!')
        sub = Model(

            name=form.name.data,
            mail=form.mail.data,
            phone=form.phone.data,
            start=form.start.data,
            status=form.status.data,
            public=form.public.data,
            datetime=nowtime
        )

        db.session.add(sub)
        db.session.commit()
        return redirect(appurl+"#Lähetetty")
    return render_template('index.html', title='Fucu Ilmo',
                           fuksit=fuksit,
                           prot=prot,
                           hallitus=hallitus,
                           koops=koops,
                           teekkarit=teekkarit,
                           starttime=starttime,
                           endtime=endtime,
                           nowtime=nowtime,
                           appurl=appurl,
                           form=form)

@app.route('/admin', methods=['GET'])
@basic_auth.required
def admin():
    entries = Model.query.all()
    return render_template('admin.html', title='FUCU admin', appurl=appurl,
                           entries=entries)