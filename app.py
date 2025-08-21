from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():

    # renderization of index template
    # creation of database and creditos table from sql schema

    return render_template('index.html')

connect = sqlite3.connect('database.db')


    # creditos table creation

"""
connect.execute(
    'CREATE TABLE IF NOT EXISTS creditos (id INTEGER PRIMARY KEY AUTOINCREMENT, \
    cliente TEXT, \
    monto REAL, \
    tasa_interes REAL, \
    plazo INTEGER, \
    fecha_otorgamiento TEXT)')
    """

with open('schema.sql') as f:
    connect.executescript(f.read())

@app.route('/creditsRegister', methods=['GET', 'POST'])
def creditsRegister():

    # Renderization of creditsRegister template [POST]
    # Registration of new credits

    if request.method == 'POST':
        cliente = request.form['cliente']
        monto = request.form['monto']
        tasa = request.form['tasa_interes']
        plazo = request.form['plazo']
        fecha = request.form['fecha_otorgamiento']
        with sqlite3.connect("database.db") as clientes:
            cursor = clientes.cursor()
            cursor.execute("INSERT INTO creditos \
            (cliente,monto,tasa_interes,plazo,fecha_otorgamiento) VALUES (?,?,?,?,?)",
                           (cliente, monto, tasa, plazo, fecha))
            clientes.commit()
        return render_template("index.html")
    else:
        return render_template('creditsRegister.html')

@app.route('/creditsList')
def creditsList():

    # Visualization of table creditos in creditsList template

    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM creditos')

    data = cursor.fetchall()
    return render_template("creditsList.html", data=data)

@app.route('/creditsEdit/<int:idCred>', methods=['GET', 'POST'])
def creditsEdit(idCred):

    # Edition of credits in creditsEdit template

    if request.method == 'POST':

        cliente = request.form['cliente']
        monto = request.form['monto']
        tasa = request.form['tasa_interes']
        plazo = request.form['plazo']
        fecha = request.form['fecha_otorgamiento']
        with sqlite3.connect("database.db") as clientes:
            cursor = clientes.cursor()
            cursor.execute("UPDATE creditos \
            SET cliente = ?, monto = ?, tasa_interes = ?, plazo = ?, fecha_otorgamiento = ? \
            WHERE id = ?",(cliente, monto, tasa, plazo, fecha, idCred))
            clientes.commit()
        return render_template("index.html")
    else:
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        #print("LOG test query edit")
        cursor.execute("SELECT * FROM creditos WHERE id = ?",[(idCred)])
        

        data = cursor.fetchall()

        return render_template("creditsEdit.html", data=data)

        

@app.route('/creditsDelete/<int:idCred>', methods=['GET', 'POST'])
def creditsDelete(idCred):

    # Deletion of selected credit

        with sqlite3.connect("database.db") as clientes:
            cursor = clientes.cursor()
            cursor.execute("DELETE FROM creditos \
            WHERE id = ?",[(idCred)])
            clientes.commit()

        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)