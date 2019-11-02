import MySQLdb

def do (statement, condition):
    db = MySQLdb.connect(user = "spectra", passwd="123456789",db="csm_database")
    c = db.cursor()
    c.execute(statement)

    if condition:
        db.commit()
        c.close()
        db.close()
    else:
        myresult = c.fetchall()
        c.close()
        db.close()
        return myresult
        
    #Devuelve un arreglo de arreglos con todos los datos
    #Condition true => Es una update
    #         false => Es una querry