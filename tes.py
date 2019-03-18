import os
import time
import pymysql
import schedule
import requests
import datetime
import win32api
import win32print
import urrllib.request
from requests.auth import HTTPBasicAuth

# def DbConn():
#     global conn
#     global cursor
#     global date
#     conn = pymysql.connect(
#         host='mysql.opsigo.id',
#         user='SupportQa',
#         password='cbc726de6accda94ba7e56d2768d9d68',
#         db='Qa_1_Db',
#         port=7706
#     )
#     timestamp = time.time()
#     # date1 = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
#     date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
#     cursor = conn.cursor()

def post():
    global url
    auth = HTTPBasicAuth('opsifin','opsifin123')
    response = requests.post('https://antavaya.opsifin.com/opsifin_api_print', auth=auth)
    url = response.json()['link']

# def insertInv():
#     sql = """a query"""
#     cursor.execute(sql)
#     conn.commit()
#     conn.close()

# def getinv():
#     global rows
#     sql = """a query"""
#     cursor.execute(sql)
#     rows = cursor.fetchall()
#     conn.close()

def getFile():
    global path
    path = os.path.join(os.getcwd(), 'Inv')
    urrllib.request.urlretrieve(url,path)

def printInv():
    
    printer = win32print.GetDefaultPrinter()
    
    for inv in rows:
        getFile()
        win32api.ShellExecute(
            0,
            "print",
            "{}.pdf".format(inv),
            None,
            path,
            0
        )
    
def aJob():
    return

def cronJob(timeformat,timeset):
    
    aJob()
    
    if timeformat == "1":
        schedule.every(timeset).minutes.do(aJob)
    else:
        schedule.every(timeset).hours.do(aJob)

    while True:
        schedule.run_pending()


if __name__=='__main__':
    
    global time_set

    print("*********************************")
    print("Welcome to scheduled printing app")
    print("*********************************")
    time.sleep(2)
    def pickTime():
        global time_format
        time_format = input("\nPick a schedule format:\n[1] In Minutes\n[2] In Hours\n\n>> ")

        if time_format != ("1" and "2"):
            print("Please input \'1\' or \'2\' only...")
            pickTime()    
    
    t_format = "minutes" if time_format == "1" else "hours"
    time_set = input("\nInput time in {}: ".format(t_format))
        
    cronJob(time_format, time_set)