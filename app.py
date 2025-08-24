from flask import Flask, render_template, request
import sqlite3, pandas, os, base64
from matplotlib.figure import Figure
from io import BytesIO
import matplotlib.ticker as tck

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    # Renderization of index template

    return render_template('index.html')

    # Creation of database and creditos table from sql schema

    # DB connection

    connect = sqlite3.connect('database.db')

    # DB execution of the schema sql file

    with open('schema.sql') as f:
        connect.executescript(f.read())

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

    

@app.route('/creditsRegister', methods=['GET', 'POST'])
def creditsRegister():
    # Registration of new credits

    if request.method == 'POST':

        # Data retreival from html (creditsRegister) form

        cliente = request.form['cliente']
        monto = request.form['monto']
        tasa = request.form['tasa_interes']
        plazo = request.form['plazo']
        fecha = request.form['fecha_otorgamiento']

        # DB insertion of new data

        with sqlite3.connect("database.db") as clientes:
            cursor = clientes.cursor()
            cursor.execute("INSERT INTO creditos \
            (cliente,monto,tasa_interes,plazo,fecha_otorgamiento) VALUES (?,?,?,?,?)",
                           (cliente, monto, tasa, plazo, fecha))
            clientes.commit()

        # Renderization of index template [POST]

        return render_template("index.html")
    else:

        # Renderization of creditsRegister template [GET]

        return render_template('creditsRegister.html')

@app.route('/creditsList')
def creditsList():
    # Visualization of table creditos in creditsList template

    # DB retreival of all fields from table creditos

    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM creditos')

    data = cursor.fetchall()

    # Renderization of creditsList template [GET]

    return render_template("creditsList.html", data=data)

@app.route('/creditsEdit/<int:idCred>', methods=['GET', 'POST'])
def creditsEdit(idCred):
    # Edition of credits in creditsEdit html template
    # int idCred: stands for the id of the credit 

    if request.method == 'POST':

        # Data retreival from updated html (creditsEdit) form

        cliente = request.form['cliente']
        monto = request.form['monto']
        tasa = request.form['tasa_interes']
        plazo = request.form['plazo']
        fecha = request.form['fecha_otorgamiento']

         # DB insertion of new data

        with sqlite3.connect("database.db") as clientes:
            cursor = clientes.cursor()
            cursor.execute("UPDATE creditos \
            SET cliente = ?, monto = ?, tasa_interes = ?, plazo = ?, fecha_otorgamiento = ? \
            WHERE id = ?",(cliente, monto, tasa, plazo, fecha, idCred))
            clientes.commit()

        # Renderization of creditsList template [GET]

        return creditsList()

    else:

        # Data retreival from DB of selected credit 

        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM creditos WHERE id = ?",[(idCred)])
        data = cursor.fetchall()

        # Renderization of creditsEdit template with information of selected credit [GET]

        return render_template("creditsEdit.html", data=data)

        

@app.route('/creditsDelete/<int:idCred>', methods=['GET', 'POST'])
def creditsDelete(idCred):
    # Deletion of selected credit
    # int idCred: stands for the id of the credit

    # Data deletion from DB of selected credit 

    with sqlite3.connect("database.db") as clientes:
        cursor = clientes.cursor()
        cursor.execute("DELETE FROM creditos \
        WHERE id = ?",[(idCred)])
        clientes.commit()

    # Renderization of creditsList template [GET]

    return creditsList()

@app.route('/creditsDashboard', methods=['GET', 'POST'])
def creditsDashboard():
    # Dashboard that show the credits given by client

    # Data retreival from DB of cliente, monto fields and their respective credit count grouped by clients and ordered in descendant order 

    connect = sqlite3.connect('database.db')

    query = "SELECT count(cliente) as Creditos_Activos, cliente as Cliente, monto as Monto FROM creditos \
    GROUP BY cliente ORDER BY count(cliente) DESC"

    # Easy data reading using pandas

    data = pandas.read_sql(query, connect)

    # test log
    #print(data)

    # Generate the figure **without using pyplot** (avoiding memory leaks)
    fig = Figure()

    # Bar diagram creation using cliente and count as axis (x,y)

    ax = fig.subplots()
    ax.barh(data.Cliente, data.Creditos_Activos)

    # Integer value graphication
    
    ax.xaxis.set_major_locator(tck.MultipleLocator())

    # File saved locally inside static/images/ as plot.png
    
    path = os.path.join('static', 'images', 'plot.png')

    # File saved without crops

    fig.savefig(path, bbox_inches = 'tight')

    # Renderization of creditsGraph template sending path for image display [GET]

    return render_template("creditsGraph.html", pathImage = path)

if __name__ == '__main__':
    app.run(debug=True)