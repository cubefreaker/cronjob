import os
import json
import time
import shutil
import schedule
import requests
import datetime
import win32api
import win32print
import urllib.request
from requests.auth import HTTPBasicAuth


class printJob:

    def __init__(self, url, usr, pwd):
        self.url = url
        self.usr = usr
        self.pwd = pwd

    def get(self):
        url = self.url
        usr = self.usr
        pwd = self.pwd
        auth = HTTPBasicAuth( usr, pwd)
        response = requests.get(url, auth=auth)

        return response.json()

    def post(self, Inv, status):
        url = self.url
        usr = self.usr
        pwd = self.pwd
        auth = HTTPBasicAuth( usr, pwd)
        data = {"InvNo": Inv, "PrintProcess": status}

        return requests.post(url, data=json.dumps(data), auth=auth)

    def getFile(self, Inv, url):
        self.path = os.path.join(os.getcwd(), 'tempFile')
        
        return urllib.request.urlretrieve(url, self.path + '/{}.pdf'.format(Inv))

    def rmFile(self, Inv):
        path = os.path.join(self.path, Inv)
        
        return os.remove(path+'.pdf')

    def mkDir(self):
        dir = 'tempFile'
        if not os.path.exists(dir):
            return os.makedirs(dir)
        else:
            pass

    def printFile(self, Inv):
        path = self.path
        return win32api.ShellExecute(
            0,
            "print",
            "{}.pdf".format(Inv),
            None,
            path,
            0
        )


if __name__=='__main__':

    printInv = printJob('https://antavaya.opsifin.com/opsifin_api_print', 'anv-ops189', '$2y$10$XFSAh4wRcteGhbzXoEEuU./6XWinKmEunDNdqs1/dRX9oylpNJ9da')
    
    printInv.mkDir()

    def aJob():
        dataList = printInv.get()
        # print(dataList)

        for data in dataList:
            print('Downloading File : ' + data['InvNo'] + '...')
            printInv.getFile(data['InvNo'], data['Link'])
            printInv.printFile(data['InvNo'])
            print('Printing File...\n')
            printInv.post(data['InvNo'], 'Success')
            # print('posting data')

        for rmdata in dataList:
            printInv.rmFile(rmdata['InvNo'])

    aJob()

    schedule.every(10).minutes.do(aJob)

    while True:
        schedule.run_pending()






    # global time_set

    # print("*********************************")
    # print("Welcome to scheduled printing app")
    # print("*********************************")
    # time.sleep(2)
    # def pickTime():
    #     global time_format
    #     time_format = input("\nPick a schedule format:\n[1] In Minutes\n[2] In Hours\n\n>> ")

    #     if time_format != ("1" and "2"):
    #         print("Please input \'1\' or \'2\' only...")
    #         pickTime()    
    
    # t_format = "minutes" if time_format == "1" else "hours"
    # time_set = input("\nInput time in {}: ".format(t_format))
        
    # cronJob(time_format, time_set)





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