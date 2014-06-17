#INITIAL IMPORTS
from datetime import datetime
import time, random
import os, re, csv

#DEFINE TIME
pingtime = datetime.now().strftime('%Y-%m-%d %H:%M')
in_time = datetime.now().replace(microsecond=0)

#TITLE
print ' _    _  _____  ______ ___  _____ '
print '| |  | ||  ___||___  //   ||  _  |'
print '| |  | ||___ \    / // /| | \ V / '
print '| |/\| |    \ \  / // /_| | / _ \ '
print '\  /\  //\__/ /_/ / \___  || |_| |'
print ' \/  \/ \____/ \_/      |_/\_____/\n'

print '----------------------------> INFO'
print '* ' + pingtime
print '* \PROPHECY\social\o-twitter-tweets.csv'
print '* \PROPHECY\social\o-twitter-users.csv' + '\n'
print '----------------------------> LOG'

################################# TWITTER #################################

#OUTPUT BUCKET
bucket = {}
bucket2 = {}
bucket[0] = '0'
START = '0'

#FILE LIST
LOL = '\\twitout - LOL.csv'
LOLC = '\\twitout - LOL - UN.txt'
LOLN = 'League of Legends'

HON = '\\twitout - HON.csv'
HONC = '\\twitout - HON - UN.txt'
HONN = 'Heroes of Newerth'

DO2 = '\\twitout - DO2.csv'
DO2C = '\\twitout - DO2 - UN.txt'
DO2N = 'Defense of the Ancients 2'

GW2 = '\\twitout - GW2.csv'
GW2C = '\\twitout - GW2 - UN.txt'
GW2N = 'Guild Wars 2'

XIV = '\\twitout - XIV.csv'
XIVC = '\\twitout - XIV - UN.txt'
XIVN = 'Final Fantasy XIV'

WOW = '\\twitout - WOW.csv'
WOWC = '\\twitout - WOW - UN.txt'
WOWN = 'World of Warcraft'

ESO = '\\twitout - ESO.csv'
ESOC = '\\twitout - ESO - UN.txt'
ESON = 'Elder Scrolls Online'

EQN = '\\twitout - EQN.csv'
EQNC = '\\twitout - EQN - UN.txt'
EQNN = 'EverQuest Next'

WIS = '\\twitout - WIS.csv'
WISC = '\\twitout - WIS - UN.txt'
WISN = 'WildStar'

#LIST FORM / POSITION
LIST = [START, LOL, HON, DO2, GW2, XIV, WOW, ESO, EQN, WIS]
LISTN = [START, LOLN, HONN, DO2N, GW2N, XIVN, WOWN, ESON, EQNN, WISN]
LISTC = [START, LOLC, HONC, DO2C, GW2C, XIVC, WOWC, ESOC, EQNC, WISC]
N = 1

#REPEAT FOR LOOP
while N <= 9:

    #IF THE FILE EXISTS (IT SHOULD) DELETE IT
    if os.path.isfile(r'C:\Users\Jesse_000\My Projects\PROPHECY-TEMP'+LIST[N]):
        row_count = sum(1 for row in csv.reader(open(r'C:\Users\Jesse_000\My Projects\PROPHECY-TEMP'+LIST[N])))
        i = int(row_count)
        os.remove(r'C:\Users\Jesse_000\My Projects\PROPHECY-TEMP'+LIST[N])
    else:
        i = 0
        pass

    if os.path.isfile(r'C:\Users\Jesse_000\My Projects\PROPHECY-TEMP'+LISTC[N]):
        row_count2 = sum(1 for line in open(r'C:\Users\Jesse_000\My Projects\PROPHECY-TEMP'+LISTC[N]))
        i2 = int(row_count2)
        os.remove(r'C:\Users\Jesse_000\My Projects\PROPHECY-TEMP'+LISTC[N])
    else:
        i2 = 0
        pass

    #RECREATE FILES
    saveFile = open(r'C:\Users\Jesse_000\My Projects\PROPHECY-TEMP'+LIST[N],'a')
    saveFile.write(pingtime+'\n')
    saveFile.close()

    saveFile2 = open(r'C:\Users\Jesse_000\My Projects\PROPHECY-TEMP'+LISTC[N],'a')
    saveFile2.write(pingtime+'\n')
    saveFile2.close()


    #SAVING FORK#
    if N <=9 :
        bucket[N] = i
        bucket2[N] = i2

    #NEXT
    N+=1


#OUTPUT#
print '*!* LIST COMPLETE -- PLEASE WAIT *!*' + '\n'
with open('o-twitter-tweets.csv', 'ab') as fp:
    output = csv.writer(fp, delimiter=',')
    data = [[pingtime, bucket[1], bucket[2], bucket[3], bucket[4], bucket[5], bucket[6], bucket[7], bucket[8], bucket[9]]]
    output.writerows(data)

with open('o-twitter-users.csv', 'ab') as fp:
    output = csv.writer(fp, delimiter=',')
    data = [[pingtime, bucket2[1], bucket2[2], bucket2[3], bucket2[4], bucket2[5], bucket2[6], bucket2[7], bucket2[8], bucket2[9]]]
    output.writerows(data)



################################# TWITTER #################################

#WRAP UP#
out_time = datetime.now().replace(microsecond=0)
duration = out_time-in_time
print '----------------------------> SENT'
print '       Completed in: ' + str(duration)
print 'w5748 <---------------------------'
time.sleep(2)
