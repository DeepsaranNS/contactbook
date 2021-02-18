import sqlite3
try:
    con=sqlite3.connect("database_dir\contact_database.db")
    cur=con.cursor()
except:
    print('cannot connect to the database')

def write_to_database(name,num,address):
    global cur,con
    try:
        cur.execute(f"insert into contacts values('{name}','{num}','{address}')")
        con.commit()
    except:
        print('error!!!')


def fetch_from_database():
    global con,cur
    try:
        cur.execute('select * from contacts')
        return(cur.fetchall())

    except:
        print('error!!')


def fetch_by_name(name):
    global con,cur
    try:
        cur.execute(f"select * from contacts where name='{name}'")
        return(cur.fetchall())


    except:
        print('error!!')


def delete_from_base(num):
    global con, cur
    try:
        cur.execute(f"delete from contacts where number='{num}'")
        con.commit()

    except:
        print('error!!')


