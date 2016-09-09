
import smtplib, cx_Oracle
import time
from datetime import datetime

def db_query(db):
    cursor = db.cursor()
    query = []
    avg = 0
    for x in range(2):
        cursor.execute("""SELECT COUNT(1) FROM gv$session WHERE STATUS='ACTIVE' and type not in 'BACKGROUND'""")
        for record in cursor.fetchall():
            query.append(record)
        avg += query[0][0]
        time.sleep(5)
    return avg

def Connection_db(db_name):
    try:
        db = cx_Oracle.connect('usr/pass@' + str(db_name))
        print('Connected to Oracle database')
        avg = db_query(db)
        db.close()
        print('Connection closed')
        return avg
    except ValueError:
        print ("Oops!  That was no valid number.  Try again...")

def connect(db_name):
    try:
        print("Trying to connect " + db_name + "...")
        query = Connection_db(db_name)
        return query
    except ValueError:
        print("Oops!  Can't connect to " + db_name + "...")

def try_connect():
    try:
        query = connect("primary_db")
        return query
    except:
        print("Oops!  Can't connect to standby_db...")
        try:
            query = connect("fns_standby")
            return query
        except:
            print("Oops!  Can't connect to any database...")
            return

def topic():
    query = try_connect()
    new_date = datetime.now().strftime("%d/%m/%y %H:%M")
    subj = "DB status (" + str(new_date) + ")"
    body = "В данный момент (" + str(new_date) + ") среднее значение количества сессий за последнюю минуту - " + str(query/2)
    return (body, subj)

def messg():
    print("New Message is coming\n")
    FROM = "from@someone"
    TO = ["to@someone",]
    TEXT, SUBJECT = topic()

    message = ("From: %s\r\n"
               "To: %s\r\n"
               "Subject: %s\r\n\r\n"
               "%s"
       % (FROM, ", ".join(TO), SUBJECT, TEXT))

    message = message.encode('cp1251')
    send_msg = smtplib.SMTP("smtp_server", 25)
    send_msg.set_debuglevel(2)
    send_msg.ehlo()
    send_msg.sendmail(FROM, TO, message)
    time.sleep(600)

if __name__ == "__main__":
    while 1:
        try:
            if datetime.today().minute == 0:
                messg()
            else:
                time.sleep(20)
        except:
            time.sleep(600)

