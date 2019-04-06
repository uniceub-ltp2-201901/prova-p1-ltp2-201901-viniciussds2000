from flask import Flask,render_template,request
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

    return render_template('listaprofessores.html', prof=get_professores(cursor))


@app.route('/exibir',methods=['GET','POST'])
def exibirprofessores():
    cursor = mysql.get_db().cursor()
    if request.method == 'POST':
        nome = request.form.get('nomeprof')

        cursor = mysql.get_db().cursor()

        idprof=validar_prof(cursor,nome)

        if idprof is None:
            return render_template('listaprofessore.html', erro='Professor não encontrado, digite o nome completo')
        else:
            cursor = mysql.get_db().cursor()

            return render_template('exibirprofessores.html',nomep=idprof, det=get_detalhes(cursor,idprof))

    else:
        return render_template('listaprofessores.html.html')
    return render_template('exibirprofessores.html')




if __name__ == '__main__':
    app.run(debug=True)