import mysql.connector


def connect():
    conn = mysql.connector.connect(
        host='185.154.14.82',
        user='root',
        password='1U3t3W2h',
        database='shopbot'
    )

    cursor = conn.cursor()

    return conn, cursor

conn, cursor = connect()

def create_tables():
    try:
        cursor.execute(f'CREATE TABLE users (user_id TEXT, first_name TEXT, username TEXT, balance DECIMAL(10, 2), who_invite TEXT, date TEXT, pact TEXT)')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE check_payment (user_id TEXT, code TEXT, date TEXT)')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE sending (type TEXT, text TEXT, photo TEXT, date TEXT)')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE catalogs (catalog_id TEXT, catalog_name TEXT, photo TEXT)')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE subdirectories (catalog_id TEXT, subdirectory_id TEXT, subdirectory_name TEXT, photo TEXT)')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE purchase_logs (user_id TEXT, file_name TEXT, amount TEXT, price TEXT, date TEXT)')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE buttons (name TEXT, info TEXT, photo TEXT)')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE btc_list (user_id TEXT, code TEXT)')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE payouts (user_id TEXT, sum TEXT, btc_check TEXT)')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE payouts_step_0 (user_id TEXT, code TEXT, time TEXT)')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE deposit_logs (user_id TEXT, type TEXT, sum DECIMAL(10, 2), date TEXT)')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE deposit_logs (user_id TEXT, type TEXT, sum DECIMAL(10, 2), date TEXT)')
        conn.commit()
    except:
        pass


create_tables()
