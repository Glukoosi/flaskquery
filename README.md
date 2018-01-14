```
sudo apt install virtualenv
virtualenv env -p python3
source env/bin/activate
pip install -r requirements.txt
export FLASK_APP=ilmo.py

flask db init
flask db migrate
flask db upgrade

flask run

```

flaskilmo.wsgi
```
#!/usr/bin/python
import sys
import logging
import os
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/glukoosi/flaskilmo/")

from app import app as application
application.secret_key = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

```

apache.conf
```
...
        WSGIDaemonProcess flaskilmo python-path=/home/glukoosi/flaskilmo/env/lib/python3.5/site-packages
        WSGIProcessGroup flaskilmo
        WSGIScriptAlias /5wag /home/glukoosi/flaskilmo/flaskilmo.wsgi
        <Directory /home/glukoosi/flaskilmo/>
                Require all granted
        </Directory>
...

```
