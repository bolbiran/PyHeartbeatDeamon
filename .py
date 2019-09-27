import sys
import time
import requests
import schedule

#Fucntion to run
def autoScan():
    #Make the request or close the connection
    try:
        r = requests.get("http://ah-1089145-001.sdi.corp.bankofamerica.com:9999/api/auto_search",
                        headers={"username" : "automated",
                                "apiKey" : "f6c69a9e71de18c12921",
                                "amount" : "75"
                        })
    except:
        print('Connection Failed, Shutting Down Auto Search...')
        sys.exit(0)

def checkScan():
    hostname = "http://ah-1089145-001.sdi.corp.bankofamerica.com:9999/schedule/ping"
    
    try:
        r = requests.get(hostname) 
        if r.status_code != 200:
            print('Connection Failed, Shutting Down Auto Search...')
            sys.exit(0)
    except:
        print('Connection Failed, Shutting Down Auto Search...')
        sys.exit(0)

#Start the scheduler
schedule.every(.5).minutes.do(checkScan)
schedule.every(12).hours.do(autoScan)
print('Starting Scheduler...')
while True:
    schedule.run_pending()
    time.sleep(6)
