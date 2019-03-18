import time
# import schedule

# def job():
#     print('Hello World!\n123')

# def cron():
#     job()
#     schedule.every(5).seconds.do(job)
#     while True:
#         schedule.run_pending()

# cron()

print("*********************************")
print("Welcome to scheduled printing app")
print("*********************************")
time.sleep(2)
def pickTime():
    global time_format
    time_format = input("\nPick a schedule format:\n[1] In Minutes\n[2] In Hours\n\n>> ")

    if time_format != ("1" or "2"):
        print("Please input \'1\' or \'2\' only...")
        time.sleep(1)
        pickTime()    
pickTime()    
def setTime():
    global time_set
    t_format = "minutes" if time_format == "1" else "hours"
    time_set = input("\nInput time in {}: ".format(t_format))
    
    if time_set.isdigit()
 