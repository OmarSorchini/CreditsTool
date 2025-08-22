from flask import Flask, render_template, request
import sqlite3, pandas, os, base64
from matplotlib.figure import Figure
from io import BytesIO
import matplotlib.ticker as tck

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():

    # renderization of index template
    # creation of database and creditos table from sql schema

    return render_template('index.html')

connect = sqlite3.connect('database.db')


    # creditos table creation (testing purposes)

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

@app.route('/creditsDashboard', methods=['GET', 'POST'])
def creditsDashboard():

    # Deletion of selected credit

    connect = sqlite3.connect('database.db')

    query = "SELECT count(cliente) as Creditos_Activos, cliente as Cliente, monto as Monto FROM creditos \
    GROUP BY cliente ORDER BY count(cliente) DESC"

    data = pandas.read_sql(query, connect)

    print(data)

    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.bar(data.Cliente, data.Creditos_Activos)
    
    ax.yaxis.set_major_locator(tck.MultipleLocator())
    
    path = os.path.join('static', 'images', 'plot.png')
    fig.savefig(path)

    return render_template("creditsGraph.html", pathImage = path)

if __name__ == '__main__':
    app.run(debug=True)