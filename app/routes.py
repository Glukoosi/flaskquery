from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import Form
from app.models import Model
from datetime import datetime
from flask_basicauth import BasicAuth
import os

app.config['BASIC_AUTH_USERNAME'] = os.environ.get("ADMIN_USER") or 'admin'
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get("ADMIN_PASSWORD") or 'helevetinhyvasalasana' # TODO: this could be somewhere else

basic_auth = BasicAuth(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()

    starttime = datetime(2019, 2, 18, 13, 37, 00)
    endtime = datetime(2019, 3, 15, 00, 00, 00)
    nowtime = datetime.now()

    limit = 24

    o_entries = Model.query.filter_by(guild="otit")
    s_entries = Model.query.filter_by(guild="sik")
    o_count = Model.query.filter_by(guild="otit").count()
    s_count = Model.query.filter_by(guild="sik").count()

    if form.validate_on_submit():
        flash('Kiitos ilmoittautumisesta!')
        sub = Model(

            name=form.name.data,
            mail=form.mail.data,
            guild=form.guild.data,
            phone=form.phone.data,
            place=form.place.data,
            datetime=nowtime
        )
        db.session.add(sub)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', title='KMP-2019 Ilmoittautuminen',
                           o_entries=o_entries,
                           s_entries=s_entries,
                           o_count=o_count,
                           s_count=s_count,
                           starttime=starttime,
                           endtime=endtime,
                           nowtime=nowtime,
                           limit=limit,
                           form=form)

@app.route('/admin', methods=['GET'])
@basic_auth.required
def admin():
    limit = 24
    o_entries = Model.query.filter_by(guild="otit")
    s_entries = Model.query.filter_by(guild="sik")
    o_count = Model.query.filter_by(guild="otit").count()
    s_count = Model.query.filter_by(guild="sik").count()
    return render_template('admin.html', title='KMP-2019 ADMIN',
                           o_entries=o_entries,
                           s_entries=s_entries,
                           o_count=o_count,
                           s_count=s_count,
                           limit=limit)