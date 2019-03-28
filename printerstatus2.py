import wmi
c = wmi.WMI ()

print_job_watcher = c.Win32_PrintJob.watch_for(notification_type="Creation", delay_secs=1)

while True:
  pj = print_job_watcher()
  print("User %s has submitted %d pages to printer %s" %(pj.Owner, pj.TotalPages, pj.Name))

print("done")
