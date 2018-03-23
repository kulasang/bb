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
cl.login(token="ErKakGR6QbhKHryE86b7.JCxLmhfn3/VLfwqc5bVyPW.0HXJCtfbtptaZf2iYcpIDVV3PwaKQsWV1gclNFiSuvM=")
cl.loginResult()
ki=ki2=ki3=ki4=ki5=cl

#ki = LINETCR.LINE()
#ki.login(token="EoX1rd3xpjK82kF2IMA9.t7v2LvRz3GCkUHyLzDDc2q.Nl+M5DW4HnCzJdoXde2scFt93rfLZlJsPZDq5p7a6+M=")
#ki.loginResult()

#ki2 = LINETCR.LINE()
#ki2.login(token="EoFvJ5ccVW2gvlJHOf3a.vEBY+Y2QVdOqemdC3PQ6AG.uCx2I8G4XUcRfkyoSjbQcoh/cUb26Nl9DMJsKl61r3E=")
#ki2.loginResult()

#ki3 = LINETCR.LINE()
#ki3.login(token="Eox1dXOz6AX7uqr3nqSd.094l8EE2ISIuSUEfzNdk7q.GHnL/cQ0mjN3MDCQSykGsO8bI/ICr4hOyj1eBeW+fgs=")
#ki3.loginResult()

#ki4 = LINETCR.LINE()
#ki4.login(token="Eo3yuOTuGn2PPYZjsxv4.96gpD5B6YLmvdeMovojpXa.+yLY0CWxpvuV4xRZ2qrFzS5rqADY7Ll8y1A2dgKZ30s=")
#ki4.loginResult()

#ki5 = LINETCR.LINE()
#ki5.login(token="EoPKH5gqEzR1JiKWneJ9.hTRNKLkHz4SUmofwievP2q.kgrbOut1ZywJsFViVF4jaxwuCiKN8/J+6S0d1J7Do1I=")
#ki5.loginResult()

print u"Login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""═╬═══════════
✿ Command Player ★
═╬═══════════
✪ Tagall ≫ แท็กทั้งหมด
✪ Point ≫ ตั้งจุดคนอ่าน
✪ Read ≫ ดูคนอ่าน
✪ Clear ≫ ลบจุดคนอ่าน
✪ Gift ≫ ส่งของขวัญ
✪ Myid ≫ ดู id
✪ Mymid ≫ ดู Mid
✪ Mycopy @ ≫ แปลงร่าง
✪ Mybackup ≫ คืนร่าง
✪ Mybio ≫ ข้อความสถานะ
✪ Mypict ≫ รูปของฉัน
✪ Mypict-u ≫ ลิงค์รูป
✪ Mycover ≫ รูปปกของฉัน
✪ Mycover-u ≫ ลิงค์รูปปก
✪ Myname ≫ ชื่อที่แสดง
✪ Blocklist ≫ ผู้ใช้ที่บล็อค
✪ Clearchat ≫ ล้างแชท
✪ Block @ ≫ บล็อค
✪ Getprofile @ ≫ โปรไฟล์
✪ Getpict @ ≫ รูปคนอื่น
✪ Getpict-u @ ≫ ลิงค์รูป
✪ Getcover @ ≫ รูปปกคนอื่น
✪ Getcover-u @ ≫ ลิงค์ปก
✪ Getbio @ ≫ สถานะคนอื่น
✪ Getcontact @ ≫ คท.
✪ Getinfo @ ≫ ข้อมูลคนอื่น
✪ Getmid @ ≫ Mid คนอื่น
✪ Getname @ ≫ ดูชื่อคนอื่น
✪ Spam @ ≫ สแปมแชท
✪ Mimic on/off ≫ เลียนคำพูด
✪ Micadd @ ≫ เพิ่มเป้าหมาย
✪ Micdel @ ≫ ยกเลิกเป้าหมาย
✪ Wc check ≫ เช็คข้อความต้อนรับ
✪ Wc update:_ ≫ ข้อความต้อนรับ
✪ Bc:ct_ ≫ ส่งข้อความถึงทุกคน
✪ Bc:grup_ ≫ ส่งข้อความทุกกลุ่ม
✪ Myname:_ ≫ เปลี่ยนชื่อ
✪ Mybio:_ ≫ เปลี่ยนสถานะ
✪ Msg check ≫ เช็คข้อความ
✪ Msg set:_ ≫ เปลี่ยนข้อความ
✪ Comment ≫ เช็คคอมเมนต์
✪ Comment set:_ ≫ ตั้งค่า
✪ Timeline:_ ≫ โพสต์ไทม์ไลน์
✪ Stop ≫ คำสั่งหยุด

═╬═══════════
✪ Command for kicker ★
═╬═══════════
✿ All mid ≫ Mid บอททั้งหมด
✿ Allbio:_ ≫ เปลี่ยนสถานะ
✿ Allname:_ ≫ เปลี่ยนชื่อบอท
✿ Bot sp ≫ เช็คความเร็วบอท
✿ Cleargrup* ≫ ล้างกลุ่ม
✿ Copy @ ≫ แปลงร่าง
✿ Backup ≫ คืนร่าง
✿ Invite ≫ เชิญด้วย คท.
✿ Mid @ ≫ Mid คนอื่น
✿ Mybot ≫ บอท คท.
✿ Rsk @ ≫ สั่งเตะด้วยบอท
✿ Sbye ≫ ไล่บอทออกกลุ่ม
✿ Scome ≫ เชิญบอทเข้ากลุ่ม
✿ Sgohome ≫ สั่งบอทออกทุกกลุ่ม
✿ Sgreet ≫ ให้บอททักทาย
✿ Sname ≫ เช็คชื่อบอท
✿ Bot:ct_ ≫ ส่งข้อความถึงทุกคน
✿ Bot:grup_≫ ส่งข้อความทุกกลุ่ม
✿ S1-4glist ≫ บอทอยู่กลุ่มไหน
✿ As1-5 ≫ บอท คท. ทีละตัว
✿ 1-5 in ≫ เชิญเข้ากลุ่มทีละตัว
✿ 1-5 Bye ≫ ให้ออกกลุ่มที่ละตัว
✿ 1-5 Gift ≫ ส่งของขวัญทีละตัว
✿ 1-5 Mid ≫ ดู Mid บอททีละตัว
✿ 1-5pro:_ ≫ เปลี่ยนชื่อทีละตัว

═╬═══════════
✿ Command Admin ★
═╬═══════════ 
✪ Ban @ ≫ แบน
✪ Unban @ ≫ ยกเลิกแบน
✪ Banlist ≫ รายการแบน
✪ Clearban ≫ ล้างแบน
✪ Kick @ ≫ เตะ
✪ kill ≫ เตะคนติดแบน
✪ Bye all* ≫ ออกทุกกลุ่ม
✪ Cancel ≫ ยกเลิกเชิญ
✪ Ginfo ≫ ข้อมูลกลุ่ม
✪ Glist ≫ รายชื่อกลุ่ม
✪ Gname:_ ≫ แก้ไขชื่อกลุ่ม
✪ Invite:_ ≫ เชิญด้วย Mid
✪ Ingrup ≫ ดูกลุ่มที่เชิญ
✪ List grup ≫ ไอดีทุกกลุ่ม
✪ Nuke* (ล้างกลุ่ม)
✪ Recover ≫ เชิญเข้ากลุ่มใหม่
✪ Reject ≫ ยกเลิกถูกเชิญ
✪ Rejectall ≫ ล้างโดนรัน
✪ Url ≫ ขอลิงค์กลุ่ม

═╬═══════════
✪ Command Setting ★
═╬═══════════
✿ Add on/off ≫ ทักก่อนรับแอด
✿ Contact on/off ≫ อ่าน คท.
✿ Join on/off ≫ เข้ากลุ่มอัตโนมัติ
✿ Leave on/off ≫ กันรันแชทรวม
✿ Like on/off ≫ ไลค์อัตโนมัติ
✿ Link on/off ≫ ลิงค์กลุ่ม
✿ Ment on/off ≫ คอมเมนต์
✿ Share on/off ≫ แชร์ไทม์ไลน์
✿ Wc on/off ≫ ข้อความต้อนรับ
✿ Tag on/off ≫ ตอบแท็กอัตโนมัติ
✿ Tagkick on/off ≫ เตะคนแท็ก
✿ Set ≫ ดูการตั้งค่า

═╬═══════════
✿ Command Guard ★
═╬═══════════
✪ Allguard on/off ≫ ป้องกันทั้งหมด
✪ Cancel on/off ≫ ยกเลิกคำเชิญ
✪ Guard on/off ≫ บอทเตะทำงาน
✪ Invite on/off ≫ ให้เชิญเพื่อน
✪ Qr link on/off ≫ ป้องกันลิงค์กลุ่ม  

═╬═══════════
✪ Translate ★
═╬═══════════
✿ .th _ ≫ แปลภาษาไทย
✿ .ja _ ≫ แปลภาษาญี่ปุ่น
✿ .ko _ ≫ แปลภาษาเกาหลี
✿ .en _ ≫ แปลภาษาอังกฤษ
✿ .id _ ≫ แปลภาษาอินโดนีเซีย

═╬═══════════
✿ Command System ★
═╬═══════════
✪ CPU ≫ ข้อมูล CPU เซิร์ฟเวอร์
✪ ifconfig ≫ ข้อมูล ip เซิร์ฟเวอร์
✪ Kernel ≫ Kernel เซิร์ฟเวอร์
✪ System ≫ ข้อมูลระบบเซิร์ฟเวอร์
✪ Runtime ≫ เช็คการทำงาน

⌘ จอมขมังเวทย์ ⌘
http://line.me/ti/p/~ed-kulasang
                    
