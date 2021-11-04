import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Projects secret key. Used to keep some level of security for modules such as forms
    # Please CHANGE THIS WHEN RUNNING IN PRODUCTION
    SECRET_KEY = os.environ.get("SECRET_KEY") or "BACKUP_SECRET_KEY"
    # Database URI. First tries connecting remotely before using a local copy.
    # Database URL format <db type>://<user>:<password>@<hostname>/<db name>
    SQLALCHEMY_DATABASE_URI = "DATABASE_URL" or "sqlite:///" + os.path.join(
        basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
