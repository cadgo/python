import smtplib
from smtplib import SMTPAuthenticationError, SMTPSenderRefused
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

time_throttle=None
mins_wait = 10

def mail_throttle(func):
    min_wait = mins_wait * 60
    def wrapper(*args, **kwargs):
        global time_throttle
        if time_throttle == None:
            print("Mo mail used previously sending mail at: {}".format(time.ctime()))
            time_throttle = time.time() + min_wait
            func(*args, **kwargs)
        elif time_throttle < time.time():
            print("sending mail at: {}".format(time.ctime()))
            time_throttle = time.time() + min_wait
            func(*args, **kwargs)
        else:
            print("Not mail to send, time as not expired")
    return wrapper

@mail_throttle
def SendMailAlertGmail(sender, receivers, sender_password,subject,mailbody):
    message = MIMEMultipart()
    message['Form'] = sender
    try:
        mailpassword= sender_password
    except KeyError:
        print("No email password defined on the enviroment, not mail alert")
        return False
    message['To'] = receivers
    message['Subject'] = subject
    message.attach(MIMEText(mailbody, "plain"))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    try:
        session.login(sender, mailpassword)
        text = message.as_string()
        session.sendmail(sender, receivers,text)
    except SMTPAuthenticationError as e:
        print("Imposible to send email, error on the account", e)
        return False
    except SMTPSenderRefused:
        print("The account used was refused by the server")
        return False
    print("email sent to recipient")
    session.quit()
    return True