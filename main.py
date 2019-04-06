from flask import Flask,render_template
from flaskext.mysql import MySQL
from BD import *

app=Flask(__name__)

mysql = MySQL()

mysql.init_app(app)

app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_DB']='faculdade'

@app.route('/')
def listarprofessores():
    cursor = mysql.get_db().cursor()

    return render_template('listaprofessores.html',prof=get_professores(cursor))


@app.route('/exibir')
def exibirprofessores():
    cursor = mysql.get_db().cursor()
    idprof=get_id(cursor)
    cursor= mysql.get_db().cursor()
    return render_template('exibirbeatriz.html',detalhes=get_detalhes(cursor,idprof))



if __name__ == '__main__':
    app.run(debug=True)