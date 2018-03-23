# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile, glob
from bs4 import BeautifulSoup
from urllib import urlopen
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator

cl = LINETCR.LINE()
cl.login(token="Eq9g4NR6tzhQEVKgYHJ6.0P3FlAwpvyaZKXTQhGnEXG.dWMzB7xRFxQ1+zUEwLvhKltnw5aqWpImoU05QpVQwu8=")
cl.loginResult()

ki = kk = kc = cl 

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""═╬═══════════
✼ คำสั่งการใช้งานบอท ✼
═╬═══════════
═ই☬ই═ ดูรูป @
═ই☬ই═ ดูปก @
═ই☬ই═ ดู Mid @
═ই☬ই═ ดูโปรไฟล์ @
═ই☬ই═ ดูชื่อคนอื่น @
═ই☬ই═ ข้อมูลคนอื่น @
═ই☬ই═ ข้อมูลติดต่อ @
═ই☬ই═ สถานะคนอื่น @
═ই☬ই═ ลิงค์รูปคนอื่น @
═ই☬ই═ ลิงค์ปกคนอื่น @
═ই☬ই═ ข้อมูลกลุ่ม ↵
═ই☬ই═ ปิดลิงค์กลุ่ม ↵
═ই☬ই═ แท็กทั้งหมด ↵
═ই☬ই═ ส่งของขวัญ ↵
═ই☬ই═ ยกเลิกคำเชิญ ↵
═ই☬ই═ ค้นหารูป [คำค้น]
═ই☬ই═ หยุด ↵
═ই☬ই═ เช็คความเร็ว ↵

═╬═══════════
✼ คำสั่งแปลภาษา ✼
═╬═══════════
❂ T-th [คำ] ↬ ไทย
❂ T-ja [คำ] ↬ ญี่ปุ่น
❂ T-ko [คำ] ↬ เกาหลี
❂ T-en [คำ] ↬ อังกฤษ
❂ T-id [คำ] ↬ อินโด

═╬═══════════
✼ คำสั่งบอทดูคนอ่าน ✼
═╬═══════════
➲ ตั้งจุดอ่าน ↵
➲ ลบจุดอ่าน ↵
➲ ดูคนอ่าน ↵
╚════════════

