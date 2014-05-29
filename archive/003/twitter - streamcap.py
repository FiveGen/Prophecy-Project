# -*- coding: UTF-8 -*-
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from datetime import datetime
import time

#RETRIEVED FROM USER-INFO @ TWITTER'S API
ckey = '????????????????'
csecret = '????????????????'
atoken = '????????????????'
asecret = '????????????????'

#FILTER TERMS
LOL = ['leagueoflegend', 'Leagueoflegend', 'LeagueofLegend', 'LeagueOfLegend', 'LEAGUEOFLEGEND', 'league of legend', 'League of legend', 'League of Legend', 'League Of Legend']
HON = ['honupdate', 'Honupdate', 'HoNupdate', 'HONupdate', 'HONUPDATES', 'heroesofnewerth', 'Heroesofnewerth', 'HeroesofNewerth', 'HeroesOfNewerth', 'HEROESOFNEWERTH', 'heroes of newerth', 'Heroes of newerth', 'Heroes of Newerth', 'Heroes Of Newerth', 'HEROES OF NEWERTH']
DO2 = ['dota2', 'Dota2', 'DotA2', 'DOTA2', 'dota 2', 'Dota 2', 'DotA 2', 'DOTA 2', 'dota2update', 'Dota2update', 'DotA2update', 'DOTA2update', 'DOTA2UPDATE']    

GW2 = ['guildwars2', 'Guildwars2', 'GuildWars2', 'GUILDWARS2', 'guild wars 2', 'Guild wars 2', 'Guild Wars 2', 'GUILD WARS 2', 'gw2', 'Gw2', 'GW2']
XIV = ['ffxiv', 'Ffxiv', 'FFxiv', 'ffXIV', 'FFXIV', 'ff xiv', 'FF XIV', 'finalfantasyxiv' ,'Finalfantasyxiv', 'FinalFantasyxiv', 'FinalFantasyXIV', 'FINALFANTASYXIV', 'final fantasy xiv', 'Final fantasy xiv', 'Final Fantasy xiv', 'Final Fantasy XIV', 'FINAL FANTASY XIV', 'ff_xiv', 'FF_XIV']
WOW = ['worldofwarcraft', 'Worldofwarcraft', 'WorldofWarcraft', 'WorldOfWarcraft', 'WORLDOFWARCRAFT', 'world of warcraft', 'World of warcraft', 'World of Warcraft', 'World Of Warcraft', 'WORLD OF WARCRAFT']

ESO = ['tesonline', 'Tesonline', 'TESonline', 'TESOnline', 'TESONLINE', '#eso', '#Eso', '#ESO', 'elderscrollsonline', 'Elderscrollsonline', 'ElderScrollsonline', 'ElderScrollsOnline', 'ELDERSCROLLSONLINE', 'elder scrolls online', 'Elder scrolls online', 'Elder Scrolls online', 'Elder Scrolls Online', 'ELDER SCROLLS ONLINE']
EQN = ['everquest_next', 'Everquest_next', 'EverQuest_next', 'EverQuest_Next', 'EVERQUEST_NEXT', 'eqnext', 'Eqnext', 'EQnext', 'EQNext', 'EQNEXT', 'everquestnext', 'Everquestnext', 'EverQuestnext', 'EverQuestNext', 'EVERQUESTNEXT', 'everquest next', 'Everquest next', 'EverQuest next', 'EverQuest Next', 'EVERQUEST NEXT', 'eqn', 'Eqn', 'EQN']
WIS = ['wildstar', 'Wildstar', 'WildStar', 'WILDSTAR']

class listener(StreamListener):

    def on_data(self, data):
        try:
            
            tweet = data.split(',"text":"')[1].split('","source')[0]
            username = data.split(',"screen_name":"')[1].split('","location')[0]

            #PRINT OUTPUT IN IDLE
            print '@' + username
            print tweet + '\n'
            
            #RAW OUTPUT - INACTIVE
            #saveThis = str(datetime.now())+ ' ¶ ' + username + ' ¶ ' + tweet
            #saveFile = open('twitout - ARCHIVE.csv','a')
            #saveFile.write(saveThis+'\n')
            #saveFile.close()
            
#LOL        #WRITE TWEETS TO 'twitout - TAG.csv'
            for TR1 in LOL:                
                if TR1 in tweet:
                    saveThis = str(datetime.now())+ ' ¶ ' + username + ' ¶ ' + tweet
                    saveFile = open('twitout - LOL.csv','a')
                    saveFile.write(saveThis+'\n')
                    saveFile.close()

                    if username in open('twitout - LOL - UN.txt').read():
                        pass
                    else:
                        checkpoint = open("twitout - LOL - UN.txt", "a")    
                        checkpoint.write(username+'\n')
                        checkpoint.close()
            else:
                pass
            
#HON        #WRITE TWEETS TO 'twitout - TAG.csv'            
            for TR2 in HON:                
                if TR2 in tweet:
                    saveThis = str(datetime.now())+ ' ¶ ' + username + ' ¶ ' + tweet
                    saveFile = open('twitout - HON.csv','a')
                    saveFile.write(saveThis+'\n')
                    saveFile.close()
                    
                    if username in open('twitout - HON - UN.txt').read():
                        pass
                    else:
                        checkpoint = open("twitout - HON - UN.txt", "a")    
                        checkpoint.write(username+'\n')
                        checkpoint.close()          
            else:
                pass

