from flask import Flask, request, url_for, redirect, abort, render_template
import mysql.connector

app = Flask(__name__)  # este valor va ser main cuando usemos el archivo

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Boldt1234',
    database='prueba'
)

cursor = midb.cursor(dictionary=True)


@app.route('/')
def index():
    return 'hola mundo'

# GET, POST, PUT, DELETE , PATCH


@app.route('/post/<post_id>', methods=['GET', 'POST'])
def lala(post_id):
    if request.method == 'GET':
        return 'el id del post es: ' + post_id
    else:
        return 'este es el otro metodo y no GET request'

# @app.route('/post/<post_id>', methods=['POST'])
# def lala(GET_id):
#   return 'el id del post es: ' + GET_id


@app.route('/lele', methods=['POST', 'GET'])
def lele():
    cursor.execute('select * from usuario')
    usuarios = cursor.fetchall()

    # es importante siempre que llamemos redirect return antes
    # abort(403)
    # return redirect(url_for('lala', post_id=2))
    # print(request.form)
    # print(request.form['llave1'])
    # print(request.form['llave2'])
    # return render_template('lele.html')
    return render_template('lele.html', usuarios=usuarios)


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', mensaje='Hola mundo')


@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        edad = request.form['edad']
        sql = 'insert into usuario (user_name, email,edad) values (%s, %s, %s)'
        values = (username, email, edad)

        cursor.execute(sql, values)
        midb.commit()
        return redirect(url_for('lele'))

    return render_template('crear.html')