"""

menu1 ="""═╬═══════════
✿ Command Player ★
═╬═══════════
✪ Tagall ≫ แท็กทั้งหมด
✪ Point ≫ ตั้งจุดคนอ่าน
✪ Read ≫ ดูคนอ่าน
✪ Clear ≫ ลบจุดคนอ่าน
✪ Gift ≫ ส่งของขวัญ
✪ Myid ≫ ดู id
✪ Mymid ≫ ดู Mid
✪ Mycopy @ ≫ แปลงร่าง
✪ Mybackup ≫ คืนร่าง
✪ Mybio ≫ ข้อความสถานะ
✪ Mypict ≫ รูปของฉัน
✪ Mypict-u ≫ ลิงค์รูป
✪ Mycover ≫ รูปปกของฉัน
✪ Mycover-u ≫ ลิงค์รูปปก
✪ Myname ≫ ชื่อที่แสดง
✪ Blocklist ≫ ผู้ใช้ที่บล็อค
✪ Clearchat ≫ ล้างแชท
✪ Block @ ≫ บล็อค
✪ Getprofile @ ≫ โปรไฟล์
✪ Getpict @ ≫ รูปคนอื่น
✪ Getpict-u @ ≫ ลิงค์รูป
✪ Getcover @ ≫ รูปปกคนอื่น
✪ Getcover-u @ ≫ ลิงค์ปก
✪ Getbio @ ≫ สถานะคนอื่น
✪ Getcontact @ ≫ คท.
✪ Getinfo @ ≫ ข้อมูลคนอื่น
✪ Getmid @ ≫ Mid คนอื่น
✪ Getname @ ≫ ดูชื่อคนอื่น
✪ Mimic on/off ≫ เลียนคำพูด
✪ Micadd @ ≫ เพิ่มเป้าหมาย
✪ Micdel @ ≫ ยกเลิกเป้าหมาย
✪ Wc check ≫ เช็คข้อความต้อนรับ
✪ Wc update:_ ≫ ข้อความต้อนรับ
✪ Bc:ct_ ≫ ส่งข้อความถึงทุกคน
✪ Bc:grup_ ≫ ส่งข้อความทุกกลุ่ม
✪ Myname:_ ≫ เปลี่ยนชื่อ
✪ Mybio:_ ≫ เปลี่ยนสถานะ
✪ Msg check ≫ เช็คข้อความ
✪ Msg set:_ ≫ เปลี่ยนข้อความ
✪ Comment ≫ เช็คคอมเมนต์
✪ Comment set:_ ≫ ตั้งค่า
✪ Timeline:_ ≫ โพสต์ไทม์ไลน์
✪ Stop ≫ คำสั่งหยุด
═╬═══════════

⌘ จอมขมังเวทย์ ⌘
http://line.me/ti/p/~ed-kulasang

"""

menu2 ="""═╬═══════════
✿ Command Admin ★
═╬═══════════ 
✪ Ban @ ≫ แบน
✪ Unban @ ≫ ยกเลิกแบน
✪ Banlist ≫ รายการแบน
✪ Clearban ≫ ล้างแบน
✪ Kick @ ≫ เตะ
✪ kill ≫ เตะคนติดแบน
✪ Bye all* ≫ ออกทุกกลุ่ม
✪ Cancel ≫ ยกเลิกเชิญ
✪ Ginfo ≫ ข้อมูลกลุ่ม
✪ Glist ≫ รายชื่อกลุ่ม
✪ Gname:_ ≫ แก้ไขชื่อกลุ่ม
✪ Invite:_ ≫ เชิญด้วย Mid
✪ Ingrup ≫ ดูกลุ่มที่เชิญ
✪ List grup ≫ ไอดีทุกกลุ่ม
✪ Nuke* (ล้างกลุ่ม)
✪ Recover ≫ เชิญเข้ากลุ่มใหม่
✪ Reject ≫ ยกเลิกถูกเชิญ
✪ Rejectall ≫ ล้างโดนรัน
✪ Url ≫ ขอลิงค์กลุ่ม
═╬═══════════

⌘ จอมขมังเวทย์ ⌘
http://line.me/ti/p/~ed-kulasang

"""

menu3 ="""═╬═══════════
✪ Command Setting ★
═╬═══════════
✿ Add on/off ≫ ทักก่อนรับแอด
✿ Contact on/off ≫ อ่าน คท.
✿ Join on/off ≫ เข้ากลุ่มอัตโนมัติ
✿ Leave on/off ≫ กันรันแชทรวม
✿ Like on/off ≫ ไลค์อัตโนมัติ
✿ Link on/off ≫ ลิงค์กลุ่ม
✿ Ment on/off ≫ คอมเมนต์
✿ Share on/off ≫ แชร์ไทม์ไลน์
✿ Wc on/off ≫ ข้อความต้อนรับ
✿ Tag on/off ≫ ตอบแท็กอัตโนมัติ
✿ Tagkick on/off ≫ เตะคนแท็ก
✿ Set ≫ ดูการตั้งค่า
═╬═══════════

⌘ จอมขมังเวทย์ ⌘
http://line.me/ti/p/~ed-kulasang

"""

menu4 ="""═╬═══════════
✿ Command Guard ★
═╬═══════════
✪ Allguard on/off ≫ ป้องกันทั้งหมด
✪ Cancel on/off ≫ ยกเลิกคำเชิญ
✪ Guard on/off ≫ บอทเตะทำงาน
✪ Invite on/off ≫ ให้เชิญเพื่อน
✪ Qr link on/off ≫ ป้องกันลิงค์กลุ่ม  
═╬═══════════

⌘ จอมขมังเวทย์ ⌘
http://line.me/ti/p/~ed-kulasang

"""

menu5 ="""═╬═══════════
✪ Translate ★
═╬═══════════
✿ .th _ ≫ แปลภาษาไทย
✿ .ja _ ≫ แปลภาษาญี่ปุ่น
✿ .ko _ ≫ แปลภาษาเกาหลี
✿ .en _ ≫ แปลภาษาอังกฤษ
✿ .id _ ≫ แปลภาษาอินโดนีเซีย
═╬═══════════

⌘ จอมขมังเวทย์ ⌘
http://line.me/ti/p/~ed-kulasang

"""

menu6 ="""═╬═══════════
✿ Command System ★
═╬═══════════
✪ CPU ≫ ข้อมูล CPU เซิร์ฟเวอร์
✪ ifconfig ≫ ข้อมูล ip เซิร์ฟเวอร์
✪ Kernel ≫ Kernel เซิร์ฟเวอร์
✪ System ≫ ข้อมูลระบบเซิร์ฟเวอร์
✪ Runtime ≫ เช็คการทำงาน
═╬═══════════

⌘ จอมขมังเวทย์ ⌘
http://line.me/ti/p/~ed-kulasang
                    