#DO2        #WRITE TWEETS TO 'twitout - TAG.csv'            
            for TR3 in DO2:                
                if TR3 in tweet:
                    saveThis = str(datetime.now())+ ' ¶ ' + username + ' ¶ ' + tweet
                    saveFile = open('twitout - DO2.csv','a')
                    saveFile.write(saveThis+'\n')
                    saveFile.close()
                    
                    if username in open('twitout - DO2 - UN.txt').read():
                        pass
                    else:
                        checkpoint = open("twitout - DO2 - UN.txt", "a")    
                        checkpoint.write(username+'\n')
                        checkpoint.close()          
            else:
                pass

#GW2        #WRITE TWEETS TO 'twitout - TAG.csv'            
            for TR4 in GW2:                
                if TR4 in tweet:
                    saveThis = str(datetime.now())+ ' ¶ ' + username + ' ¶ ' + tweet
                    saveFile = open('twitout - GW2.csv','a')
                    saveFile.write(saveThis+'\n')
                    saveFile.close()
                    
                    if username in open('twitout - GW2 - UN.txt').read():
                        pass
                    else:
                        checkpoint = open("twitout - GW2 - UN.txt", "a")    
                        checkpoint.write(username+'\n')
                        checkpoint.close()          
            else:
                pass
       
#XIV        #WRITE TWEETS TO 'twitout - TAG.csv'            
            for TR5 in XIV:                
                if TR5 in tweet:
                    saveThis = str(datetime.now())+ ' ¶ ' + username + ' ¶ ' + tweet
                    saveFile = open('twitout - XIV.csv','a')
                    saveFile.write(saveThis+'\n')
                    saveFile.close()
                    
                    if username in open('twitout - XIV - UN.txt').read():
                        pass
                    else:
                        checkpoint = open("twitout - XIV - UN.txt", "a")    
                        checkpoint.write(username+'\n')
                        checkpoint.close()          
            else:
                pass
       
#WOW        #WRITE TWEETS TO 'twitout - TAG.csv'            
            for TR6 in WOW:                
                if TR6 in tweet:
                    saveThis = str(datetime.now())+ ' ¶ ' + username + ' ¶ ' + tweet
                    saveFile = open('twitout - WOW.csv','a')
                    saveFile.write(saveThis+'\n')
                    saveFile.close()
                    
                    if username in open('twitout - WOW - UN.txt').read():
                        pass
                    else:
                        checkpoint = open("twitout - WOW - UN.txt", "a")    
                        checkpoint.write(username+'\n')
                        checkpoint.close()          
            else:
                pass
       
#ESO        #WRITE TWEETS TO 'twitout - TAG.csv'            
            for TR7 in ESO:                
                if TR7 in tweet:
                    saveThis = str(datetime.now())+ ' ¶ ' + username + ' ¶ ' + tweet
                    saveFile = open('twitout - ESO.csv','a')
                    saveFile.write(saveThis+'\n')
                    saveFile.close()
                    
                    if username in open('twitout - ESO - UN.txt').read():
                        pass
                    else:
                        checkpoint = open("twitout - ESO - UN.txt", "a")    
                        checkpoint.write(username+'\n')
                        checkpoint.close()          
            else:
                pass
       
#EQN        #WRITE TWEETS TO 'twitout - TAG.csv'            
            for TR8 in EQN:                
                if TR8 in tweet:
                    saveThis = str(datetime.now())+ ' ¶ ' + username + ' ¶ ' + tweet
                    saveFile = open('twitout - EQN.csv','a')
                    saveFile.write(saveThis+'\n')
                    saveFile.close()
                    
                    if username in open('twitout - EQN - UN.txt').read():
                        pass
                    else:
                        checkpoint = open("twitout - EQN - UN.txt", "a")    
                        checkpoint.write(username+'\n')
                        checkpoint.close()          
            else:
                pass
       
#WIS        #WRITE TWEETS TO 'twitout - TAG.csv'            
            for TR9 in WIS:                
                if TR9 in tweet:
                    saveThis = str(datetime.now())+ ' ¶ ' + username + ' ¶ ' + tweet
                    saveFile = open('twitout - WIS.csv','a')
                    saveFile.write(saveThis+'\n')
                    saveFile.close()
                    
                    if username in open('twitout - WIS - UN.txt').read():
                        pass
                    else:
                        checkpoint = open("twitout - WIS - UN.txt", "a")    
                        checkpoint.write(username+'\n')
                        checkpoint.close()          
            else:
                pass
            

            return True
        except BaseException, e:
            print 'failed ondata,',str(e)
            time.sleep(5)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["league of legends", "leagueoflegends", "heroes of newerth", "heroesofnewerth", "honupdates", "dota2", "dota 2", "dota2update", "defense of the ancients 2", "guild wars 2", "guildwars2", "gw2", "final fantasy xiv", "finalfantasyxiv", "ffxiv", "ff xiv", "ff_xiv", "worldofwarcraft", "world of warcraft", "tesonline", "#eso", "elderscrollsonline", "elder scrolls online", "everquest_next", "eqnext", "everquestnext", "everquest next", "eqn", "wildstar", "wildstaronline"])
