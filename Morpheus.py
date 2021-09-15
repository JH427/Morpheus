#BUILT ON PYTHON 3.6
#Morpheus - SYSTEM INFORMATION DESKTOP WALLPAPER GENERATOR
#by Joshua Harper (jeharper@uga.edu)

import platform, subprocess, os, time, ctypes, glob
from PIL import Image, ImageFont, ImageDraw
from datetime import datetime, timedelta, date

def roll_the_logo():
    print('''                                  
 _____             _               
|     |___ ___ ___| |_ ___ _ _ ___ 
| | | | . |  _| . |   | -_| | |_ -|
|_|_|_|___|_| |  _|_|_|___|___|___| v1.0
              |_|

SYSTEM INFORMATION DESKTOP WALLPAPER GENERATOR 
    ''')
    print("The Matrix is everywhere.")
    time.sleep(1)
    print("It is all around us.")
    time.sleep(1)
    print("Even now, in this very room.")
    time.sleep(1)
    print("You can see it when you look out your window or when you turn on your television.")
    time.sleep(1)
    print("You can feel it when you go to work... when you go to church... when you pay your taxes.")
    time.sleep(1)
    print("It is the world that has been pulled over your eyes to blind you from the truth.")
    time.sleep(1)
roll_the_logo()

###################################################################
#            A little magic can take you a long way.              #
###################################################################

def arrayMagic(array,magic):
    for line in array:
        if magic in line:
            return line.split(":")[1].lstrip()

def arrayMagicPlus(array,magic):
    for line in array:
        if magic in line:
            lineArr = line.split(":")
            del lineArr[0]
            return ":".join(lineArr).lstrip()


###################################################################
#                         MALWAREBYTES STUFF                      #
###################################################################

list_of_mwb_files = glob.glob('C:\\ProgramData\\Malwarebytes\\Malwarebytes\' Anti-Malware\\Logs\\*')# * means all if need specific format then *.csv

logArr = []
for file in list_of_mwb_files:
    if file[60] == 'm':
        logArr.append(file)
    
latest_mwb_file = max(logArr, key=os.path.getctime)
latestMWB = latest_mwb_file[60:].split('mbam-log-')[1].split(' (')[0]
mwbDateObj = datetime.strptime(latestMWB, '%Y-%m-%d').date()
mwbColorText = (255,255,255)
if mwbDateObj < date.today() - timedelta(days=14):
    mwbColorText = (255,0,0)

###################################################################
#                         SYSTEM INFORMATION                      #
###################################################################

def get_IP():
    IP_array = []
    ipconfig_array = str(subprocess.check_output('ipconfig')).split('\\r\\n')
    for line in ipconfig_array:
        if 'IPv4' in line:
            IP_array.append(line.split(':')[1])
            return IP_array[0].strip()

def SysInfoArray():
    return str(subprocess.check_output('systeminfo')).split('\\r\\n')

sysinfo = SysInfoArray()

hostName = arrayMagic(sysinfo,"Host Name")
osName = arrayMagic(sysinfo,"OS Name")
osVersion = arrayMagic(sysinfo,"OS Version")
manufacturer = arrayMagic(sysinfo,"System Manufacturer")
model = arrayMagic(sysinfo,"System Model")
biosVersion = arrayMagic(sysinfo,"BIOS Version")
systemType = arrayMagic(sysinfo,"System Type")
totalMemory = arrayMagic(sysinfo,"Total Physical Memory")
domain = arrayMagic(sysinfo,"Domain")
timeZone = arrayMagicPlus(sysinfo,"Time Zone")
ipAddress = get_IP()
user = str(os.getlogin())
pyVersion = platform.python_version()

###################################################################
#                         IMAGE CREATION                          #
###################################################################

#Create Image Object in RGB mode, 1920x1080, black
width = 1920
height = 1080
img = Image.new("RGB", (width,height), color=0)

#If you want a custom image..
#img = Image.open("space.jpg")

fontSize = 16
draw = ImageDraw.Draw(img) #testing custom img
font = ImageFont.truetype("OCRAEXT.TTF",fontSize)

textcolor = (255,255,255)
leftCONST = 1350
downCONST = 50
#Write text ((pixels from the left,pixels from the top), text to write, font)

#use a for loop to iterate fontSize*x?
draw.text((leftCONST, downCONST+fontSize*0), "USER: "+user,textcolor,font=font)
draw.text((leftCONST, downCONST+fontSize*1), "HOST NAME: "+hostName,textcolor,font=font)
draw.text((leftCONST, downCONST+fontSize*2), "OS NAME: "+osName,textcolor,font=font)
draw.text((leftCONST, downCONST+fontSize*3), "OS VERSION: "+osVersion,textcolor,font=font)
draw.text((leftCONST, downCONST+fontSize*4), "MODEL: "+manufacturer + ' ' + model,textcolor,font=font)
draw.text((leftCONST, downCONST+fontSize*5), "BIOS VERSION: "+biosVersion,textcolor,font=font)
draw.text((leftCONST, downCONST+fontSize*6), "SYSTEM TYPE: "+systemType,textcolor,font=font)
draw.text((leftCONST, downCONST+fontSize*7), "PHYSICAL MEMORY: "+totalMemory,textcolor,font=font)
draw.text((leftCONST, downCONST+fontSize*8), "DOMAIN: "+domain,textcolor,font=font)
draw.text((leftCONST, downCONST+fontSize*9), "TIME ZONE: "+timeZone,textcolor,font=font)
draw.text((leftCONST, downCONST+fontSize*10), "IP ADDRRESS: "+ipAddress,textcolor,font=font)
draw.text((leftCONST, downCONST+fontSize*11), "PYTHON VERSION: "+pyVersion,textcolor,font=font)
draw.text((leftCONST, downCONST+fontSize*12), "MALWAREBYTES: "+str(mwbDateObj),mwbColorText,font=font)
#draw.text((leftCONST, downCONST+fontSize*x), " _____             _               ", textcolor, font=font)
#draw.text((leftCONST, downCONST+fontSize*x), "|     |___ ___ ___| |_ ___ _ _ ___ ", textcolor, font=font)
#draw.text((leftCONST, downCONST+fontSize*x), "| | | | . |  _| . |   | -_| | |_ -|", textcolor, font=font)
#draw.text((leftCONST, downCONST+fontSize*x), "|_|_|_|___|_| |  _|_|_|___|___|___|", textcolor, font=font)
#draw.text((leftCONST, downCONST+fontSize*x), "              |_|", textcolor, font=font)

imgPath = "C:\\WALL\\img.png"

#Save Image Object as PNG
img.save(imgPath, format="PNG")

###################################################################
#                           SET WALLPAPER                         #
###################################################################

SPI_SETDESKWALLPAPER = 0x14
SPIF_UPDATEINIFILE   = 0x2 
src = r"C:\WALL\img.png" 

#SystemParametersInfoW instead of SystemParametersInfoA (W instead of A)
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, src, SPIF_UPDATEINIFILE)