"""

KAC=[cl,ki,ki2,ki3,ki4,ki5]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
Bots = [mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,"u8dc5e530714ddfebe5156402e41bd8a7"]
bot1 = cl.getProfile().mid
admsa = "u8dc5e530714ddfebe5156402e41bd8a7"
admin = "u8dc5e530714ddfebe5156402e41bd8a7"
creator = "u8dc5e530714ddfebe5156402e41bd8a7"

wait = {
    'contact':True,
    'autoJoin':False,
    'autoCancel':{"on":False,"members":10},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'message':"ขอบคุณที่เพิ่มฉันเป็นเพื่อน หากสนใจปั้มเหรียญคุกกี้รันทักมาได้นะครับ ล้านละ 1 บาท หรือจะปั้มอย่างอื่นก็ได้บริการถูกๆ เป็นกันเอง",
    "lang":"JP",
    "comment":"ข้าคือมือพระกาฬ ปั้มคุกกี้รัน",
    "commentOn":False,
    "likeOn":False,
    'detectMention':True,	
    'kickMention':False,  	
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "welmsg":"แนะนำตัวด้วยครับ บอกชื่อ อายุ",	
    "welcomemsg":False,	
}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    "ricoinvite":{},
    'ROM':{},
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

lgncall = ""
def logincall(this):
    cl.sendText(lgncall,"Asul login url: "+this)

setTime = {}
setTime = wait2['setTime']
blacklistFile='blacklist.txt'
pendinglistFile='pendinglist.txt'

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki2.getProfile()
backup2 = ki2.getProfile()
backup2.displayName = contact.displayName
backup2.statusMessage = contact.statusMessage
backup2.pictureStatus = contact.pictureStatus

contact = ki3.getProfile()
backup3 = ki3.getProfile()
backup3.displayName = contact.displayName
backup3.statusMessage = contact.statusMessage
backup3.pictureStatus = contact.pictureStatus

contact = ki4.getProfile()
backup4 = ki4.getProfile()
backup4.displayName = contact.displayName
backup4.statusMessage = contact.statusMessage
backup4.pictureStatus = contact.pictureStatus

contact = ki5.getProfile()
backup5 = ki5.getProfile()
backup5.displayName = contact.displayName
backup5.statusMessage = contact.statusMessage
backup5.pictureStatus = contact.pictureStatus

user1 = mid
user2 = ""

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
    
def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(0)
    akh = int(0)
    nm = nama
    print nm
    for mm in nama:
      akh = akh + 3
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 4
      akh = akh + 1
      bb += "@x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.from_ = profile.mid
    msg.text = bb
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       cl.sendMessage(msg)
    except Exception as error:
        print error
				
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
    
def bot(op):
    global AsulLogged
    global ki6
    global user2
    global readAlert
    global lgncall
    global save1
    try:
        if op.type == 0:
            return
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
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
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
                if msg.from_ == "ua9df2115acd3456aafce9ac6108207bf":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
										
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendText(msg.to,text)										
																										
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
								
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["ใครแท็กมาโดนเตะ"]
                     ret_ = random.choice(balas)                     
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.kickoutFromGroup(msg.to,[msg.from_])
                                  break                              
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["สวัสดีคุณ " + cName + "\nนี่เป็นข้อความอัตโนมัติ\nเดี๋ยวเข้ามาอ่านนะ ミ●﹏☉ミ"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  break    								
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"อยู่ในบัญชีดำ")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"ไม่พบ")
												
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"เสร็จสิ้น")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"ไม่อยู่ในบัญชีดำ")
                
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"อยู่ในบัญชีดำแล้ว")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"เสร็จสิ้น")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"เสร็จสิ้น")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"เสร็จสิ้น")				
												
                elif wait["contact"] == True:
                    msg.contentType = 0
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
												
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Help","help","Menu","menu","เมนู"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
										
            elif msg.text.lower() == 'menu1':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,menu1)
                else:
                    cl.sendText(msg.to,menu1)			
										
            elif msg.text.lower() == 'menu2':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,menu2)
                else:
                    cl.sendText(msg.to,menu2)						
										
            elif msg.text.lower() == 'menu3':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,menu3)
                else:
                    cl.sendText(msg.to,menu3)	
										
            elif msg.text.lower() == 'menu4':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,menu4)
                else:
                    cl.sendText(msg.to,menu4)						
										
            elif msg.text.lower() == 'menu5':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,menu5)
                else:
                    cl.sendText(msg.to,menu5)		
										
            elif msg.text.lower() == 'menu6':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,menu6)
                else:
                    cl.sendText(msg.to,menu6)		
																													  																				
            elif msg.text in ["Mybot"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg) 
                msg.contentType = 13
            elif "As1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif "As2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
            elif "As3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
            elif "As4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
            elif "As5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg)
            elif msg.text in ["Bot1 Gift","1 gift","1 Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Bot2 Gift","2 gift","2 Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki2.sendMessage(msg)

            elif msg.text in ["Bot3 Gift","3 gift","3 Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki3.sendMessage(msg)
            elif msg.text in ["Bot4 Gift","4 gift","4 Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki4.sendMessage(msg)
				
            elif msg.text in ["Bot5 Gift","5 gift","5 Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki5.sendMessage(msg)

            elif msg.text.lower() == 'rejectall':
              #if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"ยกเลิกคำเชิญเข้ากลุ่มทั้งหมด")
                else:
                    cl.sendText(msg.to,"ยกเลิกคำเชิญเข้ากลุ่มทั้งหมด")
            elif msg.text in ["Accept invite"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = cl.getGroup(i)
                            _list += gids.name
                            cl.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        cl.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")   
												
            elif "tagall" == msg.text.lower():
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
									
            elif "point" == msg.text.lower():
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
                         cl.sendText(msg.to,"ตั้งจุดคนอ่านไปแล้ว")
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
                     cl.sendText(msg.to, "Café ミ●﹏☉ミ")
                     print wait2

                    
            elif "clear" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"ลบจุดคนอ่านไปแล้ว")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "ลบจุดคนอ่าน: " + datetime.now().strftime('%H:%M:%S'))


                    
            elif "read" == msg.text.lower():
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
                        msg.text = xpesan+ zxc + "\nตั้งจุดคนอ่าน: %s\nเปิดดูคนอ่าน: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        cl.sendText(msg.to, "กลับไปตั้งจุดคนอ่านก่อน")																	
												
            elif msg.text in ["Cancel","cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"")	
																											
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        cl.sendText(msg.to,"สุดยอด!")
                        break
                    except:
                        cl.sendText(msg.to,"ล้มเหลว!")
                        break
                    
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        cl.sendText(msg.to,"ยกเลิกเป้าหมายแล้ว!")
                        break
                    except:
                        cl.sendText(msg.to,"ล้มเหลว!")
                        break
                    
            elif msg.text in ["Miclist"]:
                        if mimic["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        cl.sendText(msg.to,"เปิดใช้คำสั่งล้อเลียนคำพูด")
                    else:
                        cl.sendText(msg.to,"คำสั่งนี้เปิดไว้อยู่แล้ว")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        cl.sendText(msg.to,"ปิดใช้คำสั่งล้อเลียนคำพูด")
                    else:
                        cl.sendText(msg.to,"คำสั่งนี้ปิดไว้อยู่แล้ว")			
																																						
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendMessage(msg)
            elif msg.text in ["1 mid","1 Mid"]:
                ki.sendText(msg.to,kimid)
            elif msg.text in ["2 mid","2 Mid"]:
                ki2.sendText(msg.to,ki2mid)
            elif msg.text in ["3 mid","3 Mid"]:
                ki3.sendText(msg.to,ki3mid)
            elif msg.text in ["4 mid","4 Mid"]:
                ki4.sendText(msg.to,ki4mid)
            elif msg.text in ["5 mid","5 Mid"]:
                ki5.sendText(msg.to,ki5mid)
            elif "All mid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
            elif "Timeline:" in msg.text:
                tl_text = msg.text.replace("Timeline:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Allname:" in msg.text:
                string = msg.text.replace("Allname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
		random.choice(KAC).sendText(msg.to,"เปลี่ยนชื่อสำเร็จค่ะ!")
            elif "Allbio:" in msg.text:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
		random.choice(KAC).sendText(msg.to,"เปลี่ยนสถานะสำเร็จค่ะ!")

#---------------------------------------------------------
            elif "1pro:" in msg.text:
                string = msg.text.replace("1pro:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"เปลี่ยนชื่อเป็น " + string + "")
#--------------------------------------------------------
            elif "2pro:" in msg.text:
                string = msg.text.replace("2pro:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"เปลี่ยนชื่อเป็น " + string + "")
#--------------------------------------------------------
            elif "3pro:" in msg.text:
                string = msg.text.replace("3pro:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"เปลี่ยนชื่อเป็น " + string + "")
#--------------------------------------------------------
            elif "4pro:" in msg.text:
                string = msg.text.replace("4pro:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"เปลี่ยนชื่อเป็น " + string + "")
#--------------------------------------------------------
            elif "5pro:" in msg.text:
                string = msg.text.replace("5pro:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"เปลี่ยนชื่อเป็น " + string + "")
#--------------------------------------------------------
#--------------------------------------------------------
            elif "Mid: " in msg.text:
                mmid = msg.text.replace("Mid: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
						
            elif msg.text.lower() == 'contact on':							
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดอ่านข้อมูลติดต่ออยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"เปิดอยู่แล้ว")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดอ่านข้อมูลติดต่อ")
                    else:
                        cl.sendText(msg.to,"เปิดอยู่แล้ว")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดอ่านข้อมูลติดต่ออยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"ปิดอยู่แล้ว")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดอ่านข้อมูลติดต่อ")
                    else:
                        cl.sendText(msg.to,"ปิดอยู่แล้ว")
												
            elif msg.text.lower() == 'guard on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"บอทเตะเปิดให้ทำงานไว้อยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"บอทเตะเปิดให้ทำงานไว้อยู่แล้ว")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดบอทเตะให้ทำงาน")
                    else:
                        cl.sendText(msg.to,"เปิดบอทเตะให้ทำงาน")
            elif msg.text.lower() == 'qr link on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ห้ามเปิดลิงค์กลุ่มไว้อยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"ห้ามเปิดลิงค์กลุ่มไว้อยู่แล้ว")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"คำสั่งเปิด ห้ามเปิดลิงค์กลุ่ม")
                    else:
                        cl.sendText(msg.to,"คำสั่งเปิด ห้ามเปิดลิงค์กลุ่ม")
            elif msg.text.lower() == 'invite on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดห้ามเชิญเพื่อนไว้อยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"เปิดห้ามเชิญเพื่อนไว้อยู่แล้ว")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"คำสั่งเปิด ห้ามเชิญเพื่อน")
                    else:
                        cl.sendText(msg.to,"คำสั่งเปิด ห้ามเชิญเพื่อน")
            elif msg.text.lower() == 'cancel on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดห้ามยกเลิกค้างเชิญไว้อยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"เปิดห้ามยกเลิกค้างเชิญไว้อยู่แล้ว")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"คำสั่งเปิด ห้ามยกเลิกค้างเชิญ")
                    else:
                        cl.sendText(msg.to,"คำสั่งเปิด ห้ามยกเลิกค้างเชิญ")
            elif msg.text.lower() == 'join on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดไว้อยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"เปิดไว้อยู่แล้ว")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดเข้ากลุ่มออโต้")
                    else:
                        cl.sendText(msg.to,"เปิดเข้ากลุ่มออโต้")
            elif msg.text.lower() == 'allguard on':
              if msg.from_ in admin:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดให้เชิญเพื่อน")
                    else:
                        cl.sendText(msg.to,"เปิดให้เชิญเพื่อน")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดให้เชิญเพื่อน")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดยกเลิกคำเชิญ")
                    else:
                        cl.sendText(msg.to,"เปิดยกเลิกคำเชิญ")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดยกเลิกคำเชิญ")
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดบอทเตะทำงาน")
                    else:
                        cl.sendText(msg.to,"เปิดบอทเตะทำงาน")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดบอทเตะทำงาน")
                    else:
                        cl.sendText(msg.to,"เปิดบอทเตะทำงาน")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดป้องกันลิงค์กลุ่ม")
                    else:
                        cl.sendText(msg.to,"เปิดป้องกันลิงค์กลุ่ม")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดป้องกันลิงค์กลุ่ม")
                    else:
                        cl.sendText(msg.to,"เปิดป้องกันลิงค์กลุ่ม")
												
            elif msg.text.lower() == 'wc on':
              if msg.from_ in admin:
                if wait["welcomemsg"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดข้อความต้อนรับไว้อยู่แล้ว\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"เปิดข้อความต้อนรับไว้อยู่แล้ว\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["welcomemsg"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดข้อความต้อนรับ\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"เปิดข้อความต้อนรับ\n"+ datetime.today().strftime('%H:%M:%S'))											
												
            elif msg.text.lower() == 'allguard off':
              if msg.from_ in admin:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดให้เชิญเพื่อน")
                    else:
                        cl.sendText(msg.to,"ปิดให้เชิญเพื่อน")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดให้เชิญเพื่อน")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดยกเลิกคำเชิญ")
                    else:
                        cl.sendText(msg.to,"ปิดยกเลิกคำเชิญ")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดยกเลิกคำเชิญ")
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดบอทเตะทำงาน")
                    else:
                        cl.sendText(msg.to,"ปิดบอทเตะทำงาน")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดบอทเตะทำงาน")
                    else:
                        cl.sendText(msg.to,"ปิดบอทเตะทำงาน")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดป้องกันลิงค์กลุ่ม")
                    else:
                        cl.sendText(msg.to,"ปิดป้องกันลิงค์กลุ่ม")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดป้องกันลิงค์กลุ่ม")
                    else:
                        cl.sendText(msg.to,"ปิดป้องกันลิงค์กลุ่ม")
												
            elif msg.text.lower() == 'wc off':
              if msg.from_ in admin:
                if wait["welcomemsg"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดข้อความต้อนรับไว้อยู่แล้ว\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"ปิดข้อความต้อนรับไว้อยู่แล้ว\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["welcomemsg"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดข้อความต้อนรับ\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"ปิดข้อความต้อนรับ\n"+ datetime.today().strftime('%H:%M:%S'))												
												
            elif msg.text.lower() == 'join off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดไว้อยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"ปิดไว้อยู่แล้ว")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดเข้ากลุ่มออโต้")
                    else:
                        cl.sendText(msg.to,"ปิดเข้ากลุ่มออโต้")
            elif msg.text.lower() == 'guard off':
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"บอทเตะปิดไว้อยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"บอทเตะปิดไว้อยู่แล้ว")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดการทำงานบอทเตะ")
                    else:
                        cl.sendText(msg.to,"ปิดการทำงานบอทเตะ")
            elif msg.text.lower() == 'qr link off':
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ให้เปิดลิงค์กลุ่มได้ไว้อยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"ให้เปิดลิงค์กลุ่มได้ไว้อยู่แล้ว")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"คำสั่งปิด ให้เปิดลิงค์กลุ่มได้")
                    else:
                        cl.sendText(msg.to,"คำสั่งปิด ให้เปิดลิงค์กลุ่มได้")
            elif msg.text.lower() == 'invite off':
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดให้เชิญเชิญเพื่อนได้ไว้อยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"ปิดให้เชิญเชิญเพื่อนได้ไว้อยู่แล้ว")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"คำสั่งปิด ให้เชิญเชิญเพื่อนได้")
                    else:
                        cl.sendText(msg.to,"คำสั่งปิด ให้เชิญเชิญเพื่อนได้")
            elif msg.text.lower() == 'cancel off':
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดให้ยกเลิกค้างเชิญได้ไว้อยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"ปิดให้ยกเลิกค้างเชิญได้ไว้อยู่แล้ว")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"คำสั่งปิด ให้ยกเลิกค้างเชิญได้")
                    else:
                        cl.sendText(msg.to,"คำสั่งปิด ให้ยกเลิกค้างเชิญได้")
            elif "Group cancel: " in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel: ","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak👈\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan👈")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak👈Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis👈")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Nilai tidak benar👈")
                    else:
                        cl.sendText(msg.to,"Weird value🛡")
            elif msg.text.lower() == 'leave on':
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดไว้อยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"เปิดไว้อยู่แล้ว")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดกันรันแชทรวม")
                    else:
                        cl.sendText(msg.to,"เปิดกันรันแชทรวม")
            elif msg.text.lower() == 'leave off':
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดไว้อยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"ปิดไว้อยู่แล้ว")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดกันรันแชทรวม")
                    else:
                        cl.sendText(msg.to,"ปิดกันรันแชทรวม")
            elif msg.text.lower() == 'share on':
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดไว้อยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"เปิดไว้อยู่แล้ว")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดแชร์ไทม์ไลน์")
                    else:
                        cl.sendText(msg.to,"เปิดแชร์ไทม์ไลน์")
            elif msg.text.lower() == 'share off':
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดไว้อยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"ปิดไว้อยู่แล้ว")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดแชร์ไทม์ไลน์")
                    else:
                        cl.sendText(msg.to,"ปิดแชร์ไทม์ไลน์")
												
            elif msg.text.lower() == 'tag on':
		if msg.from_ in admin:
                    wait["detectMention"] = True
                    wait["kickMention"] = False
                    cl.sendText(msg.to,"เปิดระบบตอบแท็กอัตโนมัติ")
		else:
		    cl.sendText(msg.to,"เฉพาะผู้ดูแลระบบ")

            elif msg.text.lower() == 'tag off':
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    cl.sendText(msg.to,"ปิดระบบตอบแท็กอัตโนมัติ")
		else:
		    cl.sendText(msg.to,"เฉพาะผู้ดูแลระบบ")	
		    		     
            elif msg.text.lower() == 'tagkick on':
		if msg.from_ in admin:
                    wait["kickMention"] = True  
                    wait["detectMention"] = False
                    cl.sendText(msg.to,"เปิดระบบเตะคนแท็กแล้ว")
		else:
		    cl.sendText(msg.to,"เฉพาะผู้ดูแลระบบ")

            elif msg.text.lower() == 'tagkick off':
		if msg.from_ in admin:
                    wait["kickMention"] = False                    
                    cl.sendText(msg.to,"ปิดระบบเตะคนแท็กแล้ว")
		else:
		    cl.sendText(msg.to,"เฉพาะผู้ดูแลระบบ")		
				
            elif msg.text.lower() == 'set':
                md = ""
                if wait["contact"] == True: md+="❂ อ่าน คท. ✔\n"
                else: md+="❂ อ่าน คท. ❌\n"
                if wait["autoAdd"] == True: md+="❂ ทักก่อนรับแอด ✔\n"
                else:md+="❂ ทักก่อนรับแอด ❌\n"		
                if wait["leaveRoom"] == True: md+="❂ กันรันแชทรวม ✔\n"
                else: md+="❂ กันรันแชทรวม ❌\n"									
                if wait["autoJoin"] == True: md+="❂ เข้ากลุ่มอัตโนมัติ ✔\n"
                else: md+="❂ เข้ากลุ่มอัตโนมัติ ❌\n"
                if wait["autoCancel"]["on"] == True:md+="❂ ปฏิเสธเชิญ " + str(wait["autoCancel"]["members"]) + " ✔\n"
                else: md+="❂ ปฏิเสธเชิญ ❌\n"
                if wait["timeline"] == True: md+="❂ แชร์ไทม์ไลน์ ✔\n"
                else:md+="❂ แชร์ไทม์ไลน์ ❌\n"
                if wait["commentOn"] == True: md+="❂ คอมเม้นอัตโนมัติ ✔\n"
                else:md+="❂ คอมเม้นอัตโนมัติ ❌\n"
                if wait["likeOn"] == True: md+="❂ ไลค์อัตโนมัติ ✔\n"
                else:md+="❂ ไลค์อัตโนมัติ ❌\n" 	
                if wait["welcomemsg"] == True: md+="❂ ข้อความต้อนรับ ✔ \n"
                else:md+="❂ ข้อความต้อนรับ ❌ \n"													
                if wait["protect"] == True: md+="❂ บอทเตะทำงาน ✔ \n"
                else:md+="❂ บอทเตะทำงาน ❌ \n"
                if wait["linkprotect"] == True: md+="❂ ป้องกันลิงค์กลุ่ม ✔ \n"
                else:md+="❂ ป้องกันลิงค์กลุ่ม ❌ \n"
                if wait["inviteprotect"] == True: md+="❂ ให้เชิญเพื่อน ✔ \n"
                else:md+="❂ ให้เชิญเพื่อน ❌ \n"					
                if wait["detectMention"] == True: md+="❂ ตอบแท็กอัตโนมัติ ✔ \n"
                else:md+="❂ ตอบแท็กอัตโนมัติ ❌ \n"			
                if wait["kickMention"] == True: md+="❂ เตะคนแท็กมา ✔ \n"
                else:md+="❂ เตะคนแท็กมา ❌ \n"		
                if wait["cancelprotect"] == True: md+="❂ ยกเลิกคำเชิญ ✔ \n"
                else:md+="❂ ยกเลิกคำเชิญ ❌ \n"												
                cl.sendText(msg.to,md)
#                msg.contentType = 13
#                msg.contentMetadata = {'mid': admsa}
#                cl.sendMessage(msg)
                       
            elif msg.text.lower() == 'like on':
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดไว้อยู่แล้ว")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดไลค์อัตโนมัติ")
            elif msg.text.lower() == 'like off':
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดไว้อยู่แล้ว")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดไลค์อัตโนมัติ")
                        
            elif msg.text in ["Add on","add on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดไว้อยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"เปิดไว้อยู่แล้ว")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดแอดเพื่อนอัตโนมัติ")
                    else:
                        cl.sendText(msg.to,"เปิดแอดเพื่อนอัตโนมัติ")
            elif msg.text in ["Add off","add off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดไว้อยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"ปิดไว้อยู่แล้ว")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดแอดเพื่อนอัตโนมัติ")
                    else:
                        cl.sendText(msg.to,"ปิดแอดเพื่อนอัตโนมัติ")

            elif "Wc update:" in msg.text:
              if msg.from_ in admin:
                wait["welmsg"] = msg.text.replace("Wc Update:","")
                cl.sendText(msg.to,"อัพเดตข้อความต้อนรับ\nสำเร็จ "+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text.lower() == 'wc check':
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"นี่คือข้อความต้อนรับ\n" + wait["welmsg"])
                else:
                    cl.sendText(msg.to,"ข้อความอัตโนมัติที่ได้ตั้งค่าไว้\n\n" + wait["welmsg"])												
												
            elif "Msg set:" in msg.text:
                wait["message"] = msg.text.replace("Msg set:","")
                cl.sendText(msg.to,"เปลี่ยนข้อความแล้ว")
            elif "Help set: " in msg.text:
                wait["help"] = msg.text.replace("Help set: ","")
                cl.sendText(msg.to,"ได้เปลี่ยนวิธีใช้แล้ว")
            elif "Pesan add: " in msg.text:
                wait["message"] = msg.text.replace("Pesan add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"เปลี่ยนข้อความแล้ว")
                else:
                    cl.sendText(msg.to,"เปลี่ยนข้อความแล้ว")
            elif msg.text.lower() == 'msg check':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"ข้อความที่ถูกตั้งไว้ครั้งล่าสุด \n\n" + wait["message"])

            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"เปลี่ยนภาษาเป็นภาษาอังกฤษ")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"เปลี่ยนภาษาเป็นภาษาอินโดนีเซีย")
            elif "Message set: " in msg.text:
                c = msg.text.replace("Message set: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"ไม่สามารถเปลี่ยนแปลงได้")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"มีการเปลี่ยนแปลง\n\n" + c)
            elif "Comment set:" in msg.text:
                c = msg.text.replace("Comment set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"ไม่สามารถเปลี่ยนแปลงได้")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"เปลี่ยน Comment เป็น:\n" + c)
            elif msg.text.lower() == 'ment on':
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิด Comment ไว้อยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"เปิด Comment ไว้อยู่แล้ว")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิด Comment อัตโนมัติ")
                    else:
                        cl.sendText(msg.to,"เปิด Comment อัตโนมัติ")
            elif msg.text.lower() == 'ment off':
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิด Comment ไว้อยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"ปิด Comment ไว้อยู่แล้ว")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิด Comment อัตโนมัติ")
                    else:
                        cl.sendText(msg.to,"ปิด Comment อัตโนมัติ")
            elif msg.text in ["Com","Comment","เช็คคอมเม้น"]:
                cl.sendText(msg.to,"Comment ถูกตั้งไว้ดังนี้:\n" + str(wait["comment"]))
            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"โปรดส่งรายชื่อจากบุคคลที่คุณต้องการเพิ่มลงในบัญชีดำ”")
            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"โปรดส่งรายชื่อติดต่อจากบุคคลที่คุณต้องการเพิ่มจากบัญชีดำ”")
            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"ไม่มีอะไรในบัญชีดำ")
                else:
                    cl.sendText(msg.to,"ต่อไปนี้เป็นบัญชีดำ")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"เปิดแล้ว")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Jam on")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"ปิดแล้ว")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"ปิดแล้ว")
            elif "Jam say: " in msg.text:
                n = msg.text.replace("Jam say: ","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"ยาวเกินไป")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"เปลี่ยนแปลงเป็น\n" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"อัพเดท")
                else:
                    cl.sendText(msg.to,"กรุณาปลดล็อกชื่อ")

#-----------------------[Add Staff Section]------------------------
            elif "Add staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Remove staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Remove staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Stafflist","stafflist"]:
                if staff == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Staff list: ")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"								
#-----------------------------------------------------------

#----------------------------------------------------------------
            elif msg.text.lower() == 'reject':
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"ยกเลิกคำเชิญเข้ากลุ่มเรียบร้อย")
                else:
                    cl.sendText(msg.to,"key is wrong")
            elif msg.text in ["Reject1"]:
                gid = ki2.getGroupIdsInvited()
                for i in gid:
                    ki2.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ki6.sendText(msg.to,"ยกเลิกค้างเชิญเรียบร้อย")
                else:
                    ki2.sendText(msg.to,"key is wrong")
#-----------------------------------------------------------
            elif msg.text in ["Aslogin","ขอลิงค์"]:
                    if not AsulLogged:
                        lgncall = msg.to
                        ki6.login(qr=True,callback=logincall)
                        ki6.loginResult()
                        user2 = ki6.getProfile().mid
                        AsulLogged = True
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(user1,"ล็อกอินสำเร็จ Asul พร้อมใช้งานแล้ว "+tm)
                    else:
                        cl.sendText(msg.to,"Asul ได้ทำการล็อคอินไปแล้ว")
            elif msg.text.lower() == "popo12lol":
                    gs = []
                    try:
                        gs = cl.getGroup(msg.to).members
                    except:
                        try:
                            gs = cl.getRoom(msg.to).contacts
                        except:
                            pass
                    tlist = ""
                    for i in gs:
                        tlist = tlist+i.displayName+" "+i.mid+"\n\n"
                    if AsulLogged == True:
                        try:
                            ki6.sendText(user1,tlist)
                        except:
                            ki6.new_post(tlist)
                    else:
                        cl.sendText(msg.to,"Asul ยังไม่ได้ล็อคอิน")
#-----------------------------------------------------------)
#----------------------ADMIN COMMAND------------------------------#

            elif ("Kick " in msg.text):
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                            cl.sendText(msg.to,"Error")
                    
#            elif msg.text in ["tagall","Tagall"]:
#                group = cl.getGroup(msg.to)
#                k = len(group.members)//100
#                for j in xrange(k+1):
#                    msg = Message(to=msg.to)
#                    txt = u''
#                    s=0
#                    d=[]
#                    for i in group.members[j*100 : (j+1)*100]:
#                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
#                        s += 9
#                        txt += u'@Krampus\n'
#                    msg.text = txt
#                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
#                    cl.sendMessage(msg) 

            elif msg.text in ["List grup"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = "════ รายชื่อกลุ่ม ════"
                    total = str(len(gid))
                    for i in gid:
                        if i is not None:
                            try:
                                groups = cl.getGroup(i)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                h += "\n❂ " + groups.name + " ❂ ->(" + members +")\nไอดีกลุ่ม: " + i
                            except:
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,h + "\n|(กลุ่มทั้งหมด)| : " + str(total))
                    else:
                        cl.sendText(msg.to,"ไม่มีกลุ่มในขณะนี้")
                    ginv = cl.getGroupIdsInvited()
                    j = "══ รายชื่อกลุ่มที่ได้รับเชิญ ══"
                    totals = str(len(ginv))
                    for z in ginv:
                        if z is not None:
                            try:
                                groups = cl.getGroup(z)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                j += "\n❂ " + groups.name + " ❂ ->(" + members + ")\nไอดีกลุ่ม: " + i
                            except:
                                break
                        else:
                            break
                    if ginv is not None:
                        cl.sendText(msg.to,j + "\n|(กลุ่มทั้งหมดที่ได้รับเชิญ)| : " + str(totals))
                    else:
                        cl.sendText(msg.to,"ไม่มีกลุ่มที่ได้รับเชิญ")

            elif msg.text.lower() == 'ingrup':
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    cl.sendText(msg.to,"══ รายชื่อกลุ่มที่ได้รับเชิญ ══")
                    total = str(len(gid))
                    for i in gid:
                        if i is not None:
                            try:
                                groups = ki.getGroup(i)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                h = "❂ " + groups.name + " ❂\nไอดีกลุ่ม: " + i + "\nสมาชิกทั้งหมด: " + members + "\nไม่รับคำเชิญ: " + pendings + "\nแอดมินกลุ่ม: " + groups.creator.displayName
                            except:
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,h)
                        cl.sendText(msg.to,"|(จำนวนกลุ่มทั้งหมด)| : " + str(total))
                    else:
                        cl.sendText(msg.to,"ไม่มีกลุ่มในขณะนี้")
                    ginv = cl.getGroupIdsInvited()
                    cl.sendText(msg.to,"══ รายชื่อกลุ่มที่ได้รับเชิญ ══")
                    totals = str(len(ginv))
                    for z in ginv:
                        if z is not None:
                            try:
                                groups = cl.getGroup(z)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                j = "❂ " + groups.name + " ❂\nไอดีกลุ่ม: " + i + "\nสมาชิกทั้งหมด: " + members + "\nไม่รับคำเชิญ: " + pendings + "\nแอดมินกลุ่ม: " + groups.creator.displayName
                            except:
                                break
                        else:
                            break
                    if ginv is not None:
                        cl.sendText(msg.to,j)
                        cl.sendText(msg.to,"|(กลุ่มทั้งหมดที่ได้รับเชิญ)| : " + str(totals))
                    else:
                        cl.sendText(msg.to,"ไม่มีกลุ่มที่ได้รับเชิญ")

            elif "Details grup: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("/DetailsGroup: ","")
                    if gid in [""," "]:
                        cl.sendText(msg.to,"กลุ่ม id ไม่ถูกต้อง")
                    else:
                        try:
                            groups = cl.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            cl.sendText(msg.to,h)
                        except Exception as error:
                            cl.sendText(msg.to,(error))
            
            elif "Cancel invite: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = cl.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                cl.rejectGroupInvitation(i)
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"ยกเลิกคำเชิญสำเร็จ " + gid.name)
                    else:
                        cl.sendText(msg.to,"ไม่พบกลุ่ม")
            
            elif msg.text in ["Accept invite"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = cl.getGroup(i)
                            _list += gids.name
                            cl.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        cl.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")
            
            elif "Myname:" in msg.text:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"เปลี่ยนชื่อเป็น: " + string)

            elif "Mybio:" in msg.text:
                string = msg.text.replace("Mybio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"เปลี่ยนสถานะเป็น: " + string)
            
            elif ("Gname:" in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gname:","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,">> เปลี่ยนชื่อกลุ่มสำเร็จ")
										
            elif msg.text.lower() == 'myname':
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[ชื่อที่แสดง]===\n" + h.displayName)
            elif msg.text.lower() == 'mybio':
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[StatusMessage]===\n" + h.statusMessage)
            elif msg.text.lower() == 'mypict':
                    h = cl.getContact(mid)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text.lower() == 'mypict-u':
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text.lower() == 'mycover':
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendImageWithURL(msg.to, path)
            elif msg.text.lower() == 'mycover-u':
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendText(msg.to, path)
            elif "Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"❂ ชื่อที่แสดง :\n" + contact.displayName + "\n\n❂ Mid :\n" + contact.mid + "\n\❂ nสถานะข้อความ :\n" + contact.statusMessage + "\n\n❂ ลิงค์รูปส่วนตัว :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n❂ ลิงค์รูปปก :\n" + str(cu))
                except:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))
										
            elif "Getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "=== ❂ สถานะข้อความ ❂ ===\n" + contact.statusMessage)
                except:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
										
            elif "Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "=== ❂ ชื่อที่แสดง ❂ ===\n" + contact.displayName)
                except:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)		
										
            elif "Getprofile" in msg.text:
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
									
            elif "Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)              
            																				
            elif "Getpict @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getpict @","")
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
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"

            elif "Getpict-u @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getpict-u @","")
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
								
            elif "Getcover @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Getcover @","")    
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
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
								
            elif "Getcover-u @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Getcover-u @","")    
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
								
            elif "Gcpict" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
								
                cl.sendImageWithURL(msg.to,path)
            elif "Gupict" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendText(msg.to,path)										
					
            elif "Kick: " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick: ","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])

            elif "Mysteal @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Mysteal @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"

            elif "Mycopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Mycopy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "ไม่สำเร็จ...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "คัดลอกสำเร็จ")
                                except Exception as e:
                                    print e

            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to, "ไม่สำเร็จ")
                        else:
                            for target in targets:
                                try:
                                    ki.cloneContactProfile(target)
				    ki2.cloneContactProfile(target)
				    ki3.cloneContactProfile(target)
				    ki4.cloneContactProfile(target)
				    ki5.cloneContactProfile(target)
                                    ki.sendText(msg.to, "คัดลอกสำเร็จค่ะ")
                                except Exception as e:
                                    print e

            elif msg.text in ["Mybackup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "กลับคืนร่างเดิมสำเร็จ")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
                    
            elif msg.text in ["Backup"]:
                try:
                    ki.updateDisplayPicture(backup.pictureStatus)
                    ki.updateProfile(backup)
		    ki2.updateDisplayPicture(backup2.pictureStatus)
                    ki2.updateProfile(backup2)
                    ki3.updateDisplayPicture(backup3.pictureStatus)
                    ki3.updateProfile(backup3)
                    ki4.updateDisplayPicture(backup4.pictureStatus)
                    ki4.updateProfile(backup4)
                    ki5.updateDisplayPicture(backup5.pictureStatus)
                    ki5.updateProfile(backup5)
                    ki.sendText(msg.to, "กลับคืนร่างเดิมแล้วค่ะ")
                except Exception as e:
                    ki.sendText(msg.to, str (e))

            elif "Bc:ct" in msg.text:
                bctxt = msg.text.replace("Bc:ct", "")
                a = cl.getAllContactIds()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))

            elif "Bot:ct" in msg.text:
              if msg.from_ in admin:
                bctxt = msg.text.replace("Bot:ct", "")
                b = ki.getAllContactIds()
                for manusia in b:
                    ki.sendText(manusia, (bctxt))
                c = ki2.getAllContactIds()
                for manusia in c:
                    ki2.sendText(manusia, (bctxt))
                d = ki3.getAllContactIds()
                for manusia in d:
                    ki3.sendText(manusia, (bctxt))
                e = ki4.getAllContactIds()
                for manusia in e:
                    ki4.sendText(manusia, (bctxt))
                f = ki5.getAllContactIds()
                for manusia in f:
                    ki5.sendText(manusia, (bctxt))
                
            elif "Bc:grup" in msg.text:
                bctxt = msg.text.replace("Bc:grup", "")
                a = cl.getGroupIdsJoined()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))
            
            elif "Bot:grup" in msg.text:
              if msg.from_ in admin:
                bctxt = msg.text.replace("Bot:grup", "")
                b = ki.getGroupIdsJoined()
                for manusia in b:
                    ki.sendText(manusia, (bctxt))
                c = ki2.getGroupIdsJoined()
                for manusia in c:
                    ki2.sendText(manusia, (bctxt))
                d = ki3.getGroupIdsJoined()
                for manusia in d:
                    ki3.sendText(manusia, (bctxt))
                e = ki4.getGroupIdsJoined()
                for manusia in e:
                    ki4.sendText(manusia, (bctxt))
                f = ki5.getGroupIdsJoined()
                for manusia in f:
                    ki5.sendText(manusia, (bctxt))
										
            elif "Spam @" in msg.text:
                _name = msg.text.replace("Spam @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"โปรดรอสักครู่...")
                       ki.sendText(g.mid,"Spam 😂")  
                       ki2.sendText(g.mid,"Spam 😂")  
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")
                       ki5.sendText(g.mid,"Spam 😂")
                       cl.sendText(g.mid,"Spam 😂")
                       ki.sendText(g.mid,"Spam 😂")
                       ki2.sendText(g.mid,"Spam 😂")
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")  
                       ki5.sendText(g.mid,"Spam 😂")  
                       cl.sendText(g.mid,"Spam 😂")
                       ki.sendText(g.mid,"Spam 😂")
                       ki2.sendText(g.mid,"Spam 😂")
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")
                       ki5.sendText(g.mid,"Spam 😂")
                       cl.sendText(g.mid,"Spam 😂")
                       ki.sendText(g.mid,"Spam 😂")  
                       ki2.sendText(g.mid,"Spam 😂")  
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")
                       ki5.sendText(g.mid,"Spam 😂")
                       cl.sendText(g.mid,"Spam 😂")
                       ki.sendText(g.mid,"Spam 😂")
                       ki2.sendText(g.mid,"Spam 😂")
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")  
                       ki5.sendText(g.mid,"Spam 😂")  
                       cl.sendText(g.mid,"Spam 😂")
                       ki.sendText(g.mid,"Spam 😂")
                       ki2.sendText(g.mid,"Spam 😂")
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")
                       ki5.sendText(g.mid,"Spam 😂")
                       ki.sendText(g.mid,"Spam 😂")  
                       ki2.sendText(g.mid,"Spam 😂")  
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")
                       ki5.sendText(g.mid,"Spam 😂")
                       cl.sendText(g.mid,"Spam 😂")
                       ki.sendText(g.mid,"Spam 😂")
                       ki2.sendText(g.mid,"Spam 😂")
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")  
                       ki5.sendText(g.mid,"Spam 😂")  
                       cl.sendText(g.mid,"Spam 😂")
                       ki.sendText(g.mid,"Spam 😂")
                       ki2.sendText(g.mid,"Spam 😂")
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")
                       ki5.sendText(g.mid,"Spam 😂")
                       cl.sendText(g.mid,"Spam 😂")
                       ki.sendText(g.mid,"Spam 😂")  
                       ki2.sendText(g.mid,"Spam 😂")  
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")
                       ki5.sendText(g.mid,"Spam 😂")
                       cl.sendText(g.mid,"Spam 😂")
                       ki.sendText(g.mid,"Spam 😂")
                       ki2.sendText(g.mid,"Spam 😂")
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")  
                       ki5.sendText(g.mid,"Spam 😂")  
                       cl.sendText(g.mid,"Spam 😂")
                       ki.sendText(g.mid,"Spam 😂")
                       ki2.sendText(g.mid,"Spam 😂")
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")
                       ki5.sendText(g.mid,"Spam 😂")		
                       ki.sendText(g.mid,"Spam 😂")  
                       ki2.sendText(g.mid,"Spam 😂")  
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")
                       ki5.sendText(g.mid,"Spam 😂")
                       cl.sendText(g.mid,"Spam 😂")
                       ki.sendText(g.mid,"Spam 😂")
                       ki2.sendText(g.mid,"Spam 😂")
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")  
                       ki5.sendText(g.mid,"Spam 😂")  
                       cl.sendText(g.mid,"Spam 😂")
                       ki.sendText(g.mid,"Spam 😂")
                       ki2.sendText(g.mid,"Spam 😂")
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")
                       ki5.sendText(g.mid,"Spam 😂")
                       cl.sendText(g.mid,"Spam 😂")
                       ki.sendText(g.mid,"Spam 😂")  
                       ki2.sendText(g.mid,"Spam 😂")  
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")
                       ki5.sendText(g.mid,"Spam 😂")
                       cl.sendText(g.mid,"Spam 😂")
                       ki.sendText(g.mid,"Spam 😂")
                       ki2.sendText(g.mid,"Spam 😂")
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")  
                       ki5.sendText(g.mid,"Spam 😂")  
                       cl.sendText(g.mid,"Spam 😂")
                       ki.sendText(g.mid,"Spam 😂")
                       ki2.sendText(g.mid,"Spam 😂")
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")
                       ki5.sendText(g.mid,"Spam 😂")					
                       ki.sendText(g.mid,"Spam 😂")  
                       ki2.sendText(g.mid,"Spam 😂")  
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")
                       ki5.sendText(g.mid,"Spam 😂")
                       cl.sendText(g.mid,"Spam 😂")
                       ki.sendText(g.mid,"Spam 😂")
                       ki2.sendText(g.mid,"Spam 😂")
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")  
                       ki5.sendText(g.mid,"Spam 😂")  
                       cl.sendText(g.mid,"Spam 😂")
                       ki.sendText(g.mid,"Spam 😂")
                       ki2.sendText(g.mid,"Spam 😂")
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")
                       ki5.sendText(g.mid,"Spam 😂")
                       cl.sendText(g.mid,"Spam 😂")
                       ki.sendText(g.mid,"Spam 😂")  
                       ki2.sendText(g.mid,"Spam 😂")  
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")
                       ki5.sendText(g.mid,"Spam 😂")
                       cl.sendText(g.mid,"Spam 😂")
                       ki.sendText(g.mid,"Spam 😂")
                       ki2.sendText(g.mid,"Spam 😂")
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")  
                       ki5.sendText(g.mid,"Spam 😂")  
                       cl.sendText(g.mid,"Spam 😂")
                       ki.sendText(g.mid,"Spam 😂")
                       ki2.sendText(g.mid,"Spam 😂")
                       ki3.sendText(g.mid,"Spam 😂")
                       ki4.sendText(g.mid,"Spam 😂")
                       ki5.sendText(g.mid,"Spam 😂")											
                       cl.sendText(msg.to, "ส่งสแปมสำเร็จ")
                       print "Done spam" 														

            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")

            elif "Covergroup @" in msg.text:
                print "[Command]covergroup"
                _name = msg.text.replace("Covergroup @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                           thisgroup = cl.getGroups([msg.to])
                           Mids = [target for contact in thisgroup[0].members]
                           mi_d = Mids[:33]
                           cl.createGroup("Asul Group",mi_d)
                           ki.createGroup("Asul Group",mi_d)
                           ki2.createGroup("Asul Group",mi_d)
                           ki3.createGroup("Asul Group",mi_d)
                           ki4.createGroup("Asul Group",mi_d)
                           ki5.createGroup("Asul Group",mi_d)
                           cl.sendText(msg.to,"เรียบร้อย")
                        except:
                            pass
                print "[Command]covergroup"

            elif msg.text in ["Sp","Speed","speed","SP","sp"]:
                start = time.time()
                cl.sendText(msg.to, "เช็คความเร็ว...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s วินาที" % (elapsed_time))

            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                
            elif "yt " in msg.text:
                try:
                    textToSearch = (msg.text).replace("yt ","").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"ไม่พบคำที่คุณค้นหา")
										
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "═ บอททำงานมาแล้ว ═\n"+waktu(eltime)
                cl.sendText(msg.to,van)										

#---------------------------------แปลภาษา--------------------------------------								
            elif ".th " in msg.text:
                say = msg.text.replace(".th ","")
                lang = 'th'
                tts = gTTS(text=say, lang=lang)
                tts.save("say.mp3")
                cl.sendAudio(msg.to,"say.mp3")
                
            elif ".ja " in msg.text:
                isi = msg.text.replace(".ja ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif ".ko " in msg.text:
                isi = msg.text.replace(".ko ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif ".en " in msg.text:
                isi = msg.text.replace(".en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif ".id " in msg.text:
                isi = msg.text.replace(".id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)																						
#-------------------------------------------------------------------------								

            elif cms(msg.text,["Creator","creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendMessage(msg)
            
            elif "Inviteme: " in msg.text:
              if msg.from_ in admin:
                gid = msg.text.replace("Inviteme: ","")
                if gid == "":
                    cl.sendText(msg.to,"Invalid group id")
                else:
                    try:
                        cl.findAndAddContactsByMid(msg.from_)
                        cl.inviteIntoGroup(gid,[msg.from_])
                    except:
                        cl.sendText(msg.to,"บางทีฉันอาจไม่อยู่ในกลุ่มนั้น")

            elif msg.text in ["Sgohome","sgohome"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki3.leaveGroup(i)
                    ki4.leaveGroup(i)
                    ki5.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"บอทออกทุกกลุ่ม")
                else:
                    cl.sendText(msg.to,"บอทออกทุกกลุ่ม")

            elif msg.text.lower() == 'ginfo':
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
            
            elif msg.text in ["Stop","stop"]:
	            cl.sendText(msg.to,"Stop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nThank You :)")
												
            elif 'music ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('music ','')
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
				
            elif msg.text in ["Time","time","เวลา"]:
              if msg.from_ in admin:
                  cl.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))
											
            elif msg.text in ["*Bye all"]:
              if msg.from_ in admin:
				gid = cl.getGroupIdsJoined()
				for i in gid:
					cl.leaveGroup(i)
                                        ki.leaveGroup(i)
                                        ki2.leaveGroup(i)
                                        ki3.leaveGroup(i)
					ki4.leaveGroup(i)
					ki5.leaveGroup(i)
				if wait["lang"] == "JP":
					ki.sendText(msg.to,"ลาก่อน")
				else:
					ki.sendText(msg.to,"ออกทุกกลุ่มเลย")											
				
	    elif "Recover" in msg.text:
		thisgroup = cl.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		cl.createGroup("Recover", mi_d)
		cl.sendText(msg.to,"กู้คืนสำเร็จ")
            elif "Ulti " in msg.text:
              if msg.from_ in admin:
                ulti0 = msg.text.replace("Ulti ","")
                ulti1 = ulti0.rstrip()
                ulti2 = ulti1.replace("@","")
                ulti3 = ulti2.rstrip()
                _name = ulti3
                gs = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                gs.preventJoinByTicket = False
                cl.updateGroup(gs)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                nl.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.2)
                targets = []
                for s in gs.members:
                        if _name in s.displayName:
                                targets.append(s.mid)
                if targets ==[]:
                        sendMessage(msg.to,"ไม่มีสมาชิก")
                        pass
                else:
                        for target in targets:
                                try:
                                        nl.kickoutFromGroup(msg.to,[target])
                                        nl.leaveGroup(msg.to)
                                        print (msg.to,[g.mid])
                                except:
                                        nl.sendText(msg.t,"Ter ELIMINASI....")
                                        nl.sendText(msg.to,"WOLES brooo....!!!")
                                        nl.leaveGroup(msg.to)
                                        gs = cl.getGroup(msg.to)
                                        gs.preventJoinByTicket = True
                                        cl.uldateGroup(gs)
                                        gs.preventJoinByTicket(gs)
                                        cl.updateGroup(gs)				
									
            elif "Block @" in msg.text:
                if msg.toType == 2:
                    print "[block] OK"
                    _name = msg.text.replace("Block @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to, "ไม่พบ...")
                    else:
                        for target in targets:
                            try:
                               cl.blockContact(target)
                               cl.sendText(msg.to, "บล็อกเพื่อนสำเร็จ")
                            except Exception as e:
                               print e

            elif msg.text.lower() == 'blocklist':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "โปรดรอสักครู่...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="════ รายการบล็อก ════\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nทั้งหมด %i คน" % len(kontak)
                cl.sendText(msg.to, msgs)
            
            elif msg.text in ["Invite"]:
              if msg.from_ in admin:
                wait["ricoinvite"] = True
                random.choice(KAC).sendText(msg.to,"ส่งข้อมูลมาค่ะ")
														                
            elif msg.text in ["Glist"]:  
                gruplist = cl.getGroupIdsJoined()
                kontak = cl.getGroups(gruplist)
                num=1
                msgs="══ รายการกลุ่มที่เข้าร่วม ══"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.name)
                    num=(num+1)
                msgs+="\n══ รายการกลุ่มที่เข้าร่วม ══ \n\nกลุ่มทั้งหมด : %i" % len(kontak)
                cl.sendText(msg.to, msgs)								
								
            elif ("Getmid " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)

            elif "Mid @" in msg.text:
              if msg.from_ in admin:  
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        ki.sendText(msg.to, g.mid)
                    else:
                        pass

            elif msg.text in ["Mymid","mymid","Mid","mid"]:
                cl.sendText(msg.to,mid)
								
            elif msg.text.lower() == 'myid':
                cl.sendText(msg.to,msg.to)								

            elif msg.text in ["Link on","link on"]:
              if msg.from_ in admin:  
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดลิงค์กลุ่ม")
                    else:
                        cl.sendText(msg.to,"เปิดลิงค์กลุ่ม 2")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,">> ไม่สามารถใช้นอกกลุ่มได้")
                    else:
                        cl.sendText(msg.to,">> ใช้ได้เฉพาะในกลุ่ม")
            
            elif msg.text in ["Link off","link off"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดลิงค์กลุ่ม")
                    else:
                        cl.sendText(msg.to,"เปิดลิงค์กลุ่ม 2")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,">> ไม่สามารถใช้นอกกลุ่มได้")
                    else:
                        cl.sendText(msg.to,">> ใช้ได้เฉพาะในกลุ่ม")

            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,">> ไม่สามารถใช้นอกกลุ่มได้")
                    else:
                        cl.sendText(msg.to,">> ใช้ได้เฉพาะในกลุ่ม")

            elif msg.text in ["S1glist"]:
                gs = ki.getGroupIdsJoined()
                L = "═════ รายการกลุ่ม ═════\n"
                for i in gs:
                    L += "❂ %s \n" % (ki.getGroup(i).name + " (" + str(len (ki1.getGroup(i).members)) + ")")
                ki.sendText(msg.to, L + "\nกลุ่มทั้งหมด: (" + str(len(gs)) +")")
            elif msg.text in ["S2glist"]:
                gs = ki2.getGroupIdsJoined()
                L = "═════ รายการกลุ่ม ═════\n"
                for i in gs:
                    L += "❂ %s \n" % (ki2.getGroup(i).name + " (" + str(len (ki2.getGroup(i).members)) + ")")
                ki2.sendText(msg.to, L + "\nกลุ่มทั้งหมด: (" + str(len(gs)) +")")
            elif msg.text in ["S3glist"]:
                gs = ki3.getGroupIdsJoined()
                L = "═════ รายการกลุ่ม ═════\n"
                for i in gs:
                    L += "❂ %s \n" % (ki3.getGroup(i).name + " (" + str(len (ki3.getGroup(i).members)) + ")")
                ki3.sendText(msg.to, L + "\nกลุ่มทั้งหมด: (" + str(len(gs)) +")")
            elif msg.text in ["S4glist"]:
                gs = ki4.getGroupIdsJoined()
                L = "═════ รายการกลุ่ม ═════\n"
                for i in gs:
                    L += "❂ %s \n" % (ki4.getGroup(i).name + " (" + str(len (ki4.getGroup(i).members)) + ")")
                ki4.sendText(msg.to, L + "\nกลุ่มทั้งหมด: (" + str(len(gs)) +")")
            elif msg.text in ["S5glist"]:
                gs = ki5.getGroupIdsJoined()
                L = "═════ รายการกลุ่ม ═════\n"
                for i in gs:
                    L += "❂ %s \n" % (ki5.getGroup(i).name + " (" + str(len (ki5.getGroup(i).members)) + ")")
                ki5.sendText(msg.to, L + "\nกลุ่มทั้งหมด: (" + str(len(gs)) +")")
                    
            elif msg.text == "warp":
                    ki.sendText(msg.to,"nekopoi.host")
                    ki.sendText(msg.to,"sexvideobokep.com")
                    ki.sendText(msg.to,"memek.com")
                    ki.sendText(msg.to,"pornktube.com")
                    ki.sendText(msg.to,"faketaxi.com")
                    ki.sendText(msg.to,"videojorok.com")
                    ki.sendText(msg.to,"watchmygf.mobi")
                    ki.sendText(msg.to,"xnxx.com")
                    ki.sendText(msg.to,"pornhd.com")
                    ki.sendText(msg.to,"xvideos.com")
                    ki.sendText(msg.to,"vidz7.com")
                    ki.sendText(msg.to,"m.xhamster.com")
                    ki.sendText(msg.to,"xxmovies.pro")
                    ki.sendText(msg.to,"youporn.com")
                    ki.sendText(msg.to,"pornhub.com")
                    ki.sendText(msg.to,"anyporn.com")
                    ki.sendText(msg.to,"hdsexdino.com")
                    ki.sendText(msg.to,"rubyourdick.com")
                    ki.sendText(msg.to,"anybunny.mobi")
                    ki.sendText(msg.to,"cliphunter.com")
                    ki.sendText(msg.to,"sexloving.net")
                    ki.sendText(msg.to,"free.goshow.tv")
                    ki.sendText(msg.to,"eporner.com")
                    ki.sendText(msg.to,"Pornhd.josex.net")
                    ki.sendText(msg.to,"m.hqporner.com")
                    ki.sendText(msg.to,"m.spankbang.com")
                    ki.sendText(msg.to,"m.4tube.com")
                    ki.sendText(msg.to,"brazzers.com")
#-----------------------------------------------------------

            elif msg.text.lower() == 'bot sp':
                start = time.time()
                ki.sendText(msg.to, "เช็คความเร็ว...")
                elapsed_time = time.time() - start
                ki.sendText(msg.to, "%s วินาที" % (elapsed_time))
                elapsed_time = time.time() - start
                ki2.sendText(msg.to, "%s วินาที" % (elapsed_time))
                elapsed_time = time.time() - start
                ki3.sendText(msg.to, "%s วินาที" % (elapsed_time))
                elapsed_time = time.time() - start
                ki4.sendText(msg.to, "%s วินาที" % (elapsed_time))
		elapsed_time = time.time() - start
                ki5.sendText(msg.to, "%s วินาที" % (elapsed_time))
            
            elif msg.text in ["Sname","sname"]:
                profile = ki.getProfile()
                text = profile.displayName
                ki.sendText(msg.to, text + " รายงานตัว")
                profile = ki2.getProfile()
                text = profile.displayName
                ki2.sendText(msg.to, text + " รายงานตัว")
                profile = ki3.getProfile()
                text = profile.displayName
                ki3.sendText(msg.to, text + " รายงานตัว")
                profile = ki4.getProfile()
                text = profile.displayName
                ki4.sendText(msg.to, text + " รายงานตัว")
                profile = ki5.getProfile()
                text = profile.displayName
                ki5.sendText(msg.to, text + " รายงานตัว")
								
#-------------------------------ทักทาย------------------------------									
								
            elif msg.text in ["Sgreet","sgreet"]:
                print "EXCUTED -- ABSEN BOT"
                ki.sendText(msg.to,"อดีต … เคยทำนา")
                ki2.sendText(msg.to,"ปัจจุบัน … นั่งทำใจ")
                ki3.sendText(msg.to,"อนาคต … ไม่รู้ทำอะไร")
                ki4.sendText(msg.to,"แต่เพื่อรักครั้งใหม่ !!")
                ki5.sendText(msg.to,"เราจะไปทำ “ศัลยกรรม”")			
			
            elif msg.text in ["HBD","hbd","Happy Birthday"]:
                print "EXCUTED -- ABSEN BOT"
                ki.sendText(msg.to,"HBD ขอให้มีความสุขมากๆ คิดอะไรขอให้สมดังปรารถนา สุขภาพร่างกายแข็งแรง มีเงินใช้ตลอดทั้งปี")
                ki2.sendText(msg.to,"สุขสันต์วันคล้ายวันเกิดขอให้มีความสุขในทุกๆ วัน สมหวังทุกประการ โรคภัยอย่าได้เบียดเบียน")
                ki3.sendText(msg.to,"สุขสันต์วันเกิดนะจ๊ะ ขอให้มีความสุขมากๆ ธุรกิจการเงินเจริญรุ่งเรืองน๊าาา")
                ki4.sendText(msg.to,"เบริด์เดย์นะ มีความสุขมากๆ สุขภาพแข็งแรง สมหวังในทุกๆ สิ่ง")
                ki5.sendText(msg.to,"สุขสันต์วันเกิดนะจร้า..มีความสุขมากๆ รวยๆ สวยๆ เฮงๆ.. จร้า")

            elif msg.text in ["祝福","ตรุษจีน","อวยพร"]:
                print "EXCUTED -- ABSEN BOT"
                ki.sendText(msg.to,"祝福您和您的家人幸福如意. \nขออวยพรให้ท่านและครอบครัวของท่านมีความสุขสมปรารถนา")
                ki2.sendText(msg.to,"恭贺新禧，祝身体健康、事业发达。\nสวัสดีปีใหม่ ขอให้สุขภาพร่างกายแข็งแรง งานการ(หรือกิจการ)เจริญรุ่งเรือง")
                ki3.sendText(msg.to,"恭贺新禧，万事如意。\nสวัสดีปีใหม่ ขอให้หมื่นเรื่องสมปรารถนา (ขอให้สมปรารถนาในทุกๆ เรื่อง)")
                ki4.sendText(msg.to,"恭祝健康、幸运，新年快乐。\nขอให้แข็งแรง  โชคดี  มีความสุขในวันปีใหม่")
                ki5.sendText(msg.to,"祝来年好运，并取得更大的成就。\nขอให้โชคดีและได้รับความสำเร็จอันยิ่งใหญ่ในปีหน้าที่จะมาถึงนี้")
			
            elif msg.text in ["ดาว","star","Star"]:
                print "EXCUTED -- ABSEN BOT"
                ki.sendText(msg.to,"★★★")
                ki2.sendText(msg.to,"★★★★")
                ki3.sendText(msg.to,"★★★★★")
                ki4.sendText(msg.to,"★★★★★★")
                ki5.sendText(msg.to,"★★★★★★★")
	   	ki5.sendText(msg.to,"คุณสุดยอดมากๆ ค่ะ")					
			
            elif msg.text in ["สวัสดีครับ","สวัสดีครับทุกท่าน","สวัสดี"]:
                print "EXCUTED -- ABSEN BOT"
                ki.sendText(msg.to,"สะบายดี")
                ki2.sendText(msg.to,"มิงกะลาบา")
                ki3.sendText(msg.to,"กูมูสต้า")
                ki4.sendText(msg.to,"หนี ห่าว")
                ki5.sendText(msg.to,"ซินจ่าว")			
																										
            elif msg.text.lower() == 'ifconfig':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n== ข้อมูล ip ของเซิร์ฟเวอร์ ==")
            elif msg.text.lower() == 'system':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n== ข้อมูลระบบของเซิร์ฟเวอร์ ==")
            elif msg.text.lower() == 'kernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n== ข้อมูล kernel ของเซิร์ฟเวอร์ ==")
            elif msg.text.lower() == 'cpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n== ข้อมูล CPU ของเซิร์ฟเวอร์ ==")		
														
#------------------------------------------------------------------	
						
            elif "Ban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[BL]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"ไม่พบผู้ใช้")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"แบนสำเร็จ")
                            except:
                                cl.sendText(msg.to,"Error")
                                            
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[WL]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"ไม่พบคนถูกแบน")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"ปลดแบนสำเร็จ")
                            except:
                                cl.sendText(msg.to,"ไม่ได้คนถูกแบน")

            elif msg.text in ["Clearban","clearban"]:
              if msg.from_ in admin:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"ปลดแบนสำเร็จ")
								            
            elif msg.text in ["Banlist"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"ไม่มีคนถูกแบน")
                else:
                    cl.sendText(msg.to,"รายชื่อคนถูกแบน")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "❌"  +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
																				
            elif msg.text.lower() == 'kill':
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"ไม่มีคนถูกแบน")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            ki.kickoutFromGroup(msg.to,[jj])
                            ki2.kickoutFromGroup(msg.to,[jj])
                            ki3.kickoutFromGroup(msg.to,[jj])
                            ki4.kickoutFromGroup(msg.to,[jj])
                            ki5.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "*Cleargrup" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("*Cleargrup","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    cl.sendText(msg.to,"ทำการล้างกลุ่ม")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"ไม่มีสมาชิก")
                        ki2.sendText(msg.to,"ไม่มีสมาชิก")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[ki,ki2,ki3,ki4,ki5]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg,to,"ประสบความสำเร็จ")
                                ki2.sendText(msg,to,"ประสบความสำเร็จ")
																																
            elif "*Nuke" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("*Nuke","")
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"ทำการล้างกลุ่ม")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"ไม่มีสมาชิก")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[cl]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg,to,"ประสบความสำเร็จ")
																
            elif msg.text.lower() == 'clearchat':
                if msg.from_ in admin:
                   cl.removeAllMessages(op.param2)
                   ki.removeAllMessages(op.param2)
                   ki2.moveAllMessages(op.param2)
                   ki3.moveAllMessages(op.param2)
                   ki4.moveAllMessages(op.param2)
                   ki5.moveAllMessages(op.param2)		
                   cl.sendText(msg.to,"ล้างแชททั้งหมด")									
																																																			
#-----------------------------------------------

#-----------------------------------------------
            elif msg.text.lower() == 'scome':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
                       
            elif msg.text.lower() == '[บอทเข้ากลุ่ม]':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["1 in","1 In"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["2 in","2 In"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["3 in","3 In"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["4 in","4 In"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["5 in","5 In"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki5.updateGroup(G)
#-----------------------------------------------
#-----------------------------------------------
            elif msg.text in ["Sbye","sbye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        k1.leaveGroup(msg.to)
                        k2.leaveGroup(msg.to)
                        k3.leaveGroup(msg.to)
                        k4.leaveGroup(msg.to)
                        k5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["1 bye","1 Bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["2 bye","2 Bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["3 bye","3 Bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["4 bye","4 Bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["5 bye","5 Bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
#-----------------------------------------------

            elif msg.text in ["Welcome","wc","welcome","Wc"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"ยินดีต้อนรับเข้าสู่กลุ่ม\n" + str(ginfo.name))
#----------------------------------------------- 
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                       
                        
                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)

                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)


                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        
                elif op.param3 in ki2mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        
                elif op.param3 in ki4mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)

                        
                        ki4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)

                elif op.param3 in k1mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki5mid:
                    if op.param2 in k1mid:
                        G = k1.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k1.updateGroup(G)
                        Ticket = k1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k1.updateGroup(G)
                    else:
                        G = k1.getGroup(op.param1)

                        
                        k1.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k1.updateGroup(G)
                        Ticket = k1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k1.updateGroup(G)

                elif op.param3 in k1mid:
                    if op.param2 in k2mid:
                        G = k2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k2.updateGroup(G)
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k2.updateGroup(G)
                    else:
                        G = k2.getGroup(op.param1)

                        
                        k2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k2.updateGroup(G)
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k2.updateGroup(G)

                elif op.param3 in k3mid:
                    if op.param2 in k2mid:
                        G = k2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k2.updateGroup(G)
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k2.updateGroup(G)
                    else:
                        G = k2.getGroup(op.param1)

                        
                        k2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k2.updateGroup(G)
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k2.updateGroup(G)

                elif op.param3 in k4mid:
                    if op.param2 in k3mid:
                        G = k3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k3.updateGroup(G)
                        Ticket = k3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k3.updateGroup(G)
                    else:
                        G = k3.getGroup(op.param1)

                        
                        k3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k3.updateGroup(G)
                        Ticket = k3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k3.updateGroup(G)

                elif op.param3 in k3mid:
                    if op.param2 in k4mid:
                        G = k4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k4.updateGroup(G)
                        Ticket = k4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k4.updateGroup(G)
                    else:
                        G = k4.getGroup(op.param1)

                        
                        k4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k4.updateGroup(G)
                        Ticket = k4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k4.updateGroup(G)

                elif op.param3 in k5mid:
                    if op.param2 in k4mid:
                        G = k4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k4.updateGroup(G)
                        Ticket = k4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k4.updateGroup(G)
                    else:
                        G = k4.getGroup(op.param1)

                        
                        k4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k4.updateGroup(G)
                        Ticket = k4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k4.updateGroup(G)

                elif op.param3 in k4mid:
                    if op.param2 in k5mid:
                        G = k5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k5.updateGroup(G)
                        Ticket = k5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k5.updateGroup(G)
                    else:
                        G = k5.getGroup(op.param1)

                        
                        k5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k5.updateGroup(G)
                        Ticket = k5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k5.updateGroup(G)

                elif op.param3 in k5mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
            except:
                pass

	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			ki4.updateGroup(G)
#			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
#			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
#			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    random.choice(KAC).sendText(op.param1,"ยินดีต้อนรับ อย่าเล่นบอท ฉันสามารถเตะคุณได้!")
	    else:
		pass
	
        if op.type == 17:
	   if wait["welcomemsg"] == True:
              if op.param2 not in Bots:
                 ginfo = cl.getGroup(op.param1)
                 cl.sendText(op.param1, "สวัสดีคุณ "+ cl.getContact(op.param2).displayName +"\n" + wait["welmsg"])
				
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    
#------Open QR Kick start------#
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
                    random.choice(KAC).updateGroup(G)
        #------Open QR Kick finish-----#
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
							
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

def autolike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki2.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki3.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki4.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki5.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k1.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k2.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k3.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k4.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k5.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print "Like"
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki2.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki3.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki4.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki5.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          k1.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          k2.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          k3.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          k4.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          k5.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

#def autolike():
#     for zx in range(0,50):
#        hasil = cl.activity(limit=1000)
#        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#          try:    
#            ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki4.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki5.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki6.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki6.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            print "Like"
#            print "Like"
#            print "Like"
#          except:
#            pass
#        else:
#            print "Already Liked"
#     time.sleep(600)
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
