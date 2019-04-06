def get_professores(cursor):
    cursor.execute(f'select nome from professor order by nome')

    professores=cursor.fetchall()

    cursor.close()

    return professores
def validar_prof(cursor,name):
    cursor.execute(f'select id from professor where nome = "{name}"')

    idprof= cursor.fetchone()

    cursor.close()

    return idprof


def get_detalhes(cursor,idprof):
    cursor.execute(f'select professor.nome, professor.nomemae,professor.datanasc,professor.titulacao from professor where id="{idprof[0]}"')

    detalhes=cursor.fetchall()

    cursor.close()

    return detalhes

