from flask import Flask
from flask import render_template

from flaskext.mysql import MySQL
app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = '192.168.1.229'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'diego'
app.config['MYSQL_DATABASE_DB'] = 'cac23008team11'

mysql.init_app(app)


@app.route('/')
def index():
    sql = "insert into pedidos ( uuId,  platoId, cantidad, time) values ('11asdadsasd1q2eqdasds', 2, 2,  current_timestamp) "
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)

    conn.commit()
    return render_template('pedidos/index.html')



if __name__ == '__main__':
    app.run(debug=True)
