from flask import Flask, request, jsonify
from flask import render_template
from pymysql.cursors import DictCursor
from flaskext.mysql import MySQL


app = Flask(__name__)
# app.config['MYSQL_DATABASE_HOST'] = '192.168.1.229'
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'diego'
app.config['MYSQL_DATABASE_HOST'] = 'comaschi.mysql.pythonanywhere-services.com'
app.config['MYSQL_DATABASE_USER'] = 'comaschi'
app.config['MYSQL_DATABASE_PASSWORD'] = 'diego100'
app.config['MYSQL_DATABASE_DB'] = 'comaschi$cac23008team11'

mysql = MySQL()
mysql.init_app(app)


# Ruta para listar platos
@app.route('/platos', methods=['GET'])
def listPlatos():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()

        sql = "select platoId, title, imageUrl, description, precio from platos order by platoId"
        cursor.execute(sql)

        rows = cursor.fetchall()

        pedidos = []
        for row in rows:
            platoId, title,  imageUrl, description, precio = row
            pedido = {'platoId': platoId, 'title': title,
                      'description': description, 'imageUrl': imageUrl, 'precio': precio}
            pedidos.append(pedido)

        cursor.close()
        conn.close()
        return jsonify(pedidos), 200

    except:
        cursor.close()
        conn.close()
        return jsonify({'error': 'Error al consultar los platos'}), 500

# Ruta para ver un plato


@app.route('/platos/<int:platoId>', methods=['GET'])
def viewPlatos(platoId):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(cursor=DictCursor)

        sql = "select platoId, title, imageUrl, description, precio from platos where platoId = %s order by platoId"
        cursor.execute(sql, platoId)

        plato = cursor.fetchone()

        cursor.close()
        conn.close()

        if plato is None:
            return jsonify({'error': 'Plato no encontrado'}), 404
        else:
            return jsonify({'platoId': plato['platoId'],
                            'title': plato['title'],
                            'description': plato['description'],
                            'imageUrl': plato['imageUrl'],
                            'precio': plato['precio']}), 200
    except:
        cursor.close()
        conn.close()
        return jsonify({'error': 'Error al consultar el plato'}), 500


# Ruta para listar pedidos
@app.route('/pedidos',  methods=['GET'])
def listPedidos():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()

        sql = "select a.uuid,a.platoId,description, imageUrl, precio, cantidad, precio * cantidad as importe from pedidos a join platos b on a.platoId = b.platoId order by a.uuid,a.platoId"
        cursor.execute(sql)

        rows = cursor.fetchall()

        pedidos = []
        for row in rows:
            uuid, platoId, description, imageUrl, precio, cantidad, importe = row
            pedido = {'uuid': uuid, 'platoId': platoId, 'description': description,
                      'imageUrl': imageUrl, 'precio': precio, 'cantidad': cantidad, 'importe': importe}
            pedidos.append(pedido)

        cursor.close()
        conn.close()
        return jsonify(pedidos), 200

    except:
        cursor.close()
        conn.close()
        return jsonify({'error': 'Error al consultar los pedidos'}), 500

# Ruta para Ver un pedido


@app.route('/pedidos/<string:pedidoId>',  methods=['GET'])
def viewPedidos(pedidoId):

    try:
        conn = mysql.connect()
        cursor = conn.cursor()

        sql = "select a.uuid,a.platoId,description, imageUrl, precio, cantidad, precio * cantidad as importe from pedidos a join platos b on a.platoId = b.platoId where a.uuid = %s order by a.uuid,a.platoId"
        cursor.execute(sql, pedidoId)

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        if rows is None:
            return jsonify({'error': 'Pedido no encontrado'}), 404
        else:
            pedido = []
            for row in rows:
                uuid, platoId, description, imageUrl, precio, cantidad, importe = row
                plato = {'uuid': uuid, 'platoId': platoId, 'description': description,
                         'imageUrl': imageUrl, 'precio': precio, 'cantidad': cantidad, 'importe': importe}
                pedido.append(plato)
            return jsonify(pedido), 200
    except:
        cursor.close()
        conn.close()
        return jsonify({'error': 'Error al consultar el pedido'}), 500

# Ruta para crear un Pedido
# Si el pedido UUID no existe se crea el plato (INSERT)
# si el pedido existe y el plato no se agrega un plato al pedido (INSERT)
# si existe el pedido y el plato se cambia la cantidad (CHANGE)
@app.route('/pedidos', methods=["POST"])
def addPedido():

    if request.method == 'POST':
        try:
          _uuid = request.json['uuid']
          _platoId = request.json['platoId']
          _cantidad = request.json['cantidad']

          conn = mysql.connect()
          cursor = conn.cursor(cursor=DictCursor)

          sql = "select * from pedidos a where a.uuid = %s and a.platoId = %s"
          cursor.execute(sql, (_uuid, _platoId))

          msg = ''
          if cursor.rowcount > 0:
              sql = "update pedidos set cantidad = %s where  uuid = %s and platoId = %s"
              cursor.execute(sql, (_cantidad, _uuid, _platoId))
              msg = "{'message': 'Pedido Cambiado'}"
          else:
              sql = "insert into pedidos ( uuId,  platoId, cantidad, time) values (%s,%s,%s, current_timestamp)"
              cursor.execute(sql, (_uuid, _platoId, _cantidad))
              msg = "{'message': 'Pedido creado'}"

          conn.commit()
          cursor.close()
          conn.close()
          return jsonify(msg), 200
        except:
            return jsonify({'error': 'Error al crear pedido'}), 500

    else:
        return jsonify({'error': 'Request tiene que ser [POST]'}), 500


# Ruta para eliminar Pedido
# /pedido?pedidoId=xxxxx&platoId=xxxx  elimina un plato del pedido
# /pedido?pedidoId=xxxxx  elimina todo el pedido
@app.route('/pedidos', methods=['DELETE'])
def removePedido():

    try:
        pedidoId = request.args.get('pedidoId', None)
        platoId = request.args.get('platoId', None)

        conn = mysql.connect()
        cursor = conn.cursor()

        if platoId is None:
            sql = "delete from pedidos a where a.uuid = %s"
            cursor.execute(sql, (pedidoId))
        else:
            sql = "delete from pedidos a where a.uuid = %s and a.platoId = %s"
            cursor.execute(sql, (pedidoId, platoId))

        if cursor.rowcount > 0:
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({'message': 'Pedido eliminado correctamente.'}), 200
        else:
            cursor.close()
            conn.close()
            return jsonify({'Error': 'Pedido no encontrado'}), 404

    except:
        return jsonify({'error': 'Error al eliminar el pedido'}), 500

# Ruta para Index


@app.route('/')
def index():
    return 'API de Pedidos'


# lanzar la Applicacion
if __name__ == '__main__':
    app.run(debug=True)
