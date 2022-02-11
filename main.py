###############TODO Create Database to write a temperature from ESP8266
#
# import sqlite3
#
# con=sqlite3.connect('read_temperature.db')
#
# cur=con.cursor()
#
# cur.execute('''
#             CREATE TABLE temperature (ID INTEGER PRIMARY KEY autoincrement,time text, date text , temperature text);
# ''')
#
# con.commit()
# con.close()

#####################TODO zamienic w read_temperature.db kolumne date na kolumne zawierajaca godzine odczytu
#####################TODO tabela utworzona dopisac kod do zapisywania temperatury do tabeli i odczytu temperatury z tabeli i daty i godziny

from datetime import datetime,date
import requests
import sqlite3
import time

def return_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time
def return_temperature():
    r = requests.get("http://192.168.4.1")
    temperature=r.text
    return temperature
def return_date():
    today=date.today()
    today=today.strftime("%d/%m/%y")
    return str(today)



con = sqlite3.connect('read_temperature.db')
cur = con.cursor()



request = f' INSERT INTO "temperature" (time , date , temperature) VALUES (?,?,?)'
while True:
    cur.execute(request,(return_time(),return_date() ,return_temperature()))
    con.commit()

    time.sleep(5)

con.close()


