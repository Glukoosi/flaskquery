```
docker-compose up

or

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

flask run


for prod:
docker-compose -f docker-compose_prod.yml up -d

```

```
If you change db model you have to remove app.db
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
