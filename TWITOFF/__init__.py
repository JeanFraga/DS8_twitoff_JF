"""
Entry point for our twitoff flask app
DB.session.add(u1)
>>> DB.session.add(t1)
>>> DB.session.commit()
"""

from .app import create_app

# APP is global variable
APP = create_app()

# run this in terminal with set FLASK_APP=TWITOFF:APP flask run