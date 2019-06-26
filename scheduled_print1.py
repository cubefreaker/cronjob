import schedule
import win32api
import win32print
import urllib.request
from threading import Thread, Event
from requests.auth import HTTPBasicAuth
import os, json, time, logging, requests



class printJob:

    def __init__(self, url, usr, pwd):
        self.url = url
        self.usr = usr
        self.pwd = pwd

    def get(self):
        url = self.url
        usr = self.usr
        pwd = self.pwd
        auth = HTTPBasicAuth(usr, pwd)
        response = requests.get(url, auth=auth)

        return response.json()

    def post(self, Inv, status):
        url = self.url
        usr = self.usr
        pwd = self.pwd
        auth = HTTPBasicAuth(usr, pwd)
        data = json.dumps({"InvNo": Inv, "PrintProcess": status})
        response = requests.post(url, data=data, auth=auth)

        return response

    def getFile(self, Inv, url):
        self.path = os.path.join(os.getcwd(), 'tempFile')

        return urllib.request.urlretrieve(url, self.path + '/{}.pdf'.format(Inv))

    def rmFile(self, Inv):
        path = os.path.join(self.path, Inv)

        return os.remove(path + '.pdf')


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

stop_event = Event()

def printChecker():
    jobs = [1]
    while jobs:
        jobs = []
        for p in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1):

            flags, desc, name, comment = p

            phandle = win32print.OpenPrinter(name)
            print_jobs = win32print.EnumJobs(phandle, 0, -1, 1)
            if print_jobs:
                jobs.extend(list(print_jobs))
            for job in print_jobs:
                document = job["pDocument"]
                print("Printing Now: " + document)
            win32print.ClosePrinter(phandle)
        time.sleep(5)
        # check if the other thread sent a signal to stop execution.
        if stop_event.is_set():
            break
    print("Printing Complete")

def cancelPrint():
    jobs=[1]
    while jobs:
        jobs = []
        for p in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1):

            flags, desc, name, comment = p

            phandle = win32print.OpenPrinter(name)
            print_jobs = win32print.EnumJobs(phandle, 0, -1, 1)
            if print_jobs:
                jobs.extend(list(print_jobs))
            for job in print_jobs:
                win32print.SetJob(phandle, win32print.AddJob(phandle)[1], 0, None, win32print.JOB_CONTROL_DELETE)
                document = job["pDocument"]
                print("Canceling Print: " + document)
            win32print.ClosePrinter(phandle)
        time.sleep(5)


logging.basicConfig(filename='print.log', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

if __name__ == '__main__':

    print('APP STARTING...')
    time.sleep(2)

    print('\nINITIALIZATION')
    time.sleep(2)
	
    #api = input('\nInput API endpoint : ')
    #apiuser = input('\nInput user : ')
    #apipass = input('\nInput password : ')
    printInv = printJob('https://goldennusa.opsifin.com/opsifin_api_print', 'gld-ops189',
                        '$2y$10$sI1H2wMYDzX8LHh27Gevku7D5R4auoWWWarKysXObJjQtHIm.IiqG')

    printInv.mkDir()
	
    def timeSec():
        global val
        sec = input('\nInput time schedule (in minutes): ')
        if sec.isdigit() == True:
            val = sec
        else:
            print('\nPlease input in numerical format...')
            timeSec()
	
    timeSec()


    def aJob():
        global identifier
        # -- Fetching List File -- #
        print('\nFETCHING FILE FROM SERVER')
        dataList = printInv.get()
        # print(dataList)

        for data in dataList:

            # ----------------- Download File ----------------- #
            print('\nDownloading File : ' + data['InvNo'])
            printInv.getFile(data['InvNo'], data['Link'])
            print('Download Complete')

            identifier = 1
            def printFix():
                global identifier
                # ------ Print File ------ #
                print('\nPrinting File...')
                printInv.printFile(data['InvNo'])

                # check print status
                state = Thread(target=printChecker)

                state.start()
                # set timeout
                state.join(timeout=15)

                if state.is_alive():
                    stop_event.set()
                    if identifier < 3:
                        identifier = identifier + 1
                        printFix()
                    else:
                        cancelPrint()
                        print('TIME OUT: Print Failed')
                        printInv.post(data['InvNo'], 'Failed')
                        logging.warning('Print failed on invoice %s - Time Out ', data['InvNo'])
                        return False
                else:
                    return True

            if printFix() == True:
                # -------- Posting status ----- #
                print('Posting data')
                printInv.post(data['InvNo'], 'Success')
                print('Done Posting\n')
                printInv.rmFile(data['InvNo'])
            else:
                break


        # for rmdata in dataList:
        #     printInv.rmFile(rmdata['InvNo'])


    aJob()

    schedule.every(int(val)).minutes.do(aJob)

    while True:
        schedule.run_pending()