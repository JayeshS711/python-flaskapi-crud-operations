from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Victor@7111997'
app.config['MYSQL_DATABASE_DB'] = 'jsdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)