Heart CookieRun Tⓗ
ツ จอมขมังเวทย์ ™
"""

imageed ="""═╬═══════════
✿ คำสั่งค้นหารูป ✿
═╬═══════════
✪ ค้นหารูป [พิมพ์คำค้นหา]
╠════════════
╠ ตัวอย่าง
╠ ค้นหารูป [ข้อความ]
╚════════════
"""

KAC=[cl,ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid]
admin=["ud29ddf2da58f558033931b6a1e035ec6"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'message':"ขอบคุณที่เพิ่มฉันเป็นเพื่อน\nHeart CookieRun Tⓗ\nกฏกติกาของกลุ่ม\nhttps://sites.google.com/view/cookierun/home",
    "lang":"JP",
    "comment":"Heart CookieRun Tⓗ",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True,
    "atjointicket":False,
    }

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

setTime = {}
setTime = wait2['setTime']

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d ชม. %02d นาที %02d วินาที' % (hours, mins, secs)    

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
	
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()
	
	
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error		

#-------------------------------------------------------------------------------------

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
            cl.acceptGroupInvitation(op.param1)
            cl.sendText(op.param1, "ขณะนี้มีการเชิญสมาชิกเข้ากลุ่ม")
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []

        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
												
#----------------------------------------------------------------------ส่งข้อมูลเข้ากลุ่ม
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                           cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"❂ ชื่อที่แสดง :\n" + msg.contentMetadata["displayName"] + "\n\n❂ MID :\n" + msg.contentMetadata["mid"] + "\n\n❂ สถานะข้อความ :\n" + contact.statusMessage + "\n\n❂ ลิงค์รูปส่วนตัว :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n❂ ลิงค์รูปปก :\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"❂ ชื่อที่แสดง :\n" + contact.displayName + "\n\n❂ MID :\n" + msg.contentMetadata["mid"] + "\n\n❂ สถานะข้อความ :\n" + contact.statusMessage + "\n\n❂ ลิงค์รูปส่วนตัว :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n❂ ลิงค์รูปปก :\n" + str(cu))
												
#---------------------------------------แปลภาษา--------------------------------------------------------------	

            elif "T-th " in msg.text:
                isi = msg.text.replace("T-th ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)                 
            elif "T-ja " in msg.text:
                isi = msg.text.replace("T-ja ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "T-ko " in msg.text:
                isi = msg.text.replace("T-ko ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "T-en " in msg.text:
                isi = msg.text.replace("T-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "T-id " in msg.text:
                isi = msg.text.replace("T-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)				
								
#---------------------------------พูดภาษา--------------------------------------								
            elif "S-th " in msg.text:
                say = msg.text.replace("S-th ","")
                lang = 'th'
                tts = gTTS(text=say, lang=lang)
                tts.save("say.mp3")
                cl.sendAudio(msg.to,"say.mp3")
							
            elif "S-ja " in msg.text:
                say = msg.text.replace("S-ja ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("say.mp3")
                cl.sendAudio(msg.to,"say.mp3")					
								
            elif "S-ko " in msg.text:
                say = msg.text.replace("S-ko ","")
                lang = 'ko'
                tts = gTTS(text=say, lang=lang)
                tts.save("say.mp3")
                cl.sendAudio(msg.to,"say.mp3")						
								
            elif "S-en " in msg.text:
                say = msg.text.replace("S-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("say.mp3")
                cl.sendAudio(msg.to,"say.mp3")			
								
            elif "S-id " in msg.text:
                say = msg.text.replace("S-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("say.mp3")
                cl.sendAudio(msg.to,"say.mp3")										
												
#-----------------------------------------------ค้นหารูป-------------------------------------------------------	

            elif "ค้นหารูป " in msg.text:
                search = msg.text.replace("ค้นหารูป ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass    
									
            elif "บอทค้นหายูทูป " in msg.text.lower():
                 query = msg.text.lower().replace("บอทค้นหายูทูป ","")
                 with requests.session() as s:
                     s.headers['user-agent'] = 'Mozilla/5.0'
                     url    = 'http://www.youtube.com/results'
                     params = {'search_query': query}
                     r    = s.get(url, params=params)
                     soup = BeautifulSoup(r.content, 'html5lib')
                     for a in soup.select('.yt-lockup-title > a[title]'):
                         if '&List' not in a['href']:
                             cl.sendText(msg.to,'Judul : ' + a['title'] + '\nLink : ' + 'http://www.youtube.com' + a['href'])			
														
            elif 'บอทค้นหาเพลง ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('บอทค้นหาเพลง ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Music : ' + song[0]
                        hasil += '\nLength : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "โปรดรอสักครู่... กำลังดึงเพลง")
                        cl.sendAudioWithURL(msg.to, song[3])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
																																																								
            elif msg.text.lower() == 'bot restart':
                cl.sendText(msg.to, "บอทกำลังรีสตาร์ท...")
                restart_program()
                print "@Restart"
																																				
            elif 'บอทค้นหาไอจี ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("บอทค้นหาไอจี ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))																	

            elif msg.text in ["บอท","บอด","Bot","bot"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)																		
											
            elif msg.text in ["ปิดลิงค์กลุ่ม","Link off"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดลิงค์กลุ่มสำเร็จค่ะ")
                    else:
                        cl.sendText(msg.to,"ปิดแล้ว")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ไม่สามารถใช้นอกกลุ่มได้")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
				
            elif msg.text.lower() == 'ข้อมูลกลุ่ม':
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "═════ ข้อมูลกลุ่ม ═════\n❂ ชื่อกลุ่ม :\n" + group.name + "\n\n❂ ไอดีกลุ่ม :\n" + group.id + "\n\n❂ ผู้สร้างกลุ่ม :\n" + gCreator + "\n\n❂ รูปกลุ่ม :\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nลิงค์กลุ่ม: เปิด"
                    else: md += "\n\nลิงค์กลุ่ม: ปิด"
                    if group.invitee is None: md += "\nสมาชิกทั้งหมด: " + str(len(group.members)) + " คน" + "\nไม่รับคำเชิญ: 0 คน"
                    else: md += "\nสมาชิกทั้งหมด : " + str(len(group.members)) + " คน" + "\nไม่รับคำเชิญ: " + str(len(group.invitee)) + " คน"
                    cl.sendText(msg.to,md)

								
            elif msg.text in ["สมน้ำหน้า","5555","55555"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["อิอิ","ชอบใจ"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["เศร้า"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["ชี้หน้า"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["โมโห","โกรธ"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["กรุณา","เมตตา"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in [";ว๊าย","ว้าย","ตกใจ"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["ฮ่าๆ","555","หัวเราะ"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["อืม","อืมม"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["ยินดีต้อนรับ","Welcome","Wc","wc"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
																		
#-----------------------------------------------runtime-------------------------------										
										
            elif msg.text.lower() == 'เช็คบอททำงาน':
                eltime = time.time() - mulai
                van = "═ บอททำงานมาแล้ว ═\n"+waktu(eltime)
                cl.sendText(msg.to,van)				
						
            elif "ตั้งจุดอ่าน" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"ตั้งจุดอ่านไปแล้ว")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "ตั้งจุดอ่านเรียบร้อยค่ะ")										
                     print wait2

                    
            elif "ลบจุดอ่าน" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"ลบจุดอ่านไปแล้ว")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "ลบจุดอ่าน: " + datetime.now().strftime('%H:%M:%S'))


                    
            elif "ดูคนอ่าน" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "คนอ่าน: ไม่มีใครอ่าน")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Readers: \n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nตั้งจุดอ่าน: %s\nเปิดดูคนอ่าน: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        cl.sendText(msg.to, "กลับไปตั้งจุดอ่านก่อน")			
								
            elif "แท็กทั้งหมด" == msg.text.lower():
                 group = cl.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                 if jml > 200  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "จำนวน: " + str(jml) +  " คน"
                 cnt.to = msg.to
                 cl.sendMessage(cnt)			
									
            elif "ดูโปรไฟล์" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"❂ ชื่อที่แสดง :\n" + contact.displayName + "\n❂ สถานะข้อความ :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"❂ รูปส่วนตัว : " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"❂ รูปปก : " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass	
									
            elif "ข้อมูลคนอื่น" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"❂ ชื่อที่แสดง :\n" + contact.displayName + "\n\n❂ Mid :\n" + contact.mid + "\n\❂ nสถานะข้อความ :\n" + contact.statusMessage + "\n\n❂ ลิงค์รูปส่วนตัว :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n❂ ลิงค์รูปปก :\n" + str(cu))
                except:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))
										
            elif "สถานะคนอื่น" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "=== ❂ สถานะข้อความ ❂ ===\n" + contact.statusMessage)
                except:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
										
            elif "ดูชื่อคนอื่น" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "=== ❂ ชื่อที่แสดง ❂ ===\n" + contact.displayName)
                except:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)			
										
            elif "ข้อมูลติดต่อ" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)  										

            elif msg.text in ["หยุด"]:
	            cl.sendText(msg.to,"Stop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nThank You :)")
							
            elif "ลิงค์ปกคนอื่น @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("ลิงค์ปกคนอื่น @","")    
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"ไม่พบที่อยู่ติดต่อ")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)          
                            path = str(cu)
                            cl.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
								
            elif "ลิงค์รูปคนอื่น @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("ลิงค์รูปคนอื่น @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"ไม่พบที่อยู่ติดต่อ")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"					
								
            elif ("ดู Mid " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)		
									
            elif msg.text in ["ส่งของขวัญ","ของขวัญ"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)									
								
#-----------------------------------------------ล้างกลุ่ม--------------------------------													
#            elif "Cleanse" in msg.text:
#                if msg.toType == 2:
#                    print "ok"
#                    _name = msg.text.replace("Cleanse","")
#                    gs = ki.getGroup(msg.to)
#                    gs = kk.getGroup(msg.to)
#                    gs = kc.getGroup(msg.to)
#                    ki.sendText(msg.to,"Just some casual cleansing ô")
#                    kk.sendText(msg.to,"Group cleansed.")
#                    kc.sendText(msg.to,"Fuck You All")
#                    targets = []
#                    for g in gs.members:
#                        if _name in g.displayName:
#                            targets.append(g.mid)
#                    if targets == []:
#                        ki.sendText(msg.to,"Not found.")
#                        kk.sendText(msg.to,"Not found.")
#                        kc.sendText(msg.to,"Not found.")
#                    else:
#                        for target in targets:
#                            try:
#                                klist=[ki,kk,kc]
#                                kicker=random.choice(klist)
#                                kicker.kickoutFromGroup(msg.to,[target])
#                                print (msg.to,[g.mid])
#                            except:
#                                ki.sendText(msg.to,"Group cleanse")
#                                kk.sendText(msg.to,"Group cleanse")
#                                kc.sendText(msg.to,"Group cleanse")
#-----------------------------------------------ล้างกลุ่ม--------------------------------
#            elif "Nk " in msg.text:
#                  if msg.from_ in admin:
#                       nk0 = msg.text.replace("Nk ","")
#                       nk1 = nk0.lstrip()
#                       nk2 = nk1.replace("@","")
#                       nk3 = nk2.rstrip()
#                       _name = nk3
#                       gs = cl.getGroup(msg.to)
#                       targets = []
#                       for s in gs.members:
#                           if _name in s.displayName:
#                              targets.append(s.mid)
#                       if targets == []:
#                           sendMessage(msg.to,"user does not exist")
#                           pass
#                       else:
#                           for target in targets:
#                                try:
#                                    klist=[cl,ki,kk,kc]
#                                    kicker=random.choice(klist)
#                                    kicker.kickoutFromGroup(msg.to,[target])
#                                    print (msg.to,[g.mid])
#                                except:
#                                    ki.sendText(msg.to,"Succes Cv")
#                                    kk.sendText(msg.to,"Fuck You")
#------------------------------------------------------------------
            elif msg.text in ["เมา"]:
                ki.sendText(msg.to,"บางคนว่า ไปดื่มสุรามา")
#------------------------------------------------------------------
            elif msg.text in ["วันวาเลนไทน์","Happy Valentine's Day","สุขสันต์วันวาเลนไทน์"]:
                ki.sendText(msg.to,"ไม่ได้เสียดแทงสักนิด\nแค่ตรงอกข้างซ้ายมันจี๊ดๆ ก็เท่านั้น\nไม่ได้ให้ความสำคัญ\nแค่วันวาเลนไทน์หนึ่งวัน ไม่มีอะไร")
#------------------------------------------------------------------
            elif msg.text in ["55"]:
                ki.sendText(msg.to,"สวัสดีเพื่อน 􀜁􀅔Har Har􏿿")
#------------------------------------------------------------------

            elif msg.text in ["5555"]:
                ki.sendText(msg.to,"เอิ๊กกก!! 􀜁􀅔Har Har􏿿")
#------------------------------------------------------------------
            elif msg.text in ["สุดยอด","ยอดเยี่ยม","ดีเลิศ"]:
                ki.sendText(msg.to,"สุดยอด 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"ยอดเยี่ยม 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"ดีเลิศ 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#------------------------------------------------------------------	
            elif "ดูปก @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("ดูปก @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"ไม่พบข้อมูลติดต่อ")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"			
#------------------------------------------------------------------
            elif "ดูรูป @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("ดูรูป @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"ไม่พบข้อมูลติดต่อ")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"			
#------------------------------------------------------------------

            elif msg.text in ["ยกเลิกเชิญ","ยกเลิกค้างเชิญ","ยกเลิกคำเชิญ","ยกเลิกเข้ากลุ่ม"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"ยกเลิกคำเชิญสำเร็จค่ะ")
										
            elif msg.text in ["สปีดบอท","สปิดบอท","บอทสปีด","บอทสปิด","bs","Bs","เช็คความเร็ว"]:
                start = time.time()
                cl.sendText(msg.to, "เช็คความเร็ว...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s วินาที" % (elapsed_time))					
																									
#---------------------ทักคนเข้าออก
#        if op.type == 17:
#          if op.param2 in Bots:
#            return
#          ginfo = cl.getGroup(op.param1)
#          random.choice(KAC).sendText(op.param1, "สวัสดีค่ะ "+ cl.getContact(op.param2).displayName +"\nยินดีต้อนรับเข้าสู่กลุ่ม " + str(ginfo.name))
#          random.choice(KAC).sendText(op.param1, "กรุณาอ่านกฏของกลุ่ม\nและการปิดแจ้งเตือนกลุ่มได้ที่โน้ตค่ะ")
#          random.choice(KAC).sendText(op.param1, "ขอบคุณค่ะ !!!😘")
#          print "MEMBER HAS JOIN THE GROUP"
#        if op.type == 15:
#          if op.param2 in Bots:
#             return
#          random.choice(KAC).sendText(op.param1, "ออกกลุ่มกันอีกแล้ว\nโชคดีนะคะ บ๊ะบาย 😊")
#          print "MEMBER HAS LEFT THE GROUP"
#					
#---------------------ทักคนเข้าออกแบบมีดึงรูป
        if op.type == 17:
          if op.param2 in Bots:
            return
          ginfo = cl.getGroup(op.param1)
          contact = cl.getContact(op.param2)
          image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
          cl.sendImageWithURL(op.param1,image)					
          random.choice(KAC).sendText(op.param1, "สวัสดีค่ะ "+ cl.getContact(op.param2).displayName +"\nยินดีต้อนรับเข้าสู่กลุ่ม\n" + str(ginfo.name))
          random.choice(KAC).sendText(op.param1, "กรุณาอ่านกฏของกลุ่ม⚡\nและวิธีปิดเสียงแจ้งเตือนในกลุ่ม\nhttps://sites.google.com/view/cookierun/home")
          random.choice(KAC).sendText(op.param1, "ขอบคุณค่ะ !!!^_^")
          print "MEMBER HAS JOIN THE GROUP"
					
        if op.type == 15:
          if op.param2 in Bots:
             return
          random.choice(KAC).sendText(op.param1, "โชคดีนะคะ บ๊ะบาย ^_^")
          print "MEMBER HAS LEFT THE GROUP"	
																				
#------------------------------------------------------------------
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass



        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)

			