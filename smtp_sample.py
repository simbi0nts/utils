
import smtplib, cx_Oracle
import time
from datetime import datetime
from email.message import Message

def ConnectionDB():
    average = 0
    try:
        db = cx_Oracle.connect('login/pass@db_alias')
        print('Connected to Oracle database')
        cursor = db.cursor()
        for x in range(1):
            query = []
            cursor.execute("""select VALUE from V$DATAGUARD_STATS where name='apply lag'""")
            for record in cursor.fetchall():
                query.append(record)
            query = query[0][0]
            average = query
            #print("Запрос [" + str(x + 1) + "] : ")
            #print("Кол-во сессий - " + str(query))
            #print("Сумма по запросам - " + str(average))
            #print("Среднее по запросам - " + str(average/(x+1)))
            #time.sleep(5)
        db.close()
        print('Connection closed')
        return average
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

def topic():
    body_part = ""
    Importance = 0
    average = ConnectionDB()
	#if (average/5 < 300):
    #    body_part = 'в пределах нормы (менее 300 активных сессий)'
    #elif (average/5 >= 300) and (average/5 < 550):
    #    body_part = 'повышенная (около 300-550 активных сессий)'
    #elif(average/5 >= 550):
    #    body_part = 'критическая (более 550 активных сессий)'
    #    Importance = 1
    cur_minute = datetime.strftime(datetime.now(), "%M")
    cur_hour = datetime.strftime(datetime.now(), "%H")
    cur_day = datetime.strftime(datetime.now(), "%d/%m/%Y")
    subj = 'DB lag status (' + str(cur_day) + ' ' + str(cur_hour) + ':' + str(cur_minute) + ')'
    body = 'В данный момент (' + str(cur_hour) + ':' + str(cur_minute) + ') apply lag на KPEX53 составляет: ' + str(average)
    return (body, subj, Importance)

def messg():
    print("New Message is coming\n")
    FROM = "from@someone"
    TO = ["to@someone, to@someone, to@someone"]
    TEXT, SUBJECT, Importance = topic()

    m = Message()
    m['From'] = "DB_status@fcod.nalog.ru"
    m['To'] = "to@someone, to@someone, to@someone"
    if Importance:
        m['Importance'] = 'High'
    else:
        m['Importance'] = 'Low'
    m['Subject'] = SUBJECT
    m.set_payload(TEXT)

    send_msg = smtplib.SMTP("smtp_server", 25)
    send_msg.set_debuglevel(2)
    send_msg.ehlo()
    send_msg.sendmail(FROM, TO, m.as_string().encode('cp1251'))

if __name__ == "__main__":
    while 1:
        try:
            #if datetime.today().minute == 0:
                messg()
                time.sleep(1800)
            #else:
            #    time.sleep(1)
        except:
            continue
