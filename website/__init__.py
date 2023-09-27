from flask import Flask
import mysql.connector as mc

mysql = None


def create_app():
    app = Flask(__name__)
    global mysql
    # app.config['SECRET_KEY'] = 'bwabqebgberubfjd civvnqerijgnirebvbh'

    # app configurations
    app.config["MYSQL_HOST"] = "localhost"
    app.config["MYSQL_USER"] = "root"
    app.config["MYSQL_PASSWORD"] = "Suj@y543"
    app.config["MYSQL_DB"] = "test"

    # connection configurations
    options = {
        "host": app.config["MYSQL_HOST"],
        "user": app.config["MYSQL_USER"],
        "password": app.config["MYSQL_PASSWORD"],
        "database": app.config["MYSQL_DB"],
    }

    # connect to DB
    try:
        mysql = mc.connect(**options)
        if mysql.is_connected():
            print(f"connected to database succssfully !")
    except mysql.error as err:
        print(f"failed to connect error : {err}")

    app.static_folder = "static"
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth")
    return app
