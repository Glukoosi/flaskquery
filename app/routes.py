from flask import render_template, flash, redirect, request
from app import app, db
from app.forms import Form
from app.models import Model, Admin
from datetime import datetime, timedelta
from flask_basicauth import BasicAuth
import os

app.config['BASIC_AUTH_USERNAME'] = os.environ.get("ADMIN_USER") or 'admin'
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get("ADMIN_PASSWORD") or 'helevetinhyvasalasana' # TODO: this could be somewhere else
appurl = os.environ.get("URL")
basic_auth = BasicAuth(app)

reserved = ['admin', '']


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()

    nowtime = datetime.now()


    entries = Model.query.all()
    admin = Admin.query.first().adminpass


    if form.validate_on_submit():
        new = True
        url = form.url.data
        short = form.short.data
        expiration = nowtime + timedelta(days=31)
        public = form.public.data

        if short in reserved: #OR not valid short url ??? glukoos ples
            flash('Lyhenne ei saatavilla')
            return render_template('index.html', title='asd.otit.fi', form=form, entries=entries)

        if form.premium.data:
            if form.premiumpass.data != admin:
                flash('Väärä salasana. :(')
                return render_template('index.html', title='asd.otit.fi', form=form, entries=entries)
        else:
            short = 'asd/' + short

        for entry in entries:
            if entry.short == short:
                if entry.url == url:
                    flash('lyhenne uusittu!')
                    new = False
                    if entry.public != public:
                        flash('Listausta ei voida muuttaa :(')
                        public = entry.public

                else:
                    if datetime.strptime(entry.expiration, '%Y-%m-%d %H:%M:%S.%f') > nowtime:
                        flash('Lyhenne jo käytössä :(')
                        return render_template('index.html', title='asd.otit.fi', form=form, entries=entries)
                    else:
                        db.session.delete(entry)
        if new:
            flash('Lyhenne lisätty')
        sub = Model(
            short=short,
            url=url,
            expiration=expiration,
            public=public
        )

        db.session.add(sub)
        db.session.commit()
        return redirect(appurl)
    return render_template('index.html', title='asd.otit.fi', form=form, entries=entries)




@app.route('/admin', methods=['GET', 'POST'])
@basic_auth.required
def admin():
    entries = Model.query.all()

    if Admin.query.first():
        admin = Admin.query.first().adminpass
    else:
        admin = "huutistaglukoosille"


    nowtime = datetime.now()

    if request.form:

        if request.form["adminpass"]:
            db.session.query(Admin).delete()

            sub = Admin(
                adminpass=request.form["adminpass"]
            )

            db.session.add(sub)



        for entry in entries:
            if str(entry.id) in request.form.keys():
                if request.form[str(entry.id)] == "perma":
                    entry.expiration = nowtime + timedelta(days=999999)
                    flash(entry.short + " is now permanent")

                elif request.form[str(entry.id)] == "prolong":
                    entry.expiration = datetime.now() + timedelta(days=31)
                    flash(entry.short + " is now continued")

                elif request.form[str(entry.id)] == "delete":
                    flash("removed " + entry.short)
                    db.session.delete(entry)
        db.session.commit()
        return redirect(appurl + '/admin')

    return render_template('admin.html', title='asd admin', appurl=appurl, admin=admin,
                           entries=entries, nowtime=nowtime)


@app.route('/<shorturl>')
def premium(shorturl):
    return go_url(shorturl)

@app.route('/asd/<shorturl>')
def pleb(shorturl):
    return go_url('asd/' + shorturl)


def go_url(shorturl):
    entries = Model.query.all()
    for entry in entries:
        if entry.short == shorturl:
            return redirect(entry.url)
    flash('Osoite ei vienyt mihinkään!')
    return redirect(appurl)