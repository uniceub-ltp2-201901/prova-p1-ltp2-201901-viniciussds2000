def get_professores(cursor):
    cursor.execute(f'select nome from professor order by nome')

    professores=cursor.fetchall()

    cursor.close()

    return professores

def get_id(cursor):
    cursor.execute(f'select id from professor')

    idprof=cursor.fetchone()

    cursor.close()

    return idprof

def get_detalhes(cursor,idprof):
    cursor.execute(f'select nome,nomemae,datanasc,titulacao from professor where id="{idprof}"')

    detalhes=cursor.fetchall()

    cursor.close()

    return detalhes
