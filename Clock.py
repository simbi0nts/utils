
from datetime import datetime
import os, time


zero =["  ____  ",
       " |    | ",
       " |    | ",
       " |    | ",
       " |____| "]

one =["        ",
      "   /|   ",
      "  / |   ",
      "    |   ",
      "    |   "]

two =["  ____  ",
      "      | ",
      "  ____| ",
      " |      ",
      " |____  "]

three =["  ____  ",
        "      | ",
        "  ____| ",
        "      | ",
        "  ____| "]

four =["        ",
       "  |   | ",
       "  |_ _| ",
       "      | ",
       "      | "]

five =["  ____  ",
       " |      ",
       " |____  ",
       "      | ",
       "  ____| "]

six =["  ____  ",
      " |      ",
      " |____  ",
      " |    | ",
      " |____| "]

seven =[" ____   ",
        "     |  ",
        "   __|__",
        "     |  ",
        "     |  "]

eight =["  ____  ",
        " |    | ",
        " |____| ",
        " |    | ",
        " |____| "]

nine =["  ____  ",
       " |    | ",
       " |____| ",
       "      | ",
       "  ____| "]

scp =["     ",
      "  *  ",
      "     ",
      "  *  ",
      "     "]

def score(x):
    if x == '0':
        return zero
    elif x == '1':
        return one
    elif x == '2':
        return two
    elif x == '3':
        return three
    elif x == '4':
        return four
    elif x == '5':
        return five
    elif x == '6':
        return six
    elif x == '7':
        return seven
    elif x == '8':
        return eight
    elif x == '9':
        return nine


while True:

    os.system('cls')

    x = 0

    if datetime.today().weekday() == 0:
        wkday = 'Monday'
    elif datetime.today().weekday() == 1:
        wkday = 'Tuesday'
    elif datetime.today().weekday() == 2:
        wkday = 'Wednesday'
    elif datetime.today().weekday() == 3:
        wkday = 'Thursday'
    elif datetime.today().weekday() == 4:
        wkday = 'Friday'
    elif datetime.today().weekday() == 5:
        wkday = 'Saturday'
    elif datetime.today().weekday() == 6:
        wkday = 'Sunday'
    else:
        print ('err')

    cur_day = datetime.strftime(datetime.now(), "%d/%m/%Y")
    cur_hour = datetime.strftime(datetime.now(), "%H")
    cur_minute = datetime.strftime(datetime.now(), "%M")
    cur_second = datetime.strftime(datetime.now(), "%S")

    t1 = 18 - int(cur_hour) - 1
    t2 = 60 - int(cur_minute) - 1
    t3 = 60 - int(cur_second)

    if t1 < 0:
        t1 = t1 + 24

    chr1 = score(str(t1 // 10))
    cmnt1 = score(str(t2 // 10))
    csc1 = score(str(t3 // 10))

    chr2 = score(str(t1 % 10))
    cmnt2 = score(str(t2 % 10))
    csc2 = score(str(t3 % 10))

    print ("\n                   Time to 18:00:00")

    while x < 5:
        print (chr1[x] + chr2[x] + scp[x] + cmnt1[x] + cmnt2[x] + scp[x] + csc1[x] + csc2[x])
        x = x + 1

    x = 0

    t1 = 22 - int(cur_hour) - 1
    t2 = 60 - int(cur_minute) - 1
    t3 = 60 - int(cur_second)

    if t1 < 0:
        t1 = t1 + 24

    chr1 = score(str(t1 // 10))
    cmnt1 = score(str(t2 // 10))
    csc1 = score(str(t3 // 10))

    chr2 = score(str(t1 % 10))
    cmnt2 = score(str(t2 % 10))
    csc2 = score(str(t3 % 10))

    print ("\n                   Time to 22:00:00")

    while x < 5:
        print (chr1[x] + chr2[x] + scp[x] + cmnt1[x] + cmnt2[x] + scp[x] + csc1[x] + csc2[x])
        x = x + 1

    x = 0

    chr1 = score(cur_hour[0])
    cmnt1 = score(cur_minute[0])
    csc1 = score(cur_second[0])

    chr2 = score(cur_hour[1])
    cmnt2 = score(cur_minute[1])
    csc2 = score(cur_second[1])

    print ("        It's ", wkday, ",", cur_day, " Cur time:")

    while x < 5:
        print (chr1[x] + chr2[x] + scp[x] + cmnt1[x] + cmnt2[x] + scp[x] + csc1[x] + csc2[x])
        x = x + 1

    time.sleep(1)