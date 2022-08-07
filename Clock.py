from datetime import datetime,time,date,timedelta


ltime = datetime.now()
ltime = str(ltime)

if int(ltime[11:13]) > 12:
    correctT = int(ltime[11:13]) - 12
    correctT = str(correctT)
    ltime = ltime.replace(ltime[11:13], correctT)
    ltime = str(ltime)
elif int(ltime[11:13]) == '00':
    ltime = str(ltime)


# Watch the linkedin video stupid
# propert = int(ltime[11:19])
# propert = datetime.strftime()

print(ltime[11:19])