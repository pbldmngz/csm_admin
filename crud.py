from con_csm import do

def ver (col, table, cond):
    return do("select {} from {} where {}"
    .format(col, table, cond), False)

def crear (table, cond, data):
    return do("insert into {} ({}) values ({})"
    .format(table, cond, data), True)

def modificar (table, original1, new1, original2, new2):
    return do("update {} set {} = {} where {} = {}"
    .format(table, original1, new1, original2, new2), True)

def eliminar (table, cond):
    return do("delete from {} where {}"
    .format(table, cond), True)

def direct(statement):
    return do(statement, True)